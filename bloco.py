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
    def update(self):
        if self.move_direction == 'x':
            if self.rect.x < self.target_x:
                self.rect.x += min(self.speed,self.target_x - self.rect.x)
            else:
                self.rect.x -= min(self.speed, self.rect.x - self.target_x)
        elif self.move_direction == 'y':
            if self.rect.y < self.target_y:
                self.rect.y += min(self.speed, self.target_y - self.rect.y)
            elif self.rect.y > self.target_y:
                self.rect.y -= min(self.speed, self.rect.y - self.target_y)
        
        self.moving = not(self.rect.x == self.target_x and self.rect.y == self.target_y)

    #desenha os blocos
    def draw(self, window):
        print("draw")
        window.blit(self.image,(self.rect.x,self.rect.y))


        