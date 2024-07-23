from ubot import *

__MODULE__ = "PMPermit"
__HELP__ = """
Bantuan Untuk PMPermit

• Perintah: <code>{0}antipm</code> [on atau off]
• Penjelasan: Untuk menghidupkan atau mematikan antipm

• Perintah: <code>{0}setmsg</code> [balas atau berikan pesan]
• Penjelasan: Untuk mengatur pesan antipm.

• Perintah: <code>{0}setlimit</code> [angka]
• Penjelasan: Untuk mengatur peringatan pesan blokir.

• Perintah: <code>{0}ok</code>
• Penjelasan: Untuk menyetujui pesan.

• Perintah: <code>{0}no</code>
• Penjelasan: Untuk menolak pesan.

<u>Catatan</u>: <blockquote>Untuk mengetahui format teks menjadi tombol silahkan ketik `{0}markdown`</blockquote>
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
