import pygame

class Player():
    def __init__(self, screen, screenSize):
        #self.status = "down_idle"
        self.frame_index = 0
        self.screen = screen
        self.screenX = screenSize[0]
        self.screenY = screenSize[1]

        self.rect = pygame.Rect(self.screenX // 2 - 25, self.screenY // 2 - 50, 50, 100)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            #self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            #self.status = "down"
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            #self.status = "left"
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            #self.status = "right"
        else:
            self.direction.x = 0

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    
    def update():

        pass