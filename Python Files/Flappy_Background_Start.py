import pygame

class FlappyBackgroundStart:
    """Background for start screen."""

    def __init__(self, BackgroundInstanceLogic, MainInstance):
        """Basic values used in Start Screen."""
        self.BackgroundInstanceLogic = BackgroundInstanceLogic
        self.MainInstance = MainInstance
        self.settings = self.MainInstance.settings
        self.screen = self.MainInstance.screen

        # Load the game logo
        self.logo_image = pygame.image.load('Images/Driver/logo.png')
        self.logo_image = pygame.transform.scale(self.logo_image,\
            (self.settings.logo_width_start, self.settings.logo_height_start))

        # Load the play button
        self.play_button = pygame.image.load('Images/Buttons/playgame.PNG').convert()
        self.play_button.set_colorkey((255, 255, 255))
        self.play_button = pygame.transform.scale(self.play_button, \
            (self.settings.button_width_start, self.settings.button_height_start))

        # Load the settings button
        self.settings_button = pygame.image.load('Images/Buttons/settings.PNG').convert()
        self.settings_button.set_colorkey((255, 255, 255))
        self.settings_button = pygame.transform.scale(self.settings_button,\
            (self.settings.button_width_start, self.settings.button_height_start))

        # Load the scores button
        self.score_button = pygame.image.load('Images/Buttons/scores.PNG').convert()
        self.score_button.set_colorkey((255, 255, 255))
        self.score_button = pygame.transform.scale(self.score_button,\
            (self.settings.button_width_start, self.settings.button_height_start))

        # Load default rects
        self._position_rects_default()

        # Load the start button highlight
        self.play_button_highlight = pygame.image.load('Images/Buttons/playgame.PNG').convert()
        self.play_button_highlight.set_colorkey((255, 255, 255))
        self.play_button_highlight = pygame.transform.scale(self.play_button_highlight, \
            (int(self.settings.button_width_start * (1 + self.settings.button_expansion_rate_start)),\
            int(self.settings.button_height_start * (1 + self.settings.button_expansion_rate_start)))
            )
        self.play_button_highlight_rect = self.play_button_highlight.get_rect()
        self.play_button_highlight_rect.center = self.play_button_rect.center

        # Load the settings button highlight
        self.settings_button_highlight = pygame.image.load('Images/Buttons/settings.PNG').convert()
        self.settings_button_highlight.set_colorkey((255, 255, 255))
        self.settings_button_highlight = pygame.transform.scale(self.settings_button_highlight, \
            (int(self.settings.button_width_start * (1 + self.settings.button_expansion_rate_start)),\
            int(self.settings.button_height_start * (1 + self.settings.button_expansion_rate_start)))
            )
        self.settings_button_highlight_rect = self.settings_button_highlight.get_rect()
        self.settings_button_highlight_rect.center = self.settings_button_rect.center

        # Load the score button highlight
        self.score_button_highlight = pygame.image.load('Images/Buttons/scores.PNG').convert()
        self.score_button_highlight.set_colorkey((255, 255, 255))
        self.score_button_highlight = pygame.transform.scale(self.score_button_highlight, \
            (int(self.settings.button_width_start * (1 + self.settings.button_expansion_rate_start)),\
            int(self.settings.button_height_start * (1 + self.settings.button_expansion_rate_start)))
            )
        self.score_button_highlight_rect = self.score_button_highlight.get_rect()
        self.score_button_highlight_rect.center = self.score_button_rect.center

        # Flags for dynamic highlighting
        self.play_button_highlighted = False
        self.score_button_highlighted = False
        self.settings_button_highlighted = False


    def _position_rects_default(self):
        # Position the rects in default position

        # For the logo
        self.logo_image_rect = self.logo_image.get_rect()
        self.logo_image_rect.center = self.screen.get_rect().center
        self.logo_image_rect.top =  self.settings.logo_gap_start

        # For the play button
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.center = self.screen.get_rect().center
        self.play_button_rect.bottom += self.play_button_rect.height

        # For the settings button
        self.settings_button_rect = self.settings_button.get_rect()
        self.settings_button_rect.y = (self.play_button_rect.y + self.play_button_rect.height + \
            self.settings.button_gap_start)
        self.settings_button_rect.x = (self.play_button_rect.x - (self.settings.button_gap_start / 2) - \
            (self.play_button_rect.width / 2))

        # For the score button
        self.score_button_rect = self.score_button.get_rect()
        self.score_button_rect.y = self.settings_button_rect.y
        self.score_button_rect.x = (self.play_button_rect.x + (self.play_button_rect.width / 2) + \
            (self.settings.button_gap_start / 2))


    def _draw_highlights(self):
        # Draw highlights if a collision between mouse and button occurs
        mouse = pygame.mouse.get_pos()

        # First if statement for play button
        if self.play_button_rect.collidepoint(mouse) or \
           self.play_button_highlight_rect.collidepoint(mouse) and self.play_button_highlighted:
               self.screen.blit(self.play_button_highlight, self.play_button_highlight_rect)
               self.play_button_highlighted = True
        else:
            self.play_button_highlighted = False

        # Second statement for settings button
        if self.settings_button_rect.collidepoint(mouse) or \
           self.settings_button_highlight_rect.collidepoint(mouse) and self.settings_button_highlighted:
               self.screen.blit(self.settings_button_highlight, self.settings_button_highlight_rect)
               self.settings_button_highlighted = True
        else:
            self.settings_button_highlighted = False

        # Third statement for the score button
        if self.score_button_rect.collidepoint(mouse) or \
           self.score_button_highlight_rect.collidepoint(mouse) and self.score_button_highlighted:
               self.screen.blit(self.score_button_highlight, self.score_button_highlight_rect)
               self.score_button_highlighted = True
        else:
            self.score_button_highlighted = False


    def draw_start_background(self):
        # Draw the background for start screen
        self.BackgroundInstanceLogic.BackgroundAndBaseInstance.draw_background()
        self.BackgroundInstanceLogic.BackgroundAndBaseInstance.draw_base()
        self.screen.blit(self.logo_image, self.logo_image_rect)

        # Draw the buttons
        self.screen.blit(self.play_button, self.play_button_rect)
        self.screen.blit(self.settings_button, self.settings_button_rect)
        self.screen.blit(self.score_button, self.score_button_rect)

        # Check for highlights if no animation
        if not self.BackgroundInstanceLogic.animation_running:
            self._draw_highlights()
