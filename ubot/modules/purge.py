from ubot import *

__MODULE__ = "🇵​​🇺​​🇷​​🇬​​🇪​"
__HELP__ = """
​🇧​​🇦​​🇳​​🇹​​🇺​​🇦​​🇳​ ​🇺​​🇳​​🇹​​🇺​​🇰​ ​🇵​​🇺​​🇷​​🇬​​🇪​

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴘᴜʀɢᴇ</ᴄᴏᴅᴇ> [ʀᴇᴘʟʏ ᴛᴏ ᴍᴇꜱꜱᴀɢᴇ
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ʙᴇʀꜱɪʜᴋᴀɴ (ʜᴀᴘᴜꜱ ꜱᴇᴍᴜᴀ ᴘᴇꜱᴀɴ) ᴏʙʀᴏʟᴀɴ ᴅᴀʀɪ ᴘᴇꜱᴀɴ ʏᴀɴɢ ᴅɪʙᴀʟᴀꜱ ʜɪɴɢɢᴀ ʏᴀɴɢ ᴛᴇʀᴀᴋʜɪʀ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴅᴇʟ</ᴄᴏᴅᴇ> [ʀᴇᴘʟʏ ᴛᴏ ᴍᴇꜱꜱᴀɢᴇ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ʜᴀᴘᴜꜱ ᴘᴇꜱᴀɴ ʏᴀɴɢ ᴅɪʙᴀʟᴀꜱ.

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴘᴜʀɢᴇᴍᴇ</ᴄᴏᴅᴇ> [ɴᴜᴍʙᴇʀ ᴏꜰ ᴍᴇꜱꜱᴀɢᴇꜱ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ʜᴀᴘᴜꜱ ᴘᴇꜱᴀɴ ᴀɴᴅᴀ ꜱᴇɴᴅɪʀɪ ᴅᴇɴɢᴀɴ ᴍᴇɴᴇɴᴛᴜᴋᴀɴ ᴛᴏᴛᴀʟ ᴘᴇꜱᴀɴ.
"""


@PY.UBOT("del", sudo=True)
async def _(client, message):
    await del_cmd(client, message)


@PY.UBOT("purgeme", sudo=True)
async def _(client, message):
    await purgeme_cmd(client, message)


@PY.UBOT("purge", sudo=True)
async def _(client, message):
    await purge_cmd(client, message)
