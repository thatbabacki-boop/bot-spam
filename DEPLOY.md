# 🚀 Hướng dẫn Deploy Super Ultimate Bot 3.0 lên Render

## 📋 Chuẩn bị

1. **Đảm bảo bạn đã có:**
   - Tài khoản GitHub
   - Tài khoản Render (miễn phí)
   - Token Discord Bot
   - ID Discord của bạn (để làm admin)
   - Python 3.8+ trên local (để test)

## 🔧 Cấu hình Local

1. **Cài đặt dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Các dependencies v3.0:**
   - `discord.py>=2.0.0` - Discord API
   - `aiohttp>=3.8.0` - Async HTTP
   - `paho-mqtt>=1.6.0` - MQTT (cho Facebook theme)
   - Và các packages khác...

3. **Tạo file .env:**
   ```bash
   cp .env.example .env
   ```

4. **Chỉnh sửa .env với thông tin của bạn:**
   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   ADMIN_IDS=your_discord_user_id
   ```

5. **Test bot local:**
   ```bash
   python start.py
   ```

## 📤 Deploy lên Render

### Cách 1: Sử dụng render.yaml (Tự động - Khuyên dùng)

1. **Push code lên GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Super Ultimate Bot 3.0 - Multi-platform with AI"
   git branch -M main
   git remote add origin https://github.com/username/repo-name.git
   git push -u origin main
   ```

2. **Tạo Web Service trên Render:**
   - Đăng nhập vào [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect GitHub repository của bạn
   - Render sẽ tự động đọc file `render.yaml` (đã tối ưu cho v3.0)
   - Click "Deploy Web Service"

### Cách 2: Cấu hình thủ công

1. **Tạo Web Service:**
   - Name: `super-ultimate-bot-3` (hoặc tên bạn muốn)
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python start.py`

2. **Thêm Environment Variables:**
   Trong tab "Environment", thêm:
   - `DISCORD_TOKEN`: Token bot Discord của bạn
   - `ADMIN_IDS`: ID Discord của bạn

3. **Deploy:**
   - Click "Create Web Service"

## ✅ Sau khi Deploy

1. **Kiểm tra log:**
   - Vào tab "Logs" trên Render dashboard
   - Đợi bot khởi động và connect thành công
   - Kiểm tra message: "✅ Bot đã online với tên: YourBot"

2. **Test bot:**
   - Mời bot vào server Discord của bạn
   - Sử dụng lệnh `/menu_new` để test menu mới (6 danh mục)
   - Sử dụng lệnh `/menu` để test menu cũ (để tương thích)
   - Test các lệnh mới như `/nova`, `/treopolldis`, `/createthread`

## 🎮 Các Lệnh Mới v3.0

### Menu System
- `/menu_new`: Menu tương tác với 6 danh mục
- `/menu`: Menu gốc (để tương thích)

### Facebook & Messenger
- `/addgroup`: Thêm user vào Facebook group
- `/setnenmess`: Đổi nền Messenger
- `/theme_mess`: Chọn theme Messenger (MQTT)
- `/nhaypollmess`: Spam poll Messenger
- `/combomess`: Combo siêu mạnh Messenger
- `/namechange`: Đổi tên thành viên box

### Discord
- `/treoaudio`: Spam audio Discord
- `/treopolldis`: Treo poll Discord (với rate limiting)
- `/createthread`: Tạo thread tự động
- `/allnhaydis`: Tất cả chức năng nhây Discord

### Admin & Tiện ích
- `/addadmin`: Thêm admin phụ
- `/xoaadmin`: Xóa admin phụ
- `/listadmin`: Danh sách admin phụ
- `/nova`: Hỏi AI Nova Pro
- `/say1`: Bot nhái v1
- `/say2`: Bot nhái v2
- `/checkuid`: Check acc Discord bằng UID
- `/idkenh`: Lấy ID kênh Discord

## 🛠 Troubleshooting v3.0

### Bot không khởi động
- Kiểm tra log trong Render dashboard
- Đảm bảo environment variables được set đúng
- Kiểm tra token Discord có hợp lệ không
- Kiểm tra Python version (cần 3.8+)

### Dependencies error
- Render sẽ tự động install từ requirements.txt
- Nếu lỗi với paho-mqtt, kiểm tra Python version
- Các lỗi dependencies khác sẽ hiển thị trong log

### Lệnh không hoạt động
- Đảm bảo bot đã được invite vào server với đúng permissions
- Kiểm tra lệnh đã được sync chưa (có thể mất vài phút sau khi deploy)
- F5 Discord để refresh lệnh
- Test với `/menu_new` trước

### MQTT Theme không hoạt động
- Cần cookie Facebook hoạt động
- Kiểm tra file nenMqtt.py đã được deploy
- MQTT có thể bị block bởi một số mạng

### Discord Poll/Thread không hoạt động
- Bot cần quyền Admin trong server
- Kiểm tra token có đủ permissions
- Rate limiting có thể giới hạn tốc độ

### Memory issues
- Version 3.0 đã tối ưu memory
- Nâng cấp plan trên Render nếu cần (free plan: 512MB)
- Tối ưu số lượng tab/tasks đang chạy

## 📝 Notes v3.0

- Bot sử dụng plan free của Render
- Free plan có thể sleep sau 15 phút không hoạt động
- Bot sẽ tự động restart khi có request mới
- Để bot hoạt động 24/7, cần upgrade plan
- **Version 3.0** đã tối ưu performance và memory
- Có tính năng rate limiting để tránh bị block

## 🎉 Tính Năng Đặc Biệt

### Performance Improvements
- **Rate Limiter**: Tránh bị rate limit bởi các platform
- **Memory Management**: Tối ưu bộ nhớ
- **Async Processing**: Xử lý nhanh hơn

### New Features
- **AI Integration**: Nova Pro AI
- **Advanced Menu**: 6 danh mục tương tác
- **Discord Poll/Thread**: Tính năng Discord mới
- **Facebook Theme**: MQTT-based theme changer
- **Admin System**: Đa cấp admin

---

**Super Ultimate Bot 3.0** - Deploy Guide

Made with ❤️ by zawng dep chai