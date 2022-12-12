import random
import pygame
import armor
import weapons


class Monster:
    def __init__(
        self,
        playerMapPos: list[int, int],
        screenSize: tuple[int, int],
        startPos: tuple[int, int],
        collisionBoxList: list[pygame.Rect],
    ):
        self.health = 0
        self.damage = 0
        self.critChance = 5
        self.speed = 0
        self.armor = None
        self.weapon = None
        self.type = None
        self.color = None

        self.screen = pygame.display.get_surface()
        self.playerMapPos = playerMapPos

        self.screenSize = screenSize
        self.size: tuple[int, int] = ()

        self.collisionBoxList: list[pygame.Rect] = collisionBoxList
        self.startPos: tuple[int, int] = startPos

        self.rect = pygame.Rect(
            self.startPos[0],
            self.startPos[1],
            0,
            0,
        )
        self.hitbox: pygame.Rect = self.rect.copy()

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)

        self.active = False
        self.moveDurationCheck = 0
        self.XChance = 0
        self.YChance = 0
        self.moveDuration = 0
        self.returnVal = 0

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def collision(self, direction):
        
        for box in self.collisionBoxList:
            if box.colliderect(self.hitbox):
                if direction == "horizontal":
                    if self.direction.x > 0:
                        self.hitbox.right = box.left
                        self.returnVal = 1
                    if self.direction.x < 0:
                        self.hitbox.left = box.right
                        self.returnVal = 2
                    self.rect.centerx = self.hitbox.centerx
                    self.pos.x = self.hitbox.centerx

                if direction == "vertical":
                    if self.direction.y > 0:
                        self.hitbox.bottom = box.top
                        self.returnVal = 3
                    if self.direction.y < 0:
                        self.hitbox.top = box.bottom
                        self.returnVal = 4
                    self.rect.centery = self.hitbox.centery
                    self.pos.y = self.hitbox.centery
        

            #print(self.returnVal)
        self.returnVal = 0
        return self.returnVal

    def move(self, time):
        moveChance = 0
        collisionCheckVal = self.collision("horizontal")
        if self.active == False:
            moveChance =  random.randint(0, 250)
        if moveChance == 0:
            self.active = True

            if self.moveDurationCheck == 0:
                self.XChance = random.randint(0, 3)
                self.YChance = random.randint(0, 3)
                self.moveDuration = random.randint(20, 80)
            if self.moveDurationCheck < self.moveDuration:
                
                if collisionCheckVal == 1:
                    self.XChance = 2
                if collisionCheckVal == 2:
                    self.XChance = 1
                if collisionCheckVal == 3:
                    self.YChance = 2
                if collisionCheckVal == 4:
                    self.YChance = 1

                if (self.hitbox.right <= self.screenSize[0] and self.hitbox.left >= 0):
                    if self.XChance == 1 and self.hitbox.right <= self.screenSize[0]:
                        self.direction.x = 1
                    elif self.XChance == 2 and self.hitbox.left >= 0:
                        self.direction.x = -1
                else: self.direction.x *= -1

                if (self.hitbox.bottom <= self.screenSize[1] and self.hitbox.top >= 0):
                    if self.YChance == 1 and self.hitbox.bottom <= self.screenSize[1]:
                        self.direction.y = 1
                    elif self.YChance == 2 and self.hitbox.top >= 0:
                        self.direction.y = -1
                else: self.direction.y *= -1
                self.moveDurationCheck += 1
            else:
                self.active = False
                self.moveDurationCheck = 0
                self.XChance = 0
                self.YChance = 0
                self.moveDuration = 0

            self.pos.x += self.direction.x * self.speed * time
            self.hitbox.centerx = round(self.pos.x)
            self.rect.centerx = self.hitbox.centerx
            if self.collision("horizontal"):
                self.active = False

            self.pos.y += self.direction.y * self.speed * time
            self.hitbox.centery = round(self.pos.y)
            self.rect.centery = self.hitbox.centery
            if self.collision("vertical"):
                self.active = False

    def loot(self):

        pass

    def detection(self):

        pass

    def attack(self):

        pass

    def update(self, time):
        self.move(time)
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
        self.speed = 200
        self.size = (40, 40)
        self.rect.w, self.rect.h = self.size
        self.hitbox.w, self.hitbox.h = self.size
        self.color = "green"


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
        self.speed = 175
        self.size = (50, 100)
        self.rect.w, self.rect.h = self.size
        self.hitbox.w, self.hitbox.h = self.size
        hasArmor = random.randint(0, 100)
        self.color = "lightblue"
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
        self.speed = 132
        self.size = (50, 100)
        self.rect.w, self.rect.h = self.size
        self.hitbox.w, self.hitbox.h = self.size
        hasArmor = random.randint(0, 100)
        self.color = "blue"
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
        self.damage = 0
        self.speed = 100
        self.size = (50, 50)
        self.rect.w, self.rect.h = self.size
        self.hitbox.w, self.hitbox.h = self.size
        self.color = "limegreen"


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
        self.speed = 210
        self.size = (20, 20)
        self.rect.w, self.rect.h = self.size
        self.hitbox.w, self.hitbox.h = self.size
        self.color = "bisque"
