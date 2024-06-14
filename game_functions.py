import sys 
import pygame
from bullet import Bullet 
from alien import Alien
def fire_bullet(ai_settings, screen, ship,  bullets):
    #create a new bullet and add it to the bullets group. 
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet) 
    

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True   
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False



def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


            
        

        

def update_screen(ai_settings, screen, ship, aliens, bullets):
     #update images on the screen and flip to the new screen 
     #Redraw the screen during each pass through the loop
     screen.fill(ai_settings.bg_color)
     
     
     ship.blitme()
     aliens.draw(screen)
     for bullet in bullets.sprites():
         bullet.draw_bullet()
     
     
     
     #Make the most recently drawn screen visible 
     pygame.display.flip()

def update_bullets(bullets):
    """
    Update position of bullets and get rid of old bullets.
    """
    # Update bullet positions.
    bullets.update()
    
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

     
     
def get_number_aliens_x(ai_settings, alien_width):
        
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x /(2 * alien_width))
    return number_aliens_x
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    
        
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x 
    alien.rect.y = alien.rect.height + 2* alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    #create an alien and find the number of aliens in a row
    #spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    row_number = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
       
    for row_number in range(row_number):
        
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3* alien_height) - ship_height)
    number_rows = int(available_space_y / (2* alien_height))
    return number_rows

def update_aliens(ai_settings, aliens):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()  
     
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y  += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1 

   
def check_fleet_edges(ai_settings, aliens):
        for alien in aliens.sprites():
            if alien.check_edges():
                change_fleet_direction(ai_settings, aliens)
                break


    
             
