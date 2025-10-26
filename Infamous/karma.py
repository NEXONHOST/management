# <============================================== IMPORTS =========================================================>
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://files.catbox.moe/1jvj34.jpg",
    "https://files.catbox.moe/idjyr8.jpg",
]

PM_START_TEXT = (
    "✨ *ɪ ᴀᴍ 𝚁𝚘𝚜𝚜𝚢, ᴀ ɢᴇɴꜱʜɪɴ ɪᴍᴘᴀᴄᴛ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ "
    "ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ "
    "ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"
)

HELP_STRINGS = """
🫧 *ROSSY* 🫧 [ㅤ](https://files.catbox.moe/xxiylg.jpg)

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""

# <============================================== BUTTONS =========================================================>
START_BTN = [
    [InlineKeyboardButton("⇦ ADD ME ⇨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
    [InlineKeyboardButton("HELP", callback_data="extra_command_handler")],
    [InlineKeyboardButton("DETAILS", callback_data="Miko_")],
    [InlineKeyboardButton("CREATOR", url=f"tg://user?id={OWNER_ID}")],
]

GROUP_START_BTN = [
    [InlineKeyboardButton("⇦ ADD ME ⇨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
    [
        InlineKeyboardButton("SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton("CREATOR", url=f"tg://user?id={OWNER_ID}")
    ],
]

ALIVE_BTN = [
    [
        InlineKeyboardButton("UPDATES", url="https://t.me/Hydra_Updates"),
        InlineKeyboardButton("SUPPORT", url="https://t.me/hydraXsupport"),
    ],
    [InlineKeyboardButton("⇦ ADD ME ⇨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
]

# <============================================== /start HANDLER =========================================================>
@Client.on_message(filters.command("start"))
async def start(client, message):
    # Check chat type
    if message.chat.type == "private":
        markup = InlineKeyboardMarkup(START_BTN)
        text = PM_START_TEXT.format(message.from_user.first_name)
    else:
        markup = InlineKeyboardMarkup(GROUP_START_BTN)
        text = f"✨ Hello {message.from_user.first_name}! I am Rossy 🤖"

    # Send start message with buttons
    await message.reply_text(
        text=text,
        reply_markup=markup,
        disable_web_page_preview=True
    )
