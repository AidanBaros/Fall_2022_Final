import pygame
from rooms import Room


class Player:
    def __init__(
        self,
        screen: pygame.Surface,
        playerMapPos: list[int, int],
        screenSize: tuple[int, int],
    ):
        self.frame_index = 0
        self.screen = screen
        self.playerMapPos = playerMapPos

        self.screenSize = screenSize

        self.rect = pygame.Rect(
            self.screenSize[0] // 2 - 25, self.screenSize[1] // 2 - 50, 50, 100
        )
        self.hitbox = self.rect.copy()

        self.collisionBoxList: list[pygame.Rect] = []

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 700

        self.screenTransition = False

        self.health = 50

    def getCollisionBoxList(self, collisionBoxList):
        self.collisionBoxList = collisionBoxList

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.rect.top >= 0:
            self.direction.y = -1
            # self.status = "up"
        elif keys[pygame.K_s] and self.rect.bottom <= self.screenSize[1]:
            self.direction.y = 1
            # self.status = "down"
        else:
            self.direction.y = 0

        if keys[pygame.K_a] and self.rect.left >= 0:
            self.direction.x = -1
            # self.status = "left"
        elif keys[pygame.K_d] and self.rect.right <= self.screenSize[0]:
            self.direction.x = 1
            # self.status = "right"
        else:
            self.direction.x = 0

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

    def move(self, time: float, roomList: list[list[Room]]):
        if (
            self.hitbox.left <= 0
            and roomList[self.playerMapPos[1]][self.playerMapPos[0]].hallwayDirection[3]
            == 1
        ):
            self.playerMapPos[0] -= 1
            self.pos.x = self.screenSize[0] - 100
            self.pos.y = self.screenSize[1] // 2
            self.screenTransition = True

        if (
            self.hitbox.right >= self.screenSize[0]
            and roomList[self.playerMapPos[1]][self.playerMapPos[0]].hallwayDirection[1]
            == 1
        ):
            self.playerMapPos[0] += 1
            self.pos.x = 100
            self.pos.y = self.screenSize[1] // 2
            self.screenTransition = True

        if (
            self.hitbox.top <= 0
            and roomList[self.playerMapPos[1]][self.playerMapPos[0]].hallwayDirection[0]
            == 1
        ):
            self.playerMapPos[1] -= 1
            self.pos.x = self.screenSize[0] // 2
            self.pos.y = self.screenSize[1] - 100
            self.screenTransition = True

        if (
            self.hitbox.bottom >= self.screenSize[1]
            and roomList[self.playerMapPos[1]][self.playerMapPos[0]].hallwayDirection[2]
            == 1
        ):
            self.playerMapPos[1] += 1
            self.pos.x = self.screenSize[0] // 2
            self.pos.y = 100
            self.screenTransition = True

        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.pos.x += self.direction.x * self.speed * time
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        self.collision("horizontal")

        self.pos.y += self.direction.y * self.speed * time
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collision("vertical")

        self.screenTransition = False

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)

    def update(self, time: float, roomList: list[Room]):
        self.input()
        self.move(time, roomList)
        self.draw()
