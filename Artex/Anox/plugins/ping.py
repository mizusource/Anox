from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from strings.filters import command
from AnonX import app
from AnonX.core.call import Anon
from AnonX.utils import bot_sys_stats
from AnonX.utils.decorators.language import language
from AnonX.utils.inline.play import close_keyboard

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    command(PING_COMMAND)
)
@language
async def ping_com(client, message: Message, _):
    Idd = app.id
    response = await message.reply_photo(
        photo=f"https://telegra.ph/file/dfb0a1577ee284d99ce86.jpg",
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Anon.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            resp, app.name, UP, RAM, CPU, DISK, pytgping
        ),
    )