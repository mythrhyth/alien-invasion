import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        #initialize the ship and set its starting position
        self.screen = screen
        self.ai_settings = ai_settings
       
        
        
        
        #load the ship image and get its rect
        self.image = pygame.image.load('C:\\Users\\rhyth\\Downloads\\rock.zip\\alien-invasion\\ship.bmp')
        

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #store a decimal value for the ship's center. 
        
        
        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.center = float(self.rect.centerx)
        
        #Movement Flag
        self.moving_right = False 
        self.moving_left = False
        
        
        
    def update(self):
            
            if self.moving_right and self.rect.right < self.screen_rect.right:
                
                self.center += self.ai_settings.ship_speed_factor
                
            if self.moving_left and self.rect.left > 0:
                
                self.center -= self.ai_settings.ship_speed_factor
            self.rect.centerx = self.center
        
        
    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image, self.rect)
        
        
   
        
        
        
        
        
        
        