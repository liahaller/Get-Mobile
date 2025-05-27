import pygame
from os import path
from programa import branco_transparente,FPS,window,largura,altura,branco,cinza_escuro,ret_tentar_novamente,raio,titulo1,titulo2,logo_mobile_grande
from funcoes import *

INIT = 0
GAME = 1
QUIT = 2

def tela_inicial(window):
    clock = pygame.time.Clock()

    ret_translucido_branco = pygame.Surface((largura,altura), pygame.SRCALPHA)
    ret_translucido_branco.fill(branco_transparente)

    font = pygame.font.SysFont('Clear Sans Bold',47)
    texto_iniciar_jogo = font.render('INICIAR JOGO',True,branco)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ret_tentar_novamente.collidepoint(event.pos):
                    state = GAME
                    running = False
        window.blit(ret_translucido_branco, (0, 0))
        window.blit(titulo1, (40, 50))
        window.blit(titulo2, (130, 50))
        window.blit(logo_mobile_grande,(295,45))
        desenha_quadrado_arredondado(window,cinza_escuro,66,y_quadrado_grande+50+largura_quadrado_pequeno+30,380,largura_quadrado_pequeno,raio)
        pos_mouse = pygame.mouse.get_pos()
        if ret_tentar_novamente.collidepoint(pos_mouse):
            desenha_quadrado_arredondado(window,branco_transparente,66,y_quadrado_grande+50+largura_quadrado_pequeno+30,380,largura_quadrado_pequeno,raio)
        window.blit(texto_iniciar_jogo,(x_quadrado_grande-20,y_quadrado_grande+70+largura_quadrado_pequeno+10+20))
        pygame.display.flip()
    return state
