from ubot import *

__MODULE__ = "ᴛʀᴀɴꜱʟᴀᴛᴇ"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛʀᴀɴꜱʟᴀᴛᴇ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴛʀ</ᴄᴏᴅᴇ> [ʀᴇᴘʟʏ/ᴛᴇxᴛ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴᴇʀᴊᴇᴍᴀʜᴋᴀɴ ᴛᴇxᴛ ᴅᴇɴɢᴀɴ ᴋᴏᴅᴇ ɴᴇɢᴀʀᴀ ʏᴀɴɢ ᴅɪɪɴɢɪɴᴋᴀɴ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ꜱᴇᴛ_ʟᴀɴɢ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ʙᴀʜᴀꜱᴀ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴛᴛꜱ</ᴄᴏᴅᴇ> [ʀᴇᴘʟʏ/ᴛᴇxᴛ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴᴇʀᴊᴇᴍᴀʜᴋᴀɴ ᴛᴇxᴛ ᴅᴇɴɢᴀɴ ᴋᴏᴅᴇ ɴᴇɢᴀʀᴀ ʏᴀɴɢ ᴅɪɪɴɢɪɴᴋᴀɴ ꜱᴇʀᴛᴀ ᴍᴇʀᴜʙᴀʜɴʏᴀ ᴍᴇɴᴊᴀᴅɪ ᴘᴇꜱᴀɴ ꜱᴜᴀʀᴀ.
"""


@PY.UBOT("tts", sudo=True)
async def _(client, message):
    await tts_cmd(client, message)


@PY.UBOT("tr|tl", sudo=True)
async def _(client, message):
    await tr_cmd(client, message)


@PY.UBOT("set_lang", sudo=True)
async def _(client, message):
    await set_lang_cmd(client, message)


@PY.INLINE("^ubah_bahasa")
@INLINE.QUERY
async def _(client, inline_query):
    await ubah_bahasa_inline(client, inline_query)


@PY.CALLBACK("^set_bahasa")
@INLINE.DATA
async def _(client, callback_query):
    await set_bahasa_callback(client, callback_query)
