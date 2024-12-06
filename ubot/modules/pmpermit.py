from ubot import *

__MODULE__ = "Pmpermit"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘᴍᴘᴇʀᴍɪᴛ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴀɴᴛɪᴘᴍ</ᴄᴏᴅᴇ> [ᴏɴ ᴀᴛᴀᴜ ᴏꜰꜰ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢʜɪᴅᴜᴘᴋᴀɴ ᴀᴛᴀᴜ ᴍᴇᴍᴀᴛɪᴋᴀɴ ᴀɴᴛɪᴘᴍ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ꜱᴇᴛᴍꜱɢ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ᴘᴇꜱᴀɴ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴛᴜʀ ᴘᴇꜱᴀɴ ᴀɴᴛɪᴘᴍ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ꜱᴇᴛʟɪᴍɪᴛ</ᴄᴏᴅᴇ> [ᴀɴɢᴋᴀ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴛᴜʀ ᴘᴇʀɪɴɢᴀᴛᴀɴ ᴘᴇꜱᴀɴ ʙʟᴏᴋɪʀ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴏᴋ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴʏᴇᴛᴜᴊᴜɪ ᴘᴇꜱᴀɴ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ɴᴏ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴᴏʟᴀᴋ ᴘᴇꜱᴀɴ.

<ᴜ>ᴄᴀᴛᴀᴛᴀɴ</ᴜ>: <ʙʟᴏᴄᴋQᴜᴏᴛᴇ>ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ꜰᴏʀᴍᴀᴛ ᴛᴇᴋꜱ ᴍᴇɴᴊᴀᴅɪ ᴛᴏᴍʙᴏʟ ꜱɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ `{0}ᴍᴀʀᴋᴅᴏᴡɴ`</ʙʟᴏᴄᴋQᴜᴏᴛᴇ>
"""


@PY.UBOT("antipm|pmpermit", sudo=True)
async def _(client, message):
    await permitpm(client, message)


@PY.UBOT("ok|a", sudo=True)
async def _(client, message):
    await approve(client, message)


@PY.UBOT("da|no", sudo=True)
async def _(client, message):
    await disapprove(client, message)


@PY.UBOT("getvar", sudo=True)
async def _(client, message):
    await get_msg(client, message)


@PY.UBOT("setmsg", sudo=True)
async def _(client, message):
    await set_msg(client, message)


@PY.UBOT("setlimit", sudo=True)
async def _(client, message):
    await set_limit(client, message)


@PY.COSTUM_CMD("PMPERMIT", ubot)
async def _(client, message):
    await handle_pmpermit(client, message)


@PY.INLINE("^ambil_tombolpc")
async def _(client, message):
    await pc_inline(client, message)


@PY.INLINE("^get_teks_but")
async def _(client, message):
    await geteksbut(client, message)
