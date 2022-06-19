import pygame

class ScoreBoard:
    """Background for ScoreBoard screen."""

    def __init__(self, MainInstance):
        """Basic values and image loading."""

        # References
        self.screen = MainInstance.screen
        self.settings = MainInstance.settings

        # Load the images
        self.zero = pygame.image.load('Images/Numbers/0.png').convert_alpha()
        self.one = pygame.image.load('Images/Numbers/1.png').convert_alpha()
        self.two = pygame.image.load('Images/Numbers/2.png').convert_alpha()
        self.three = pygame.image.load('Images/Numbers/3.png').convert_alpha()
        self.four = pygame.image.load('Images/Numbers/4.png').convert_alpha()
        self.five = pygame.image.load('Images/Numbers/5.png').convert_alpha()
        self.six = pygame.image.load('Images/Numbers/6.png').convert_alpha()
        self.seven = pygame.image.load('Images/Numbers/7.png').convert_alpha()
        self.eight = pygame.image.load('Images/Numbers/8.png').convert_alpha()
        self.nine = pygame.image.load('Images/Numbers/9.png').convert_alpha()

        # Values dict
        self.score_dict = {0: self.zero, 1: self.one, 2: self.two, 3: self.three, 4: self.four,
                           5: self.five, 6: self.six, 7: self.seven, 8: self.eight, 9: self.nine}
        self.basic_rect = self.zero.get_rect()
        self.screen_center = self.screen.get_rect().center

        # Basic call for default score of 0
        self._determine_score(self.settings.dynamic_score)


    def _determine_score(self, score):
        # Function to determine the score

        # Create a surface
        self.surface = pygame.Surface(((self.basic_rect.width + 5) * len(str(score)), \
            self.basic_rect.height), pygame.SRCALPHA)
        self.surface_rect = self.surface.get_rect()

        # Blit each score number onto surface
        for number, score_val in enumerate(str(score)):
            value = self.score_dict[int(score_val)]
            self.basic_rect.x = ((self.basic_rect.width + 5) * number)
            self.surface.blit(value, self.basic_rect)

        # Determine rect of surface
        self.surface_rect.center = self.screen_center
        self.surface_rect.y = self.settings.scoreboard_gap


    def draw_score(self):
        # Draw the actual scoreboard to game screen
        self._determine_score(self.settings.dynamic_score)
        self.screen.blit(self.surface, self.surface_rect)
