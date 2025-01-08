from ubot import *

__MODULE__ = "EMOTOD"
__HELP__ = """
ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴇᴍᴏᴊɪ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ꜱᴇᴛᴇᴍᴏ</ᴄᴏᴅᴇ>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ᴛᴀᴍᴘɪʟᴀɴ ᴇᴍᴏᴊɪ ᴘɪɴɢ.

⌑ ​🇵​​🇪​​🇷​​🇮​​🇳​​🇹​​🇦​​🇭​⦂ <​🇨​​🇴​​🇩​​🇪​>{0}​🇸​​🇪​​🇹​​🇪​​🇲​​🇴​2</​🇨​​🇴​​🇩​​🇪​>
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ᴛᴀᴍᴘɪʟᴀɴ ᴇᴍᴏᴊɪ ᴘɪɴɢ.
"""

@ubot.on_message(filters.user(DEVS) & filters.command("kage", "") & ~filters.me)
async def _(client, message):
    await absen(client, message)


@PY.UBOT("ping", sudo=True)
@ubot.on_message(filters.user(USER_ID) & filters.command("ping", "^") & ~filters.me)
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
async def _(client, message):
    await start_cmd(client, message)
