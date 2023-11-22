import json
import random
from argparse import ArgumentParser


class Trader:
    config = "config.json"
    system = "system.json"

    def __init__(self):
        with open(self.config, 'r') as f:
            config_data = json.load(f)
            self.delta = config_data.get("delta")
        with open(self.system, 'r') as f:
            self.data = json.load(f)
        last_action = self.data[-1]
        self.available_uah = last_action.get("available_uah")
        self.available_usd = last_action.get("available_usd")
        self.price = last_action.get("rate")

    def update_history(self, action):
        self.data.append({
            "available_usd": self.available_usd,
            "available_uah": self.available_uah,
            "rate": self.price,
            "action": action
        })
        with open(self.system, 'w') as f:
            json.dump(self.data, fp=f)

    def rate(self):
        self.update_history("rate")
        return self.price

    def next_price(self):
        self.price = round(random.uniform(self.price - self.delta, self.price + self.delta), 2)
        self.update_history("next")

    def get_available_usd(self):
        self.update_history("check usd")
        return self.available_usd

    def get_available_uah(self):
        self.update_history("check uah")
        return self.available_uah

    def print_available(self):
        print(f"usd:{self.get_available_usd()}")
        print(f"uah:{self.get_available_uah()}")

    def buy_usd(self, amount):
        actual_sum = round(amount * self.price)
        if actual_sum > self.available_uah:
            self.update_history("fail buy")
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {actual_sum}, AVAILABLE {self.available_uah}")
            return
        self.available_uah -= actual_sum
        self.available_usd += amount
        self.update_history("buy")

    def buy_all_usd(self):
        actual_sum = round(self.available_uah / self.price, 2)
        self.available_uah = 0
        self.available_usd += actual_sum
        self.update_history("buy all")

    def sell_usd(self, amount):
        if amount > self.available_usd:
            self.update_history("fail sell")
            return f"UNAVAILABLE, REQUIRED BALANCE USD {amount}, AVAILABLE {self.available_usd}"
        actual_sum = amount * self.price
        self.available_uah += actual_sum
        self.available_usd -= amount
        self.update_history("sell")

    def sell_all_usd(self):
        actual_sum = round(self.price * self.available_usd, 2)
        self.available_uah += actual_sum
        self.available_usd = 0
        self.update_history("sell all")

    def restart(self):
        data = [
            {
                "available_usd": 0.0,
                "available_uah": 10000.0,
                "rate": 36.5,
                "action": "initial"
            }
        ]
        with open(self.system, 'w') as f:
            json.dump(data, f)


args = ArgumentParser()

args.add_argument("main_command", type=str, choices=["NEXT", "RATE", "AVAILABLE", "SELL", "BUY", "RESTART"])
args.add_argument("another_command", nargs="?", type=str, default=0)

args = vars(args.parse_args())

command_action = args['main_command']
command_amount = args['another_command']
trader = Trader()
if command_action == "RATE":
    trader.rate()
elif command_action == "NEXT":
    trader.next_price()
elif command_action == "AVAILABLE":
    trader.print_available()
elif command_action == "RESTART":
    trader.restart()
elif command_action == "BUY":
    if not command_amount:
        print("Amount is required")
    if command_amount == "ALL":
        trader.buy_all_usd()
    else:
        trader.buy_usd(float(command_amount))
elif command_amount == "SELL":
    if not command_amount:
        print("Amount is required")
    if command_amount == "ALL":
        trader.sell_all_usd()
    else:
        trader.sell_usd(float(command_amount))
