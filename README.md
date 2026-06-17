# 🤖 Super Ultimate Bot 3.0 - Multi-Platform Tool

Bot Discord đa nền tảng **Siêu Tối Thượng Version 3.0** với đầy đủ tính năng: Facebook, Messenger, Discord, Zalo, Telegram, Instagram, Gmail, SMS, WeChat + Tích hợp AI & Công nghệ mới!

## 🚀 Tính Năng Mới & Cải Tiến

### 🌟 **Version 3.0 Super Ultimate**
- ✅ **Menu tương tác đẹp mắt** với 6 danh mục
- ✅ **Tích hợp AI Nova Pro** - Trí tuệ nhân tạo
- ✅ **Discord Poll & Thread** - Tạo poll và thread tự động
- ✅ **Facebook Theme Management** - Đổi theme Messenger
- ✅ **Facebook Group Management** - Quản lý nhóm Facebook
- ✅ **Hệ thống Admin đa cấp** - Quản lý admin phụ
- ✅ **Bot Nhái thông minh** - Nhái tin nhắn v1 & v2
- ✅ **Rate Limiting** - Tối ưu hiệu suất
- ✅ **Tối ưu cho Render** - Deploy dễ dàng

### 📘 Facebook & Messenger
- 🖼️ Treo top ảnh
- 💬 Treo nhây top tin nhắn
- 📸 Réo story
- 👥 **Quản lý Facebook Group** - Thêm user vào group
- 🎨 **Đổi theme Messenger** - MQTT Theme Client
- 💭 Treo ngôn tin nhắn
- 🏷️ Nhây réo tên
- 📢 Nhây tag Messenger
- 📋 Lấy danh sách nhóm
- ✏️ Nhây đổi tên box
- 🖼️ Treo ảnh Messenger
- 📊 **Spam Poll Messenger**
- 💥 **Combo siêu mạnh Messenger**
- 🔄 **Đổi tên thành viên box**

### 🌀 Discord
- 💭 Treo ngôn Discord
- 🎭 Nhây tag fake soạn
- 🎵 **Spam Audio Discord**
- 📊 **Treo Poll Discord** - Với rate limiting
- 🧵 **Tạo Thread tự động** - Multi-thread support
- ⚡ **All Nhây Discord** - Tất cả chức năng

### 📱 Zalo
- 💭 Treo ngôn Zalo
- 🎭 Nhây tag fake soạn (box)
- 📊 Treo bình chọn + tag
- 🎨 Treo sticker
- 🎭 Nhây tag fake soạn (1-1)
- ✏️ Nhây đổi tên box Zalo

### 📢 Telegram
- 📢 Treo ngôn kèm ảnh

### 📸 Instagram
- 📸 Treo ngôn Instagram

### 📧 Gmail
- 📧 Treo spam Gmail

### 📲 SMS
- 📲 Treo spam OTP SMS (60+ services)

### 💼 WeChat
- 💼 Treo spam tin nhắn WeChat

### �️ Quản lý & Tiện Ích
- 👤 **Hệ thống Admin đa cấp** - Thêm/xóa/list admin phụ
- 🤖 **AI Nova Pro** - Hỏi AI tích hợp
- 💬 **Bot Nhái v1 & v2** - Nhái tin nhắn thông minh
- 🔍 **Check UID** - Check acc Discord bằng UID
- 📋 **ID Kênh** - Lấy ID kênh Discord
- 🔧 Check cookie Facebook

## 📦 Cài đặt

### Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Các dependencies chính:
- `discord.py>=2.0.0` - Discord API
- `aiohttp>=3.8.0` - Async HTTP client
- `requests>=2.28.0` - HTTP library
- `instagrapi>=2.0.0` - Instagram API
- `paho-mqtt>=1.6.0` - MQTT cho Facebook Messenger
- `colorama>=0.4.6` - Terminal colors
- `pycryptodome>=3.15.0` - Encryption
- `pillow>=8.1.1` - Image processing

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

## 🎮 Sử dụng

### Menu mới siêu đẹp
- Sử dụng lệnh `/menu_new` để xem menu tương tác mới
- Sử dụng lệnh `/menu` để xem menu gốc (để tương thích)

### Các lệnh mới
- **Facebook**: `/addgroup`, `/setnenmess`, `/theme_mess`
- **Messenger**: `/nhaypollmess`, `/combomess`, `/namechange`
- **Discord**: `/treoaudio`, `/treopolldis`, `/createthread`, `/allnhaydis`
- **Admin**: `/addadmin`, `/xoaadmin`, `/listadmin`, `/nova`, `/say1`, `/say2`
- **Tiện ích**: `/checkuid`, `/idkenh`

### File cấu hình
- `nhay.txt` - File nội dung nhây
- `nhay1.txt` - File nội dung nhây phụ
- `users.json` - Database users
- `ngonmess_data/` - Thư mục dữ liệu Messenger

## 🌐 Deploy lên Render (Tối ưu cho Version 3.0)

1. **Push code lên GitHub**
   ```bash
   git init
   git add .
   git commit -m "Super Ultimate Bot 3.0 - Multi-platform with AI"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

2. **Kết nối repository với Render**
   - Đăng nhập vào [Render](https://render.com)
   - Click "New +" -> "Web Service"
   - Kết nối GitHub repository của bạn
   - Render sẽ tự động phát hiện file `render.yaml` (đã tối ưu cho v3.0)

3. **Cấu hình Environment Variables**
   Trong dashboard của Render, thêm các environment variables:
   - `DISCORD_TOKEN`: Token bot Discord của bạn
   - `ADMIN_IDS`: ID admin (ngăn cách bằng dấu phẩy)

4. **Deploy**
   - Click "Deploy Web Service"
   - Render sẽ tự động build và deploy bot của bạn
   - Bot sẽ tự động sync commands khi online

## 🎮 Sử dụng

- Sử dụng lệnh `/menu` để xem danh sách chức năng
- Sử dụng `/` trước tên lệnh để thực thi chức năng tương ứng
- Một số chức năng yêu cầu quyền admin

## 📝 Lưu ý

- Bot chỉ hoạt động với các tài khoản có quyền phù hợp
- Sử dụng bot có trách nhiệm và tuân thủ Terms of Service của các nền tảng
- Không sử dụng cho các mục đích spam hoặc gây phiền toái
- **Version 3.0** yêu cầu Python 3.8+ và các dependencies mới
- MQTT theme có thể yêu cầu cookie Facebook hoạt động
- Discord Poll và Thread yêu cầu quyền Bot Admin trong server

## 🛠 Bảo trì & Hỗ trợ

- **Phiên bản**: Super Ultimate Bot 3.0
- **Phát triển bởi**: zawng dep chai
- **Release**: June 2026
- **Support**: Đa nền tảng - Tối ưu - Tích hợp AI

## 🎉 Tính Năng Đặc Biệt

### 🤖 AI Integration
- **Nova Pro AI**: Hỗ trợ hỏi trả lời thông minh
- **Smart Reply**: Bot nhái với context

### 🚀 Performance
- **Rate Limiting**: Tối ưu hiệu suất với RateLimiter class
- **Async Processing**: Xử lý bất đồng bộ cao
- **Memory Management**: Tối ưu bộ nhớ với garbage collection

### 🔒 Security
- **Environment Variables**: Bảo mật token và credentials
- **Admin System**: Đa cấp với admin phụ
- **User Management**: Database users với thời hạn

---

**Super Ultimate Bot 3.0** - Đa nền tảng, Tối ưu, Tích hợp AI

Made with ❤️ by zawng dep chai