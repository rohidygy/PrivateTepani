import re

from pyrogram.helpers import InlineKeyboard 
from pyrogram.errors import MessageNotModified
from pyrogram.types import (InlineKeyboardMarkup,InlineKeyboardButton, InlineQueryResultArticle,
                            InputTextMessageContent)

from ubot import *


class Button:
    def alive(get_id):
        button = [
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ",
                    callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                )
            ]
        ]
        return button

    def button_add_expired(user_id):
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in range(1, 13):
            keyboard.append(
                InlineKeyboardButton(
                    f"{X} Bulan",
                    callback_data=f"success {user_id} {X}",
                )
            )
        buttons.add(*keyboard)
        buttons.row(
            InlineKeyboardButton(
                "ʟɪɴᴋ ᴀᴋᴜɴ", callback_data=f"profil {user_id}"
            )
        )
        buttons.row(
            InlineKeyboardButton(
                "ᴛᴏʟᴀᴋ ᴘᴇᴍʙᴀʏᴀʀᴀɴ", callback_data=f"failed {user_id}"
            )
        )
        return buttons

    def deak(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "ᴋᴇᴍʙᴀʟɪ",
                    callback_data=f"prev_ub {int(count)}",
                ),
                InlineKeyboardButton(
                    "ᴛᴇʀɪᴍᴀ", callback_data=f"deak_akun {int(count)}"
                ),
            ],
        ]
        return button

    def expired_button_bot():
        button = [
            [
                InlineKeyboardButton(
                    text=f"{bot.me.first_name}",
                    url=f"https://t.me/{bot.me.username}",
                )
            ]
        ]
        return button

    def start(message):
        if message.from_user.id not in USER_ID:
            button = [
                [InlineKeyboardButton("💎 ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ", callback_data="bahan")],
                [
                    InlineKeyboardButton("🤖 ᴛᴇɴᴛᴀɴɢ ʙᴏᴛ", callback_data="informasi"),
                    InlineKeyboardButton("🥷 ᴏᴡɴᴇʀ", callback_data="cb_tutor"),
                ],
                [
                    InlineKeyboardButton("📢 sᴜᴘᴘᴏʀᴛ", callback_data="diskusi"),
                    InlineKeyboardButton("🛑 sᴛᴀᴛᴜs ᴀᴋᴜɴ", callback_data="start_profile"),
                ],
            ]
        else:
            button = [
                [
                    InlineKeyboardButton("💎 ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ", callback_data="bahan"),
                ],
                [
                    InlineKeyboardButton("🧧 ᴜᴘᴅᴀᴛᴇ", callback_data="gitpull"),
                    InlineKeyboardButton("🎮 ʀᴇsᴛᴀʀᴛ", callback_data="restart"),
                ],
                [
                    InlineKeyboardButton("🛑sᴛᴀᴛᴜs ᴀᴋᴜɴ", callback_data="start_profile"),
                    InlineKeyboardButton("ʜᴏsᴛ", callback_data="host"),
                ],
            ]
        return button

    def plus_minus(query, user_id):
        button = [
            [
                InlineKeyboardButton(
                    "-𝟷",
                    callback_data=f"kurang {query}",
                ),
                InlineKeyboardButton(
                    "+𝟷",
                    callback_data=f"tambah {query}",
                ),
            ],
            [InlineKeyboardButton("ᴋᴏɴғɪʀᴍᴀsɪ", callback_data="confirm")],
            [InlineKeyboardButton("Batalkan", callback_data=f"home {user_id}")],
        ]
        return button

    def userbot(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "Hapus Dari Database",
                    callback_data=f"del_ubot {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Cek Nomor",
                    callback_data=f"get_phone {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Cek Kadaluarsa",
                    callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Cek Otp",
                    callback_data=f"get_otp {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Cek Verifikasi 2L",
                    callback_data=f"get_faktor {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Musnah", callback_data=f"ub_deak {int(count)}"
                )
            ],
            [
                InlineKeyboardButton("❮", callback_data=f"prev_ub {int(count)}"),
                InlineKeyboardButton("❯", callback_data=f"next_ub {int(count)}"),
            ],
            [
                InlineKeyboardButton("Tutup", callback_data=f"0_cls"),
            ],
        ]
        return button

    def ambil_akun(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "Hapus Dari Database",
                    callback_data=f"del_ubot {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Cek Nomor",
                    callback_data=f"get_phone {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Cek Kadaluarsa",
                    callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Cek Otp",
                    callback_data=f"get_otp {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Cek Verifikasi 2L",
                    callback_data=f"get_faktor {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Musnah", callback_data=f"ub_deak {int(count)}"
                )
            ],
            [
                InlineKeyboardButton("❮", callback_data=f"prev_ub {int(count)}"),
                InlineKeyboardButton("❯", callback_data=f"next_ub {int(count)}"),
            ],
            [
                InlineKeyboardButton("Tutup", callback_data=f"close_user")
            ],
        ]
        return button


class INLINE:
    def QUERY(func):
        async def wrapper(client, inline_query):
            users = ubot._get_my_id
            if inline_query.from_user.id not in users:
                await client.answer_inline_query(
                    inline_query.id,
                    cache_time=0,
                    results=[
                        (
                            InlineQueryResultArticle(
                                title=f"Anda Belum Melakukan Pembelian @{bot.me.username}",
                                input_message_content=InputTextMessageContent(
                                    f"Kamu Bisa Melakukan Pembelian @{bot.me.username} Agar Bisa Menggunakan"
                                ),
                            )
                        )
                    ],
                )
            else:
                await func(client, inline_query)

        return wrapper

    def DATA(func):
        async def wrapper(client, callback_query):
            users = ubot._get_my_id
            if callback_query.from_user.id not in users:
                await callback_query.answer(
                    f"Silakan Order Bot @{bot.me.username} Agar Bisa Menggunakan Bot Ini",
                    True,
                )
            else:
                try:
                    await func(client, callback_query)
                except MessageNotModified:
                    await callback_query.answer("❌ ERROR")

        return wrapper