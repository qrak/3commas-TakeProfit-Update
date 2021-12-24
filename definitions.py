from classes import *
import typing
import config
import logging
import asyncio
logger = logging.getLogger()


def initialize_logger():
    formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
    if config.LOGGING:
        file_handler = logging.FileHandler('info.log')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)

    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)
    logger.addHandler(stream_handler)


def get_current_bot_take_profit(bot_class: typing.ClassVar, get_bot_id: int) -> float:
    get_bot = bot_class.get_bot()
    bot_take_profit = get_bot[get_bot_id].take_profit

    return bot_take_profit


def calculate_step_scale_profit(bot_take_profit: float, current_deal_take_profit: float, current_deal_completed_so: int
                                ) -> float:
    count_take_profit = bot_take_profit + (config.PROFIT_STEP_SCALE * current_deal_completed_so)

    if count_take_profit != current_deal_take_profit and current_deal_completed_so != 0:
        return count_take_profit


def calculate_fixed_take_profit(deal: typing.ClassVar, deal_index: int, current_deal_take_profit: float,
                                current_deal_completed_so: int, current_bot_take_profit: float) -> float:
    count_take_profit = 0
    try:
        if current_deal_completed_so != 0:
            safety_order_number = current_deal_completed_so - 1
            safety_order_index = config.PROFIT_INCREASE_STEPS[safety_order_number]
            count_take_profit = current_bot_take_profit + safety_order_index
    except IndexError as e:
        logger.error("Can't change profit of deal id: %s pair: %s because profit of safety order number: %s is not set"
                     ".: %s",
                     deal[deal_index].id, deal[deal_index].pair, current_deal_completed_so, e)

    if count_take_profit != current_deal_take_profit and current_deal_completed_so != 0:
        return count_take_profit


def update_bot_deals_profit(deal: typing.ClassVar, active_deal, deal_index: int, bot_id: int, bot_take_profit):
    if active_deal[deal_index].bot_id in config.BOT_IDS:
        current_deal_completed_so = active_deal[deal_index].completed_safety_orders
        current_deal_take_profit = active_deal[deal_index].take_profit
        if config.FIXED_INCREASE_MODE:
            take_profit = calculate_fixed_take_profit(active_deal, deal_index, current_deal_take_profit,
                                                      current_deal_completed_so, bot_take_profit)
        else:
            take_profit = calculate_step_scale_profit(bot_take_profit, current_deal_take_profit,
                                                      current_deal_completed_so)
        if take_profit:
            try:
                deal.update_deal_take_profit(deal_index, take_profit)
            except Exception as e:
                logger.error("Error updating deal id %s: %s", active_deal[deal_index].id, e)

            logger.info("New take profit of bot id: %s deal pair: %s deal id: %s safety orders count: %s"
                        " new take profit: %s", bot_id, active_deal[deal_index].pair, active_deal[deal_index].id,
                        current_deal_completed_so, take_profit)


async def loop_through_bot_id_from_config():
    while True:
        deals = int()
        deal_ids = int()
        active_deal = int()
        current_bot_take_profit = float()
        for bot_id in config.BOT_IDS:
            try:
                bot = Bots(bot_id)
                current_bot_take_profit = get_current_bot_take_profit(bot, bot_id)
                deals = Deals(bot_id)
                active_deal = deals.get_active_deals()
                deal_ids = deals.get_deals_ids()
            except KeyError as e:
                logger.error("Wrong bot id: %s!", e)
            for deal_index in deal_ids:
                update_bot_deals_profit(deals, active_deal, deal_index, bot_id, current_bot_take_profit)

        if config.TIME_INTERVAL > 0:
            logger.info("Checking deals finished, next iteration in: %s seconds", config.TIME_INTERVAL)
            await asyncio.sleep(config.TIME_INTERVAL)
        else:
            logger.info("Checking deals finished.")
            break
