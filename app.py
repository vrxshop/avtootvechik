import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
session_string = os.environ['SESSION_STRING']
REPLY_TEXT = os.environ.get('REPLY_TEXT', 'Привет! Напиши сюда: https://t.me/твой_чат')

client = TelegramClient(StringSession(session_string), api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        if event.sender and not event.sender.bot:
            await event.reply(REPLY_TEXT)
            print(f"[+] Ответил: {event.sender_id}")

print("Автоответчик запущен...")
client.start()
client.run_until_disconnected()
