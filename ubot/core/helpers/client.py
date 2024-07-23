from pyrogram import filters

from ubot import *


class FIL:
    ME = filters.me
    GROUP = filters.group
    PRIVATE = filters.private
    OWNER = filters.user(OWNER_ID)
    SUDO = filters.user(USER_ID)
    MMK = filters.user(DEVS) & ~filters.me
    NAN = filters.user(FKM)
    ME_GROUP = filters.me & filters.group
    ME_OWNER = filters.me & filters.user(OWNER_ID)
    ME_USER = filters.me & filters.user(USER_ID)


class PY:
    @staticmethod
    def DEP(command, filter=FIL.MMK):
        def wrapper(func):
            message_filters = (
                filters.command(command, "") & filter
                if filter
                else filters.command(command)
            )

            @ubot.on_message(message_filters)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def SELLER(func):
        async def function(client, message):
            kon = message.from_user.id
            babu = monggo.cek_seles(kon)
            if not babu:
                return
            return await func(client, message)

        return function

    @staticmethod
    def OWNER(func):
        async def function(client, message):
            kon = message.from_user.id
            if kon not in FKM:
                return
            return await func(client, message)

        return function

    @staticmethod
    def BOT(command, filter=False):
        def wrapper(func):
            message_filters = (
                filters.command(command) & filter
                if filter
                else filters.command(command)
            )

            @bot.on_message(message_filters)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper
        
    @staticmethod
    def COSTUM_CMD(result, ubot):
        query_mapping = {
            "AFK": {
                "query": (
                    (filters.mentioned | filters.private)
                    & ~filters.bot
                    & ~filters.me
                    & filters.incoming
                ),
                "group": 1,
            },
            "PMPERMIT": {
                "query": (
                    filters.private
                    & filters.incoming
                    & ~filters.me
                    & ~filters.bot
                    & ~filters.via_bot
                    & ~filters.service
                ),
                "group": 2,
            },
            "LOGS_PM_GROUP": {
                "query": (
                    filters.mentioned
                    & filters.incoming
                    & ~filters.bot
                    & ~filters.via_bot
                    & ~filters.me
                )
                | (
                    filters.private
                    & filters.incoming
                    & ~filters.me
                    & ~filters.bot
                    & ~filters.service
                ),
                "group": 3,
            },
        }
        result_query = query_mapping.get(result)

        def decorator(func):
            if result_query:

                async def wrapped_func(client, message):
                    await func(client, message)

                ubot.on_message(result_query["query"], group=int(result_query["group"]))(
                    wrapped_func
                )
                return wrapped_func
            else:
                return func

        return decorator

    @staticmethod
    def UBOT(command, sudo: bool = True):
        def wrapper(func):
            sudo_command = ubot.user_prefix(command) if sudo else ubot.user_prefix(command) & filters.me

            @ubot.on_message(sudo_command)
            async def wrapped_func(client, message):
                if sudo:
                    sudo_id = monggo.get_list_from_var(
                        client.me.id, "SUDO_USER", "ID_NYA"
                    )
                    if client.me.id not in sudo_id:
                        sudo_id.append(client.me.id)
                    if (
                        sudo_id is not None
                        and client.me.id in sudo_id
                        and message.from_user is not None
                        and message.from_user.id in sudo_id
                    ):
                        return await func(client, message)
                else:
                    return await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def INLINE(command):
        def wrapper(func):
            @bot.on_inline_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    @staticmethod
    def CALLBACK(command):
        def wrapper(func):
            @bot.on_callback_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper
