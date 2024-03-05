class Settings():
    
    def __init__(self):
        """Initialize the game's static settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        #Ship settings
        self.ship_limit = 3

        #Bullet settings

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 233, 0
        self.bullets_allowed = 3

        #Alien settings

        self.fleet_drop_speed = 15

        #How quickly the game speeds up
        self.speedup_scale = 1.2

        #How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1.5

        #fleet_direction of 1 represent right; -1 represents left 
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
