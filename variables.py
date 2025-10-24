import os
import json

def safe_load_json(path, default=None):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default if default is not None else {}

def get_user_list(config_filename, key):
    path = os.path.join(os.getcwd(), "Mikobot", config_filename)
    data = safe_load_json(path, {})
    return data.get(key, [])

class Config(object):
    LOGGER = os.getenv("LOGGER", "True").lower() in ("1","true","yes")

    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    TOKEN = os.getenv("TOKEN", "")
    OWNER_ID = int(os.getenv("OWNER_ID", "0"))

    DATABASE_URL = os.getenv("DATABASE_URL", "")
    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

    EVENT_LOGS = int(os.getenv("EVENT_LOGS", "-100"))
    MESSAGE_DUMP = int(os.getenv("MESSAGE_DUMP", "-100"))
    SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "")
    SUPPORT_ID = int(os.getenv("SUPPORT_ID", "0"))
    DB_NAME = os.getenv("DB_NAME", "")

    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    DEMONS = get_user_list("elevated_users.json", "supports")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    BL_CHATS = []
    ALLOW_CHATS = os.getenv("ALLOW_CHATS", "True").lower() in ("1","true","yes")
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    BAN_STICKER = os.getenv("BAN_STICKER", "")
    TEMP_DOWNLOAD_DIRECTORY = "./"

class Production(Config):
    pass

class Development(Config):
    pass
