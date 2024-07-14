import os
import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("RJ"):
  load_dotenv("RJ")

API_ID = int(getenv("API_ID" "26965889"))
API_HASH = getenv("API_HASH" "f0f95dc1f56e849ebb4bf7b6c5cdc531")
BOT_TOKEN = getenv("BOT_TOKEN" "6509734752:AAHq0WRlHlA5oQurEHbzEwdjnBLhrRcE8YY")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Devilmusic:poLgMY6bWVhpyMGG@cluster0.0bogl8n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID" "-1001870600508"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "❦︎𝐃𝐡𝐚𝐝𝐤𝐚𝐧❥︎𝗠𝘂𝘀𝗶𝗰❦︎𝗕𝗼𝘁シ︎")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5606562055").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/sankidevil/Dmena_musicBot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/devilxdy")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/devilxdy")
SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "540"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "540"))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "7cfbb3efeacf40a9a103fd8eb55c6b30")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "3abee1a7d53b42adaaf14fb2f1a00cff")
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
SET_CMDS = getenv("SET_CMDS", False)
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "AQARyWiWsDLj_hOHNyU8GuFk8vk0yukLDD6cIPJo5T3aGnVQjK48od5AGwdPcdzKNzWfg29HTg4iO5_XMIZ1TWGPxEpbMs82nWCweno0wuavmXlIMxyVCeT6JWppWirD0fU5igLTgfUMqKpBU4yBCtXAG0-ZTsHJiBpWjxtE6Q25P09ert42aQBKGo6Jb38QSMikw5Xzw4AfxhENkzNE8qSoFp50RRv4oar0n7_TXuJRlm_BV305psklxj0qrihtC-8Cyj78PLL0pXizTjH21NvdcHL77DBngPZf7IhosUSko-tu9jg8mSe7CLKGnf-L_I08kt4OEA0bFRFSEohz7WbTAAAAAU4tWQcA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

############################
COMMAND_PREFIXES.append('')
OWNER_ID.append(5368154755)
############################
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
############################

START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/927fbe11f6a3f3f1cb835.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/d472458ae900a212af32d.jpg")

PLAYLIST_IMG_URL = "https://telegra.ph//file/48b76e483720f1c949992.jpg"
GLOBAL_IMG_URL = "https://telegra.ph//file/54a0cc0a38e242df6312f.jpg"
STATS_IMG_URL = "https://telegra.ph//file/6cfd7340e36d061fefd17.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph//file/aaa234fa0f64fb61bc77d.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph//file/55d053f98972397ed2545.jpg"
STREAM_IMG_URL = "https://telegra.ph//file/26488a81d1dac3a74b1fe.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph//file/45aa319424afac672cc4f.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph//file/fa1867b8d0067db7e3132.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph//file/d4a38d19f5472aba24324.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph//file/dc12b72d9a0797d2de327.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph//file/5706bbc7df4c5ab589220.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "resources/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/e745fdaf1966f228582dc.jpg"

if START_IMG_URL:
    if START_IMG_URL != "resources/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/e745fdaf1966f228582dc.jpg"
