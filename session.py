from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 38017100
api_hash = "0d1ee14a452e04c86c4dd37709bb7a2f"

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())