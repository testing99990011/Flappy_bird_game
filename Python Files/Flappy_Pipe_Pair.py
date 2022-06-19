import random, pygame
from pygame.sprite import Sprite

class PipePair(Sprite):
    """Pipe pair used for the game."""

    def __init__(self, GameBackground, MainInstance):
        """Inhertitance and values used for pipes."""
        super().__init__()

        # References for values
        self.MainInstance = MainInstance
        self.GameBackground = GameBackground
        self.settings = MainInstance.settings
        self.screen = MainInstance.screen

        # Loading the images
        self.pipe = pygame.image.load('Images/Driver/pipe-green.png')
        self.pipe = pygame.transform.scale(self.pipe, \
            (self.pipe.get_rect().width, self.pipe.get_rect().height + 100))
        self.top_pipe = pygame.transform.rotate(self.pipe, 180)
        self.bottom_pipe = self.pipe

        # Rects for top and bottom pipe
        self.top_pipe_rect = self.top_pipe.get_rect()
        self.bottom_pipe_rect = self.bottom_pipe.get_rect()

        # Generation and initial y-pos of bottom pipe.
        # Remember 0 is top and (+) is down
        self.bottom_value = self.settings.screen_height - self.GameBackground.BackgroundInstanceLogic.BackgroundAndBaseInstance.base_rect.height - \
            self.settings.pipe_distance_border
        self.top_value = self.settings.pipe_gap + self.settings.pipe_distance_border
        self.generated_y = random.randint(self.top_value, self.bottom_value)

        self.bottom_pipe_rect.top = self.generated_y
        self.top_pipe_rect.bottom = self.generated_y - self.settings.pipe_gap

        self.bottom_pipe_rect.x = self.settings.screen_width
        self.top_pipe_rect.x = self.settings.screen_width


    def update(self):
        # Update the pipes position
        self.top_pipe_rect.x -= self.settings.game_speed
        self.bottom_pipe_rect.x -= self.settings.game_speed


    def draw_pipe(self):
        # Draw the piped
        self.screen.blit(self.top_pipe, self.top_pipe_rect)
        self.screen.blit(self.bottom_pipe, self.bottom_pipe_rect)
