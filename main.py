from definitions import *
import asyncio


async def compounding():
    while True:
        logging.info("Before compounding")
        await asyncio.sleep(5)


async def start():
    initialize_logger()
    """if config.BOT_COMPOUNDING:
        compound = asyncio.create_task(compounding())
    else:
        compound = asyncio.create_task(compounding())
        """
    if config.TIME_INTERVAL > 0:
        deals = asyncio.create_task(loop_through_bot_id_from_config())
    else:
        deals = asyncio.create_task(loop_through_bot_id_from_config())

    await deals
    #await asyncio.gather(compound, deals)

if __name__ == '__main__':
    asyncio.run(start())