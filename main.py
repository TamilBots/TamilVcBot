from os import environ
# import logging
from pyrogram import Client, idle

API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
SESSION_NAME = environ["SESSION_NAME"]

plugins = dict(
    root="plugins",
    include=[
        "vc." + environ["PLUGIN"],
        "ping",
        "sysinfo"
    ]
)

app = Client(SESSION_NAME, API_ID, API_HASH, plugins=plugins)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED by @redchipvcbot')
idle()
app.stop()
print('\n>>> USERBOT STOPPED by @redchipvcbot')

