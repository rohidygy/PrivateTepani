import asyncio
from datetime import datetime

from pyrogram.types import InlineKeyboardMarkup
from pytz import timezone

from ubot import bot, ubot
from ubot.config import LOG_UBOT
from ubot.core.database import monggo
from ubot.core.helpers import MSG, Button


async def expired_userbot(X):
    try:
        time = datetime.now(timezone("Asia/Jakarta")).strftime("%d-%m-%Y")
        exp = (monggo.get_expired_date(X.me.id)).strftime("%d-%m-%Y")
        if time == exp:
            for chat in monggo.get_chat(X.me.id):
                monggo.remove_chat(X.me.id, chat)
            monggo.rm_all(X.me.id)
            monggo.remove_ubot(X.me.id)
            monggo.rem_expired_date(X.me.id)
            ubot._get_my_id.remove(X.me.id)
            ubot._ubot.remove(X)
            await X.log_out()
            expired_text = MSG.EXPIRED_MSG_BOT(X)
            expired_button = Button.expired_button_bot()
            await bot.send_message(
                LOG_UBOT,
                expired_text,
                reply_markup=InlineKeyboardMarkup(expired_button),
            )
    except Exception as e:
        print(f"Error: {str(e)}")


async def expiredUserbots():
    while True:
        tasks = [expired_userbot(X) for X in ubot._ubot]
        await asyncio.gather(*tasks)
        await asyncio.sleep(60)
