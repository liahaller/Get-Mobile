# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((512, 700))
pygame.display.set_caption('GetMóbile')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    azul = (0, 61, 102)
    verde = (0, 204, 102)
    font = pygame.font.SysFont('Montserrat',72)
    texto1 = font.render('Get',True,verde)
    texto2 = font.render('Móbile',True,azul)
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(texto1, (40, 60))
    window.blit(texto2, (100, 60))

    
    azul = (0, 61, 102)
    verde = (0, 204, 102)
    vertices = [(0,0),(512,0),(0,4),(512,4)]
    pygame.draw.polygon(window,azul,vertices)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados