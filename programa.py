# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
pygame.init()
pygame.mixer.init()
largura = 512 #parametro de largura da tela do jogo
altura = 700  #parametro de altura da tela do jogoi
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('GetMóbile')
from funcoes import *
from copy import deepcopy
from bloco import Bloco
from math import *



# ----- Gera tela principal


#definição das cores utilizadas
azul = (0, 61, 102)
verde = (0, 204, 102)
cinza_escuro = (153, 153, 153)
cinza_claro = (221, 221, 221)
bege = (237, 224, 200)
preto = (0,0,0)
branco = (255,255,255)
azul_transparente = (0, 61, 102, 128)
vermelho_transparente = (255,0,0, 190)

#definição das fontes do título, corpo, pontos e recorde   
font = pygame.font.SysFont('Montserrat',72)
titulo1 = font.render('Get',True,verde)
titulo2 = font.render('Móbile',True,azul)
font = pygame.font.SysFont('Clear Sans Bold',22)
texto_pontos = font.render('PONTOS',True,bege)
texto_recorde = font.render('RECORDE',True,bege)
font = pygame.font.SysFont('Sans-serif',20)

#definição das cores com transparencia da vitória ou fim de jogo
ret_translucido_vermelho = pygame.Surface((largura,altura), pygame.SRCALPHA)
ret_translucido_vermelho.fill(vermelho_transparente)
ret_translucido_azul = pygame.Surface((largura,altura), pygame.SRCALPHA)
ret_translucido_azul.fill(azul_transparente)

#definição do botão de tentar novamente
ret_tentar_novamente = pygame.Rect(66,y_quadrado_grande+50+largura_quadrado_pequeno+50,380,largura_quadrado_pequeno)

#definição de medidas da grade principal e dos quadrados contidos nela
largura_quadrado_grande = 312
x_quadrado_grande = (largura-largura_quadrado_grande)/2
y_quadrado_grande = 200
largura_quadrado_pequeno = 65.5
raio = 4 #raio utilizado para fazer os cantos arredondados dos quadrados

#definir o texto de instruções
instrucoes = font.render("COMO JOGAR: Use as setas para mover as figuras.",True,preto)
instrucoes2 = font.render('Quando duas figuras da mesma faculdade se tocam,',True,preto)
instrucoes3 = font.render('elas se combinam em uma só!',True,preto)

#importação das imagens de cada escola
imagens = {2:pygame.image.load("imagens pygame\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_2ae55e46.jpg").convert(),4:pygame.image.load('imagens pygame\\Captura de tela 2025-05-13 141135.png').convert(),8:pygame.image.load("imagens pygame\\Captura de tela 2025-05-13 141437.png").convert(),16:pygame.image.load("imagens pygame\\maxresdefault-2-1024x576 (1).jpg").convert(),32:pygame.image.load("imagens pygame\\Captura de tela 2025-05-13 145644.png").convert(),64:pygame.image.load("imagens pygame\\Captura de tela 2025-05-13 150226.png").convert(),128:pygame.image.load("imagens pygame\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_578a1758.jpg").convert(),256:pygame.image.load("imagens pygame\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_e44b1291.jpg").convert(),512:pygame.image.load("imagens pygame\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_9311db58.jpg").convert(),1024:pygame.image.load("imagens pygame\\Captura de tela 2025-05-13 142138.png").convert(),2048: pygame.image.load('imagens pygame\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.55_fc0e097a.jpg').convert()}

#transformando as imagens para a escala do jogo
marista_img = pygame.transform.scale(imagens[2],(66,66))
consa_img = pygame.transform.scale(imagens[4],(66,66))
lourenco_img = pygame.transform.scale(imagens[8],(66,66))
miguel_img = pygame.transform.scale(imagens[16],(66,66))
santo_americo_img = pygame.transform.scale(imagens[32],(66,66))
porto_seguro_img = pygame.transform.scale(imagens[64],(66,66))
dante_img = pygame.transform.scale(imagens[128],(66,66))
santa_cruz_img = pygame.transform.scale(imagens[256],(66,66))
band_img = pygame.transform.scale(imagens[512],(66,66))
vertice_img = pygame.transform.scale(imagens[1024],(66,66))
mobile_img = pygame.transform.scale(imagens[2048],(66,66))

#dicionário associando os números da grade com as imagens
img = {2:marista_img,4:consa_img,8:lourenco_img,16:miguel_img,32:santo_americo_img,64:porto_seguro_img,128:dante_img,256:santa_cruz_img,512:band_img,1024:vertice_img,2048:mobile_img}

#importação do logo que aparece ao lado do título
logo_mobile_grande = pygame.image.load('imagens pygame\\logo mobile.png').convert()

#transformando o logo a escala do jogo
logo_mobile_grande = pygame.transform.scale(logo_mobile_grande,(50,50))


#definição do maior como parâmetro para definição do recorde
maior = 0


# ----- Inicia estruturas de dados
game = True

clock = pygame.time.Clock()
FPS = 60

all_blocos = pygame.sprite.Group()

#cria a grade e gera os primeiros blocos a partir da função
grade = [[0 for _ in range(4)] for _ in range(4)]
gerar_bloco(grade, all_blocos)
gerar_bloco(grade, all_blocos)

#utilizado para verificar se o bloco concluiu o movimento
ultimo_movimento = pygame.time.get_ticks()

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos (um novo bloco é gerado a cada movimento)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN and ultimo_movimento + 200 < pygame.time.get_ticks():
            ultimo_movimento = pygame.time.get_ticks()
            tabuleiro_antigo = deepcopy(grade)
            if event.key == pygame.K_LEFT:
                if mover_esquerda(grade,all_blocos):
                    gerar_bloco(grade, all_blocos)
            elif event.key == pygame.K_RIGHT:
                if mover_direita(grade,all_blocos):
                    gerar_bloco(grade, all_blocos)
            elif event.key == pygame.K_UP:
                if mover_cima(grade,all_blocos):
                    gerar_bloco(grade, all_blocos)
            elif event.key == pygame.K_DOWN:
                if mover_baixo(grade,all_blocos):
                    gerar_bloco(grade, all_blocos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if verificar_fim_de_jogo(grade) or verificar_vitoria(grade):
                #reiniciando a grade se o jogador clicar em "tentar novamente"
                if ret_tentar_novamente.collidepoint(event.pos):
                    all_blocos.empty()
                    grade = [[0 for _ in range(4)] for _ in range(4)]
                    gerar_bloco(grade, all_blocos)
                    gerar_bloco(grade, all_blocos)
                    verificar_fim_de_jogo(grade) == False
    
    #atualiza o estado dos blocos
    all_blocos.update()

   
    
    # ----- Gera saídas
    window.fill(branco)
    window.blit(titulo1, (40, 50))
    window.blit(titulo2, (130, 50))
    window.blit(logo_mobile_grande,(295,45))
    window.blit(instrucoes,(x_quadrado_grande,y_quadrado_grande+largura_quadrado_grande+50))
    window.blit(instrucoes2,(x_quadrado_grande,y_quadrado_grande+largura_quadrado_grande+50+15))
    window.blit(instrucoes3,(x_quadrado_grande,y_quadrado_grande+largura_quadrado_grande+50+30))
    
    #desenha a pequena linha azul no topo
    pygame.draw.rect(window, azul, pygame.Rect(0,0,largura,4))
    
    
    #desenha a grade e os quadrados menores dentro dela
    desenha_quadrado_arredondado(window,cinza_escuro,x_quadrado_grande,y_quadrado_grande,largura_quadrado_grande,largura_quadrado_grande,raio)
    y_quadrado_pequeno = y_quadrado_grande+10
    pontos_grade = []
    for i in range(4):
        pontos_linha = []
        x_quadrado_pequeno = x_quadrado_grande+10
        y_quadrado_pequeno = y_quadrado_grande+10+(largura_quadrado_pequeno+10)*i
        for j in range(4):
            x = x_quadrado_pequeno+(largura_quadrado_pequeno+10)*j
            y = y_quadrado_pequeno
            pontos_linha.append((x,y))
            valor = grade[i][j]
            desenha_quadrado_arredondado(window,cinza_claro,x,y,largura_quadrado_pequeno,largura_quadrado_pequeno,raio/2)
        pontos_grade.append(pontos_linha)
    
    all_blocos.draw(window)
    
    #desenha os retângulos de pontuação e recorde
    for i in range(2):
        desenha_quadrado_arredondado(window,cinza_escuro,280+85*i,120,80,45,raio/2)

    #define a fonte e escreve a pontuação de acordo com a função e o recorde a partir da maior pontuação registrada
    font = pygame.font.SysFont('Clear Sans Bold',22)
    texto_valor_pontos = font.render(f'{calcula_pontos(grade)}',True,bege)
    if int(calcula_pontos(grade)) > maior:
        maior = int(calcula_pontos(grade))
    texto_valor_recorde = font.render(f'{maior}',True,bege)
    window.blit(texto_pontos,(287,125))
    window.blit(texto_valor_pontos,(287,125+20))
    window.blit(texto_recorde,(282.5+85,125))
    window.blit(texto_valor_recorde,(282.5+85,125+20))

    #mostra a tela do fim do jogo quando o jogador perde
    if verificar_fim_de_jogo(grade):
        font = pygame.font.SysFont('Clear Sans Bold',57)
        window.blit(ret_translucido_vermelho,(0,0))
        texto_fim_de_jogo = font.render('GAME OVER',True,branco)
        font = pygame.font.SysFont('Clear Sans Bold',47)
        texto_tentar_novamente = font.render('TENTAR NOVAMENTE',True,branco)
        desenha_quadrado_arredondado(window,cinza_escuro,66,y_quadrado_grande+50+largura_quadrado_pequeno+30,380,largura_quadrado_pequeno,raio)
        pos_mouse = pygame.mouse.get_pos()
        #se passar o mouse no botão de tentar novamente, ele muda de cor
        if ret_tentar_novamente.collidepoint(pos_mouse):
            desenha_quadrado_arredondado(window,vermelho_transparente,66,y_quadrado_grande+50+largura_quadrado_pequeno+30,380,largura_quadrado_pequeno,raio)
        window.blit(texto_fim_de_jogo,(x_quadrado_grande+35,y_quadrado_grande+70))
        window.blit(texto_tentar_novamente,(x_quadrado_grande-20,y_quadrado_grande+70+largura_quadrado_pequeno+10+20))
    
    #mostra a tela de fim do jogo quando o jogador ganha(imagem da móbile está na grade)
    if verificar_vitoria(grade):
        font = pygame.font.SysFont('Clear Sans Bold',50)
        window.blit(ret_translucido_azul,(0,0))
        texto_vitoria = font.render('VOCÊ VENCEU!',True,branco)
        window.blit(texto_vitoria,(x_quadrado_grande+35,y_quadrado_grande+70))
        font = pygame.font.SysFont('Clear Sans Bold',47)
        texto_tentar_novamente = font.render('TENTAR NOVAMENTE',True,branco)
        desenha_quadrado_arredondado(window,cinza_escuro,66,y_quadrado_grande+50+largura_quadrado_pequeno+30,380,largura_quadrado_pequeno,raio)
        pos_mouse = pygame.mouse.get_pos()
        #se passar o mouse no botão de tentar novamente, ele muda de cor
        if ret_tentar_novamente.collidepoint(pos_mouse):
            desenha_quadrado_arredondado(window,azul_transparente,66,y_quadrado_grande+50+largura_quadrado_pequeno+30,380,largura_quadrado_pequeno,raio)
        window.blit(texto_tentar_novamente,(x_quadrado_grande-20,y_quadrado_grande+70+largura_quadrado_pequeno+10+20))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

