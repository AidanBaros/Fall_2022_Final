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
        startPos: tuple[int, int],
    ):
        self.health = 0
        self.damage = 0
        self.critChance = 5
        self.speed = 0
        self.armor = None
        self.weapon = None
        self.type = None

        self.screen = pygame.display.get_surface()
        self.playerMapPos = playerMapPos

        self.screenSize = screenSize
        self.size: tuple[int, int] = ()

        self.collisionBoxList: list[pygame.Rect] = []
        self.startPos: tuple[int, int] = startPos

        self.rect = pygame.Rect(
            self.startPos[0],
            self.startPos[1],
            0,
            0,
        )
        self.hitbox = self.rect.copy()

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)

    def draw(self):
        pygame.draw.rect(self.screen, (0, 255, 0), self.rect)

    def collision(self, direction):
        for box in self.collisionBoxList:
            if box.colliderect(self.hitbox):
                if direction == "horizontal":
                    if self.direction.x > 0 and not self.screenTransition:
                        self.hitbox.right = box.left
                    if self.direction.x < 0 and not self.screenTransition:
                        self.hitbox.left = box.right
                    self.rect.centerx = self.hitbox.centerx
                    self.pos.x = self.hitbox.centerx

                if direction == "vertical":
                    if self.direction.y > 0 and not self.screenTransition:
                        self.hitbox.bottom = box.top
                    if self.direction.y < 0 and not self.screenTransition:
                        self.hitbox.top = box.bottom
                    self.rect.centery = self.hitbox.centery
                    self.pos.y = self.hitbox.centery
                return True
            else:
                return False

    def move(self):
        active = False
        moveChance = 0
        if active == False:
            print("if 1")
            moveChance = 0 #random.randint(0, 100)
        if moveChance == 0:
            print("if 2")
            active = True
            moveDurationCheck = 0
            XChance = 0
            YChance = 0
            moveDuration = 0

            if moveDurationCheck == 0:
                print("if 3")
                XChance = random.randint(0, 3)
                YChance = random.randint(0, 3)
                moveDuration = random.randint(20, 80)
            if moveDurationCheck != moveDuration:
                print("if 4")
                if XChance == 1:
                    self.direction.x -= 1
                elif XChance == 2:
                    self.direction.x += 1
                self.collision("horizontal")

                if YChance == 1:
                    self.direction.y -= 1
                elif YChance == 2:
                    self.direction.y += 1
                self.collision("vertical")
                moveDurationCheck += 1
            else:
                print("if 5")
                active = False
                moveDurationCheck = 0
                XChance = 0
                YChance = 0
                moveDuration = 0

    def loot(self):

        pass

    def detection(self):

        pass

    def attack(self):

        pass

    def update(self):
        self.move()
        self.draw()


class Spider(Monster):
    def __init__(
        self,
        screen: pygame.Surface,
        playerMapPos: list[int, int],
        screenSize: tuple[int, int],
        startPos: tuple[int, int],
    ):
        super().__init__(screen, playerMapPos, screenSize, startPos)
        self.health = 30
        self.damage = 0
        self.speed = 800
        self.rect.w, self.rect.h = (40, 40)


class Skeleton(Monster):
    def __init__(
        self,
        screen: pygame.Surface,
        playerMapPos: list[int, int],
        screenSize: tuple[int, int],
        startPos: tuple[int, int],
    ):
        super().__init__(screen, playerMapPos, screenSize, startPos)
        self.health = 20
        self.damage = 0
        self.speed = 700
        self.rect.w, self.rect.h = (50, 100)
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
    def __init__(
        self,
        screen: pygame.Surface,
        playerMapPos: list[int, int],
        screenSize: tuple[int, int],
        startPos: tuple[int, int],
    ):
        super().__init__(screen, playerMapPos, screenSize, startPos)
        self.health = 40
        self.damage = 0
        self.speed = 525
        self.rect.w, self.rect.h = (50, 100)
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


class Slim(Monster):
    def __init__(
        self,
        screen: pygame.Surface,
        playerMapPos: list[int, int],
        screenSize: tuple[int, int],
        startPos: tuple[int, int],
    ):
        super().__init__(screen, playerMapPos, screenSize, startPos)
        self.health = 30
        self.damage = 350
        self.speed = 0
        self.rect.w, self.rect.h = (50, 50)


class Bat(Monster):
    def __init__(
        self,
        screen: pygame.Surface,
        playerMapPos: list[int, int],
        screenSize: tuple[int, int],
        startPos: tuple[int, int],
    ):
        super().__init__(screen, playerMapPos, screenSize, startPos)
        self.health = 10
        self.damage = 0
        self.speed = 1050
        self.rect.w, self.rect.h = (20, 20)
