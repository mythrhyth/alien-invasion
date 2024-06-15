
# import sys 
# import pygame
# from bullet import Bullet 
# from alien import Alien
# from time import sleep 
# from game_stats import GameStats 

# def fire_bullet(ai_settings, screen, ship,  bullets):
#     #create a new bullet and add it to the bullets group. 
#         if len(bullets) < ai_settings.bullets_allowed:
#             new_bullet = Bullet(ai_settings, screen, ship)
#             bullets.add(new_bullet) 
    

# def check_keydown_events(event, ai_settings, screen, ship, bullets):
    
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = True   
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = True
#     elif event.key == pygame.K_SPACE:
#         fire_bullet(ai_settings, screen, ship, bullets)
#     elif event.key == pygame.K_q:
#         sys.exit()
        

# def check_keyup_events(event, ship):
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = False
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = False



# def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             check_keydown_events(event, ai_settings, screen, ship, bullets)
#         elif event.type == pygame.KEYUP:
#             check_keyup_events(event, ship)
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             check_play_button(ai_settings, screen, stats,sb,  play_button, ship, aliens, bullets, mouse_x, mouse_y)

# def check_play_button(ai_settings, screen, stats, sb,play_button, ship, aliens, bullets, mouse_x, mouse_y):
#      """Start a new game when player clicks Play."""
#      button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
     
#      if button_clicked and not stats.game_active:
#          #Hide the mouse cursor. 
#          ai_settings.initialize_dynamic_settings()
#          pygame.mouse.set_visible(False)
         
         
         
#          stats.reset_stats()
#          stats.game_active = True 
         
#          #Reset the scoreboard images 
#          sb.prep_score()
#          sb.prep_high_score()
#          sb.prep_level()   
#          sb.prep_ships()
         
         
#          #empty the list of aliens and bullets 
#          aliens.empty()
#          bullets.empty()
         
#          #Create a new fleet and center the ship 
#          create_fleet(ai_settings, screen, ship, aliens)
#          ship.center_ship()
         
         
         
                
        

        

# def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
#      #update images on the screen and flip to the new screen 
     
#      #draw the play button if the game is inactive 
     
     
#      #Redraw the screen during each pass through the loop
#      screen.fill(ai_settings.bg_color)
     
     
#      ship.blitme()
#      aliens.draw(screen)
#      for bullet in bullets.sprites():
#          bullet.draw_bullet()
#      #draw the play button if the game is inactive
#      sb.show_score()
     
#      if not stats.game_active:
#          play_button.draw_button()
     
#      #Make the most recently drawn screen visible 
#      pygame.display.flip()
     
# def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
#     collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
#     if collisions:
#         for aliens in collisions.values():
#             stats.score += ai_settings.alien_points *len(aliens)
#             sb.prep_score()
#         check_high_score(stats, sb)
    
    
#     if len(aliens) == 0:
#         bullets.empty()
#         ai_settings.increase_speed()
        
#         #increase level 
#         stats.level += 1 
#         sb.prep_level()
        
#         create_fleet(ai_settings, screen, ship, aliens)
        
        

# def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
#     """
#     Update position of bullets and get rid of old bullets.
#     """
#     check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
#     #Check for any bullets that have hit aliens. 
#     #If so, get rid of the bullet and the alien. 
    
    
    
    
    
#     # Update bullet positions.
#     bullets.update()
    
#     # Get rid of bullets that have disappeared.
#     for bullet in bullets.copy():
#         if bullet.rect.bottom <= 0:
#             bullets.remove(bullet)
            
    
     
     
# def get_number_aliens_x(ai_settings, alien_width):
        
#     available_space_x = ai_settings.screen_width - 2 * alien_width
#     number_aliens_x = int(available_space_x /(2 * alien_width))
#     return number_aliens_x


# def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    
        
#     alien = Alien(ai_settings, screen)
#     alien_width = alien.rect.width
#     alien.x = alien_width + 2 * alien_width * alien_number
#     alien.rect.x = alien.x 
#     alien.rect.y = alien.rect.height + 2* alien.rect.height * row_number
#     aliens.add(alien)

# def create_fleet(ai_settings, screen, ship, aliens):
#     #create an alien and find the number of aliens in a row
#     #spacing between each alien is equal to one alien width
#     alien = Alien(ai_settings, screen)
#     number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
#     row_number = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
       
#     for row_number in range(row_number):
        
#         for alien_number in range(number_alien_x):
#             create_alien(ai_settings, screen, aliens, alien_number, row_number)

# def get_number_rows(ai_settings, ship_height, alien_height):
#     available_space_y = (ai_settings.screen_height - (3* alien_height) - ship_height)
#     number_rows = int(available_space_y / (2* alien_height))
#     return number_rows



# def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):   
#     if stats.ships_left > 0:
#         stats.ships_left -= 1 
#         sb.prep_ships()
#     else:
#         stats.game_active = False
#         pygame.mouse.set_visible(True)
        
    
    
#     #empty the list of aliens and bullets 
#     aliens.empty()
#     bullets.empty()
    
#     #create a new fleet and center the ship
#     create_fleet(ai_settings, screen, ship, aliens)
#     ship.center_ship()
    
#     #pause
#     sleep(0.5)



# def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
#     check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)
#     check_fleet_edges(ai_settings, aliens)
#     aliens.update()  
    
#     #Look for alien-ship collisions. 
#     if pygame.sprite.spritecollideany(ship, aliens):
#         ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)  
     
# def change_fleet_direction(ai_settings, aliens):
#     for alien in aliens.sprites():
#         alien.rect.y  += ai_settings.fleet_drop_speed
#     ai_settings.fleet_direction *= -1 

   
# def check_fleet_edges(ai_settings, aliens):
#         for alien in aliens.sprites():
#             if alien.check_edges():
#                 change_fleet_direction(ai_settings, aliens)
#                 break


# def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
#      """Check if any aliens have reached the bottom of the screen"""
#      screen_rect = screen.get_rect()
#      for alien in aliens.sprites():
#          if alien.rect.bottom >= screen_rect.bottom:
#              #Treat this the same as if the ship got hit 
#              ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)   
#              break

# def check_high_score(stats, sb):
#     """Check to see if there's new high score"""
#     if stats.score > stats.high_score:
#         stats.high_score = stats.score 
#         sb.prep_high_score()
        
import sys 
import pygame
from bullet import Bullet 
from alien import Alien
from time import sleep 
from game_stats import GameStats 

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



def check_events(ai_settings, screen, stats,sb, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats,sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb,play_button, ship, aliens, bullets, mouse_x, mouse_y):
     """Start a new game when player clicks Play."""
     button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
     
     if button_clicked and not stats.game_active:
         #Hide the mouse cursor. 
         ai_settings.initialize_dynamic_settings()
         pygame.mouse.set_visible(False)
         
         
         
         stats.reset_stats()
         stats.game_active = True 
         
         #Reset the scoreboard images 
         sb.prep_score()
         sb.prep_high_score()
         sb.prep_level()   
         sb.prep_ships()
         
         
         #empty the list of aliens and bullets 
         aliens.empty()
         bullets.empty()
         
         #Create a new fleet and center the ship 
         create_fleet(ai_settings, screen, ship, aliens)
         ship.center_ship()
         
         
         
                
        

        

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
     #update images on the screen and flip to the new screen 
     
     #draw the play button if the game is inactive 
     
     
     #Redraw the screen during each pass through the loop
     screen.fill(ai_settings.bg_color)
     
     
     ship.blitme()
     aliens.draw(screen)
     for bullet in bullets.sprites():
         bullet.draw_bullet()
     #draw the play button if the game is inactive
     sb.show_score()
     
     if not stats.game_active:
         play_button.draw_button()
     
     #Make the most recently drawn screen visible 
     pygame.display.flip()
     
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points *len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    
    
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        
        #increase level 
        stats.level += 1 
        sb.prep_level()
        
        create_fleet(ai_settings, screen, ship, aliens)
        
        

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    Update position of bullets and get rid of old bullets.
    """
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
    #Check for any bullets that have hit aliens. 
    #If so, get rid of the bullet and the alien. 
    
    
    
    
    
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



def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1 
        sb.prep_ships()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        
    
    
    #empty the list of aliens and bullets 
    aliens.empty()
    bullets.empty()
    
    #create a new fleet and center the ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    
    #pause
    sleep(0.5)



def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    check_aliens_bottom(ai_settings, stats,sb, screen, ship, aliens, bullets)
    check_fleet_edges(ai_settings, aliens)
    aliens.update()  
    
    #Look for alien-ship collisions. 
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
     
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y  += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1 

   
def check_fleet_edges(ai_settings, aliens):
        for alien in aliens.sprites():
            if alien.check_edges():
                change_fleet_direction(ai_settings, aliens)
                break


def check_aliens_bottom(ai_settings, stats,sb, screen, ship, aliens, bullets):
     """Check if any aliens have reached the bottom of the screen"""
     screen_rect = screen.get_rect()
     for alien in aliens.sprites():
         if alien.rect.bottom >= screen_rect.bottom:
             #Treat this the same as if the ship got hit 
             ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)   
             break

def check_high_score(stats, sb):
    """Check to see if there's new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score 
        sb.prep_high_score()       
