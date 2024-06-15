import pygame
import sys


pygame.init()

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        print(f"Created ball with color: {color}")
        
    def update(self):
        self.rect.x += 1
        if self.rect.x > 1200:
            self.rect.x = 0
            
all_sprites = pygame.sprite.Group()
ball1 = Ball((255, 0, 0), 20, 20)
ball2 = Ball((0, 0, 255), 20, 20)
all_sprites.add(ball1)

all_sprites.add(ball2)
ball1.rect.y = 100 
ball2.rect.y = 200

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Moving Balls")
    


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    all_sprites.update()
    
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    
    pygame.display.flip()
    

        
    
        
        
    