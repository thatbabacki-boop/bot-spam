import asyncio
import aiohttp
import gc
from datetime import datetime

TREO_POLL_LOCK = asyncio.Lock()
user_treo_poll_tasks: dict[str, list[dict]] = {}

RESET = "\033[0m"
BOLD = "\033[1m"
PURPLE = "\033[38;2;180;0;255m"
WHITE = "\033[97m"
RED = "\033[91m"
YELLOW = "\033[93m"

def purple_gradient_text(text: str) -> str:
    return f"{PURPLE}{text}{RESET}"

def log_ok(msg: str):
    print(f"{PURPLE}{BOLD}[✔ TREOPOLLDIS]{RESET} {WHITE}{msg}{RESET}")

def log_err(msg: str):
    print(f"{RED}{BOLD}[✗ TREOPOLLDIS]{RESET} {WHITE}{msg}{RESET}")

def log_warn(msg: str):
    print(f"{YELLOW}{BOLD}[! TREOPOLLDIS]{RESET} {WHITE}{msg}{RESET}")

async def create_treo_poll(
    session: aiohttp.ClientSession,
    token: str,
    channel_id: str,
    content: str
):
    """
    Gửi poll Discord thật (API v10)
    Câu hỏi + 2 lựa chọn = cùng nội dung người dùng nhập
    """

    headers = {
        "Authorization": token.strip(),
        "Content-Type": "application/json"
    }

    payload = {
        "poll": {
            "question": {
                "text": content
            },
            "answers": [
                {
                    "answer_id": 1,
                    "poll_media": {
                        "text": content
                    }
                },
                {
                    "answer_id": 2,
                    "poll_media": {
                        "text": content
                    }
                }
            ],
            "allow_multiselect": False,
            "layout_type": 1,
            "duration": 300
        }
    }

    try:
        async with session.post(
            f"https://discord.com/api/v10/channels/{channel_id}/messages",
            headers=headers,
            json=payload,
            timeout=aiohttp.ClientTimeout(total=15)
        ) as resp:
            text = await resp.text()

            if resp.status in (200, 201):
                log_ok(
                    purple_gradient_text(
                        f"Đã treo poll | Channel={channel_id} | Nội dung='{content}'"
                    )
                )
            else:
                log_err(f"HTTP {resp.status} | {text}")

    except Exception as e:
        log_err(f"Exception gửi poll: {e}")


async def treo_poll_worker(
    token: str,
    channel_id: str,
    content: str,
    delay: float,
    stop_event: asyncio.Event
):
    """
    Worker treo poll
    - Không while True vô hạn
    - Dùng Event để stop an toàn
    """

    log_ok(
        purple_gradient_text(
            f"Bắt đầu treo poll | Channel={channel_id} | Delay={delay}s"
        )
    )

    async with aiohttp.ClientSession() as session:
        try:
            while not stop_event.is_set():
                await create_treo_poll(session, token, channel_id, content)

                try:
                    await asyncio.wait_for(stop_event.wait(), timeout=delay)
                except asyncio.TimeoutError:
                    pass

        except asyncio.CancelledError:
            pass
        except Exception as e:
            log_err(f"Lỗi worker: {e}")
            gc.collect()
        finally:
            log_warn(f"Đã dừng treo poll tại channel {channel_id}")

async def start_treo_poll(
    user_id: str,
    token: str,
    channel_id: str,
    content: str,
    delay: float
):
    stop_event = asyncio.Event()

    task = asyncio.create_task(
        treo_poll_worker(
            token=token,
            channel_id=channel_id,
            content=content,
            delay=delay,
            stop_event=stop_event
        )
    )

    async with TREO_POLL_LOCK:
        user_treo_poll_tasks.setdefault(user_id, []).append({
            "task": task,
            "stop": stop_event,
            "channel": channel_id,
            "delay": delay,
            "content": content,
            "start": datetime.now()
        })

    log_ok(
        purple_gradient_text(
            f"Tạo tab treo poll thành công | User={user_id} | Channel={channel_id}"
        )
    )

    return task

async def stop_treo_poll(user_id: str, index: int) -> bool:
    """
    index bắt đầu từ 0 (tab 1 = index 0)
    """

    async with TREO_POLL_LOCK:
        tabs = user_treo_poll_tasks.get(user_id)
        if not tabs or index < 0 or index >= len(tabs):
            return False

        tab = tabs.pop(index)

        tab["stop"].set()
        tab["task"].cancel()

        log_warn(
            purple_gradient_text(
                f"Đã dừng tab treo poll số {index + 1} | Channel={tab['channel']}"
            )
        )

        if not tabs:
            user_treo_poll_tasks.pop(user_id, None)

    return True
