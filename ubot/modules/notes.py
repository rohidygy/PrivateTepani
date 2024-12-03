from ubot.core.helpers import PY
from ubot.core.plugins import (cb_notes, clear_note, get_note, inline_notes,
                               local_notes, save_note)

__MODULE__ = "Notes"
__HELP__ = """
❒ Bantuan Untuk Notes
┃
┣ Perintah: <code>{0}save</code> [nama catatan] [balas pesan|teks]
┣ Penjelasan: Untuk menyimpan catatan.
┃
┣ Perintah: <code>{0}get</code> [nama catatan]
┣ Penjelasan: Untuk mengambil catatan.
┃
┣ Perintah: <code>{0}rm</code> [nama catatan]
┣ Penjelasan: Untuk menghapus catatan.
┃
┣ Perintah: <code>{0}notes</code>
┣ Penjelasan: Untuk melihat semua catatan.
┃
┖ Button Format :
<code>[Teks](buttonurl://google.com)</code>
<code>[Teks 2](buttonurl://google.com:same)</code>
"""


@PY.UBOT("save", sudo=True)
async def _(client, message):
    await save_note(client, message)


@PY.UBOT("get", sudo=True)
async def _(client, message):
    await get_note(client, message)


@PY.UBOT("notes", sudo=True)
async def _(client, message):
    await local_notes(client, message)


@PY.UBOT("rm", sudo=True)
async def _(client, message):
    await clear_note(client, message)


@PY.INLINE("^get_note_")
async def _(client, inline_query):
    await inline_notes(client, inline_query)


@PY.CALLBACK("^#")
async def _(client, callback_query):
    await cb_notes(client, callback_query)
