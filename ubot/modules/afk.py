from ubot import *

__MODULE__ = "afk"
__HELP__ = """
<b>『 bantuan untuk afk 』</b>

  <b>• perintah:</b> <code>{0}afk</code></code>
  <b>• penjelasan:</b> untuk mengaktifkan afk 

  <b>• perintah:</b> <code>{0}unafk</code></code>
  <b>• penjelasan:</b> untuk menonaktifkan afk
"""


@PY.UBOT("afk")
async def _(client, message):
    reason = get_arg(message)
    afk_handler = awayFromKeyboard(client, message, reason)
    await afk_handler.set_afk()


@PY.AFK(True)
async def _(client, message):
    afk_handler = awayFromKeyboard(client, message)
    await afk_handler.get_afk()


@PY.UBOT("unafk")
async def _(client, message):
    afk_handler = awayFromKeyboard(client, message)
    return await afk_handler.unset_afk()
