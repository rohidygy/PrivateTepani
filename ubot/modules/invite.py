from ubot import *

__MODULE__ = "Invite"
__HELP__ = """
 Bantuan Untuk Invite

• Perintah : <code>{0}invite</code> [username] 
• Penjelasan : Untuk mengundang anggota ke grup.
  """


@PY.UBOT("invite", sudo=True)
async def _(client, message):
    await invite_cmd(client, message)


@PY.UBOT("inviteall", sudo=True)
async def _(client, message):
    await inviteall_cmd(client, message)


@PY.UBOT("cancel", sudo=True)
async def _(client, message):
    await cancel_cmd(client, message)
