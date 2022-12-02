class Armor:
    def __init__(self):
        self.damageReductionPercent = 0
        self.speedDebuff = 0
        self.EnchantmentList = []
        self.Sockets = []


class Leather(Armor):
    def __init__(self):
        super().__init__()
        self.damageReductionPercent = 20


class ChainMail(Armor):
    def __init__(self):
        super().__init__()
        self.damageReductionPercent = 40
        self.speedDebuff = 50


class ScaleMail(Armor):
    def __init__(self):
        super().__init__()
        self.damageReductionPercent = 60
        self.speedDebuff = 100


class Plate(Armor):
    def __init__(self):
        super().__init__()
        self.damageReductionPercent = 80
        self.speedDebuff = 200
