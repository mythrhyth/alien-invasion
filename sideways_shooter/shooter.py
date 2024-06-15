import pygame

class Shooter():
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        
        load_image = pygame.image.load("C:\\Users\\rhyth\\Downloads\\rock.zip\\alien-invasion\\sideways_shooter\\ship.bmp")
        self.image = pygame.transform.rotate(load_image, -90)
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.midleft = self.screen_rect.midleft 
        
        self.center = float(self.rect.centery)
        
        self.moving_down = False
        self.moving_up = False
    
    def update(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.settings.shooter_speed_factor
        elif self.moving_up and self.rect.top > 0:
            self.center -= self.settings.shooter_speed_factor
        self.rect.centery = self.center
            
               
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
        
        
    