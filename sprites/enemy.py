import pygame 
import sys 
import random


pygame.init()

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.reset_position()
        
    def reset_position(self):
        self.rect.x = random.randint(0, 1200-self.rect.x) 
        self.rect.y = random.randint(0, 800 - self.rect.y)
        
    def update(self):
        pass
    
Enemies = pygame.sprite.Group()

num_enemies = 10 
for n in range(num_enemies) :
    enemy = Enemy((255, 0, 0), 30, 30)
    Enemies.add(enemy)
    enemy.reset_position()
    


screen = pygame.display.set_mode([1200, 800])
pygame.display.set_caption("enemies randomized")
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    
    Enemies.update()
    
    screen.fill((255, 255, 255))
    
    Enemies.draw(screen)
    
    
    
    pygame.display.flip()
    
            
    