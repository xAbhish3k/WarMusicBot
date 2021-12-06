import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "xAbhish3k")
ALIVE_NAME = getenv("ALIVE_NAME", "xAbhish3k")
BOT_USERNAME = getenv("BOT_USERNAME", "camillamusicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "warbotzsupport")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "warbotz")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheWarBotZ")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/8bad7843782ee1a1cc4f0.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "540000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/xAbhish3k/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/cd573e828a010ef46534c.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/a91c17a11f1e3a9cf4a3e.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/e2250edc9ec36f489db02.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/554b047bd413dcd518cdf.png")
