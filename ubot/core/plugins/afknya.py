from time import time
from ubot.core.database import monggo
from ubot.core.helpers import get_time

class awayFromKeyboard:
    def __init__(self, client, message, reason=""):
        self.client = client
        self.message = message
        self.reason = reason

    async def set_afk(self):
        db_afk = {"time": time(), "reason": self.reason}
        msg_afk = (
            f"<b>❏ sedang afk\n ╰ alasan: {self.reason}</b>"
            if self.reason
            else "<b>❏ sedang afk</b>"
        )
        monggo.set_var(self.client.me.id, "AFK", db_afk)
        await self.message.reply(msg_afk, disable_web_page_preview=True)
        return await self.message.delete()

    async def get_afk(self):
        vars = monggo.get_var(self.client.me.id, "AFK")
        if vars:
            afk_time = vars.get("time")
            afk_reason = vars.get("reason")
            afk_runtime = await get_time(time() - afk_time)
            afk_text = (
                f"<b>❏ sedang afk\n ├ waktu: {afk_runtime}\n ╰ alasan: {afk_reason}</b>"
                if afk_reason
                else f"<b>❏ sedang afk\n ╰ waktu: {afk_runtime}</b>"
            )
            return await self.message.reply(afk_text, disable_web_page_preview=True)

    async def unset_afk(self):
        vars = monggo.get_var(self.client.me.id, "AFK")
        if vars:
            afk_time = vars.get("time")
            afk_runtime = await get_time(time() - afk_time)
            afk_text = f"<b>❏ kembali online\n ╰ afk selama: {afk_runtime}"
            await self.message.reply(afk_text)
            await self.message.delete()
            return monggo.remove_var(self.client.me.id, "AFK")


