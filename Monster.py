import random
import pygame
import armor
import weapons


class Monster:
    def __init__(
        self,
        screen: pygame.Surface,
        playerMapPos: list[int, int],
        screenSize: tuple[int, int],
    ):
        self.health = 0
        self.damage = 0
        self.critChance = 5
        self.speed = 0
        self.armor = None
        self.weapon = None
        self.type = None

        self.screen = screen
        self.playerMapPos = playerMapPos

        self.screenSize = screenSize
        self.size: tuple[int, int] = ()

        self.rect = pygame.Rect(
            self.screenSize[0] // 2 - 25,
            self.screenSize[1] // 2 - 50,
            self.size[0],
            self.size[1],
        )
        self.hitbox = self.rect.copy()

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)


class Spider(Monster):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.damage = 0
        self.speed = 800
        self.size = (40, 40)


class Skeleton(Monster):
    def __init__(self):
        super().__init__()
        self.health = 20
        self.damage = 0
        self.speed = 700
        self.size = (50, 100)
        hasArmor = random.randint(0, 100)
        if hasArmor <= 7:
            whichArmor = random.randint(0, 5)
            if whichArmor >= 4:
                self.armor = armor.Leather()
            else:
                self.armor = armor.ChainMail()

        hasWeapon = random.randint(0, 100)
        if hasWeapon <= 7:
            whichWeapon = random.randint(0, 20)
            if whichWeapon >= 7:
                self.weapon = weapons.Club()
            elif whichWeapon >= 12:
                self.weapon = weapons.Dagger()
            elif whichWeapon >= 16:
                self.weapon = weapons.Axe()
            elif whichWeapon >= 19:
                self.weapon = weapons.ShortSword()
            else:
                self.weapon = weapons.LongSword()

        self.weapon = None


class Zombie(Monster):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.damage = 0
        self.speed = 525
        self.size = (50, 100)

        self.armor = None
        self.weapon = None


class Slim(Monster):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.damage = 350
        self.speed = 0
        self.size = (50, 50)


class Bat(Monster):
    def __init__(self):
        super().__init__()
        self.health = 10
        self.damage = 0
        self.speed = 1050
        self.size = (20, 20)
