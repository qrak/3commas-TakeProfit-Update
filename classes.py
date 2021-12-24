from py3cw.request import Py3CW
from models import *

import config
import typing


p3cw = Py3CW(
    key=config.params["apiKey"],
    secret=config.params["apiSecret"],

    request_options={
        'request_timeout': 10,
        'nr_of_retries': 1,
        'retry_status_codes': [502],

    }
)


class Bots:
    def __init__(self, bot: int):
        self.bot = int(bot)
        self.error, self.data = p3cw.request(
            entity='bots',
            action='show',
            action_id=str(bot)
        )

    def get_bot(self) -> typing.Dict[int, Bot]:
        bot_dict = dict()

        if self.data is not None:
            bot_dict = {int(self.bot): Bot(self.data)}
        return bot_dict


class Deals:
    def __init__(self, bot: int):
        self.error, self.data = p3cw.request(
            entity='deals',
            action='',
            action_id='',
            payload={
                "scope": 'active',
                "bot_id": bot
            }
        )

    def get_active_deals(self) -> typing.Dict[int, Deal]:
        deals = dict()

        if self.data is not None:
            deals = {int(deal['id']): Deal(deal) for deal in self.data}

        return deals

    def get_deals_ids(self) -> typing.List[int]:
        deals = list()

        if self.data is not None:
            for deal_id in self.data:
                deals.append(deal_id['id'])

        return deals

    @staticmethod
    def update_deal_take_profit(deal_id: int, take_profit: float):

        error, data = p3cw.request(
            entity='deals',
            action='update_deal',
            action_id=str(deal_id),
            payload={
                'take_profit': take_profit
            })

        return data

