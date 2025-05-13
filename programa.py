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

imagens = {2:pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_2ae55e46.jpg").convert(),4:pygame.image.load('C:\\Users\\liaha\\OneDrive\\Imagens\\Capturas de tela\\Captura de tela 2025-05-13 141135.png').convert(),8:pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Capturas de tela\\Captura de tela 2025-05-13 141437.png").convert(),16:pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Capturas de tela\\maxresdefault-2-1024x576 (1).jpg").convert(),32:pygame.image.load("C:\Users\\liaha\\OneDrive\\Imagens\\Capturas de tela\\Captura de tela 2025-05-13 145644.png").convert(),64:pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Capturas de tela\\Captura de tela 2025-05-13 150226.png").convert(),128:pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_578a1758.jpg").convert(),256:pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_e44b1291.jpg").convert(),512:pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_9311db58.jpg").convert(),1024:pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Capturas de tela\\Captura de tela 2025-05-13 142138.png").convert(),2048: pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.55_fc0e097a.jpg").convert()}

marista_img = pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_2ae55e46.jpg").convert()
consa_img = pygame.image.load('C:\\Users\\liaha\\OneDrive\\Imagens\\Capturas de tela\\Captura de tela 2025-05-13 141135.png').convert()
lourenco_img = pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Capturas de tela\\Captura de tela 2025-05-13 141437.png").convert()
miguel_img = pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Capturas de tela\\maxresdefault-2-1024x576 (1).jpg").convert()
santo_americo_img = pygame.image.load("C:\Users\\liaha\\OneDrive\\Imagens\\Capturas de tela\\Captura de tela 2025-05-13 145644.png").convert()
porto_seguro_img = pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Capturas de tela\\Captura de tela 2025-05-13 150226.png").convert()
dante_img = pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_578a1758.jpg").convert()
santa_cruz_img = pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_e44b1291.jpg").convert()
band_img = pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_9311db58.jpg").convert()
vertice_img = pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Capturas de tela\\Captura de tela 2025-05-13 142138.png").convert()
mobile_img = pygame.image.load("C:\\Users\\liaha\\OneDrive\\Imagens\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.55_fc0e097a.jpg").convert()

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    azul = (0, 61, 102)
    verde = (0, 204, 102)
    cinza_escuro = (153, 153, 153)
    cinza_claro = (221, 221, 221)
    bege = (237, 224, 200)
    preto = (0,0,0)
    branco = (255,255,255)
    
    font = pygame.font.SysFont('Montserrat',72)
    titulo1 = font.render('Get',True,verde)
    titulo2 = font.render('Móbile',True,azul)
    font = pygame.font.SysFont('Clear Sans Bold',22)
    texto_pontos = font.render('PONTOS',True,bege)
    texto_recorde = font.render('RECORDE',True,bege)
    font = pygame.font.SysFont('Sans-serif',20)
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

    instrucoes = font.render("COMO JOGAR: Use as setas para mover as figuras.",True,preto)
    instrucoes2 = font.render('Quando duas figuras da mesma faculdade se tocam,',True,preto)
    instrucoes3 = font.render('elas se combinam em uma só!',True,preto)
    window.blit(instrucoes,(x_quadrado_grande,y_quadrado_grande+largura_quadrado_grande+50))
    window.blit(instrucoes2,(x_quadrado_grande,y_quadrado_grande+largura_quadrado_grande+50+15))
    window.blit(instrucoes3,(x_quadrado_grande,y_quadrado_grande+largura_quadrado_grande+50+30))
    
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

