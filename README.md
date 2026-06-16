# 🤖 Discord Bot - Multi-Platform Tool

Bot Discord đa nền tảng với các chức năng: Facebook, Messenger, Discord, Zalo, Telegram, Instagram, Gmail, SMS, WeChat

## 🚀 Tính năng

### 📘 Facebook
- Treo top ảnh
- Treo nhây top tin nhắn
- Réo story

### 💬 Messenger
- Treo ngôn tin nhắn
- Nhây réo tên
- Nhây tag Messenger
- Lấy danh sách nhóm
- Nhây đổi tên box
- Treo ảnh Messenger

### 🌀 Discord
- Treo ngôn Discord
- Nhây tag fake soạn

### 📱 Zalo
- Treo ngôn Zalo
- Nhây tag fake soạn (box)
- Treo bình chọn + tag
- Treo sticker
- Nhây tag fake soạn (1-1)
- Nhây đổi tên box Zalo

### 📢 Telegram
- Treo ngôn kèm ảnh

### 📸 Instagram
- Treo ngôn Instagram

### 📧 Gmail
- Treo spam Gmail

### 📲 SMS
- Treo spam OTP SMS

### 💼 WeChat
- Treo spam tin nhắn WeChat

### 🔧 Tiện ích
- Check cookie Facebook

## 📦 Cài đặt

### Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Cấu hình biến môi trường
Sao chép file `.env.example` thành `.env` và điền thông tin:
```bash
cp .env.example .env
```

Chỉnh sửa file `.env`:
```
DISCORD_TOKEN=your_discord_bot_token_here
ADMIN_IDS=your_admin_id_1,your_admin_id_2
```

### Chạy bot
```bash
python start.py
```

## 🌐 Deploy lên Render

1. **Push code lên GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

2. **Kết nối repository với Render**
   - Đăng nhập vào [Render](https://render.com)
   - Click "New +" -> "Web Service"
   - Kết nối GitHub repository của bạn
   - Render sẽ tự động phát hiện file `render.yaml`

3. **Cấu hình Environment Variables**
   Trong dashboard của Render, thêm các environment variables:
   - `DISCORD_TOKEN`: Token bot Discord của bạn
   - `ADMIN_IDS`: ID admin (ngăn cách bằng dấu phẩy)

4. **Deploy**
   - Click "Deploy Web Service"
   - Render sẽ tự động build và deploy bot của bạn

## 🎮 Sử dụng

- Sử dụng lệnh `/menu` để xem danh sách chức năng
- Sử dụng `/` trước tên lệnh để thực thi chức năng tương ứng
- Một số chức năng yêu cầu quyền admin

## 📝 Lưu ý

- Bot chỉ hoạt động với các tài khoản có quyền phù hợp
- Sử dụng bot có trách nhiệm và tuân thủ Terms of Service của các nền tảng
- Không sử dụng cho các mục đích spam hoặc gây phiền toài

## 🛠 Bảo trì

Bot được phát triển bởi **zawng dep chai**

---

Made with ❤️