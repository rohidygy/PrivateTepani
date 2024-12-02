
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultVideo, InlineQueryResultPhoto
from ubot import PY, Emo, monggo, get_msg_button, create_tl_btn, INLINE, bot, ubot, get_text, get_arg
#from .notes import kontol_siapa
from telegraph import upload_file


__MODULE__ = "ʙᴜᴛᴛᴏɴ"
__HELP__ = """
 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙᴜᴛᴛᴏɴ

⌑ ᴘᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ʙᴜᴛᴛᴏɴ</ᴄᴏᴅᴇ> [ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ]
⌑ ᴘᴇɴᴊᴇʟᴀꜱᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇᴋꜱ ᴍᴇɴᴊᴀᴅɪ ᴛᴏᴍʙᴏʟ.

<ᴜ>ᴄᴀᴛᴀᴛᴀɴ</ᴜ>: <ʙʟᴏᴄᴋQᴜᴏᴛᴇ>ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ꜰᴏʀᴍᴀᴛ ᴛᴇᴋꜱ ᴍᴇɴᴊᴀᴅɪ ᴛᴏᴍʙᴏʟ ꜱɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ `{0}ᴍᴀʀᴋᴅᴏᴡɴ`</ʙʟᴏᴄᴋQᴜᴏᴛᴇ>
"""

id_button = {}

def tomi_send_you_to_hell(m):
    if m.photo:
        return {"photo": m.photo.file_id}
    elif m.video:
        return {"video": m.video.file_id}
    else:
        return None

@PY.UBOT("button")
async def _(c: ubot, m):
    em = Emo(c.me.id)
    em.initialize()
    rep = m.reply_to_message or m
    teks = c.get_text(m)
    babi = await m.reply("{} Processing...".format(em.proses))
    id_button[c.me.id] = c.get_arg(m)
    if rep.text:
        monggo.set_var(c.me.id, "id_button", id_button[c.me.id])
    elif rep.media:
        if rep.photo:
            file = rep.photo.file_id
            don = await c.download_media(file)
            oh = upload_file(don)
            mmk = f"https://telegra.ph/{oh[0]}"
            monggo.set_var(c.me.id, "id_button_pic", mmk)
            monggo.set_var(c.me.id, "id_button", id_button[c.me.id])
        elif rep.video:
            file = rep.video.file_id
            don = await c.download_media(file)
            oh = upload_file(don)
            mmk = f"https://telegra.ph/{oh[0]}"
            monggo.set_var(c.me.id, "id_button_pic", mmk)
            monggo.set_var(c.me.id, "id_button", id_button[c.me.id])
    text, keyboard = get_msg_button(teks)
    if keyboard:
        try:
            x = await c.get_inline_bot_results(bot.me.username, f"buat_button {c.me.id}")
            await c.send_inline_bot_result(
                m.chat.id, x.query_id, x.results[0].id, reply_to_message_id=m.id
            )
        except Exception as e:
            await babi.edit("{} Error : {}".format(em.gagal, e))
            return
    await babi.delete()
    return


@PY.INLINE("^buat_button")
@INLINE.QUERY
async def _(c: bot, iq):
    dia = iq.from_user.id
    haha = monggo.get_var(dia, "id_button")
    text, keyboard = get_msg_button(haha)
    if keyboard:
        keyboard = create_tl_btn(keyboard)
    pic = monggo.get_var(dia, "id_button_pic")
    if pic:
        filem = (
            InlineQueryResultVideo if pic.endswith(".mp4") else InlineQueryResultPhoto
        )
        url_ling = (
            {"video_url": pic, "thumb_url": pic}
            if pic.endswith(".mp4")
            else {"photo_url": pic}
        )
        duar = [
            filem(
                **url_ling,
                title="PIC Buttons !",
                caption=text,
                reply_markup=(keyboard),
            )
        ]
    else:
        duar = [
            (
                InlineQueryResultArticle(
                    title="Tombol PM!",
                    input_message_content=InputTextMessageContent(text, disable_web_page_preview=True),
                    reply_markup=(keyboard),
                )
            )
        ]
    await c.answer_inline_query(iq.id,cache_time=0,results=duar)
    monggo.remove_var(dia, "id_button_pic")
    monggo.remove_var(dia, "id_button")
    """
    await c.answer_inline_query(

        iq.id,

        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get button!",
                    reply_markup=keyboard,
                    input_message_content=InputTextMessageContent(text, disable_web_page_preview=True),
                )
            )
        ],
    )
    """
    
