import pygame
import sys

def check_keyup_events(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
        

def check_keydown_events(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True




def check_events(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
            
def update_screen(ai_settings, screen, rocket):
    
    
    screen.fill(ai_settings.bg_color)
    rocket.update()
    
    rocket.blitme()
    pygame.display.flip()


        
        
     