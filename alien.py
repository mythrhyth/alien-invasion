<<<<<<< HEAD
import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    #a class to represent a single alien in the fleet
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load("C:\\Users\\rhyth\\OneDrive\\Documents\\alien-invasion\\alien.bmp")
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
        self.alien_speed_factor = 1
        
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction )
        self.rect.x = self.x 
        
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
=======
import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    #a class to represent a single alien in the fleet
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load("C:\\Users\\rhyth\\OneDrive\\Documents\\alien-invasion\\alien.bmp")
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
        self.alien_speed_factor = 1
        
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction )
        self.rect.x = self.x 
        
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
>>>>>>> origin/main
    