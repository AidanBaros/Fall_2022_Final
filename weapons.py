class Weapon:
    def __init__(self):
        self.damage = 0
        self.critChance = 10
        self.attackSpeed = 0
        self.length = 0
        self.width = 0
        self.damageType = None
        self.EnchantmentList = []
        self.Sockets = []


class Dagger(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 7
        self.attackSpeed = 0.5
        self.length = 40
        self.width = 10
        self.damageType = "Piercing"


class Club(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 6
        self.attackSpeed = 1
        self.length = 55
        self.width = 20
        self.damageType = "Bludgeoning"


class Axe(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 12
        self.attackSpeed = 1
        self.length = 55
        self.width = 5
        self.damageType = "Slashing"


class Spear(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 10
        self.attackSpeed = 1.25
        self.length = 100
        self.width = 10
        self.damageType = "Piercing"


class Mace(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 12
        self.attackSpeed = 1
        self.length = 55
        self.width = 20 
        self.damageType = "Bludgeoning"


class BattleAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 16
        self.attackSpeed = 1.75
        self.length = 70
        self.width = 10
        self.damageType = "Slashing"


class Maul(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 14
        self.attackSpeed = 1.5
        self.length = 65
        self.width = 20
        self.damageType = "Bludgeoning"


class GreatSword(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 20
        self.attackSpeed = 2
        self.length = 70
        self.width = 25
        self.damageType = "Slashing"


class LongSword(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 14
        self.attackSpeed = 1.5
        self.length = 80
        self.width = 15
        self.damageType = "Slashing"


class ShortSword(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 12
        self.attackSpeed = 0.75
        self.length = 60
        self.width = 10
        self.damageType = "Slashing"


class WarHammer(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 14
        self.attackSpeed = 1.25
        self.length = 60
        self.width = 20
        self.damageType = "Bludgeoning"
