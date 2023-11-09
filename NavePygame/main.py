import pygame
import random
from sys import exit
from variaveis import *



pygame.init()

tela = pygame.display.set_mode((largura_tela,altura_tela))
pygame.display.set_caption('Espaços Infinitios')

cloque = pygame.time.Clock()
fonte = pygame.font.Font(None ,50)


texto_surf = fonte.render('Espaços Infinitos', True, '#e6e6e6')

espaco_surf = pygame.image.load('Graficos/fundoespaco.jpg').convert()

playeralien_surf = pygame.image.load('Graficos/Player/alienpuro.png').convert_alpha()
playeralien_rect = playeralien_surf.get_rect(bottomleft = (500,200))

nave_surf = pygame.image.load('Graficos/Test/tiny_ship.png').convert_alpha()
nave_x_pos = -320
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    tela.blit(espaco_surf,(0,0))
    tela.blit(playeralien_surf,playeralien_rect)
    tela.blit(texto_surf,(500,200))
    tela.blit(nave_surf,(nave_x_pos,250))
    nave_x_pos+=10
    
    if nave_x_pos >= 1280+320:
        nave_x_pos=-320


    pygame.display.update()
    cloque.tick(60)