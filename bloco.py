import pygame

#cria Classe Bloco
class Bloco(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.target_x = x
        self.target_y = y
        self.speed = 30
        self.moving = False
        self.move_direction = None
    
    #define a função que atualiza a posição do bloco
    def _calcular_passo(self, atual, alvo):
        """Retorna o deslocamento ideal para um eixo."""
        if atual < alvo:
            return min(self.speed, alvo - atual)
        elif atual > alvo:
            return -min(self.speed, atual - alvo)
        return 0

    def update(self):
        if self.move_direction == 'x':
            self.rect.x += self._calcular_passo(self.rect.x, self.target_x)
        elif self.move_direction == 'y':
            self.rect.y += self._calcular_passo(self.rect.y, self.target_y)

        self.moving = not(self.rect.x == self.target_x
                        and self.rect.y == self.target_y)

    #desenha os blocos
    def draw(self, window):
        print("draw")
        window.blit(self.image,(self.rect.x,self.rect.y))


        