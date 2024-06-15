import pygame 
import sys
import random



pygame.init()

class Star(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.reset_position()
        
    def reset_position(self):
        self.rect.x = random.randint(0, 1200- self.rect.width)
        self.rect.y = random.randint(0, 800- self.rect.height)

Stars = pygame.sprite.Group()
star_num = random.randint(100, 200)
for x in range(star_num):
    star = Star((255, 255, 255), random.randint(0, 10), random.randint(0, 10)) 
    Stars.add(star)
    star.reset_position()
    



screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Stars in Sky")




while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    Stars.update()
    
    screen.fill((0, 0, 0))
    
    Stars.draw(screen)
    
    
    
    pygame.display.flip()
    
    
    