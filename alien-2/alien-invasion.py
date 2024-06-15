
import pygame
from settings import Settings 
from ship import Ship
import game_functions as gf 
import sys 

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    # mario=Mario(screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)
        ship.blitme()
        
        # gf.update_screen(ai_settings, screen, mario)

        # Watch for keyboard and mouse events.
        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()