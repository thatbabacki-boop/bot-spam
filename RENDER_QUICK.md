# ⚡ Render Setup Nhanh - 5 Bước

## 🎯 BƯỚC 1: Đăng Ký (2 Phút)

1. Vào: **https://render.com**
2. Click **"Sign Up"**
3. Chọn **"Continue with GitHub"**
4. Authorize truy cập GitHub

## 🎯 BƯỚC 2: Tạo Web Service (1 Phút)

1. Click **"New+"** → **"Web Service"**
2. Chọn repository GitHub của bạn
3. Render tự động đọc `render.yaml`
4. Tên service: `super-ultimate-bot-3`

## 🎯 BƯỚC 3: Environment Variables (2 Phút)

Thêm vào **"Environment"** section:

| Key | Value | Type |
|-----|-------|------|
| `DISCORD_TOKEN` | Token Discord của bạn | Secret |
| `ADMIN_IDS` | ID Discord admin của bạn | Secret |
| `PYTHON_VERSION` | `3.9.0` | General |

## 🎯 BƯỚC 4: Deploy (1 Phút)

1. Click **"Create Web Service"**
2. Đợi 3-5 phút để build
3. Xem progress trong tab **"Events"**

## 🎯 BƯỚC 5: Kiểm Tra (1 Phút)

1. Xem **"Logs"** tab
2. Tìm message: `Bot đã online và đã sync slash command`
3. Test bot trên Discord với `/menu_new`

## ✅ HOÀN THÀNH!

**Bot sẽ online với:**
- ✅ Menu 6 categories
- ✅ AI Integration
- ✅ Facebook Management
- ✅ Discord Poll & Thread
- ✅ Performance tối ưu

---

**Xem chi tiết:** `RENDER_SETUP.md`