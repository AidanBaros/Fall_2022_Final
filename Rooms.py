import pygame
import random

pygame.init()


class room:
    def __init__(
        self,
        tile,
        screenSize,
        screen,
        playerSize,
    ):
        self.hallwayDirection = tile.sides
        self.ID = tile.ID
        self.screenX = screenSize[0]
        self.screenY = screenSize[1]
        self.screen = screen
        self.playerSize = playerSize
        self.collisionBoxList = []
        self.RoomYes = [1, 2, 3, 4, 11, 12, 13, 14, 15]
        self.RoomNo = [5, 6, 7, 8, 9, 10]

        self.hallwaySize = self.screenX // 8
        self.WidthNoHallway = self.screenX // 2 - self.hallwaySize // 2
        self.HeightNoHallway = self.screenY // 2 - self.hallwaySize // 2
        self.WidthHallway = self.screenX // 2 + self.hallwaySize // 2
        self.HeightHallway = self.screenY // 2 + self.hallwaySize // 2
        self.offset = 0
        self.color = (255, 255, 255)

        #SET OFFSET
        if self.ID == 1:
            self.offset = 200
        elif self.ID == 2:
            self.offset = 200
        elif self.ID == 3:
            self.offset = 200
        elif self.ID == 4:
            self.offset = 200
        elif self.ID == 11:
            self.offset = 300
        elif self.ID == 12:
            self.offset = 300
        elif self.ID == 13:
            self.offset = 300
        elif self.ID == 14:
            self.offset = 300
        elif self.ID == 15:
            self.offset = 100


        #COLLISION BOXS
        self.CornerTL = pygame.Rect(
            0,
            0,
            self.WidthNoHallway,
            self.HeightNoHallway - playerSize[1] + (playerSize[1] // 4),
        )
        self.CornerTR = pygame.Rect(
            self.WidthHallway,
            0,
            self.WidthNoHallway,
            self.HeightNoHallway - playerSize[1] + (playerSize[1] // 4),
        )
        self.CornerBR = pygame.Rect(
            self.WidthHallway,
            self.HeightHallway,
            self.WidthNoHallway,
            self.HeightNoHallway,
        )
        self.CornerBL = pygame.Rect(
            0,
            self.HeightHallway,
            self.WidthNoHallway,
            self.HeightNoHallway,
        )
        self.TopNR = pygame.Rect(
            0,
            0,
            self.screenX,
            self.HeightNoHallway - playerSize[1] + (playerSize[1] // 4),
        )
        self.BottomNR = pygame.Rect(
            0,
            self.HeightHallway,
            self.screenX,
            self.HeightNoHallway,
        )
        self.LeftNR = pygame.Rect(
            0,
            0,
            self.WidthNoHallway,
            self.screenY,
        )
        self.RightNR = pygame.Rect(
            self.WidthHallway,
            0,
            self.WidthNoHallway,
            self.screenY,
        )
        
        self.TLT = pygame.Rect(
            0,
            0,
            self.WidthNoHallway,
            self.offset,
        )
        self.TLL = pygame.Rect(
            0,
            0,
            self.offset,
            self.HeightNoHallway,
        )
        self.TRT = pygame.Rect(
            self.WidthHallway,
            0,
            self.WidthNoHallway,
            self.offset,
        )
        self.TRR = pygame.Rect(
            self.screenX - self.offset,
            0,
            self.offset,
            self.HeightNoHallway,
        )
        self.BRR = pygame.Rect(
            self.screenX - self.offset,
            self.HeightHallway,
            self.offset,
            self.HeightNoHallway,
        )
        self.BRB = pygame.Rect(
            self.WidthHallway,
            self.screenY - self.offset,
            self.WidthNoHallway,
            self.offset,
        )
        self.BLL = pygame.Rect(
            0,
            self.HeightHallway,
            self.offset,
            self.HeightNoHallway,
        )
        self.BLB = pygame.Rect(
            0,
            self.screenY - self.offset,
            self.WidthNoHallway,
            self.offset,
        )
        self.TopR = pygame.Rect(
            0,
            0,
            self.screenX,
            self.offset - playerSize[1] + (playerSize[1] // 4),
        )
        self.BottomR = pygame.Rect(
            0,
            self.screenY - self.offset,
            self.screenX,
            self.offset,
        )
        self.LeftR = pygame.Rect(
            0,
            0,
            self.offset,
            self.screenY,
        )
        self.RightR = pygame.Rect(
            self.screenX - self.offset,
            0,
            self.offset,
            self.screenY,
        )

        if self.ID == 1:
            self.collisionBoxList.append(self.TLT)
            self.collisionBoxList.append(self.TLL)
            self.collisionBoxList.append(self.TRT)
            self.collisionBoxList.append(self.TRR)
            self.collisionBoxList.append(self.BLL)
            self.collisionBoxList.append(self.BRR)
            self.collisionBoxList.append(self.BottomR)
        elif self.ID == 2:
            self.collisionBoxList.append(self.BRR)
            self.collisionBoxList.append(self.BRB)
            self.collisionBoxList.append(self.TRT)
            self.collisionBoxList.append(self.TRR)
            self.collisionBoxList.append(self.BLB)
            self.collisionBoxList.append(self.TLT)
            self.collisionBoxList.append(self.LeftR)
        elif self.ID == 3:
            self.collisionBoxList.append(self.BLL)
            self.collisionBoxList.append(self.BLB)
            self.collisionBoxList.append(self.BRR)
            self.collisionBoxList.append(self.BRB)
            self.collisionBoxList.append(self.TLL)
            self.collisionBoxList.append(self.TRR)
            self.collisionBoxList.append(self.TopR)
        elif self.ID == 4:
            self.collisionBoxList.append(self.TLT)
            self.collisionBoxList.append(self.TLL)
            self.collisionBoxList.append(self.BLL)
            self.collisionBoxList.append(self.BLB)
            self.collisionBoxList.append(self.TRT)
            self.collisionBoxList.append(self.BRB)
            self.collisionBoxList.append(self.RightR)
        elif self.ID == 5:
            self.collisionBoxList.append(self.TopNR)
            self.collisionBoxList.append(self.BottomNR)
        elif self.ID == 6:
            self.collisionBoxList.append(self.LeftNR)
            self.collisionBoxList.append(self.RightNR)
        elif self.ID == 7:
            self.collisionBoxList.append(self.CornerTR)
            self.collisionBoxList.append(self.BottomNR)
            self.collisionBoxList.append(self.LeftNR)
        elif self.ID == 8:
            self.collisionBoxList.append(self.CornerBR)
            self.collisionBoxList.append(self.TopNR)
            self.collisionBoxList.append(self.LeftNR)
        elif self.ID == 9:
            self.collisionBoxList.append(self.CornerBL)
            self.collisionBoxList.append(self.TopNR)
            self.collisionBoxList.append(self.RightNR)
        elif self.ID == 10:
            self.collisionBoxList.append(self.CornerTL)
            self.collisionBoxList.append(self.BottomNR)
            self.collisionBoxList.append(self.RightNR)
        elif self.ID == 11:
            self.collisionBoxList.append(self.TLT)
            self.collisionBoxList.append(self.TRT)
            self.collisionBoxList.append(self.RightR)
            self.collisionBoxList.append(self.LeftR)
            self.collisionBoxList.append(self.BottomR)
        elif self.ID == 12:
            self.collisionBoxList.append(self.BRR)
            self.collisionBoxList.append(self.TRR)
            self.collisionBoxList.append(self.LeftR)
            self.collisionBoxList.append(self.BottomR)
            self.collisionBoxList.append(self.TopR)
        elif self.ID == 13:
            self.collisionBoxList.append(self.BRB)
            self.collisionBoxList.append(self.BLB)
            self.collisionBoxList.append(self.RightR)
            self.collisionBoxList.append(self.LeftR)
            self.collisionBoxList.append(self.TopR)
        elif self.ID == 14:
            self.collisionBoxList.append(self.TLL)
            self.collisionBoxList.append(self.BLL)
            self.collisionBoxList.append(self.RightR)
            self.collisionBoxList.append(self.BottomR)
            self.collisionBoxList.append(self.TopR)
        elif self.ID == 15:
            self.collisionBoxList.append(self.TLT)
            self.collisionBoxList.append(self.TLL)
            self.collisionBoxList.append(self.BRR)
            self.collisionBoxList.append(self.BRB)
            self.collisionBoxList.append(self.TRR)
            self.collisionBoxList.append(self.TRT)
            self.collisionBoxList.append(self.BLL)
            self.collisionBoxList.append(self.BLB)

        # Playable area rects
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


    def draw(self):
        self.screen.fill((0, 0, 0))
        for i in range(len(self.collisionBoxList)):
            pygame.draw.rect(
                self.screen,
                (
                    50 + (25*i),
                    50 + (25*i),
                    50 + (25*i),
                ),
                self.collisionBoxList[i],
            )
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
        

    def collision(self, player: pygame.Rect, PlayerSpeed):
        for i in self.collisionBoxList:
            if player.colliderect(i):
                if (player.top < i.bottom and player.top + PlayerSpeed > i.bottom):
                    player.top = i.bottom
                elif (player.left < i.right and player.left + PlayerSpeed > i.right):
                    player.left = i.right
                elif (player.bottom > i.top and player.bottom - PlayerSpeed< i.top):
                    player.bottom = i.top
                elif (player.right > i.left and player.right - PlayerSpeed < i.left):
                    player.right = i.left
                return True
            return False
            
            



    """def collision(self, player: pygame.Rect, direction):
        if self.ID in (1, 2, 3, 4, 11, 12, 13, 14, 15):
            if direction == "w":
                print("w1")
                print(
                    player.colliderect(self.LT.bottom)
                    or player.colliderect(self.TL.bottom)
                    or player.colliderect(self.TR.bottom)
                    or player.colliderect(self.RT.bottom)
                )
                return (
                    player.colliderect(self.LT.bottom)
                    or player.colliderect(self.TL.bottom)
                    or player.colliderect(self.TR.bottom)
                    or player.colliderect(self.RT.bottom)
                )
            if direction == "a":
                print("a1")
                print(
                    player.colliderect(self.TR.right)
                    or player.colliderect(self.RT.right)
                    or player.colliderect(self.RB.right)
                    or player.colliderect(self.BR.right)
                )
                return (
                    player.colliderect(self.TR.right)
                    or player.colliderect(self.RT.right)
                    or player.colliderect(self.RB.right)
                    or player.colliderect(self.BR.right)
                )
            if direction == "s":
                print("s1")
                print(
                    player.colliderect(self.RB.top)
                    or player.colliderect(self.BR.top)
                    or player.colliderect(self.BL.top)
                    or player.colliderect(self.LB.top)
                )
                return (
                    player.colliderect(self.RB.top)
                    or player.colliderect(self.BR.top)
                    or player.colliderect(self.BL.top)
                    or player.colliderect(self.LB.top)
                )
            if direction == "d":
                print("d1")
                print(
                    player.colliderect(self.BL.left)
                    or player.colliderect(self.LB.left)
                    or player.colliderect(self.LT.left)
                    or player.colliderect(self.TL.left)
                )
                return (
                    player.colliderect(self.BL.left)
                    or player.colliderect(self.LB.left)
                    or player.colliderect(self.LT.left)
                    or player.colliderect(self.TL.left)
                )
        else:
            if self.hallwayDirection[0] == 0:
                self.NoRoomTL.width = self.WidthHallway
            if self.hallwayDirection[1] == 0:
                self.NoRoomTR.height = self.HeightHallway
            if self.hallwayDirection[2] == 0:
                self.NoRoomBR.x = self.WidthNoHallway
                self.NoRoomBR.width = self.WidthHallway
            if self.hallwayDirection[3] == 0:
                self.NoRoomBL.y = self.HeightNoHallway
                self.NoRoomBL.height = self.HeightHallway

            def testPrint():
                print(self.w2, end=", w\n")
                print(self.a2, end=", a\n")
                print(self.s2, end=", s\n")
                print(self.d2, end=", d\n")
                print()

            if player.top == self.NoRoomTL.bottom or player.top == self.NoRoomTR.bottom:
                self.w2 = True
            else:
                self.w2 = False
            if player.left == self.NoRoomTL.right or player.left == self.NoRoomBL.right:
                self.a2 = True
            else:
                self.a2 = False
            if player.bottom == self.NoRoomBR.top or player.bottom == self.NoRoomBL.top:
                self.s2 = True
            else:
                self.s2 = False
            if player.right == self.NoRoomBR.left or player.right == self.NoRoomTR.left:
                self.d2 = True
            else:
                self.d2 = False

            print("---------")
            testPrint()
            if direction == "w":
                self.w2 = False
                if player.bottomright[0] <= self.NoRoomTL.bottomright[0]:
                    if player.top >= self.NoRoomTL.bottom:
                        self.w2 = False
                    elif (
                        self.w2 == False
                        and self.a2 == False
                        and self.s2 == False
                        and self.d2 == False
                    ):
                        self.w2 = True
                        player.top = self.NoRoomTL.bottom
                if player.bottomleft[0] >= self.NoRoomTR.bottomleft[0]:
                    if player.top >= self.NoRoomTR.bottom:
                        self.w2 = False
                    elif (
                        self.w2 == False
                        and self.a2 == False
                        and self.s2 == False
                        and self.d2 == False
                    ):
                        self.w2 = True
                        player.top = self.NoRoomTR.bottom
                testPrint()
                return self.w2
            elif direction == "w2":
                return player.y
            if direction == "a":
                self.a2 = False
                if player.topright[1] <= self.NoRoomTL.bottomright[1]:
                    if player.left >= self.NoRoomTL.right:
                        self.a2 = False
                    elif (
                        self.w2 == False
                        and self.a2 == False
                        and self.s2 == False
                        and self.d2 == False
                    ):
                        self.a2 = True
                        player.left = self.NoRoomTL.right
                if player.bottomright[1] >= self.NoRoomBL.topright[1]:
                    if player.left >= self.NoRoomBL.right:
                        self.a2 = False
                    elif (
                        self.w2 == False
                        and self.a2 == False
                        and self.s2 == False
                        and self.d2 == False
                    ):
                        self.a2 = True
                        player.left = self.NoRoomBL.right
                testPrint()
                return self.a2
            elif direction == "a2":
                return player.x
            if direction == "s":
                self.s2 = False
                if player.topleft[0] >= self.NoRoomBR.topleft[0]:
                    if player.bottom <= self.NoRoomBR.top:
                        self.s2 = False
                    elif (
                        self.w2 == False
                        and self.a2 == False
                        and self.s2 == False
                        and self.d2 == False
                    ):
                        self.s2 = True
                        player.bottom = self.NoRoomBR.top
                if player.topright[0] <= self.NoRoomBL.topright[0]:
                    if player.bottom <= self.NoRoomBL.top:
                        self.s2 = False
                    elif (
                        self.w2 == False
                        and self.a2 == False
                        and self.s2 == False
                        and self.d2 == False
                    ):
                        self.s2 = True
                        player.bottom = self.NoRoomBL.top
                testPrint()
                return self.s2
            elif direction == "s2":
                return player.y
            if direction == "d":
                self.d2 = False
                if player.bottomleft[1] >= self.NoRoomBR.topleft[1]:
                    if player.right <= self.NoRoomBR.left:
                        self.d2 = False
                    elif (
                        self.w2 == False
                        and self.a2 == False
                        and self.s2 == False
                        and self.d2 == False
                    ):
                        self.d2 = True
                        player.right = self.NoRoomBR.left
                if player.topleft[1] <= self.NoRoomTR.bottomleft[1]:
                    if player.right <= self.NoRoomTR.left:
                        self.d2 = False
                    elif (
                        self.w2 == False
                        and self.a2 == False
                        and self.s2 == False
                        and self.d2 == False
                    ):
                        self.d2 = True
                        player.right = self.NoRoomTR.left
                testPrint()
                return self.d2
            elif direction == "d2":
                return player.x"""

    """

        # No Room collision rects
        self.NoRoomTL = pygame.Rect(
            0,
            0,
            self.WidthNoHallway,
            self.HeightNoHallway - playerSize[1] + (playerSize[1] // 4),
        )
        self.NoRoomTR = pygame.Rect(
            self.WidthHallway,
            0,
            self.WidthNoHallway,
            self.HeightNoHallway - playerSize[1] + (playerSize[1] // 4),
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
        # Room collision rects
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

        self.w2 = False
        self.a2 = False
        self.s2 = False
        self.d2 = False
        self.colliding = False
        self.collidingX = False
        self.collidingY = False
        self.collidingW = False
        self.collidingA = False
        self.collidingS = False
        self.collidingD = False

    if direction == "w":
                self.w2 = False
                if (player.bottomright[0] <= self.NoRoomTL.bottomright[0]):
                    if self.collidingY == False and self.collidingS == False:
                        player.top = self.NoRoomTL.bottom
                        self.w2 = True
                        self.collidingY = True
                        self.collidingW = True
                        if test: print("w2,2")
                    elif (player.top >= self.NoRoomTL.bottom):
                        self.w2 = False
                        self.collidingY = False
                        self.collidingS = False
                if (player.bottomleft[0] >= self.NoRoomTR.bottomleft[0]):
                    if self.collidingY == False and self.collidingS == False:
                        player.top = self.NoRoomTR.bottom
                        self.w2 = True
                        self.collidingY = True
                        self.collidingW = True
                        if test: print("w2,4")
                    elif (player.top >= self.NoRoomTR.bottom):
                        self.w2 = False
                        self.collidingY = False
                        self.collidingS = False
                print(self.collidingY,end=", ")
                print("w\n")
                return(self.w2)
            elif direction == "w2":
                return player.y

    w2 = (
                        (
                            player.top > self.NoRoomTL.bottom 
                            and 
                            player.topright < self.NoRoomTL.bottomright
                        ) 
                        or 
                        (
                            player.top > self.NoRoomTR.bottom 
                            and 
                            player.topleft > self.NoRoomTR.bottomleft
                        )
                    )
    a2 = (
                        (
                            player.left > self.NoRoomTL.right
                            and 
                            player.bottomleft < self.NoRoomTL.bottomright
                        ) 
                        or 
                        (
                            player.left > self.NoRoomBL.right
                            and 
                            player.topleft > self.NoRoomBL.topright
                        )
                    )
    s2 = (
                        (
                            player.bottom < self.NoRoomBR.top
                            and 
                            player.bottomleft > self.NoRoomBR.topleft
                        ) 
                        or 
                        (
                            player.bottom < self.NoRoomBL.top
                            and 
                            player.bottomright < self.NoRoomBL.topright
                        )
                    )
    d2 = (
                        (
                            player.right < self.NoRoomBR.left
                            and 
                            player.topright > self.NoRoomBR.topleft

                        ) 
                        or 
                        (
                            player.right < self.NoRoomTR.left
                            and 
                            player.bottomright < self.NoRoomTR.bottomleft
                        )
                    )

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
