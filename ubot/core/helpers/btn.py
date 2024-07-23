import re

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# NOTE: the url \ escape may cause double escapes
# match * (bold) (don't escape if in url)
# match _ (italics) (don't escape if in url)
# match ` (code)
# match []() (markdown link)
# else, escape *, _, `, and [

# Gojo
# William



def is_url(text):
    regex = r"(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:[/?]\S+)?|tg://\S+"
    matches = re.findall(regex, text)
    if matches:
        return True
    return False



def get_msg_button(texts: str):
    btn = []
    for z in re.findall(r"\[(.*?)\|(.*?)\]", texts):
        text, url = z
        urls = url.split("|")
        url = urls[0]
        if len(urls) > 1:
            btn[-1].append([text, url])
        else:
            btn.append([[text, url]])

    txt = texts
    for z in re.findall(r"\[.+?\|.+?\]", texts):
        txt = txt.replace(z, "")

    return txt.strip(), btn


def create_tl_btn(button: list):
    btn = []
    for z in button:
        if len(z) > 1:
            kk = []
            for x, y in z:
                if is_url(y):
                    kk.append(InlineKeyboardButton(text=x, url=y.strip()))
                else:
                    kk.append(InlineKeyboardButton(text=x, callback_data=y.strip()))
            btn.append(kk)
        else:
            x, y = z[0]
            if is_url(y):
                btn.append([InlineKeyboardButton(text=x, url=y.strip())])
            else:
                btn.append([InlineKeyboardButton(text=x, callback_data=y.strip())])
    return InlineKeyboardMarkup(btn)


def format_btn(buttons: list):
    txt = ""
    for i in buttons:
        a = 0
        for i in i:
            if hasattr(i.button, "url"):
                a += 1
                if a > 1:
                    txt += f"[{i.button.text} | {i.button.url} | same]"
                else:
                    txt += f"[{i.button.text} | {i.button.url}]"
    _, btn = get_msg_button(txt)
    return btn