import pygame
from settings import *

class Player():
    def __init__(self, screen, grid):
        #self.status = "down_idle"
        self.frame_index = 0
        self.screen = screen

        self.rect = pygame.Rect(self.screenX // 2 - 25, self.screenY // 2 - 50, 50, 100)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def input(self):
        keys = pygame.key.get_pressed()
        if self.rect.x <= 0 and grid.tile.sides[3] == 1:
            MapXPos -= 1
            self.rect.x = SCREENX - self.rect.w - 10
            self.rect.y = SCREENY // 2 - self.rect.height // 2
        if self.rect.x >= SCREENX - self.rect.w and grid.tile.sides[1] == 1:
            MapXPos += 1
            self.rect.x = 10
            self.rect.y = SCREENY // 2 - self.rect.height // 2
        if self.rect.y <= 0 and grid.tile.sides[0] == 1:
            MapYPos -= 1
            self.rect.x = SCREENX // 2 - self.rect.width // 2
            self.rect.y = SCREENY - self.rect.h - 10
        if self.rect.y >= SCREENY - self.rect.h and grid.tile.sides[2] == 1:
            MapYPos += 1
            self.rect.x = SCREENX // 2 - self.rect.width // 2
            self.rect.y = 10

        if keys[pygame.K_w] and self.rect.top >= 0:
            self.direction.y = -1
            #self.status = "up"
        elif keys[pygame.K_s] and self.rect.bottom <= SCREENY:
            self.direction.y = 1
            #self.status = "down"
        else:
            self.direction.y = 0

        if keys[pygame.K_a] and self.rect.left >= 0:
            self.direction.x = -1
            #self.status = "left"
        elif keys[pygame.K_d] and self.rect.right <= SCREENX:
            self.direction.x = 1
            #self.status = "right"
        else:
            self.direction.x = 0

        grid.collision(self.rect)

    def move(self, time):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        self.pos.x += self.direction.x * self.speed * time
        self.rect.centerx = self.pos.x

        self.pos.y += self.direction.y * self.speed * time
        self.rect.centery = self.pos.y

    
    def update(self, time):
        self.input()
        self.move()

        pass