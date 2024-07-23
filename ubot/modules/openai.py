from ubot import *
import os

import google.generativeai as genai
from google.generativeai.types import generation_types
from pyrogram.enums import ChatAction
from pyrogram.errors import *


__MODULE__ = "Gemini"
__HELP__ = """
 Help Command For Gemini

 • Command: `{0}ai` or `{0}ask` [question or reply msg]
 • Description: For answer to Ai  Gemini by Google.
"""

def cetbut(query: str, user_id: int):
    genai.configure(api_key="AIzaSyC28dJ5wTyjm44ng1WCuz4uTppelgRcLuU")
    model = genai.GenerativeModel(model_name="gemini-1.0-pro-latest")
    convo = model.start_chat(history=[])
    try:
        convo.send_message(query)
        return convo.last.text
    except generation_types.StopCandidateException:
        return "Maaf saya tidak bisa membahas yang berbau porno atau kekerasan"
    except generation_types.BlockedPromptException:
        return "Maaf saya tidak bisa membahas yang berbau porno atau kekerasan"


async def mari_kirim(m, query):
    try:
        chat_id = m.chat.id
        if m.sender_chat:
            user_id = m.sender_chat.id
        else:
            user_id = m.from_user.id
        # query = m.text.strip()
        respon = cetbut(query, user_id)
        await m._client.send_chat_action(chat_id, ChatAction.TYPING)
        await asyncio.sleep(2)
        if len(respon) > 4096:
            with open("chatbot.txt", "wb") as file:
                file.write(respon.encode("utf-8"))
            await m._client.send_chat_action(chat_id, ChatAction.UPLOAD_DOCUMENT)
            await asyncio.sleep(2)
            await m._client.send_document(
                chat_id, "chatbot.txt", reply_to_message_id=m.id
            )
            os.remove("chatbot.txt")
            await m._client.send_chat_action(chat_id, ChatAction.CANCEL)
        else:
            await m.reply_text(respon, reply_to_message_id=m.id)
        await m._client.send_chat_action(chat_id, ChatAction.CANCEL)
    except ChatWriteForbidden:
        pass


@PY.UBOT("ai|ask", sudo=True)
async def _(c: ubot, m):
    em = Emo(c.me.id)
    em.initialize()
    pros = await m.reply(f"{em.proses} Sebentar tolol...")
    reply_text = c.get_text(m)
    if not reply_text:
        return pros.edit(f"{em.gagal} Kasih query or balas text lah dongok!!")
    await mari_kirim(m, reply_text)
    await pros.delete()