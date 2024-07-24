from ubot import *

__MODULE__ = "ᴄᴏᴘʏ"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏᴘʏ

• ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴄᴏᴘʏ</ᴄᴏᴅᴇ> [ʟɪɴᴋ]
• ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ᴘᴇꜱᴀɴ ᴍᴇʟᴀʟᴜɪ ʟɪɴᴋ ᴛᴇʟᴇɢʀᴀᴍ.
  """


@PY.BOT("copy")
async def _(client, message):
    await copy_bot_msg(client, message)


@PY.UBOT("copy", sudo=True)
async def _(client, message):
    await copy_ubot_msg(client, message)


@PY.UBOT("ccopy")
async def _(client, message):
    await cancel_nyolong(client, message)


@PY.INLINE("^get_msg")
@INLINE.QUERY
async def _(client, inline_query):
    await copy_inline_msg(client, inline_query)


@PY.CALLBACK("^copymsg")
@INLINE.DATA
async def _(client, callback_query):
    await copy_callback_msg(client, callback_query)
