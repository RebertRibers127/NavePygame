import pygame



def centro_certinho(centro, medidas):
    x=centro[0]-medidas[0]/2
    y=centro[1]-medidas[1]/2
    return (x,y)

largura_tela = 1280
altura_tela = 720

centro=(largura_tela/2,altura_tela/2)

surface_=0