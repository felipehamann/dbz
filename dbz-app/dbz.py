import pygame, sys
from pygame.locals import *
import random

#variables inicio
win = pygame.display.set_mode((600,500), FULLSCREEN)
pygame.init()
pygame.display.set_caption("Mercenary Z")
clock = pygame.time.Clock()

#dimensiones personajes
x = 0
y = 0
width = 40
height = 60
vel = 5


#imagenes mapa
introimagen = pygame.image.load("namek1.png")
introimagen =pygame.transform.scale(introimagen,(600,500))
win.blit(introimagen,(0,0))

#imagenes personajes
frezaasoldier = pygame.image.load("Freeza soldier.bmp")
frezaasoldier = pygame.transform.scale(frezaasoldier,(40,60))

# loop principal juego.
while True:
    keys = pygame.key.get_pressed()
    pygame.time.delay(100)

    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if keys[pygame.K_SPACE]:
        xaux = random.randint(0,14)
        x = xaux * 40
        yaux = random.randint(0,7)
        y = yaux * 60
        win.blit(introimagen,(0,0))
        win.blit(frezaasoldier,(x,y))


    pygame.display.update()
