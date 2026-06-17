import discord

class MenuView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.select(
        placeholder="📘 Chọn chức năng Facebook...",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="🖼️ Treo top ảnh", description="Treo ảnh lên top Facebook", emoji="🖼️"),
            discord.SelectOption(label="💬 Treo nhây top tin nhắn", description="Treo nhây lên top tin nhắn", emoji="💬"),
            discord.SelectOption(label="📸 Réo story", description="Réo story Facebook", emoji="📸"),
            discord.SelectOption(label="👥 Quản lý Group", description="Thêm user vào Facebook group", emoji="👥"),
            discord.SelectOption(label="🎨 Đổi nền Messenger", description="Đổi theme Facebook Messenger", emoji="🎨"),
        ]
    )
    async def facebook_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(
            "📘 **FACEBOOK & MESSENGER**\n"
            "• `/anhtop` - Treo top ảnh\n"
            "• `/nhaytop` - Treo nhây top tin nhắn\n"
            "• `/reostr` - Réo story\n"
            "• `/addgroup` - Thêm user vào Facebook group\n"
            "• `/setnenmess` - Đổi nền Messenger\n"
            "• `/theme_mess` - Chọn theme Messenger",
            ephemeral=True
        )

    @discord.ui.select(
        placeholder="💬 Chọn chức năng Messenger...",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="💭 Treo ngôn", description="Treo tin nhắn Messenger", emoji="💭"),
            discord.SelectOption(label="🏷️ Nhây réo tên", description="Nhây réo tên Messenger", emoji="🏷️"),
            discord.SelectOption(label="📢 Nhây tag Messenger", description="Spam tag Messenger", emoji="📢"),
            discord.SelectOption(label="📋 Lấy danh sách nhóm", description="Lấy danh sách nhóm Messenger", emoji="📋"),
            discord.SelectOption(label="✏️ Nhây đổi tên box", description="Nhây đổi tên box Messenger", emoji="✏️"),
            discord.SelectOption(label="🖼️ Treo ảnh Messenger", description="Spam ảnh Messenger", emoji="🖼️"),
            discord.SelectOption(label="📊 Spam Poll Messenger", description="Tạo poll trong Messenger", emoji="📊"),
            discord.SelectOption(label="💥 Combo Messenger", description="Combo siêu mạnh Messenger", emoji="💥"),
            discord.SelectOption(label="🔄 Đổi tên thành viên", description="Đổi tên thành viên box", emoji="🔄"),
        ]
    )
    async def messenger_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(
            "💬 **MESSENGER**\n"
            "• `/treomess` - Treo tin nhắn\n"
            "• `/nhaynamebox` - Nhây đổi tên box\n"
            "• `/nhaytagmess` - Nhây tag Messenger\n"
            "• `/listbox` - Lấy danh sách nhóm\n"
            "• `/treoanhmess` - Treo ảnh Messenger\n"
            "• `/nhaypollmess` - Spam poll Messenger\n"
            "• `/combomess` - Combo siêu mạnh\n"
            "• `/namechange` - Đổi tên thành viên",
            ephemeral=True
        )

    @discord.ui.select(
        placeholder="🌀 Chọn chức năng Discord...",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="💭 Treo ngôn", description="Treo tin nhắn Discord", emoji="💭"),
            discord.SelectOption(label="🎭 Nhây tag fake soạn", description="Spam tag Discord", emoji="🎭"),
            discord.SelectOption(label="🎵 Spam Audio", description="Spam audio Discord", emoji="🎵"),
            discord.SelectOption(label="📊 Treo Poll Discord", description="Treo poll Discord", emoji="📊"),
            discord.SelectOption(label="🧵 Tạo Thread", description="Tạo thread tự động", emoji="🧵"),
            discord.SelectOption(label="⚡ All Nhây Discord", description="Tất cả chức năng nhây Discord", emoji="⚡"),
        ]
    )
    async def discord_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(
            "🌀 **DISCORD**\n"
            "• `/treodis` - Treo ngôn Discord\n"
            "• `/nhaydis` - Nhây tag Discord\n"
            "• `/treoaudio` - Spam audio Discord\n"
            "• `/treopolldis` - Treo poll Discord\n"
            "• `/createthread` - Tạo thread tự động\n"
            "• `/allnhaydis` - All chức năng nhây Discord",
            ephemeral=True
        )

    @discord.ui.select(
        placeholder="📱 Chọn chức năng Zalo...",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="💭 Treo ngôn", description="Treo tin nhắn Zalo", emoji="💭"),
            discord.SelectOption(label="🎭 Nhây tag fake soạn (box)", description="Spam tag Zalo box", emoji="🎭"),
            discord.SelectOption(label="📊 Treo bình chọn + tag", description="Treo poll Zalo", emoji="📊"),
            discord.SelectOption(label="🎨 Treo sticker", description="Treo sticker Zalo", emoji="🎨"),
            discord.SelectOption(label="🎭 Nhây tag fake soạn (1-1)", description="Spam tag Zalo 1-1", emoji="🎭"),
            discord.SelectOption(label="✏️ Nhây đổi tên box", description="Nhây đổi tên box Zalo", emoji="✏️"),
        ]
    )
    async def zalo_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(
            "📱 **ZALO**\n"
            "• `/treozalo` - Treo ngôn Zalo\n"
            "• `/nhayzalo` - Nhây tag Zalo\n"
            "• `/treopollzl` - Treo bình chọn\n"
            "• `/treosticker` - Treo sticker\n"
            "• `/nhaytagzalo` - Nhây tag Zalo 1-1\n"
            "• `/nhaynameboxzl` - Nhây đổi tên box Zalo",
            ephemeral=True
        )

    @discord.ui.select(
        placeholder="🌐 Chọn nền tảng khác...",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="📢 Telegram", description="Treo ngôn Telegram kèm ảnh", emoji="📢"),
            discord.SelectOption(label="📸 Instagram", description="Treo ngôn Instagram", emoji="📸"),
            discord.SelectOption(label="📧 Gmail", description="Treo spam Gmail", emoji="📧"),
            discord.SelectOption(label="📲 SMS", description="Treo spam OTP SMS", emoji="📲"),
            discord.SelectOption(label="💼 WeChat", description="Treo spam tin nhắn WeChat", emoji="💼"),
            discord.SelectOption(label="🔧 Tiện ích", description="Check cookie Facebook", emoji="🔧"),
        ]
    )
    async def other_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        selected = select.values[0]
        if selected == "📢 Telegram":
            msg = "• `/treotele` - Treo ngôn Telegram"
        elif selected == "📸 Instagram":
            msg = "• `/treoig` - Treo ngôn Instagram"
        elif selected == "📧 Gmail":
            msg = "• `/treogmail` - Treo spam Gmail"
        elif selected == "📲 SMS":
            msg = "• `/treosms` - Treo spam OTP SMS"
        elif selected == "💼 WeChat":
            msg = "• `/treowechat` - Treo spam tin nhắn WeChat"
        else:
            msg = "• `/checkcookie` - Check cookie Facebook"
        
        await interaction.response.send_message(f"🌐 **KHÁC**\n{msg}", ephemeral=True)

    @discord.ui.select(
        placeholder="🛠️ Quản lý & Tiện ích...",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="👤 Quản lý Admin", description="Thêm/xóa admin phụ", emoji="👤"),
            discord.SelectOption(label="🤖 AI Nova Pro", description="Hỏi AI Nova Pro", emoji="🤖"),
            discord.SelectOption(label="💬 Bot Nhái", description="Bot nhái tin nhắn", emoji="💬"),
            discord.SelectOption(label="🔍 Check UID", description="Check acc Discord bằng UID", emoji="🔍"),
            discord.SelectOption(label="📋 ID Kênh", description="Lấy ID kênh Discord", emoji="📋"),
        ]
    )
    async def admin_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(
            "🛠️ **QUẢN LÝ & TIỆN ÍCH**\n"
            "• `/addadmin` - Thêm admin phụ\n"
            "• `/xoaadmin` - Xóa admin phụ\n"
            "• `/listadmin` - Danh sách admin phụ\n"
            "• `/nova` - Hỏi AI Nova Pro\n"
            "• `/say1` - Bot nhái v1\n"
            "• `/say2` - Bot nhái v2\n"
            "• `/checkuid` - Check acc Discord bằng UID\n"
            "• `/idkenh` - Lấy ID kênh Discord",
            ephemeral=True
        )

    @discord.ui.button(
        label="📊 Thông tin Bot",
        style=discord.ButtonStyle.secondary,
        custom_id="info_bot"
    )
    async def info_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="📊 THÔNG TIN BOT",
            description=(
                "### 👑 **Super Ultimate Bot**\n"
                "• **Version:** `3.0 Ultimate`\n"
                "• **Ngôn ngữ:** Python · discord.py\n"
                "• **Tính năng:** Đa nền tảng & Tối ưu\n"
                "━━━━━━━━━━━━━━━━━━\n\n"
                "### 🚀 **Tính Năng Nổi Bật**\n"
                "› Menu tương tác đẹp mắt\n"
                "› Support Facebook, Messenger, Discord, Zalo, Telegram, Instagram, Gmail, SMS, WeChat\n"
                "› Hệ thống admin đa cấp\n"
                "› Tích hợp AI Nova Pro\n"
                "› Discord Poll & Thread\n"
                "› Facebook Theme & Group Management\n"
                "› Tối ưu cho Render deployment\n"
                "━━━━━━━━━━━━━━━━━━\n\n"
                "🛠 **Bot by zawng dep chai | Super Ultimate Edition**"
            ),
            color=discord.Color.from_rgb(88, 101, 242)
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.set_footer(text="🛠 Super Ultimate Bot by zawng dep chai")
        await interaction.response.send_message(embed=embed, ephemeral=True)