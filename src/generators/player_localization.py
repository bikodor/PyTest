from faker import Faker

fake = Faker()


class PlayerLocalization:

    def __init__(self, lang):
        self.fake = Faker(lang)
        self.result = {
            "nickname": self.fake.first_name() # можно сделать кучу фишек, смотри в документации faker'а
        }

    def build(self):
        return self.result

