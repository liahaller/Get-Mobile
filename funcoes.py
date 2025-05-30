import pygame
pygame.init()
pygame.mixer.init()
largura = 512
altura = 700
window = pygame.display.set_mode((largura, altura))
import random
from bloco import Bloco
from copy import deepcopy

all_blocos = pygame.sprite.Group()

largura_quadrado_grande = 312
x_quadrado_grande = (largura-largura_quadrado_grande)/2
y_quadrado_grande = 200
largura_quadrado_pequeno = 65.5
x_quadrado_pequeno = x_quadrado_grande+10
y_quadrado_pequeno = y_quadrado_grande+10+(largura_quadrado_pequeno+10)

#Carrega os sons do jogo
som_fundir = pygame.mixer.Sound("Sons pygame\\Som fundir.wav")
som_mexer = pygame.mixer.Sound("Sons pygame\\Som mexer.wav")
pontos_grade = []
for i in range(4):
    pontos_linha = []
    x_quadrado_pequeno = x_quadrado_grande+10
    y_quadrado_pequeno = y_quadrado_grande+10+(largura_quadrado_pequeno+10)*i
    for j in range(4):
        x = x_quadrado_pequeno+(largura_quadrado_pequeno+10)*j
        y = y_quadrado_pequeno
        pontos_linha.append((x,y))
    pontos_grade.append(pontos_linha)

imagens = {2:pygame.image.load("imagens pygame\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_2ae55e46.jpg").convert(),4:pygame.image.load('imagens pygame\\Captura de tela 2025-05-13 141135.png').convert(),8:pygame.image.load("imagens pygame\\Captura de tela 2025-05-13 141437.png").convert(),16:pygame.image.load("imagens pygame\\maxresdefault-2-1024x576 (1).jpg").convert(),32:pygame.image.load("imagens pygame\\Captura de tela 2025-05-13 145644.png").convert(),64:pygame.image.load("imagens pygame\\Captura de tela 2025-05-13 150226.png").convert(),128:pygame.image.load("imagens pygame\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_578a1758.jpg").convert(),256:pygame.image.load("imagens pygame\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_e44b1291.jpg").convert(),512:pygame.image.load("imagens pygame\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.54_9311db58.jpg").convert(),1024:pygame.image.load("imagens pygame\\Captura de tela 2025-05-13 142138.png").convert(),2048: pygame.image.load('imagens pygame\\Imagem do WhatsApp de 2025-05-13 à(s) 14.07.55_fc0e097a.jpg').convert()}

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

img = {2:marista_img,4:consa_img,8:lourenco_img,16:miguel_img,32:santo_americo_img,64:porto_seguro_img,128:dante_img,256:santa_cruz_img,512:band_img,1024:vertice_img,2048:mobile_img}

def desenha_quadrado_arredondado(tela,cor,x,y,largura,altura,raio):
    '''
    Desenha os quadrados dentro da grade com a borda arredondada.

    Parameters:
        tela em branco, cor de preenchimento, posição nos eixos x e y, largura do quadrado, altura do quadrado, raio da borda arredondada.

    Returns:
        quadrados cinzas arredondados na grade.   
    '''
    pontos = [(x+raio,y+raio),(x+largura-raio,y+raio),(x+largura-raio,y+altura-raio),(x+raio,y+altura-raio)]

    pygame.draw.ellipse(tela,cor,(x,y,raio*2,raio*2))
    pygame.draw.ellipse(tela,cor,(x+largura-raio*2,y,raio*2,raio*2))
    pygame.draw.ellipse(tela,cor,(x+largura-raio*2,y+altura-raio*2,raio*2,raio*2))
    pygame.draw.ellipse(tela,cor,(x,y+altura-raio*2,raio*2,raio*2))

    pygame.draw.polygon(tela,cor,pontos)

    pygame.draw.rect(tela, cor, pygame.Rect(x+raio,y,largura-raio*2,raio))
    pygame.draw.rect(tela, cor, pygame.Rect(x+raio,y+altura-raio,largura-raio*2,raio))
    pygame.draw.rect(tela, cor, pygame.Rect(x,y+raio,raio,altura-raio*2))
    pygame.draw.rect(tela, cor, pygame.Rect(x+largura-raio,y+raio,raio,altura-raio*2))

#Gera blocos 
def gerar_bloco(grade, all_blocos):
    '''
    Função feita com auxilio de IA.

    Gera blocos (marista ou consa).

    Parameters:
        Grade, blocos.

    Returns:
        Novo bloco na grade.   
    '''
    vazias = [(l, c) for l in range(4) for c in range(4) if grade[l][c] == 0]
    if vazias:
        linha, coluna = random.choice(vazias)
        grade[linha][coluna] = 2 if random.random() < 0.9 else 4
        x, y = pontos_grade[linha][coluna]
        bloco = Bloco(img[grade[linha][coluna]],x, y)
        all_blocos.add(bloco)
    

# Remove zeros de uma linha (comprime)
def comprimir(linha):
    '''
    Função feita com auxilio de IA.

    Remove zeros de uma linha(comprime).

    Parameters:
        Linha.

    Returns:
        Linha comprimida.   
    '''
    nova = [n for n in linha if n != 0]
    nova += [0] * (4 - len(nova))
    return nova

# Junta blocos iguais na linha
def fundir(linha):
    '''
    Junta blocos iguais na linha.

    Parameters:
        Linha.

    Returns:
        Novo valor após fundir e cmprimir os blocos iguais.   
    '''
    for i in range(3):
        if linha[i] != 0 and linha[i] == linha[i+1]:
            novo_valor = linha[i] * 2
            linha[i] = novo_valor
            linha[i+1] = 0
    return comprimir(linha)

#Busca o bloco que irá se mover de acordo com sua posição
def buscar_bloco(all_blocos, linha, coluna):
    '''
    Busca o bloco que irá se mover de acordo com sua posição.

    Parameters:
        Blocos, linha, coluna.

    Returns:
        Bloco que irá se mover.   
    '''
    for bloco in all_blocos:
        if abs(bloco.rect.x - pontos_grade[linha][coluna][0]) < 3 and abs(bloco.rect.y - pontos_grade[linha][coluna][1]) < 3:
            return bloco

#atualiza posição da imagem do bloco de acordo com os diferentes casos de movimentação para a esquerda
def atualizar_posicoes_blocos_esquerda(grade, grade_atualizada, all_blocos):
    '''
    Atualiza posição da imagem do bloco de acordo com os diferentes casos de movimentação para a esquerda.

    Parameters:
        Grade, grade depois do movimento, blocos.

    Returns:
        Imagens e posições novas dos blocos.   
    '''
    grade = deepcopy(grade)
    
    for linha in range(4):
        for coluna in range(0,3):
            if coluna == 0:
                if grade[linha][0] == 0:
                    for i in range(1,4):
                        if grade[linha][i] != 0:
                            bloco = buscar_bloco(all_blocos,linha,i)
                            bloco.target_x = pontos_grade[linha][coluna][0]
                            grade[linha][0] = grade[linha][i]
                            grade[linha][i] = 0
                            som_mexer.play()
                            break
                else:
                    for i in range(1,4):
                        if grade[linha][i] != 0:
                            if grade[linha][0] == grade[linha][i]:
                                bloco = buscar_bloco(all_blocos,linha,i)
                                bloco.target_x = pontos_grade[linha][0][0]
                                som_fundir.play()
                                grade[linha][0] = grade[linha][0] * 2
                                grade[linha][i] = 0
                                break
                            else:
                                break
            if coluna == 1:
                if grade[linha][1] == 0:
                    for i in range(2,4):
                        if grade[linha][i] != 0:
                            bloco = buscar_bloco(all_blocos,linha,i)
                            bloco.target_x = pontos_grade[linha][coluna][0]
                            grade[linha][1] = grade[linha][i]
                            grade[linha][i] = 0
                            som_mexer.play()
                            break
                else:
                    for i in range(2,4):
                        if grade[linha][i] != 0:
                            if grade[linha][1] == grade[linha][i]:
                                bloco = buscar_bloco(all_blocos,linha,i)
                                bloco.target_x = pontos_grade[linha][1][0]
                                som_fundir.play()
                                grade[linha][1] = grade[linha][1] * 2
                                grade[linha][i] = 0
                                break
                            else:
                                break
            if coluna == 2:
                if grade[linha][2] == 0:
                    for i in range(3,4):
                        if grade[linha][i] != 0:
                            bloco = buscar_bloco(all_blocos,linha,i)
                            bloco.target_x = pontos_grade[linha][coluna][0]
                            grade[linha][2] = grade[linha][i]
                            grade[linha][i] = 0
                            som_mexer.play()
                            break
                else:
                    for i in range(3,4):
                        if grade[linha][i] != 0:
                            if grade[linha][2] == grade[linha][i]:
                                bloco = buscar_bloco(all_blocos,linha,i)
                                bloco.target_x = pontos_grade[linha][2][0]
                                som_fundir.play()           
                                grade[linha][2] = grade[linha][2] * 2
                                grade[linha][i] = 0
                                break
                            else:
                                break
                            
    for linha in range(4):
        for coluna in range(4):
            for bloco in all_blocos:
                if abs(bloco.target_x - pontos_grade[linha][coluna][0]) < 5 and abs(bloco.target_y - pontos_grade[linha][coluna][1]) < 5:
                    if grade_atualizada[linha][coluna] != 0:
                        bloco.image = img[grade_atualizada[linha][coluna]]
                    if grade_atualizada[linha][coluna] == 0:
                        bloco.kill()
                    
#atualiza posição da imagem do bloco de acordo com os diferentes casos de movimentação para a direita
def atualizar_posicoes_blocos_direita(grade, grade_atualizada, all_blocos):  
    '''
    Atualiza posição da imagem do bloco de acordo com os diferentes casos de movimentação para a direita.

    Parameters:
        Grade, grade depois do movimento, blocos.

    Returns:
        Imagens e posições novas dos blocos.   
    '''
    grade = deepcopy(grade)
    
    for linha in range(4):
        for coluna in range(3,0,-1):
            if coluna == 3:
                if grade[linha][3] == 0:
                    for i in range(2,-1,-1):
                        if grade[linha][i] != 0:
                            bloco = buscar_bloco(all_blocos,linha,i)
                            bloco.target_x = pontos_grade[linha][coluna][0]
                            grade[linha][3] = grade[linha][i]
                            grade[linha][i] = 0
                            som_mexer.play()
                            break
                else:
                    for i in range(2,-1,-1):
                        if grade[linha][i] != 0:
                            if grade[linha][coluna] == grade[linha][i]:
                                bloco = buscar_bloco(all_blocos,linha,i)
                                bloco.target_x = pontos_grade[linha][coluna][0]
                                som_fundir.play()
                                grade[linha][coluna] = grade[linha][coluna] * 2
                                grade[linha][i] = 0
                                break
                            else:
                                break
            if coluna == 2:
                if grade[linha][coluna] == 0:
                    for i in range(1,-1,-1):
                        if grade[linha][i] != 0:
                            bloco = buscar_bloco(all_blocos,linha,i)
                            bloco.target_x = pontos_grade[linha][coluna][0]
                            grade[linha][coluna] = grade[linha][i]
                            grade[linha][i] = 0
                            som_mexer.play()
                            break
                else:
                    for i in range(1,-1,-1):
                        if grade[linha][i] != 0:
                            if grade[linha][coluna] == grade[linha][i]:
                                bloco = buscar_bloco(all_blocos,linha,i)
                                bloco.target_x = pontos_grade[linha][coluna][0]
                                som_fundir.play()   
                                grade[linha][coluna] = grade[linha][coluna] * 2
                                grade[linha][i] = 0
                                break
                            else:
                                break
            if coluna == 1:
                if grade[linha][coluna] == 0:
                    for i in range(0,-1,-1):
                        if grade[linha][i] != 0:
                            bloco = buscar_bloco(all_blocos,linha,i)
                            bloco.target_x = pontos_grade[linha][coluna][0]
                            grade[linha][coluna] = grade[linha][i]
                            grade[linha][i] = 0
                            som_mexer.play()
                            break
                else:
                    for i in range(0,-1,-1):
                        if grade[linha][i] != 0:
                            if grade[linha][coluna] == grade[linha][i]:
                                bloco = buscar_bloco(all_blocos,linha,i)
                                bloco.target_x = pontos_grade[linha][coluna][0]
                                som_fundir.play()
                                grade[linha][coluna] = grade[linha][coluna] * 2
                                grade[linha][i] = 0
                                break
                            else:
                                break
    
    
                            
    for linha in range(4):
        for coluna in range(4):
            for bloco in all_blocos:
                if abs(bloco.target_x - pontos_grade[linha][coluna][0]) < 5 and abs(bloco.target_y - pontos_grade[linha][coluna][1]) < 5:
                    if grade_atualizada[linha][coluna] != 0:
                        bloco.image = img[grade_atualizada[linha][coluna]]
                    if grade_atualizada[linha][coluna] == 0:
                        bloco.kill()

#atualiza posição da imagem do bloco de acordo com os diferentes casos de movimentação para baixo
def atualizar_posicoes_blocos_baixo(grade, grade_atualizada, all_blocos):
    '''
    Atualiza posição da imagem do bloco de acordo com os diferentes casos de movimentação para baixo.

    Parameters:
        Grade, grade depois do movimento, blocos.

    Returns:
        Imagens e posições novas dos blocos.   
    '''
    grade = deepcopy(grade)
    
    for coluna in range(4):
        for linha in range(3,0,-1):
            if linha == 3:
                if grade[linha][coluna] == 0:
                    for i in range(2,-1,-1):
                        if grade[i][coluna] != 0:
                            bloco = buscar_bloco(all_blocos,i,coluna)
                            bloco.target_y = pontos_grade[linha][coluna][1]
                            grade[linha][coluna] = grade[i][coluna]
                            grade[i][coluna] = 0
                            som_mexer.play()
                            break
                else:
                    for i in range(2,-1,-1):
                        if grade[i][coluna] != 0:
                            if grade[linha][coluna] == grade[i][coluna]:
                                bloco = buscar_bloco(all_blocos,i,coluna)
                                bloco.target_y = pontos_grade[linha][coluna][1]
                                som_fundir.play()
                                grade[linha][coluna] = grade[linha][coluna] * 2
                                grade[i][coluna] = 0
                                break
                            else:
                                break
            if linha == 2:
                if grade[linha][coluna] == 0:
                    for i in range(1,-1,-1):
                        if grade[i][coluna] != 0:
                            bloco = buscar_bloco(all_blocos,i,coluna)
                            bloco.target_y = pontos_grade[linha][coluna][1]
                            grade[linha][coluna] = grade[i][coluna]
                            grade[i][coluna] = 0
                            som_mexer.play()
                            break
                else:
                    for i in range(1,-1,-1):
                        if grade[i][coluna] != 0:
                            if grade[linha][coluna] == grade[i][coluna]:
                                bloco = buscar_bloco(all_blocos,i,coluna)
                                bloco.target_y = pontos_grade[linha][coluna][1]
                                som_fundir.play()
                                grade[linha][coluna] = grade[linha][coluna] * 2
                                grade[i][coluna] = 0
                                break
                            else:
                                break
            if linha == 1:
                if grade[linha][coluna] == 0:
                    for i in range(0,-1,-1):
                        if grade[i][coluna] != 0:
                            bloco = buscar_bloco(all_blocos,i,coluna)
                            bloco.target_y = pontos_grade[linha][coluna][1]
                            grade[linha][coluna] = grade[i][coluna]
                            grade[i][coluna] = 0
                            som_mexer.play()
                            break
                else:
                    for i in range(0,-1,-1):
                        if grade[i][coluna] != 0:
                            if grade[linha][coluna] == grade[i][coluna]:
                                bloco = buscar_bloco(all_blocos,i,coluna)
                                bloco.target_y = pontos_grade[linha][coluna][1]
                                som_fundir.play()
                                grade[linha][coluna] = grade[linha][coluna] * 2
                                grade[i][coluna] = 0
                                break
                            else:
                                break
                            
    for coluna in range(4):
        for linha in range(4):
            for bloco in all_blocos:
                if abs(bloco.target_x - pontos_grade[linha][coluna][0]) < 5 and abs(bloco.target_y - pontos_grade[linha][coluna][1]) < 5:
                    if grade_atualizada[linha][coluna] != 0:
                        bloco.image = img[grade_atualizada[linha][coluna]]
                    if grade_atualizada[linha][coluna] == 0:
                        bloco.kill()

#atualiza posição da imagem do bloco de acordo com os diferentes casos de movimentação para cima
def atualizar_posicoes_blocos_cima(grade, grade_atualizada, all_blocos):
    '''
    Atualiza posição da imagem do bloco de acordo com os diferentes casos de movimentação para cima.

    Parameters:
        Grade, grade depois do movimento, blocos.

    Returns:
        Imagens e posições novas dos blocos.  
    '''
    grade = deepcopy(grade)
    
    for coluna in range(4):
        for linha in range(0,3):
            if linha == 0:
                if grade[linha][coluna] == 0:
                    for i in range(1,4):
                        if grade[i][coluna] != 0:
                            bloco = buscar_bloco(all_blocos,i,coluna)
                            bloco.target_y = pontos_grade[linha][coluna][1]
                            grade[linha][coluna] = grade[i][coluna]
                            grade[i][coluna] = 0
                            som_mexer.play()
                            break
                else:
                    for i in range(1,4):
                        if grade[i][coluna] != 0:
                            if grade[linha][coluna] == grade[i][coluna]:
                                bloco = buscar_bloco(all_blocos,i,coluna)
                                bloco.target_y = pontos_grade[linha][coluna][1]
                                grade[linha][coluna] = grade[linha][coluna] * 2
                                grade[i][coluna] = 0
                                som_fundir.play()
                                break
                            else:
                                break
            if linha == 1:
                if grade[linha][coluna] == 0:
                    for i in range(2,4):
                        if grade[i][coluna] != 0:
                            bloco = buscar_bloco(all_blocos,i,coluna)
                            bloco.target_y = pontos_grade[linha][coluna][1]
                            grade[linha][coluna] = grade[i][coluna]
                            grade[i][coluna] = 0
                            som_mexer.play()
                            break
                else:
                    for i in range(2,4):
                        if grade[i][coluna] != 0:
                            if grade[linha][coluna] == grade[i][coluna]:
                                bloco = buscar_bloco(all_blocos,i,coluna)
                                bloco.target_y = pontos_grade[linha][coluna][1]
                                grade[linha][coluna] = grade[linha][coluna] * 2
                                grade[i][coluna] = 0
                                som_fundir.play()
                                break
                            else:
                                break
            if linha == 2:
                if grade[linha][coluna] == 0:
                    for i in range(3,4):
                        if grade[i][coluna] != 0:
                            bloco = buscar_bloco(all_blocos,i,coluna)
                            bloco.target_y = pontos_grade[linha][coluna][1]
                            grade[linha][coluna] = grade[i][coluna]
                            grade[i][coluna] = 0
                            som_mexer.play()
                            break
                else:
                    for i in range(3,4):
                        if grade[i][coluna] != 0:
                            if grade[linha][coluna] == grade[i][coluna]:
                                bloco = buscar_bloco(all_blocos,i,coluna)
                                bloco.target_y = pontos_grade[linha][coluna][1]
                                grade[linha][coluna] = grade[linha][coluna] * 2
                                grade[i][coluna] = 0
                                som_fundir.play()
                                break
                            else:
                                break
                            
    for linha in range(4):
        for coluna in range(4):
            for bloco in all_blocos:
                if abs(bloco.target_x - pontos_grade[linha][coluna][0]) < 5 and abs(bloco.target_y - pontos_grade[linha][coluna][1]) < 5:
                    if grade_atualizada[linha][coluna] != 0:
                        bloco.image = img[grade_atualizada[linha][coluna]]
                    if grade_atualizada[linha][coluna] == 0:
                        bloco.kill()
        
#movimentações para a esquerda
def mover_esquerda(grade,all_blocos):
    '''
    Função feita com auxilio de IA.

    Movimenta o bloco para a esquerda.

    Parameters:
        Grade, blocos.

    Returns:
        Movimento dos blocos para a esquerda.  
    '''
    for bloco in all_blocos:
        bloco.move_direction = 'x'
    tabuleiro_antigo = deepcopy(grade)
    for i in range(4):
        grade[i] = (fundir(comprimir(grade[i])))
    atualizar_posicoes_blocos_esquerda(tabuleiro_antigo, grade, all_blocos)
    return tabuleiro_antigo != grade
    
#movimentações para a direita
def mover_direita(grade,all_blocos):
    '''
    Função feita com auxilio de IA.

    Movimenta o bloco para a direita.

    Parameters:
        Grade, blocos.

    Returns:
        Movimento dos blocos para a direita.  
    '''
    for bloco in all_blocos:
        bloco.move_direction = 'x'
    tabuleiro_antigo = deepcopy(grade)
    for i in range(4):
        grade[i] = list(reversed(fundir(comprimir(list(reversed(grade[i]))))))
    atualizar_posicoes_blocos_direita(tabuleiro_antigo,grade,all_blocos)
    return tabuleiro_antigo != grade

#movimentações para cima
def mover_cima(grade,all_blocos):
    '''
    Função feita com auxilio de IA.

    Movimenta o bloco para cima.

    Parameters:
        Grade, blocos.

    Returns:
        Movimento dos blocos para cima.  
    '''
    for bloco in all_blocos:
        bloco.move_direction = 'y'
    tabuleiro_antigo = deepcopy(grade)
    transposta = list(map(list, zip(*grade)))
    for i in range(4):
        transposta[i] = fundir(comprimir(transposta[i]))
    nova_grade = list(map(list, zip(*transposta)))
    for i in range(len(nova_grade)):
        grade[i] = nova_grade[i]
    atualizar_posicoes_blocos_cima(tabuleiro_antigo,grade,all_blocos)
    return tabuleiro_antigo != grade

#movimentações para baixo
def mover_baixo(grade,all_blocos):
    '''
    Função feita com auxilio de IA.

    Movimenta o bloco para baixo.

    Parameters:
        Grade, blocos.

    Returns:
        Movimento dos blocos para baixo.  
    '''
    for bloco in all_blocos:
        bloco.move_direction = 'y'
    tabuleiro_antigo = deepcopy(grade)
    transposta = list(map(list, zip(*grade)))
    for i in range(4):
        transposta[i] = list(reversed(fundir(comprimir(list(reversed(transposta[i]))))))
    nova_grade = list(map(list, zip(*transposta)))
    for i in range(len(nova_grade)):
        grade[i] = nova_grade[i]
    atualizar_posicoes_blocos_baixo(tabuleiro_antigo,grade,all_blocos)
    return tabuleiro_antigo != grade

#soma dos elementos na grade para calcular pontos
def calcula_pontos(grade):
    '''
    Soma dos elementos na grade para calcular pontos.

    Parameters:
        Grade.

    Returns:
        Pontos.  
    '''
    pontos = 1
    for linha in grade:
        for valor in linha:
            if valor != 0:
                pontos += valor
    pontos = str(pontos)
    return pontos   
    
#fim de jogo
def verificar_fim_de_jogo(grade):
    '''
    Verifica se o jogo chegou ao fim(jogador perdeu).

    Parameters:
        Grade.

    Returns:
        Verificação se o jogo chegou ao fim.  
    '''
    for linha in grade:
        if 0 in linha:
            return False
        for i in range(3):
            if linha[i] == linha[i+1]:
                return False
    for c in range(4):
        for l in range(3):
            if grade[l][c] == grade[l+1][c]:
                return False
    return True

#verificação se o bloco da móbile está na grade para definir a vitória
def verificar_vitoria(grade):
    '''
    Verificação se o bloco da móbile está na grade para definir a vitória.

    Parameters:
        Grade.

    Returns:
        Verificação se o jogador ganhou.  
    '''
    for linha in grade:
        if 2048 in linha:
            return True
    return False

