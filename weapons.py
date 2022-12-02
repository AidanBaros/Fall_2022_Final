class Weapon:
    def __init__(self):
        self.damage = 0
        self.critChance = 10
        self.attackSpeed = 0
        self.range = 0
        self.damageType = None #This is for later but i think it would be cool to add this in (bludgeoing, slashing, piercing)
        self.EnchantmentList = []
        self.Sockets = []


class Dagger(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 7
        self.attackSpeed = 0.5
        self.range = 40


class Club(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 6
        self.attackSpeed = 1
        self.range = 55


class Axe(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 12
        self.attackSpeed = 1
        self.range = 55


class Spear(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 10
        self.attackSpeed = 1.25
        self.range = 100


class Mace(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 12
        self.attackSpeed = 1
        self.range = 55 


class BattleAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 16
        self.attackSpeed = 1.75
        self.range = 70


class Maul(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 14
        self.attackSpeed = 1.5
        self.range = 65


class GreatSword(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 20
        self.attackSpeed = 2
        self.range = 70


class LongSword(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 14
        self.attackSpeed = 1.5
        self.range = 80


class ShortSword(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 12
        self.attackSpeed = 0.75
        self.range = 60


class WarHammer(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 14
        self.attackSpeed = 1.25
        self.range = 60
