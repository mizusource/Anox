from typing import Union
from strings import get_command
from strings.filters import command
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message
import config
from config import BANNED_USERS
from strings import get_command, get_string, helpers
from AnonX import app
from AnonX.misc import SUDOERS
from AnonX.utils import help2_pannel
from AnonX.utils.database import get_lang, is_commanddelete_on
from AnonX.utils.decorators.language import (LanguageStart,
                                                  languageCB)
from AnonX.utils.inline.help2 import (help2_back_markup,
                                          private_help2_panel)

@app.on_callback_query(
    filters.regex("hawl") & ~BANNED_USERS
)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help2_pannel(_, True)
        if update.message.photo:
            await update.edit_message_text(
                _["help_11"], reply_markup=keyboard
            )
        else:
            await update.edit_message_text(
                _["help_11"], reply_markup=keyboard
            )
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(update.chat.id):
            try:
                await update.delete()
            except:
                pass
        Idd = app.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help2_pannel(_)
        async for photo in client.iter_profile_photos(Idd, limit=1):
                    await update.reply_photo(photo.file_id, caption=_["help_11"], reply_markup=keyboard)
