import pygame
import sys
from bullet import Bullet



def check_events(shooter, settings, bullets, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, shooter, settings, bullets, screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, shooter)
            
def check_keyup_events( event, shooter):
    if event.key == pygame.K_DOWN:
        shooter.moving_down = False
    elif event.key == pygame.K_UP:
        shooter.moving_up = False
        
        
def check_keydown_events(event, shooter, settings, bullets, screen):
    if event.key == pygame.K_DOWN:
        shooter.moving_down = True
    elif event.key == pygame.K_UP:
        shooter.moving_up = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(settings, screen, shooter)
        bullets.add(new_bullet)


def update_screen(screen, settings, shooter, bullets):
    screen.fill(settings.bg_color)
    shooter.blitme()
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
   
    
    pygame.display.flip()