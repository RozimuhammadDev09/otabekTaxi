from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 32924078
api_hash = "5fb624acedb64de522eff541a4b6d7f5"

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())