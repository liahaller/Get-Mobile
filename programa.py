# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from funcoes import desenha_quadrado_arredondado

pygame.init()

# ----- Gera tela principal
largura = 512
altura = 700
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('GetMóbile')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    azul = (0, 61, 102)
    verde = (0, 204, 102)
    cinza_escuro = (153, 153, 153)
    cinza_claro = (221, 221, 221)
    bege = (237, 224, 200)
    font = pygame.font.SysFont('Montserrat',72)
    titulo1 = font.render('Get',True,verde)
    titulo2 = font.render('Móbile',True,azul)
    font = pygame.font.SysFont('Clear Sans Bold',22)
    texto_pontos = font.render('PONTOS',True,bege)
    texto_recorde = font.render('RECORDE',True,bege)
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(titulo1, (40, 50))
    window.blit(titulo2, (130, 50))

    largura_quadrado_grande = 312
    x_quadrado_grande = (largura-largura_quadrado_grande)/2
    y_quadrado_grande = 200
    largura_quadrado_pequeno = 65.5
    raio = 4
    pygame.draw.rect(window, azul, pygame.Rect(0,0,largura,4))
    desenha_quadrado_arredondado(window,cinza_escuro,x_quadrado_grande,y_quadrado_grande,largura_quadrado_grande,largura_quadrado_grande,raio)
    y_quadrado_pequeno = y_quadrado_grande+10
    for i in range(4):
        x_quadrado_pequeno = x_quadrado_grande+10
        y_quadrado_pequeno = y_quadrado_grande+10+(largura_quadrado_pequeno+10)*i
        for j in range(4):
            desenha_quadrado_arredondado(window,cinza_claro,x_quadrado_pequeno+(largura_quadrado_pequeno+10)*j,y_quadrado_pequeno,largura_quadrado_pequeno,largura_quadrado_pequeno,raio/2)
    for i in range(2):
        desenha_quadrado_arredondado(window,cinza_escuro,280+85*i,120,80,45,raio/2)
    window.blit(texto_pontos,(287,125))
    window.blit(texto_recorde,(282.5+85,125))
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados