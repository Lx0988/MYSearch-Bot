import logging
import pyrogram
from bot.translation import script
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters, enums
from bot.database import temp

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

BUTTONS = {}

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()
    elif query.data == "start":
        buttons = [[
            InlineKeyboardButton('π π²πΎπΊππΌπ π', switch_inline_query_current_chat='')
            ],[
            InlineKeyboardButton('π π΄ππ½πΊππΎπ', url='https://t.me/DFF_UPDATES'),            
            InlineKeyboardButton('π€ π π»πππ', callback_data='about')
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
            InlineKeyboardButton('π π΄ππ½πΊππΎπ', url='https://t.me/DFF_UPDATES'),
            InlineKeyboardButton('π₯ π¦ππππ', url='https://t.me/Hollywood_0980')
        ], [
            InlineKeyboardButton('π π‘πΊπΌπ', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )   

