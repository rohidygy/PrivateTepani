import re

import requests
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def is_url(text):
    regex = r"(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:[/?]\S+)?|tg://\S+"
    matches = re.findall(regex, text)
    if matches:
        return True
    return False


def is_angka(text):
    try:
        int(text)
        return True
    except ValueError:
        return False


def cek_tg(text):
    tg_pattern = r"(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:[/?]\S+)?|tg://\S+"
    match = re.search(tg_pattern, text)
    if match:
        tg_link = match.group(0)
        non_tg_text = text.replace(tg_link, "").strip()
        return tg_link, non_tg_text
    else:
        return (
            None,
            text,
        )


def extract_chat_and_message_id(url):
    pattern_username = r"https://t\.me/([a-zA-Z0-9_]+)/(\d+)"
    pattern_chat_id = r"https://t\.me/c/(\d+)/(\d+)"

    match_username = re.match(pattern_username, url)
    match_chat_id = re.match(pattern_chat_id, url)

    if match_username:
        chat_username = match_username.group(1)
        message_id = int(match_username.group(2))
        return chat_username, message_id
    elif match_chat_id:
        chat_id = int("-100" + match_chat_id.group(1))
        message_id = int(match_chat_id.group(2))
        return chat_id, message_id

    return None, None


async def get_media_type_from_url(client, url):
    chat_id_or_username, message_id = extract_chat_and_message_id(url)

    if not chat_id_or_username or not message_id:
        return None

    message = await client.get_messages(chat_id_or_username, message_id)

    return message


def cek_tautan(text):
    pd_pattern = r"(https?://[^\s]+)"
    pd_links = re.search(pd_pattern, text)
    non_pd_text = re.sub(pd_pattern, "", text).strip()
    if pd_links:
        return pd_links[0], non_pd_text

    return None, non_pd_text


def extract_pixeldrain_id(url):
    match = re.search(r"pixeldrain\.com/u/([a-zA-Z0-9]+)", url)
    if match:
        return match.group(1)
    else:
        return None


async def download_pixeldrain_media_by_id(file_id):
    try:
        download_url = f"https://pixeldrain.com/api/file/{file_id}?download"
        response = requests.get(download_url, stream=True)

        if response.status_code == 200:
            content_type = response.headers.get("Content-Type")

            if "video" in content_type:
                ext = ".mp4"
            elif "image" in content_type:
                ext = ".jpg"
            else:
                ext = ".bin"

            file_path = f"downloaded_media{ext}"

            with open(file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            return file_path
        elif response.status_code == 403:
            json_response = response.json()
            if json_response["value"] == "file_rate_limited_captcha_required":
                return None
            elif json_response["value"] == "virus_detected_captcha_required":
                return None
            else:
                return None
        else:
            return None

    except Exception:
        return None


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


def cb_nts_btn(c, button: list):
    btn = []
    for z in button:
        if len(z) > 1:
            kk = []
            for x, y in z:
                if is_url(y):
                    kk.append(InlineKeyboardButton(text=x, url=y.strip()))
                elif is_angka(y):
                    kk.append(InlineKeyboardButton(text=x, user_id=y.strip()))
                else:
                    kk.append(
                        InlineKeyboardButton(text=x, callback_data=f"{y.strip()}_{c}")
                    )
            btn.append(kk)
        else:
            x, y = z[0]
            if is_url(y):
                btn.append([InlineKeyboardButton(text=x, url=y.strip())])
            elif is_angka(y):
                btn.append([InlineKeyboardButton(text=x, user_id=y.strip())])
            else:
                btn.append(
                    [InlineKeyboardButton(text=x, callback_data=f"{y.strip()}_{c}")]
                )
    return InlineKeyboardMarkup(btn)


def create_tl_btn(button: list):
    btn = []
    for z in button:
        if len(z) > 1:
            kk = []
            for x, y in z:
                if is_url(y):
                    kk.append(InlineKeyboardButton(text=x, url=y.strip()))
                elif is_angka(y):
                    kk.append(InlineKeyboardButton(text=x, user_id=y.strip()))
                else:
                    kk.append(InlineKeyboardButton(text=x, callback_data=y.strip()))
            btn.append(kk)
        else:
            x, y = z[0]
            if is_url(y):
                btn.append([InlineKeyboardButton(text=x, url=y.strip())])
            elif is_angka(y):
                btn.append([InlineKeyboardButton(text=x, user_id=y.strip())])
            else:
                btn.append([InlineKeyboardButton(text=x, callback_data=y.strip())])
    return InlineKeyboardMarkup(btn)


def format_btn(buttons: list, main_text: str):
    for tag, replacement in [
        ("<b>", "**"),
        ("<i>", "__"),
        ("<strike>", "~~"),
        ("<spoiler>", "||"),
        ("<u>", "--"),
    ]:
        main_text = main_text.replace(tag, replacement).replace(
            f"</{tag[1:]}>", replacement
        )

    txt = main_text
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