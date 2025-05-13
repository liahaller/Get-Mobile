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
    font = pygame.font.SysFont('Montserrat',72)
    texto1 = font.render('Get',True,verde)
    texto2 = font.render('Móbile',True,azul)
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(texto1, (40, 50))
    window.blit(texto2, (130, 50))

    largura_quadrado_grande = 312
    largura_quadrado_pequeno = 57.5
    raio = 4
    pygame.draw.rect(window, azul, pygame.Rect(0,0,largura,4))
    desenha_quadrado_arredondado(window,cinza_escuro,(largura-largura_quadrado_grande)/2,200,largura_quadrado_grande,largura_quadrado_grande,raio)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados