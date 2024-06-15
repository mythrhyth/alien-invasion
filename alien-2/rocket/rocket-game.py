import sys 
import pygame 
from settings import Settings
from rocket import Rocket
import gamefunctions as gf

def run_game():
    
    pygame.init()
    
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    rocket = Rocket(screen, ai_settings)
    
    pygame.display.set_caption("Rocket Game")
    
    
    
    
    while True:
        gf.check_events(rocket)
        gf.update_screen(ai_settings, screen, rocket)
        
        
run_game()
   
   