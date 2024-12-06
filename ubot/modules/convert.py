from ubot import *

__MODULE__ = "Convert"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏɴᴠᴇʀᴛ

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴛᴏᴀɴɪᴍᴇ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ꜰᴏᴛᴏ/ꜱᴛɪᴄᴋᴇʀ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇʀᴜʙᴀʜ ɢᴀᴍʙᴀʀ ᴋᴇ ᴀɴɪᴍᴇ.

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴛᴏɪᴍɢ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ꜱᴛɪᴋᴇʀ/ɢɪꜰ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇʀᴜʙᴀʜ ꜱᴛɪᴋᴇʀ/ɢɪꜰ ᴋᴇ ꜰᴏᴛᴏ.

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴛᴏꜱᴛɪᴄᴋᴇʀ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ᴋᴇ ꜰᴏᴛᴏ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇʀᴜʙᴀʜ ꜰᴏᴛᴏ ᴋᴇ ꜱᴛɪᴋᴇʀ.

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴛᴏɢɪꜰ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ꜱᴛɪᴋᴇʀ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇʀᴜʙᴀʜ ꜱᴛɪᴋᴇʀ ᴋᴇ ɢɪꜰ.

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴛᴏᴀᴜᴅɪᴏ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ᴠɪᴅᴇᴏ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇʀᴜʙᴀʜ ᴠɪᴅᴇᴏ ᴍᴇɴᴊᴀᴅɪ ᴀᴜᴅɪᴏ ᴍᴘ3.

⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴇꜰᴇᴋ</ᴄᴏᴅᴇ> [ᴇꜰᴇᴋ ᴋᴏᴅᴇ - ɴᴀᴍᴀ ᴇꜰᴇᴋ]  
   <ʙ>• ᴇꜰᴇᴋ ᴋᴏᴅᴇ:</ʙ>  <ᴄᴏᴅᴇ>ʙᴇɴɢᴇᴋ</ᴄᴏᴅᴇ> <ᴄᴏᴅᴇ>ʀᴏʙᴏᴛ</ᴄᴏᴅᴇ> <ᴄᴏᴅᴇ>ᴊᴇᴅᴜɢ</ᴄᴏᴅᴇ> <ᴄᴏᴅᴇ>ꜰᴀꜱᴛ</ᴄᴏᴅᴇ> <ᴄᴏᴅᴇ>ᴇᴄʜᴏ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴍᴇʀᴜʙᴀʜ ꜱᴜᴀʀᴀ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ.
  
⌑ ᴘᴇʀɪɴᴛᴀʜ : <ᴄᴏᴅᴇ>{0}ᴄᴜʀɪ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ : ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴜʀɪ ᴍᴇᴅɪᴀ ᴛɪᴍᴇʀ, ᴄᴇᴋ ᴘᴇꜱᴀɴ ᴛᴇʀꜱɪᴍᴘᴀɴ
"""


@PY.UBOT("toanime", sudo=True)
async def _(client, message):
    await convert_anime(client, message)


@PY.UBOT("toimg", sudo=True)
async def _(client, message):
    await convert_photo(client, message)


@PY.UBOT("tosticker", sudo=True)
async def _(client, message):
    await convert_sticker(client, message)


@PY.UBOT("togif", sudo=True)
async def _(client, message):
    await convert_gif(client, message)


@PY.UBOT("toaudio", sudo=True)
async def _(client, message):
    await convert_audio(client, message)


@PY.UBOT("efek", sudo=True)
async def _(client, message):
    await convert_efek(client, message)


@PY.UBOT("curi", sudo=True)
async def _(client, message):
    await colong_cmn(client, message)
