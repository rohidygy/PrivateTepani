

from ubot import *

async def post_to_telegraph(is_media: bool, title=None, content=None, media=None):
    telegraph = Telegraph()
    if telegraph.get_access_token() is None:
        await telegraph.create_account(short_name=bot.me.username)
    if is_media:
        # Create a Telegram Post Foto/Video
        response = await telegraph.upload_file(media)
        return f"https://img.yasirweb.eu.org{response[0]['src']}"
    # Create a Telegram Post using HTML Content
    response = await telegraph.create_page(
        title,
        html_content=content,
        author_url=f"https://t.me/{bot.me.username}",
        author_name=bot.me.username,
    )
    return f"https://graph.org/{response['path']}"

async def tg_cmd(client, message):
    XD = await message.reply("<code>Processing... . .</code>")
    if not message.reply_to_message:
        return await XD.edit("<b>Silakan balas ke pesan media.</b>")
    telegraph = Telegraph()
    if message.reply_to_message.media:
        m_d = await message.reply_to_message.download()
        try:
            url = await post_to_telegraph(True, media=m_d)
        except Exception as exc:
            return await XD.edit(f"<code>{exc}</code>")
        U_done = f"<b>Berhasil: <a href='{url}'>diupload</a></b>"
        await XD.edit(U_done, disable_web_page_preview=True)
    elif message.reply_to_message.text:
        page_title = f"{client.me.first_name} {client.me.last_name or ''}"
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            url = await post_to_telegraph(False, page_title, page_text)
        except Exception as exc:
            return await XD.edit(f"<code>{exc}</code>")
        wow_graph = f"<b>Berhasil <a href='{url}'>diupload</a></b>"
        await XD.edit(wow_graph, disable_web_page_preview=True)
