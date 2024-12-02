import requests

from ubot import *

__MODULE__ = "Base64"
__HELP__ = """
Bantuan Untuk Base64

• Perintah : {0}encode [text or reply]
• Penjelasan : Enkripsi sebuah text.

• Perintah : {0}decode [text or reply]
• Penjelasan : Dekripsi sebuah text.
"""

async def process_message(c, m, text, decode=False):
    if text:
        encoding_type = "base64" if not decode else "base64&decode=true"
        url = f"https://networkcalc.com/api/encoder/{text}?encoding={encoding_type}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if not decode and "encoded" in data:
                encoded_text = data["encoded"]
                await m.reply(f"<b>Hasil Encode : \n`{encoded_text}`</b>")
            elif decode and "decoded" in data:
                decoded_text = data["decoded"]
                await m.reply(f"<b>Hasil Decode : \n`{decoded_text}`</b>")
            else:
                gagal = f"encode" if not decode else "decode"
                await m.reply(f"<b>Format salah!! Gunakan {gagal}!!.</b>")
        else:
            await m.reply(f"<b>Error : {esponse.status_code}")
    else:
        await m.reply("<b>Silahkan balas ke pesan text!!</b>")


@PY.UBOT("encode", sudo=False)
async def _(c, m):
    
    pros = await m.reply("<b>Processing...</b>")
    if m.reply_to_message and m.reply_to_message.text:
        text = m.reply_to_message.text
    else:
        text = " ".join(m.command[1:])
    await process_message(c, m, text)
    await pros.delete()


@PY.UBOT("decode", sudo=False)
async def _(c, m):
    
    pros = await m.reply("<b>Processing...</b>")
    if m.reply_to_message and m.reply_to_message.text:
        text = m.reply_to_message.text
    else:
        text = " ".join(m.command[1:])
    await process_message(c, m, text, decode=True)
    await pros.delete()
