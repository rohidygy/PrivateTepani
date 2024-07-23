from pyrogram.enums import ParseMode
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

from ubot import *

__MODULE__ = "Markdown"
__HELP__ = """
 Bantuan untuk Markdown

• Perintah: <code>{0}markdown</code>
• Penjelasan: Untuk format tombol.
"""


def markdown_help():
    return ikb(
        [
            [("Markdown Format", "markd.butformat"), ("Fillings", "markd.filing")],
            [("Back Help", "help_back")],
        ]
    )


@PY.UBOT("markdown")
async def _(c: ubot, m):
    try:
        xi = await c.get_inline_bot_results(bot.me.username, "mark_in")
        await m.delete()
        await c.send_inline_bot_result(
            m.chat.id, xi.query_id, xi.results[0].id, reply_to_message_id=ReplyCheck(m)
        )
        return
    except Exception as e:
        await m.reply(f"{e}")
        return


@PY.INLINE("^mark_in")
async def inline_mark(c, iq):
    txt = "Untuk melihat format tombol markdown\nSilahkan klik tombol dibawah."
    await c.answer_inline_query(
        iq.id,
        cache_time=0,
        results=[
            InlineQueryResultArticle(
                title="markdown!",
                reply_markup=markdown_help(),
                input_message_content=InputTextMessageContent(txt),
            )
        ],
    )


mark_1 = """
> **Markdown Formatting**
> Anda dapat memformat pesan Anda menggunakan **tebal**, _miring_, --garis bawah--, ~~coret~~, dan banyak lagi.
>
> `<code>kata kode</code>`: Tanda kutip terbalik digunakan buat font monospace. Ditampilkan sebagai: `kata kode`.
>
> `<i>miring</i>`: Garis bawah digunakan buat font miring. Ditampilkan sebagai: __kata miring__.
>
> `<b>tebal</b>`: Asterisk digunakan buat font tebal. Ditampilkan sebagai: **kata tebal**.
>
> `<u>garis bawah</u>`: Buat membuat teks --garis bawah--.
>
> `<strike>coret</strike>`: Tilda digunakan buat strikethrough. Ditampilkan sebagai: ~~coret~~.
>
> `<spoiler>spoiler</spoiler>`: Garis vertikal ganda digunakan buat spoiler. Ditampilkan sebagai: ||spoiler||.
>
> `[hyperlink](contoh)`: Ini adalah pemformatan yang digunakan buat hyperlink.
>
> `<blockquote>teks quote</blockquote>`: Ini adalah pemformatan untuk > teks quote >
>
> `Hallo Disini [Tombol 1|https://link.com]` : Ini adalah pemformatan yang digunakan membuat tombol.
> `Halo Disini [Tombol 1|t.me/kynansupport][Tombol 2|t.me/kontenfilm|same]` : Ini akan membuat tombol berdampingan.
>
> Anda juga bisa membuat tombol callback_data dengan diawal tanda `#`. Untuk lebih lanjut silahkan ke @KynanSupport untuk meminta bantuan.
"""

mark_2 = "<blockquote><b>Fillings</b>\n\nAnda juga dapat menyesuaikan isi pesan Anda dengan data kontekstual. Misalnya, Anda bisa menyebut nama pengguna dalam pesan selamat datang, atau menyebutnya dalam filter!\n\n<b>Isian yang didukung:</b>\n\n<code>{first}</code>: Nama depan pengguna.\n<code>{last}</code>: Nama belakang pengguna.\n<code>{fullname}</code>: Nama lengkap pengguna.\n<code>{username}</code>: Nama pengguna pengguna. Jika mereka tidak memiliki satu, akan menyebutkan pengguna tersebut.\n<code>{mention}</code>: Menyebutkan pengguna dengan nama depan mereka.\n<code>{id}</code>: ID pengguna.\n<code>{chatname}</code>: Nama obrolan.</blockquote>"


@PY.CALLBACK("markd.")
async def cb_markd(c, cq):
    cmd = cq.data.split(".")[1]
    kb = ikb([[("Back", "bace.markd")]])
    if cmd == "butformat":
        await cq.edit_message_text(
            text=mark_1, reply_markup=kb, parse_mode=ParseMode.MARKDOWN
        )
    elif cmd == "filing":
        await cq.edit_message_text(
            text=mark_2,
            reply_markup=kb,
            parse_mode=ParseMode.HTML,
        )


@PY.CALLBACK("bace")
async def cb_bace(c, cq):
    txt = "Untuk melihat format tombol markdown\nSilahkan klik tombol dibawah."
    await cq.edit_message_text(text=txt, reply_markup=markdown_help())
