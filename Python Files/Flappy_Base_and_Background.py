import pygame

class BaseAndBackground:
    """"Base and background used all throughout different screens."""

    def __init__(self, MainInstance):
        """Basic values for background."""
        self.MainInstance = MainInstance
        self.settings = self.MainInstance.settings
        self.screen = self.MainInstance.screen

        # Load and create the background
        self.screen_background = pygame.image.load('Images/Driver/background-day.png')
        self.screen_background = pygame.transform.scale(self.screen_background,\
            (self.settings.screen_width, self.settings.screen_height))
        self.screen_background_rect = self.screen_background.get_rect()

        # Load the background base (bottom floor)
        self.base = pygame.image.load('Images/Driver/base.png')
        self.base = pygame.transform.scale(self.base, \
            (self.settings.screen_width * 2, self.base.get_rect().height))
        self.base_rect = self.base.get_rect()
        self.base_rect.bottomleft = 0, self.settings.screen_height


    def _update_base(self):
        # Update base position
        self.base_rect.x -= self.settings.game_speed
        if self.base_rect.right <= self.settings.screen_width:
            self.base_rect.bottomleft = 0, self.settings.screen_height


    def draw_background(self):
        # Draw the backgroud
        self.screen.blit(self.screen_background, self.screen_background_rect)
        self.screen.blit(self.base, self.base_rect)


    def draw_base(self):
        # Draw the base
        self.screen.blit(self.base, self.base_rect)
