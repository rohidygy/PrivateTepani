from ubot import *

__MODULE__ = "Search"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴇᴀʀᴄʜ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴘɪᴄ</ᴄᴏᴅᴇ> [Qᴜᴇʀʏ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ɢᴀᴍʙᴀʀ ꜱᴇᴄᴀʀᴀ ʟɪᴍɪᴛ 5

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ɢɪꜰ</ᴄᴏᴅᴇ> [Qᴜᴇʀʏ]
⌑ ​🇵​​🇪​​🇳​​🇯​​🇪​​🇱​​🇦​​🇸​​🇦​​🇳​⦂ ​🇺​​🇳​​🇹​​🇺​​🇰​ ​🇬​​🇮​​🇫​.
"""


@PY.UBOT("bing|pic", sudo=True)
async def _(client, message):
    await pic_bing_cmd(client, message)


@PY.UBOT("gif", sudo=True)
async def _(client, message):
    await gif_cmd(client, message)
