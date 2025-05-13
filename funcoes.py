import pygame

def desenha_quadrado_arredondado(tela,cor,x,y,largura,altura,raio):
    canto_superior_esquerdo = (x,y+raio)
    canto_superior_direito = (x+largura,y+raio)
    canto_inferior_direito = (x+largura,y+altura-raio)
    canto_inferior_esquerdo = (x,y+altura-raio)

    pontos = [(x+raio,y+raio),(x+largura-raio,y+raio),(x+largura-raio,y+altura-raio),(x+raio,y+largura-raio)]

    pygame.draw.ellipse(tela,cor,(x,y,raio*2,raio*2))
    pygame.draw.ellipse(tela,cor,(x+largura-raio*2,y,raio*2,raio*2))
    pygame.draw.ellipse(tela,cor,(x+largura-raio*2,y+altura-raio*2,raio*2,raio*2))
    pygame.draw.ellipse(tela,cor,(x,y+altura-raio*2,raio*2,raio*2))

    pygame.draw.polygon(tela,cor,pontos)

    pygame.draw.rect(tela, cor, pygame.Rect(x+raio,y,largura-raio*2,4))
    pygame.draw.rect(tela, cor, pygame.Rect(x+raio,y+altura-raio,largura-raio*2,4))
    pygame.draw.rect(tela, cor, pygame.Rect(x,y+raio,4,altura-raio*2))
    pygame.draw.rect(tela, cor, pygame.Rect(x+largura-raio,y+raio,4,altura-raio*2))