from pyrogram.types import InlineKeyboardButton as ib
from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# ============================================== CONSTANTS ==============================================
START_IMG = [
    "https://files.catbox.moe/1jvj34.jpg",
    "https://files.catbox.moe/idjyr8.jpg",
]

HEY_IMG = "https://files.catbox.moe/0lbgjt.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

FIRST_PART_TEXT = "✨ ʜᴇʟʟᴏ {} . . ."

PM_START_TEXT = (
    "✨ ɪ ᴀᴍ 𝚁𝚘𝚜𝚜𝚢, ᴀ ɢᴇɴꜱʜɪɴ ɪᴍᴘᴀᴄᴛ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ "
    "ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ "
    "ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ"
)

HELP_STRINGS = """
🫧 ROSSY 🫧 ㅤ

☉ Here, you will find a list of all the available commands.

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""

# ============================================== BUTTONS ==============================================
# 2x2 button layout for Private chat
START_BTN = [
    [
        ib("⇦ ADD ME ⇨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
        ib("CREATOR", url=f"tg://user?id={OWNER_ID}")
    ],
    [
        ib("HELP", callback_data="extra_command_handler"),
        ib("DETAILS", callback_data="Miko_")
    ]
]

# 2x2 button layout for Group chat
GROUP_START_BTN = [
    [
        ib("⇦ ADD ME ⇨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
        ib("CREATOR", url=f"tg://user?id={OWNER_ID}")
    ],
    [
        ib("HELP", callback_data="extra_command_handler"),
        ib("DETAILS", callback_data="Miko_")
    ]
]

# 2x2 button layout for Alive / Status
ALIVE_BTN = [
    [
        ib("⇦ ADD ME ⇨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
        ib("CREATOR", url=f"tg://user?id={OWNER_ID}")
    ],
    [
        ib("HELP", callback_data="extra_command_handler"),
        ib("DETAILS", callback_data="Miko_")
    ]
]
