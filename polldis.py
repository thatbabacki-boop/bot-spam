import asyncio, time, os

try:
    os.nice(5)
except Exception:
    pass

class RateLimiter:
    def __init__(self, max_rate_per_sec: float = 6.0):
        self.max_rate = max_rate_per_sec
        self.tokens = max_rate_per_sec
        self.last_time = time.monotonic()

    async def acquire(self, cost: float = 1.0):
        now = time.monotonic()
        elapsed = now - self.last_time
        self.last_time = now
        self.tokens = min(self.max_rate, self.tokens + elapsed * self.max_rate)
        if self.tokens < cost:
            wait = (cost - self.tokens) / self.max_rate
            await asyncio.sleep(wait)
            self.tokens = 0
        else:
            self.tokens -= cost

async def cooperative_sleep(i, every=10, delay=0.02):
    if i % every == 0:
        await asyncio.sleep(delay)

SEMAPHORE = asyncio.Semaphore(3)
GLOBAL_LIMITER = RateLimiter(max_rate_per_sec=8)

# > KẾT THÚC ĐOẠN CODE KÌM HÃM CPU

import asyncio
import aiohttp
import itertools
import sys
import os
import random
import gc
from datetime import datetime

POLL_LOCK = asyncio.Lock()
user_poll_sessions = {}

COLORS = [
    "\033[31m", 
    "\033[32m",  
    "\033[33m",  
    "\033[34m",  
    "\033[35m",  
    "\033[36m",  
]

RESET = "\033[0m"


def random_color_prefix():
    return random.choice(COLORS)


def apply_color(color_prefix: str) -> str:
    """
    Nếu color_prefix rỗng thì random màu,
    còn nếu bạn truyền vào sẵn thì dùng màu đó.
    """
    return color_prefix if color_prefix else random_color_prefix()



def format_time(seconds: int) -> str:
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    parts = []
    if d:
        parts.append(f"{d}d")
    if h:
        parts.append(f"{h}h")
    if m:
        parts.append(f"{m}m")
    parts.append(f"{s}s")
    return " ".join(parts)


async def show_typing_animation(duration, prefix=""):
    end_time = asyncio.get_event_loop().time() + duration
    for ch in itertools.cycle([".  ", ".. ", "..."]):
        if asyncio.get_event_loop().time() > end_time:
            break
        sys.stdout.write(f"\r{prefix}[Typing] Đang soạn{ch}")
        sys.stdout.flush()
        await asyncio.sleep(0.5)

    sys.stdout.write("\r" + " " * 60 + "\r")
    sys.stdout.flush()


def read_polldis_file(path="nhay2.txt"):
    items = []
    if not os.path.exists(path):
        print(f"[WARN] Không tìm thấy file {path}")
        return items

    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            items.append(line)

    if not items:
        print(f"[WARN] File {path} rỗng hoặc không có dòng hợp lệ!")
    else:
        print(f"[✅] Đã đọc {len(items)} dòng từ {path}")
    return items


async def create_poll_message(session, channel_id, headers, poll_items, color_prefix, long_poll=False):
    """Tạo poll từ file nhay2.txt"""
    if len(poll_items) < 3:
        c = apply_color(color_prefix)
        print(f"{c}[⚠️] File nhay2.txt cần ít nhất 3 dòng để tạo poll!{RESET}")
        return

    question_text = random.choice(poll_items)

    if not long_poll:
        available_options = [x for x in poll_items if x != question_text]
        if len(available_options) < 2:
            options_list = available_options
        else:
            options_list = random.sample(available_options, k=2)

    else:
        options_list = [x for x in poll_items if x != question_text]
        random.shuffle(options_list)
        options_list = [x[:10] for x in options_list]
        if len(options_list) > 10:
            options_list = options_list[:10]

    payload = {
        "poll": {
            "question": {"text": question_text[:200]},
            "answers": [
                {"answer_id": i + 1, "poll_media": {"text": opt}}
                for i, opt in enumerate(options_list)
            ],
            "allow_multiselect": False,
            "layout_type": 1,
            "duration": 300
        }
    }

    try:
        async with session.post(
            f"https://discord.com/api/v10/channels/{channel_id}/messages",
            json=payload,
            headers=headers,
            timeout=15
        ) as resp:

            text = await resp.text()
            c = apply_color(color_prefix)

            if resp.status in (200, 201):
                print(f"{c}[Thành Công]{RESET} Đã tạo poll discord!")
            else:
                print(f"{c}[Thất Bại]{RESET} Lỗi khi tạo poll!")

    except Exception as e:
        c = apply_color(color_prefix)
        print(f"{c}[⚠️] Exception khi tạo poll: {e}{RESET}")


async def poll_worker(token, channel_id, count, delay, poll_items, color_prefix, semaphore, long_poll=False):
    headers = {
        "Authorization": token.strip(),
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        while True:
            try:
                await semaphore.acquire()
                await create_poll_message(
                    session, channel_id, headers,
                    poll_items, color_prefix,
                    long_poll=long_poll
                )

            except asyncio.CancelledError:
                c = apply_color(color_prefix)
                print(f"{c}[🛑] Đã dừng spam poll ở {channel_id}.{RESET}")
                break

            except Exception as e:
                c = apply_color(color_prefix)
                print(f"{c}[⚠️] Lỗi worker: {e}{RESET}")
                await asyncio.sleep(2)
                gc.collect()

            finally:
                semaphore.release()

            await asyncio.sleep(delay)
