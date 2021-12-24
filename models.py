class Deal:
    def __init__(self, info):
        self.id = int(info['id'])
        self.pair = str(info['pair'])
        self.completed_safety_orders = int(info['completed_safety_orders_count'])
        self.take_profit = float(info['take_profit'])
        self.bot_id = int(info['bot_id'])


class Bot:
    def __init__(self, info):
        self.id = int(info['id'])
        self.take_profit = float(info['take_profit'])
        self.bot_name = str(info['name'])
