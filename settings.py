
class Settings():
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initializes the game's static settings"""
        self.screen_width = 1200 
        self.screen_height = 800 
        self.bg_color = (230, 230, 230)
        
        #ship settings
        
        self.ship_limit = 3 
        
        
        #bullet settings 
         
        self.bullet_width = 300
        self.bullet_height = 15 
        self.bullet_color = 60, 60, 60 
        self.bullets_allowed = 3
        
        
        #Alien Settings 
     
        self.fleet_drop_speed = 10
      
        
        #How quickly the game speeds up 
        self.speedup_scale = 1.1 
        self.score_scale = 1.5 
        
        self.high_score = 0
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5 
        self.bullet_speed_factor = 3 
        self.alien_speed_factor = 1 
        
        self.fleet_direction = 1 
        
        self.alien_points = 50
        
            
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale 
        self.bullet_speed_factor *= self.speedup_scale 
        self.alien_speed_factor *= self.speedup_scale 
           
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
