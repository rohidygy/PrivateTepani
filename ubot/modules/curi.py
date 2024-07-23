from ubot import *

__MODULE__ = "Curi"
__HELP__ = """
 Bantuan Untuk mencuri konten timer

• Perintah : <code>{0}curi</code> [link]
• Penjelasan : Untuk mengambil pap timer, cek pesan tersimpan.
  """


@PY.BOT("curi")
async def _(client, message):
    await copy_bot_msg(client, message)
  
