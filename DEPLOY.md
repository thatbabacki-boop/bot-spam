# 🚀 Hướng dẫn Deploy lên Render

## 📋 Chuẩn bị

1. **Đảm bảo bạn đã có:**
   - Tài khoản GitHub
   - Tài khoản Render (miễn phí)
   - Token Discord Bot
   - ID Discord của bạn (để làm admin)

## 🔧 Cấu hình Local

1. **Cài đặt dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Tạo file .env:**
   ```bash
   cp .env.example .env
   ```

3. **Chỉnh sửa .env với thông tin của bạn:**
   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   ADMIN_IDS=your_discord_user_id
   ```

4. **Test bot local:**
   ```bash
   python start.py
   ```

## 📤 Deploy lên Render

### Cách 1: Sử dụng render.yaml (Tự động)

1. **Push code lên GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Deploy bot to Render"
   git branch -M main
   git remote add origin https://github.com/username/repo-name.git
   git push -u origin main
   ```

2. **Tạo Web Service trên Render:**
   - Đăng nhập vào [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect GitHub repository của bạn
   - Render sẽ tự động đọc file `render.yaml`
   - Click "Deploy Web Service"

### Cách 2: Cấu hình thủ công

1. **Tạo Web Service:**
   - Name: `discord-bot` (hoặc tên bạn muốn)
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

2. **Test bot:**
   - Mời bot vào server Discord của bạn
   - Sử dụng lệnh `/menu_new` để test menu mới
   - Sử dụng lệnh `/menu` để test menu cũ

## 🎮 Lệnh mới

- `/menu_new`: Menu với giao diện đẹp và interactive buttons
- `/menu`: Menu gốc (vẫn giữ lại để tương thích)

## 🛠 Troubleshooting

### Bot không khởi động
- Kiểm tra log trong Render dashboard
- Đảm bảo environment variables được set đúng
- Kiểm tra token Discord có hợp lệ không

### Lệnh không hoạt động
- Đảm bảo bot đã được invite vào server với đúng permissions
- Kiểm tra lệnh đã được sync chưa (có thể mất vài phút sau khi deploy)
- F5 Discord để refresh lệnh

### Memory issues
- Nâng cấp plan trên Render (nếu cần)
- Tối ưu code để giảm memory usage

## 📝 Notes

- Bot sử dụng plan free của Render
- Free plan có thể sleep sau 15 phút không hoạt động
- Bot sẽ tự động restart khi có request mới
- Để bot hoạt động 24/7, cần upgrade plan

---

Made with ❤️ by zawng dep chai