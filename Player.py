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
        self.returnVal = False

        self.screenSize = screenSize

        self.switchSide = None

        self.rect = pygame.Rect(
            self.screenSize[0] // 2 - 25, self.screenSize[1] // 2 - 50, 50, 100
        )
        self.hitbox = self.rect.copy()

        self.collisionBoxList: list[list[pygame.Rect]] = []

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 700

    def getCollisionBoxList(self, collisionBoxList):
        self.collisionBoxList = collisionBoxList

    def input(self, roomList: list[list[Room]]):
        keys = pygame.key.get_pressed()
        if (
            self.rect.x <= 0
            and roomList[self.playerMapPos[1]][self.playerMapPos[0]].hallwayDirection[3]
            == 1
        ):
            self.switchSide = 3
        if (
            self.rect.x >= self.screenSize[0] - self.rect.w
            and roomList[self.playerMapPos[1]][self.playerMapPos[0]].hallwayDirection[1]
            == 1
        ):
            self.switchSide = 1
        if (
            self.rect.y <= 0
            and roomList[self.playerMapPos[1]][self.playerMapPos[0]].hallwayDirection[0]
            == 1
        ):
            self.switchSide = 0
        if (
            self.rect.y >= self.screenSize[1] - self.rect.h
            and roomList[self.playerMapPos[1]][self.playerMapPos[0]].hallwayDirection[2]
            == 1
        ):
            self.switchSide = 2

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
        for boxes in self.collisionBoxList:
            if boxes.colliderect(self.hitbox):
                print("collide")
                if direction == "horizontal":
                    if self.direction.x > 0:
                        self.hitbox.right = boxes.left
                    if self.direction.x < 0:
                        self.hitbox.left = boxes.right
                    self.rect.centerx = self.hitbox.centerx
                    self.pos.x = self.hitbox.centerx

                if direction == "vertical":
                    if self.direction.y > 0:
                        self.hitbox.bottom = boxes.top
                    if self.direction.y < 0:
                        self.hitbox.top = boxes.bottom
                    self.rect.centery = self.hitbox.centery
                    self.pos.y = self.hitbox.centery
        

    def move(self, time: float, roomList: list[list[Room]]):
        """if self.switchSide == 0:
            self.playerMapPos[1] -= 1
            self.pos.x = self.screenSize[0] // 2 - self.rect.width // 2
            self.pos.y = self.screenSize[1] - self.rect.h - 10
        elif self.switchSide == 1:
            self.playerMapPos[0] += 1
            self.pos.x = 100
            self.pos.y = self.screenSize[1] // 2 - self.rect.height // 2
        elif self.switchSide == 2:
            self.playerMapPos[1] += 1
            self.pos.x = self.screenSize[0] // 2 - self.rect.width // 2
            self.pos.y = 100
        elif self.switchSide == 3:
            self.playerMapPos[0] -= 1
            self.pos.x = self.screenSize[0] - self.rect.w - 10
            self.pos.y = self.screenSize[1] // 2 - self.rect.height // 2
        self.switchSide = None"""

        """self.returnVal, tempX, tempY = roomList[self.playerMapPos[1]][self.playerMapPos[0]].collision(self.rect)
        if self.returnVal:
            self.pos.x = tempX
            self.pos.y = tempY"""

        

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

        
        

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)

    def update(self, time: float, roomList: list[Room]):
        self.input(roomList)
        self.move(time, roomList)
        self.draw()
