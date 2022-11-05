import pygame
import random

pygame.init()


class room:
    def __init__(
        self,
        roomtype,
        hallwayDirection,
        ID,
        screenX,
        screenY,
        screen,
        playerSize,
    ):
        self.hallwayDirection = hallwayDirection
        self.roomtype = roomtype
        self.screenX = screenX
        self.screenY = screenY
        self.screen = screen
        self.ID = ID
        self.playerSize = playerSize

        self.hallwaySize = self.screenX // 8
        self.WidthNoHallway = self.screenX // 2 - self.hallwaySize // 2
        self.HeightNoHallway = self.screenY // 2 - self.hallwaySize // 2
        self.WidthHallway = self.screenX // 2 + self.hallwaySize // 2
        self.HeightHallway = self.screenY // 2 + self.hallwaySize // 2
        self.offset = 0
        self.color = (255, 255, 255)

        if self.ID == 0:
            self.color = (0, 0, 0)
        elif self.ID == 1 or self.ID == 2 or self.ID == 3 or self.ID == 4:
            self.offset = 200
        elif self.ID == 11 or self.ID == 12 or self.ID == 13 or self.ID == 14:
            self.offset = 300
        elif self.ID == 15:
            self.offset = 100
#Playable area rects
        self.center_square = pygame.Rect(
            self.WidthNoHallway,
            self.HeightNoHallway,
            self.hallwaySize,
            self.hallwaySize,
        )
        self.main_room = pygame.Rect(
            self.offset,
            self.offset,
            self.screenX - (self.offset * 2),
            self.screenY - (self.offset * 2),
        )
        self.top_hallway = pygame.Rect(
            self.WidthNoHallway, 0, self.hallwaySize, self.HeightNoHallway
        )
        self.right_hallway = pygame.Rect(
            self.WidthHallway,
            self.HeightNoHallway,
            self.WidthNoHallway,
            self.hallwaySize,
        )
        self.bottom_hallway = pygame.Rect(
            self.WidthNoHallway,
            self.HeightHallway,
            self.hallwaySize,
            self.HeightNoHallway,
        )
        self.left_hallway = pygame.Rect(
            0, self.HeightNoHallway, self.WidthNoHallway, self.hallwaySize
        )
#No Room collision rects
        self.NoRoomTL = pygame.Rect(
            0,
            0,
            self.WidthNoHallway,
            self.HeightNoHallway,
        )
        self.NoRoomTR = pygame.Rect(
            self.WidthHallway,
            0,
            self.WidthNoHallway,
            self.HeightNoHallway,
        )
        self.NoRoomBL = pygame.Rect(
            0,
            self.HeightHallway,
            self.WidthNoHallway,
            self.HeightNoHallway,
        )
        self.NoRoomBR = pygame.Rect(
            self.WidthHallway,
            self.HeightHallway,
            self.WidthNoHallway,
            self.HeightNoHallway,
        )
#Room collision rects
        self.TL = pygame.Rect(
            0,
            0,
            self.WidthNoHallway,
            self.offset,
        )
        self.TR = pygame.Rect(
            self.WidthHallway,
            0,
            self.WidthNoHallway,
            self.offset,
        )
        self.RT = pygame.Rect(
            self.screenX - self.offset,
            0,
            self.offset,
            self.WidthNoHallway,
        )
        self.RB = pygame.Rect(
            self.screenX - self.offset,
            self.HeightHallway,
            self.offset,
            self.WidthNoHallway,
        )
        self.BR = pygame.Rect(
            self.WidthHallway,
            self.screenY - self.offset,
            self.WidthNoHallway,
            self.offset,
        )
        self.BL = pygame.Rect(
            0,
            self.screenY - self.offset,
            self.WidthNoHallway,
            self.offset,
        )
        self.LB = pygame.Rect(
            0,
            self.HeightHallway,
            self.offset,
            self.WidthNoHallway,
        )
        self.LT = pygame.Rect(
            0,
            0,
            self.offset,
            self.WidthNoHallway,
        )

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            self.center_square,
        )
        if self.hallwayDirection[0] == 1:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                self.top_hallway,
            )
        if self.hallwayDirection[1] == 1:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                self.right_hallway,
            )
        if self.hallwayDirection[2] == 1:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                self.bottom_hallway,
            )
        if self.hallwayDirection[3] == 1:
            pygame.draw.rect(
                self.screen,
                (255, 255, 255),
                self.left_hallway,
            )

        if self.ID not in (5, 6, 7, 8, 9, 10):
            pygame.draw.rect(
                self.screen,
                self.color,
                self.main_room,
            )

    def collision(self, player: pygame.Rect, direction):
        if self.ID in (1, 2, 3, 4, 11, 12, 13, 14, 15):
            if direction == "w":
                print("w1")
                print(
                    player.colliderect(self.LT.bottom) 
                    or 
                    player.colliderect(self.TL.bottom) 
                    or 
                    player.colliderect(self.TR.bottom) 
                    or 
                    player.colliderect(self.RT.bottom)
                )
                return(
                    player.colliderect(self.LT.bottom) 
                    or 
                    player.colliderect(self.TL.bottom) 
                    or 
                    player.colliderect(self.TR.bottom) 
                    or 
                    player.colliderect(self.RT.bottom)
                )
            if direction == "a":
                print("a1")
                print(
                    player.colliderect(self.TR.right) 
                    or 
                    player.colliderect(self.RT.right) 
                    or 
                    player.colliderect(self.RB.right) 
                    or 
                    player.colliderect(self.BR.right)
                )
                return(
                    player.colliderect(self.TR.right) 
                    or 
                    player.colliderect(self.RT.right) 
                    or 
                    player.colliderect(self.RB.right) 
                    or 
                    player.colliderect(self.BR.right)
                )
            if direction == "s":
                print("s1")
                print(
                    player.colliderect(self.RB.top) 
                    or 
                    player.colliderect(self.BR.top) 
                    or 
                    player.colliderect(self.BL.top) 
                    or 
                    player.colliderect(self.LB.top)
                )
                return(
                    player.colliderect(self.RB.top) 
                    or 
                    player.colliderect(self.BR.top) 
                    or 
                    player.colliderect(self.BL.top) 
                    or 
                    player.colliderect(self.LB.top)
                )
            if direction == "d":
                print("d1")
                print(
                    player.colliderect(self.BL.left) 
                    or 
                    player.colliderect(self.LB.left) 
                    or 
                    player.colliderect(self.LT.left) 
                    or 
                    player.colliderect(self.TL.left)
                )
                return(
                    player.colliderect(self.BL.left) 
                    or 
                    player.colliderect(self.LB.left) 
                    or 
                    player.colliderect(self.LT.left) 
                    or 
                    player.colliderect(self.TL.left)
                )
        else:
            if direction == "w":
                print("w2")
                print(
                    player.colliderect(self.NoRoomTL.bottom) 
                    or 
                    player.colliderect(self.NoRoomTR.bottom)
                )
                return(
                    player.colliderect(self.NoRoomTL.bottom) 
                    or 
                    player.colliderect(self.NoRoomTR.bottom)
                )
            if direction == "a":
                print("a2")
                print(
                    player.colliderect(self.NoRoomTL.right) 
                    or 
                    player.colliderect(self.NoRoomBL.right)
                )
                return(
                    player.colliderect(self.NoRoomTL.right) 
                    or 
                    player.colliderect(self.NoRoomBL.right)
                )
            if direction == "s":
                print("s2")
                print(
                    player.colliderect(self.NoRoomBR.top) 
                    or 
                    player.colliderect(self.NoRoomBL.top)
                )
                return(
                    player.colliderect(self.NoRoomBR.top) 
                    or 
                    player.colliderect(self.NoRoomBL.top)
                )
            if direction == "d":
                print("d2")
                print(
                    player.colliderect(self.NoRoomBR.left) 
                    or 
                    player.colliderect(self.NoRoomTR.left)
                )
                return(
                    player.colliderect(self.NoRoomBR.left) 
                    or 
                    player.colliderect(self.NoRoomTR.left)
                )
                

    """
    return (
                (player.colliderect(self.main_room))
                or (player.colliderect(self.center_square))
                or (
                    self.hallwayDirection[0] == 1
                    and player.colliderect(self.top_hallway)
                )
                or (
                    self.hallwayDirection[1] == 1
                    and player.colliderect(self.right_hallway)
                )
                or (
                    self.hallwayDirection[2] == 1
                    and player.colliderect(self.bottom_hallway)
                )
                or (
                    self.hallwayDirection[3] == 1
                    and player.colliderect(self.left_hallway)
                )
            )
        return (
            (player.colliderect(self.center_square)) or
            (
                self.hallwayDirection[0] == 1
                and player.colliderect(self.top_hallway)
            )
            or (
                self.hallwayDirection[1] == 1
                and player.colliderect(self.right_hallway)
            )
            or (
                self.hallwayDirection[2] == 1
                and player.colliderect(self.bottom_hallway)
            )
            or (
                self.hallwayDirection[3] == 1
                and player.colliderect(self.left_hallway)
            )
        )

    if self.ID in (1, 2, 3, 4, 11, 12, 13, 14, 15):
            if self.hallwayDirection[0] == 1:
                if (
                    (
                        playerPos[1] >= self.offset 
                        and 
                        playerPos[0] >= self.offset
                    ) 
                    or 
                    (
                        playerPos[1] >= 0 
                        and 
                        playerPos[0] >= self.WidthNoHallway 
                        and
                        playerPos[0] + self.playerSize[0] <= self.WidthHallway
                    )
                    or 
                    (
                        playerPos[1] >= self.offset 
                        and 
                        playerPos[0] >= self.WidthHallway 
                        and
                        playerPos[0] + self.playerSize[0] <= self.screenX - self.offset
                    )
                ):
                    Colliding = False
                else:
                    Colliding = True
            if self.hallwayDirection[1] == 1:
                pass
            if self.hallwayDirection[2] == 1:
                pass
            if self.hallwayDirection[3] == 1:
                pass
        else:
            pass
    
    def collision(self, playerPos, direction):

        Colliding = False
        print(self.offset)

        if direction == "w":
            if self.hallwayDirection[0] == 1:
                if playerPos[1]:
                    pass
                pass
            if self.hallwayDirection[1] == 1:
                pass
            if self.hallwayDirection[3] == 1:
                pass

            pass
        if direction == "a":
            pass
        if direction == "s":
            pass
        if direction == "d":
            pass

        
        if self.ID in (1, 2, 3, 4, 11, 12, 13, 14, 15) and playerPos[1] >= self.offset:
                Colliding = False
            elif self.hallwayDirection[0] == 1 and playerPos[1] >= 0:
                Colliding = False
            elif self.hallwayDirection[1] == 1 and playerPos[1] <= self.HeightNoHallway:
                Colliding = False
            elif self.hallwayDirection[2] == 1 and playerPos[1] >= 0:
                Colliding = False
            elif self.hallwayDirection[3] == 1 and playerPos[1] <= self.HeightNoHallway:
                Colliding = False
            else:
                Colliding = True
        

        if self.ID in (1, 2, 3, 4, 11, 12, 13, 14, 15):
            if (
                playerPos[0] >= self.offset
                and playerPos[1] >= self.offset
                and playerPos[0] + self.playerSize[0] <= self.screenX - self.offset
                and playerPos[1] + self.playerSize[1] <= self.screenY - self.offset
            ):
                Colliding = False
            else:
                Colliding = True
        if self.hallwayDirection[0] == 1:
            if (
                playerPos[0] >= self.WidthNoHallway
                and playerPos[1] >= 0
                and playerPos[0] + self.playerSize[0]
                <= self.WidthNoHallway + self.hallwaySize
                and playerPos[1] + self.playerSize[1] <= self.HeightNoHallway
            ):
                Colliding = False
                print("3")
            else:
                Colliding = True
                print("4")
        if self.hallwayDirection[1] == 1:
            if (
                playerPos[0] >= self.WidthNoHallway + self.hallwaySize
                and playerPos[1] >= self.HeightNoHallway
                and playerPos[0] + self.playerSize[0] <= self.screenX
                and playerPos[1] + self.playerSize[1]
                <= self.HeightNoHallway + self.hallwaySize
            ):
                Colliding = False
                print("5")
            else:
                Colliding = True
                print("6")
        if self.hallwayDirection[2] == 1:
            if (
                playerPos[0] >= self.WidthNoHallway
                and playerPos[1] >= self.HeightNoHallway + self.hallwaySize
                and playerPos[0] + self.playerSize[0]
                <= self.WidthNoHallway + self.hallwaySize
                and playerPos[1] + self.playerSize[1] <= self.screenY
            ):
                Colliding = False
                print("7")
            else:
                Colliding = True
                print("8")
        if self.hallwayDirection[3] == 1:
            if (
                playerPos[0] >= 0
                and playerPos[1] >= self.HeightNoHallway
                and playerPos[0] + self.playerSize[0] <= self.WidthNoHallway
                and playerPos[1] + self.playerSize[1]
                <= self.HeightNoHallway + self.hallwaySize
            ):
                Colliding = False
                print("9")
            else:
                Colliding = True
                print("0")

        return Colliding"""
