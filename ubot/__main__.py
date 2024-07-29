import asyncio
import sys

from ubot import *

loop = asyncio.get_event_loop_policy()
event_loop = loop.get_event_loop()


async def loader_user(user_id, _ubot):
    ubot_ = Ubot(**_ubot)
    try:
        await asyncio.wait_for(ubot_.start(), timeout=90)
        await ubot_.join_chat("suportkage")
        await ubot_.join_chat("kagestore69")
    except KeyError as tol:
        LOGGER(__name__).error(f"Ni Bocah Ke Ban : {user_id} di {tol}")
    except:
        monggo.remove_ubot(user_id)
        monggo.rm_all(user_id)
        monggo.rem_expired_date(user_id)
        monggo.rem_pref(user_id)
        for X in monggo.get_chat(user_id):
            monggo.remove_chat(user_id, X)
        print(f"✅ {user_id} Expired")


async def test():
    userbots = monggo.get_userbots()
    tasks = [
        asyncio.create_task(loader_user(int(_ubot["name"]), _ubot))
        for _ubot in userbots
    ]
    await asyncio.gather(*tasks, bot.start())


async def main():
    await test()
    try:
        await loadPlugins()
        await expiredUserbots()
        await installPeer()
        if "test" not in sys.argv:
            await bot.idle()
    except KeyboardInterrupt:
        logger.warning("BOT STOP....")
    finally:
        await bot.stop()


if __name__ == "__main__":
    #install()
    asyncio.set_event_loop(event_loop)
    event_loop.run_until_complete(main())
