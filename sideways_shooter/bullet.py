import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, settings, screen, shooter):
        super().__init__()
        self.screen = screen 
        
        self.rect = pygame.Rect(0, 0, settings.bullet_height, settings.bullet_width)
        
        self.rect.centery = shooter.rect.centery
        self.rect.centerx = shooter.rect.centerx
        
        self.x = float(self.rect.x)
        
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor
        
    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        