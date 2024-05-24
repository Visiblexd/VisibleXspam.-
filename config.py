import logging

from telethon import TelegramClient

from os import getenv
from AltBots.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 12160204
API_HASH = "944053be988f83c2554a2b40429e90d7"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", visible)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "9d358c5e-3baf-465d-b00a-663e8bbf0db4")

BOT_TOKEN = getenv("BOT_TOKEN", default=6817432360:AAGwc-R5zH_sg6i6uFx7LiB1BZrQqa4gxXU)
BOT_TOKEN2 = getenv("BOT_TOKEN2", default=7004631977:AAHxPr6ZiNcTRHB3VQuHa6NrkXnzN88zUEU)
BOT_TOKEN3 = getenv("BOT_TOKEN3", default=6556220447:AAFtsPLo6QhU7nwH-Ui-5-iBvvOci56y9l8)
BOT_TOKEN4 = getenv("BOT_TOKEN4", default=6313502587:AAFtNpL-zvk34GDjIdjgTUBoxeazK7ij8_0)
BOT_TOKEN5 = getenv("BOT_TOKEN5", default=6355897298:AAFEwj9VF_6eOpqBxG6KBY-X5ST8owWs5HY)
BOT_TOKEN6 = getenv("BOT_TOKEN6", default=6619413961:AAEs_sZg8y6peBMx9P3de09hiQFzi2cx58A)
BOT_TOKEN7 = getenv("BOT_TOKEN7", default=6972036510:AAFlmfgULKN7PSgUx2LXxMEM-ZB9uOdmDYk)
BOT_TOKEN8 = getenv("BOT_TOKEN8", default=7172493504:AAGftG6pXMCvPTYQlN5DKVApheJXUn_YOoA)
BOT_TOKEN9 = getenv("BOT_TOKEN9", default=7057911906:AAFsCWUS9D5RluXxKG77PtgzJMFkhKmdwg0)
BOT_TOKEN10 = getenv("BOT_TOKEN10", default=7088983877:AAHHeQX9_mei2g1iDKkzEyFAmepao9Lgsm4)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default"6348268237").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="70489 22897"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
