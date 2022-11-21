import logging
import pyrogram
from bot.translation import script
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters, enums
from bot.database import  temp, get_settings, save_group_settings, get_size
from bot.database.users_chats_db import db
from bot.database.ia_filterdb import Media

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

BUTTONS = {}

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
    elif query.data == "start":
        buttons = [[
            InlineKeyboardButton('🔎 𝖲𝖾𝖺𝗋𝖼𝗁 🔍', switch_inline_query_current_chat='')
            ],[
            InlineKeyboardButton('🔄 𝖴𝗉𝖽𝖺𝗍𝖾𝗌', url='https://t.me/DFF_UPDATES'),            
            InlineKeyboardButton('👤 𝖠𝖻𝗈𝗎𝗍', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer('Piracy Is Crime')
    elif query.data == "about":
        buttons = [[
            InlineKeyboardButton('🔄 𝖴𝗉𝖽𝖺𝗍𝖾𝗌', url='https://t.me/DFF_UPDATES'),
            InlineKeyboardButton('👥 𝖦𝗋𝗈𝗎𝗉', url='https://t.me/Hollywood_0980')
        ], [
            InlineKeyboardButton('🔙 𝖡𝖺𝖼𝗄', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )   

