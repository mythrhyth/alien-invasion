 
import pygame
import game_functions as gf
from settings import Settings
from game_stats import GameStats
from ship import Ship
from pygame.sprite import Group 
from alien import Alien
from button import Button 
from scoreboard import Scoreboard 





def run_game():
    
    #initialize pygame, settings and screen objects
    pygame.init()
    ai_settings = Settings()
    
    stats = GameStats(ai_settings)
    
    
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #make the button play 
    play_button = Button(ai_settings, screen, "Play")
    
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    sb = Scoreboard(ai_settings, screen, stats)
    
    
    while True:
        
        gf.check_events(ai_settings, screen, stats,sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen,stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
              
        
       
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button) #to update the display by swapping the contents of the backbuffer with the front buffer 
        
        #Get rid of the bullets that have disappeared. 
        for bullet in bullets.copy():
            if bullet.rect.bottom <=0 :
                
                bullets.remove(bullet)
        
            
        
        
run_game()