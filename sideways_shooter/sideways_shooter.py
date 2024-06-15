import pygame 
import game_functions as gf
from settings import Settings
from shooter import Shooter
from pygame.sprite import Group




def run_game():
    pygame.init()
    
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    
    pygame.display.set_caption("Sideways Shooter")


    shooter = Shooter(settings, screen)
    bullets = Group()


    while True:
        gf.check_events(shooter, settings, bullets, screen)
        shooter.update()
        bullets.update()
    
        gf.update_screen(screen, settings, shooter, bullets)
    
run_game()
            