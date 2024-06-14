 
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group 
from alien import Alien





def run_game():
    
    #initialize pygame, settings and screen objects
    pygame.init()
    ai_settings = Settings()
    
    #make a ship
  
    
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    
    while True:
        
        gf.check_events(ai_settings, screen, ship, bullets )
        ship.update()
        gf.create_fleet(ai_settings, screen, ship, aliens)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets) #to update the display by swapping the contents of the backbuffer with the front buffer 
        gf.create_fleet(ai_settings, screen, ship, aliens)
        
        bullets.update()
        
        #Get rid of the bullets that have disappeared. 
        for bullet in bullets.copy():
            if bullet.rect.bottom <=0 :
                
                bullets.remove(bullet)
        
            
        
        
run_game()
