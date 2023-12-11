from src.enums.user_enums import Statuses
from src.generators.player_localization import PlayerLocalization

class Player:
    def __init__(self):
        self.result = {}
        self.reset()

    def set_status(self, status=Statuses.active.value):
        self.result["account_status"] = status
        return self

    def set_balance(self, balance=0):
        self.result["balance"] = balance
        return self

    def set_avatar(self, avatar="https://google.com/"):
        self.result["avatar"] = avatar

    def reset(self):
        self.result["localize"] = {
            "en": PlayerLocalization("en_US").build(),  # прописывать build чтобы получить данные а не объект
            "ru": PlayerLocalization("ru_RU").build()
        }
        self.set_status()
        self.set_avatar()
        self.set_balance()
        return self

    def update_inner_value(self, keys, value):
        if not isinstance(keys, list):
            self.result[keys] = value
        else:
            temp = self.result
            for item in keys[:-1]:
                if item not in temp.keys():
                    temp[item] = {}
                temp = temp[item]
            temp[keys[-1]] = value
        return self

    def build(self):
        return self.result



