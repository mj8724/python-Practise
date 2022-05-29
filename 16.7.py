import pygame
import math
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for x in range(0 ,640):
    y = int(math.sin(x/640 *4*math.pi)* 200 + 240)