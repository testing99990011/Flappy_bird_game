import pygame

class FlappyBird:
    """Actual bird used in the game."""

    def __init__(self, GameBackground, MainInstance):
        """Default values used in instance."""
        self.MainInstance = MainInstance
        self.GameBackground = GameBackground
        self.screen = MainInstance.screen
        self.settings = MainInstance.settings
        self.change_bird_color()

        # Initial starting position
        self.bird_rect = self.bird_downflap.get_rect()
        self.bird_rect.midleft = self.screen.get_rect().midleft
        self.bird_center_y = (self.settings.screen_height - self.GameBackground.BackgroundInstanceLogic.BackgroundAndBaseInstance.base_rect.height) \
            / 2 - (self.bird_rect.height / 2)
        self.bird_rect.y = self.bird_center_y
        self.bird_rect.x += 20

        # Counter for animation, velocity, and movement. Flags for jump
        self.count = 0
        self.bird_default = self.bird_downflap
        self.velocity = 0
        self.current_rotation = 0
        self.jump = False


    def change_bird_color(self):
        # Load the bird from settings

        # Yellow color
        if self.settings.settings_save_dict['bird_color'] == 'yellow':
            self.bird_downflap = pygame.image.load('Images/Driver/yellowbird-downflap.png')
            self.bird_centerflap = pygame.image.load('Images/Driver/yellowbird-midflap.png')
            self.bird_upflap = pygame.image.load('Images/Driver/yellowbird-upflap.png')

        # Red color
        elif self.settings.settings_save_dict['bird_color'] == 'red':
            self.bird_downflap = pygame.image.load('Images/Driver/redbird-downflap.png')
            self.bird_centerflap = pygame.image.load('Images/Driver/redbird-midflap.png')
            self.bird_upflap = pygame.image.load('Images/Driver/redbird-upflap.png')

        # Blue color
        elif self.settings.settings_save_dict['bird_color'] == 'blue':
            self.bird_downflap = pygame.image.load('Images/Driver/bluebird-downflap.png')
            self.bird_centerflap = pygame.image.load('Images/Driver/bluebird-midflap.png')
            self.bird_upflap = pygame.image.load('Images/Driver/bluebird-upflap.png')


    def _update_type_rect(self):
        # Change the flap animation
        if 0 <= self.count < 10:
            self.bird_default = self.bird_downflap
            self.count += 1
        elif 10 <= self.count < 20:
            self.bird_default = self.bird_centerflap
            self.count += 1
        elif 20 <= self.count < 30:
            self.bird_default = self.bird_upflap
            self.count += 1
        elif 30 <= self.count < 40:
            self.bird_default = self.bird_centerflap
            self.count += 1
        else:
            self.count = 0


    def update_y_position(self):
        # Function to update y-pos. (x no change because background moves)
        self.settings.distance_x += self.settings.distance_travel_factor_x

        # Change the flap direction
        self._update_type_rect()

        # Update the position
        if self.jump:
            self.settings.jumps += 1
            self.velocity = -self.settings.jump_power
            self.current_rotation = self.settings.max_angle
        else:
            self.settings.distance_y += self.settings.distance_travel_factor_y
            self.velocity += self.settings.settings_save_dict['gravity']
            if self.current_rotation > -90:
                self.current_rotation -= self.settings.rotation_angle

        # Transfrom and update values
        self.bird_copy = pygame.transform.rotate(self.bird_default, self.current_rotation)
        self.jump = False
        self.bird_rect.y += self.velocity

        # Hitbox normal
        self.bird_hitbox = pygame.Surface((self.bird_rect.width, self.bird_rect.height))
        self.bird_hitbox.fill((0,0,0))
        self.bird_hitbox_rect = self.bird_hitbox.get_rect()
        self.bird_hitbox_rect.center = self.bird_rect.center

        # Hitbox advanced
        self.bird_hitbox_advanced = pygame.Surface(\
            (self.bird_copy.get_rect().width, self.bird_copy.get_rect().height))
        self.bird_hitbox_advanced_rect = self.bird_hitbox_advanced.get_rect()
        self.bird_hitbox_advanced_rect.center = self.bird_rect.center
        self.bird_hitbox_advanced.fill((0, 0, 255))


    def draw_tutorial_bird(self):
        # Draw the tutorial bird
        self._update_type_rect()
        if self.GameBackground.BackgroundInstanceLogic.BackgroundInstanceTutorial.go_up:
            self.bird_rect.y -= self.settings.tutorial_bird_speed
        else:
            self.bird_rect.y += self.settings.tutorial_bird_speed
        if self.bird_rect.center[1] <= self.bird_center_y - self.settings.tutorial_bird_oscillation:
            self.GameBackground.BackgroundInstanceLogic.BackgroundInstanceTutorial.go_up = False
        elif self.bird_rect.center[1] >= self.bird_center_y + self.settings.tutorial_bird_oscillation:
            self.GameBackground.BackgroundInstanceLogic.BackgroundInstanceTutorial.go_up = True
        self.screen.blit(self.bird_default, self.bird_rect)


    def draw_bird(self):
        # Draw the game bird
        if self.settings.settings_save_dict['hitbox'] == 'default':
            self.screen.blit(self.bird_copy, self.bird_rect)
        elif self.settings.settings_save_dict['hitbox'] == 'default_box':
            self.screen.blit(self.bird_hitbox, self.bird_hitbox_rect)
        elif self.settings.settings_save_dict['hitbox'] == 'hitbox_adaptive':
            self.screen.blit(self.bird_hitbox_advanced, self.bird_hitbox_advanced_rect)


    def reset_bird_default(self):
        # Reset position of bird
        self.bird_rect.y = self.bird_center_y
        self.bird_rect.x = 20
