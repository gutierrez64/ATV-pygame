import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

#largura/altura da tela
largura = 640
altura = 480

#posição x/y da bolinha
x_mob = random.randint(40, 600)
y_mob = 0

#posição x/y do player
x_player = largura/2
y_player = altura/2+80

#tela/frame-time/nome
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
pygame.display.set_caption('doo')

#conteúdo
while True:
    #frames
    relogio.tick(30)
    #preenchimento
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #movimentação
    if pygame.key.get_pressed()[K_a]:
        x_player = x_player - 20
    if pygame.key.get_pressed()[K_d]:
        x_player = x_player + 20


    #bolinha
    mob = pygame.draw.circle(tela, (255,255,255), (x_mob,y_mob), 10)
    #player
    player = pygame.draw.rect(tela, (255,255,0), (x_player,y_player,40,1))

    #movimentação da bolinha
    if y_mob >= altura:
        y_mob = 0
    y_mob = y_mob + 8

    #barreira da bolinha
    if y_mob > 400:
        y_mob = 0
        x_mob = random.randint(40, 600)

    #barreira do player
    if x_player <= 0:
        x_player = largura/2

    elif x_player >= 640:
        x_player = largura/2

    #colisão
    if player.colliderect(mob):
        x_mob = random.randint(40, 600)
        y_mob = 0

    pygame.display.update()