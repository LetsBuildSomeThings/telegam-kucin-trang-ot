import configparser
import json
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)

api_id = 12223282
api_hash = 'dd27c92671e9b82b788c8b7d93716032'

client = TelegramClient('anon3', api_id, api_hash)

# Here you define the target channel that you want to listen to:
user_input_channel = 'https://t.me/TheMoonGroup'

@client.on(events.NewMessage(chats=user_input_channel))
async def NewMessageListener(event):
	message = event.message.message
	processMessage(message)


with client:
	client.run_until_disconnected()



