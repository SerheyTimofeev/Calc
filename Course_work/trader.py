import json
import random
from argparse import ArgumentParser
from json import JSONDecodeError


class Trader:
    config = "config.json"
    system = "system.json"

    def __init__(self):
        with open(self.config, 'r') as f:
            try:
                config_data = json.load(f)
            except JSONDecodeError:
                config_data = {"delta": 0.5}
            self.delta = config_data.get("delta")
        with open(self.system, 'r') as f:
            try:
                self.data = json.load(f)
            except JSONDecodeError:
                self.restart()
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

    def print_state(self):
        print(f"price:{self.price}")
        print(f"usd:{self.available_usd}")
        print(f"uah:{self.available_uah}")


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
        if not self.available_uah:
            self.update_history("fail buy")
            print("You dont have UAH on your balance")
            return
        actual_sum = round(self.available_uah / self.price, 2)
        self.available_uah = 0
        self.available_usd += actual_sum
        self.update_history("buy all")

    def sell_usd(self, amount):
        if amount > self.available_usd:
            self.update_history("fail sell")
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {amount}, AVAILABLE {self.available_usd}")
            return
        actual_sum = amount * self.price
        self.available_uah += actual_sum
        self.available_usd -= amount
        self.update_history("sell")

    def sell_all_usd(self):
        if not self.available_usd:
            self.update_history("fail sell")
            print("You dont have USD on your balance")
            return
        actual_sum = round(self.price * self.available_usd, 2)
        self.available_uah += actual_sum
        self.available_usd = 0
        self.update_history("sell all")

    def restart(self):
        self.data = [
            {
                "available_usd": 0.0,
                "available_uah": 10000.0,
                "rate": 36.5,
                "action": "initial"
            }
        ]
        with open(self.system, 'w') as f:
            json.dump(self.data, f)

    def print_history(self):
        for action in self.data:
            print(f"Action:{action.get('action')}\t Rate:{action.get('rate')}\t "
                  f"USD:{action.get('available_usd')}\t UAH:{action.get('available_uah')}")


args = ArgumentParser()

args.add_argument("main_command", type=str, choices=["NEXT", "HISTORY", "RATE", "AVAILABLE", "SELL", "BUY", "RESTART"])
args.add_argument("another_command", nargs="?", type=str, default=0)

args = vars(args.parse_args())

command_action = args['main_command']
command_amount = args['another_command']
trader = Trader()
if command_action == "RATE":
    trader.rate()
    trader.print_state()
elif command_action == "NEXT":
    trader.next_price()
    trader.print_state()
elif command_action == "AVAILABLE":
    print("Your balance:")
    trader.print_available()
elif command_action == "RESTART":
    print("New game")
    trader.restart()
    trader.print_state()
elif command_action == "BUY":
    if not command_amount:
        print("Amount is required")
    if command_amount == "ALL":
        trader.buy_all_usd()
        trader.print_state()
    else:
        trader.buy_usd(float(command_amount))
        trader.print_state()
elif command_action == "SELL":
    if not command_amount:
        print("Amount is required")
    if command_amount == "ALL":
        trader.sell_all_usd()
        trader.print_state()
    else:
        trader.sell_usd(float(command_amount))
        trader.print_state()
elif command_action == "HISTORY":
    trader.print_history()
