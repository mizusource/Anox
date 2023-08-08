from config import LOG, LOG_GROUP_ID
from AnonX import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnonX.utils.database import is_on_off


async def play_logs(message, client, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"https://t.me/{message.chat.username}"
        else:
            try:
                chatusername = await client.export_chat_invite_link(message.chat.id)
            except Exception as e:
                chatusername = "لايوجد"
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(f"{message.chat.title}", url=f"{chatusername}")],
        ])
        logger_text = f"""
**تم التشغيل في الجروب**

**ايدي الجروب:** [`{message.chat.id}`]
**اسم المستخدم:** {message.from_user.mention}
**يوزر المستخدم:** @{message.from_user.username}
**ايدي المستخدم:** `{message.from_user.id}`

**المطلوب:** {message.text}

**نوع التشغيل:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                reply_markup=keyboard,
                )
            except:
                pass
        return
