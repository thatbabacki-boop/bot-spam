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
        ]
    )
    async def facebook_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(
            "📘 **FACEBOOK**\n"
            "• `/anhtop` - Treo top ảnh\n"
            "• `/nhaytop` - Treo nhây top tin nhắn\n"
            "• `/reostr` - Réo story",
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
        ]
    )
    async def messenger_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(
            "💬 **MESSENGER**\n"
            "• `/treomess` - Treo tin nhắn\n"
            "• `/nhaynamebox` - Nhây đổi tên box\n"
            "• `/nhaytagmess` - Nhây tag Messenger\n"
            "• `/listbox` - Lấy danh sách nhóm\n"
            "• `/treoanhmess` - Treo ảnh Messenger",
            ephemeral=True
        )

    @discord.ui.select(
        placeholder="🌀 Chọn chức năng Discord...",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="💭 Treo ngôn", description="Treo tin nhắn Discord", emoji="💭"),
            discord.SelectOption(label="🎭 Nhây tag fake soạn", description="Spam tag Discord", emoji="🎭"),
        ]
    )
    async def discord_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.send_message(
            "🌀 **DISCORD**\n"
            "• `/treodis` - Treo ngôn Discord\n"
            "• `/nhaydis` - Nhây tag Discord",
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