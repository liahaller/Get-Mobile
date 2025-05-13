import pygame
import random

def desenha_quadrado_arredondado(tela,cor,x,y,largura,altura,raio):
    canto_superior_esquerdo = (x,y+raio)
    canto_superior_direito = (x+largura,y+raio)
    canto_inferior_direito = (x+largura,y+altura-raio)
    canto_inferior_esquerdo = (x,y+altura-raio)

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

#Gera blocos aleatorios
def gerar_bloco():
    vazias = [(l, c) for l in range(4) for c in range(4) if grade[l][c] == 0]
    if vazias:
        linha, coluna = random.choice(vazias)
        grade[linha][coluna] = 2 if random.random() < 0.9 else 4

# Remove zeros de uma linha (comprime para a esquerda)
def comprimir(linha):
    nova = [n for n in linha if n != 0]
    nova += [0] * (4 - len(nova))
    return nova

# Junta blocos iguais na linha
def fundir(linha):
    for i in range(3):
        if linha[i] != 0 and linha[i] == linha[i+1]:
            linha[i] *= 2
            linha[i+1] = 0
    return comprimir(linha)


#movimentações
def mover_esquerda():
    global grade
    grade = [fundir(comprimir(linha)) for linha in grade]

def mover_direita():
    global grade
    grade = [list(reversed(fundir(comprimir(list(reversed(linha)))))) for linha in grade]

def mover_cima():
    global grade
    grade = list(map(list, zip(*grade)))
    mover_esquerda()
    grade = list(map(list, zip(*grade)))

def mover_baixo():
    global grade
    grade = list(map(list, zip(*grade)))
    mover_direita()
    grade = list(map(list, zip(*grade)))

#fim de jogo
def verificar_fim_de_jogo():
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
