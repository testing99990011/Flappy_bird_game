import pygame

class FlappyBackgroundTutorial:
    """Background to tutorial screen after hitting 'play game'"""

    def __init__(self, BackgroundInstanceLogic, MainInstance):
        """Default values used in instance."""
        self.BackgroundInstanceLogic = BackgroundInstanceLogic
        self.MainInstance = MainInstance
        self.screen = self.MainInstance.screen
        self.settings = self.MainInstance.settings

        # Tutorial text
        self._update_text()

        # Flag for bird to oscillate
        self.go_up = True


    def _update_text(self):
        # Update the text for tutorial screen. Called at end of background main when screen change
        self.font = self.MainInstance.settings.tutorial_font
        self.tutorial_image = self.font.render(\
            f"Tap '{self.MainInstance.settings.settings_save_dict['jump']}'", \
            True, self.MainInstance.settings.tutorial_font_color)
        self.tutorial_image = pygame.transform.scale(self.tutorial_image, \
            (int(self.settings.screen_width/1.25) , int(self.settings.screen_height / 8)))
        self.tutorial_image_rect = self.tutorial_image.get_rect()
        self.tutorial_image_rect.center = self.screen.get_rect().center
        self.tutorial_image_rect.y = (self.tutorial_image_rect.height / 2)


    def draw_tutorial_screen(self):
        # Draw the tutorial screen
        self.BackgroundInstanceLogic.BackgroundAndBaseInstance.draw_background()
        self.screen.blit(self.tutorial_image, self.tutorial_image_rect)
        self.BackgroundInstanceLogic.BackgroundAndBaseInstance._update_base()
        self.BackgroundInstanceLogic.BackgroundAndBaseInstance.draw_base()
        self.BackgroundInstanceLogic.BackgroundInstanceGame.bird.draw_tutorial_bird()
