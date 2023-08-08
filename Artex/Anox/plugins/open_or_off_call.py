from pyrogram import Client, filters
import asyncio
from pyrogram.types import Message
from AnonX import app

@app.on_message(filters.video_chat_started)
async def brah(client, message):
       await message.reply("تم بدء المحادثه الصوتيه")
@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
       await message.reply("تم انهاء المحادثه الصوتيه")
@app.on_message(filters.video_chat_members_invited)
async def fuckoff(client, message):
           text = f"قام : {message.from_user.mention}\nبدعوة : "
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}\nالى المحادثه الصوتيه 😉")
           except:
             pass
