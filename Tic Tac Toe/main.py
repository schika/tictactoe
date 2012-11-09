import pygame, sys, assets
from pygame.locals import *
from decimal import ROUND_CEILING
from random import random

pygame.init()
SCREEN = pygame.display.set_mode((116, 148))
pygame.display.set_caption('Tik Tak Toe') 
ASSETS = assets.assets()
TURN = 'pc'

MAP = ['', '', '']
for i in range(0, 3):
    MAP[i] = ['', '', '']
    for j in range(0, 3):
        MAP[i][j] = ''

def init():
    'Game init'
    ASSETS.init()

def run():
    while True:
        tick()
        render()

def tick():
    'Game Update'
    if TURN == 'pc':
        xx = random(0, 2) // 1
        yy = random(0, 2) // 1
        if MAP[xx][yy] == '':
            MAP[xx][yy] = 'zero'
            TURN = 'player'
                
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == MOUSEBUTTONDOWN:
            if TURN == 'player':
                xx = max(min(event.pos[0] // 32, 2), 0)
                yy = max(min(event.pos[1] // 32, 2), 0)
                if event.button == 1:
                    MAP[xx][yy] = 'cross'
                else:
                    MAP[xx][yy] = 'zero'
                TURN = 'pc'
    'Display Update'
    pygame.display.update()

def render():
    'Game Render'
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(ASSETS.bg, (0, 0))
    for i in range(0, 3):
        for j in range(0, 3):
            SCREEN.blit(ASSETS.buttonUp, (10 + i * 32, 10 + j * 32))
            if MAP[i][j] == 'zero':
                SCREEN.blit(ASSETS.zero, (10 + i * 32 + 8, 10 + j * 32 + 8))
            elif MAP[i][j] == 'cross':
                SCREEN.blit(ASSETS.cross, (10 + i * 32 + 8, 10 + j * 32 + 8))
   
def Main():
    init()
    run()

if __name__ == "__main__": Main()