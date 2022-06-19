import pygame, sys, os
os.chdir("..")
from Flappy_Settings import FlappySettings
from Flappy_Background import FlappyBackground

class FlappyMain:
    """Flappybird main instance. Contains the main loop for game."""

    def __init__(self):
        """Default values that are always called."""

        # Init pygame
        pygame.init()

        # Create settings instance
        self.settings = FlappySettings()

        # Create main screen
        self.screen = pygame.display.set_mode(size=(self.settings.screen_width, self.settings.screen_height))

        # Instance for background logic. After screen because uses 'self.screen'
        self.background_main = FlappyBackground(self)

        # Flags to control screens
        self.start_screen = True
        self.game_screen = False
        self.settings_screen = False
        self.scores_screen = False
        self.tutorial_screen = False
        self.gameover_screen = False


    def main_loop(self):
        # Main loop for the game
        clock = pygame.time.Clock()
        while True:
            clock.tick(self.settings.fps)
            self._check_events()
            self.background_main.BackgroundLogic()


    def _check_events(self):
        # Check the events in the game
        for event in pygame.event.get():

            # Quit Event
            if event.type == pygame.QUIT:

                # Force a settings update for achiv and datas if exit during match
                if self.game_screen:
                    self.background_main.BackgroundInstanceGame._add_match_leaderboard()
                    self.background_main.BackgroundInstanceGame.achievement_logic()
                    self.background_main.BackgroundInstanceGame._add_match_data()

                # Save all items and exit
                self.settings._save_all_items()
                pygame.quit()
                sys.exit()

            # Check clicks and button presses only if animation is not running
            if not self.background_main.animation_running:

                # Mouse click event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()

                    # Check the start screen
                    if self.start_screen:

                        # Check the collision with play_button
                        if self.background_main.BackgroundInstanceStart.play_button_rect.collidepoint(mouse) or\
                           self.background_main.BackgroundInstanceStart.play_button_highlight_rect.collidepoint(mouse) and\
                           self.background_main.BackgroundInstanceStart.play_button_highlighted:
                               self.background_main.animation_running = True
                               self.background_main.animation_start_game = True

                        # Check the collision with settings_button
                        if self.background_main.BackgroundInstanceStart.settings_button_rect.collidepoint(mouse) or\
                            self.background_main.BackgroundInstanceStart.settings_button_highlight_rect.collidepoint(mouse) and\
                            self.background_main.BackgroundInstanceStart.settings_button_highlighted:
                                self.background_main.animation_running = True
                                self.background_main.animation_start_settings = True

                        # Check the collision with score_button
                        if self.background_main.BackgroundInstanceStart.score_button_rect.collidepoint(mouse) or\
                            self.background_main.BackgroundInstanceStart.score_button_highlight_rect.collidepoint(mouse) and\
                            self.background_main.BackgroundInstanceStart.score_button_highlighted:
                                self.background_main.animation_running = True
                                self.background_main.animation_start_scores = True

                                # Force a region update since your switching to scores. (Game screen -> Start -> Scores)
                                self.background_main.BackgroundInstanceScorescreen.update_region_surface()

                    # Check the gameover screen
                    elif self.gameover_screen:

                        # Check the collision between restart_button
                        if self.background_main.BackgroundInstanceGameOver.restart_button_rect.collidepoint(mouse) or\
                            self.background_main.BackgroundInstanceGameOver.restart_button_highlight_rect.collidepoint(mouse) and\
                            self.background_main.BackgroundInstanceGame.restart_button_highlighted:
                                self.gameover_screen = False
                                self.tutorial_screen = True

                        # Check the collision between the menu_button
                        if self.background_main.BackgroundInstanceGameOver.menu_button_rect.collidepoint(mouse) or\
                            self.background_main.BackgroundInstanceGameOver.menu_button_highlight_rect.collidepoint(mouse) and\
                            self.background_main.BackgroundInstanceGameOver.menu_button_highlighted:
                                self.gameover_screen = False
                                self.start_screen = True

                    # Check the scores screen
                    elif self.scores_screen:

                        # Check the collision between menu_button
                        if self.background_main.BackgroundInstanceScorescreen.menu_button_rect.collidepoint(mouse) or\
                            self.background_main.BackgroundInstanceScorescreen.menu_button_highlight_rect.collidepoint(mouse) and\
                            self.background_main.BackgroundInstanceScorescreen.menu_button_highlighted:
                                self.background_main.animation_running = True
                                self.background_main.animation_scores_start = True

                        # Check the collision between the right_arrow
                        if self.background_main.BackgroundInstanceScorescreen.right_arrow_rect.collidepoint(mouse) or\
                            self.background_main.BackgroundInstanceScorescreen.right_arrow_highlight_rect.collidepoint(mouse) and\
                            self.background_main.BackgroundInstanceScorescreen.right_arrow_highlighted:
                                if self.background_main.BackgroundInstanceScorescreen.page != self.background_main.BackgroundInstanceScorescreen.total_pages:
                                    self.background_main.BackgroundInstanceScorescreen.page += 1
                                    self.background_main.BackgroundInstanceScorescreen.update_region_surface()

                        # Check the collision between the left_arrow
                        if self.background_main.BackgroundInstanceScorescreen.left_arrow_rect.collidepoint(mouse) or\
                            self.background_main.BackgroundInstanceScorescreen.left_arrow_highlight_rect.collidepoint(mouse) and\
                            self.background_main.BackgroundInstanceScorescreen.left_arrow_highlighted:
                                if self.background_main.BackgroundInstanceScorescreen.page != 1:
                                    self.background_main.BackgroundInstanceScorescreen.page -= 1
                                    self.background_main.BackgroundInstanceScorescreen.update_region_surface()

                    # Check the settings screen
                    elif self.settings_screen:

                        # Make sure keyrebind not in progress
                        if not self.background_main.BackgroundInstanceSettings.reset_keybind_recent and not self.background_main.BackgroundInstanceSettings.reset_gravity_recent:

                            # If mouse is within defined region (needed to due blitting of settings)
                            if (self.settings.screen_width - self.settings.region_side_gap_settings) >= mouse[0] >= self.settings.region_side_gap_settings and\
                                (self.settings.region_side_gap_settings + self.settings.region_height_settings) >= mouse[1] >= self.settings.region_side_gap_settings:
                                    mouse = (mouse[0] - self.settings.region_side_gap_settings, mouse[1])
                                    mouse = (mouse[0], mouse[1] - self.settings.region_side_gap_settings)

                            # Check the collision between menu_button
                            if self.background_main.BackgroundInstanceSettings.menu_button_rect.collidepoint(mouse) or\
                                self.background_main.BackgroundInstanceSettings.menu_button_highlight_rect.collidepoint(mouse) and\
                                self.background_main.BackgroundInstanceSettings.menu_button_highlighted:
                                    self.background_main.animation_running = True
                                    self.background_main.animation_settings_start = True

                            # Check if collision between the reset_settings button
                            if not self.background_main.BackgroundInstanceSettings.reset_settings_recent:
                                if self.background_main.BackgroundInstanceSettings.reset_settings_button_rect.collidepoint(mouse) or\
                                    self.background_main.BackgroundInstanceSettings.reset_settings_button_highlight_rect.collidepoint(mouse) and\
                                    self.background_main.BackgroundInstanceSettings.reset_settings_button_highlighted:

                                        # Reset the settings
                                        self.settings.reset_saved_settings()
                                        self.background_main.BackgroundInstanceGame.bird.change_bird_color()

                                        # Flags for settings screen
                                        self.background_main.BackgroundInstanceSettings.reset_settings_recent = True
                                        self.reset_settings_start = pygame.time.get_ticks() / 1000
                                        self.background_main.BackgroundInstanceSettings._create_region()

                                        # Push left to reset. Default method needed to prevent compunded negative value
                                        self.background_main.BackgroundInstanceStart._position_rects_default()
                                        self.background_main.BackgroundInstanceStart.play_button_rect.x -= self.settings.screen_width
                                        self.background_main.BackgroundInstanceStart.settings_button_rect.x -= self.settings.screen_width
                                        self.background_main.BackgroundInstanceStart.score_button_rect.x -= self.settings.screen_width
                                        self.background_main.BackgroundInstanceStart.logo_image_rect.x -= self.settings.screen_width

                            # Check if collision between the reset_data button
                            if not self.background_main.BackgroundInstanceSettings.reset_data_recent:
                                if self.background_main.BackgroundInstanceSettings.reset_data_button_rect.collidepoint(mouse) or\
                                    self.background_main.BackgroundInstanceSettings.reset_data_button_highlight_rect.collidepoint(mouse) and\
                                    self.background_main.BackgroundInstanceSettings.reset_data_button_highlighted:

                                        # Reset the saved data
                                        self.settings.reset_saved_data()

                                        # Reset achievement instances. (Achievement instances built from saved data, so after reset_saved_data())
                                        self.background_main._create_achievements_instances()

                                        # Flags for settings screen
                                        self.background_main.BackgroundInstanceSettings.reset_data_recent = True
                                        self.reset_data_start = pygame.time.get_ticks() / 1000
                                        self.background_main.BackgroundInstanceSettings._create_region()

                            # Check if collision between difficulty (defualt)
                            if self.background_main.BackgroundInstanceSettings.hitbox_default_rect.collidepoint(mouse) and\
                                self.settings.settings_save_dict['hitbox'] != 'default':
                                    self.settings.settings_save_dict['hitbox'] = 'default'
                                    self.background_main.BackgroundInstanceSettings._create_region()

                            # Check if collision between difficulty (default box)
                            if self.background_main.BackgroundInstanceSettings.hitbox_default_box_rect.collidepoint(mouse) and\
                                self.settings.settings_save_dict['hitbox'] != 'default_box':
                                    self.settings.settings_save_dict['hitbox'] = 'default_box'
                                    self.background_main.BackgroundInstanceSettings._create_region()

                            # Check if collision between difficulty (adaptive)
                            if self.background_main.BackgroundInstanceSettings.hitbox_adaptive_rect.collidepoint(mouse) and\
                                self.settings.settings_save_dict['hitbox'] != 'hitbox_adaptive':
                                    self.settings.settings_save_dict['hitbox'] = 'hitbox_adaptive'
                                    self.background_main.BackgroundInstanceSettings._create_region()

                            # Check if collision between animation_button
                            if self.background_main.BackgroundInstanceSettings.animation_option_rect.collidepoint(mouse):
                                if self.settings.settings_save_dict['animations'] == True:
                                    self.settings.settings_save_dict['animations'] = False
                                else:
                                    self.settings.settings_save_dict['animations'] = True

                                    # Push left to reset. Default method needed to prevent compunded negative value
                                    self.background_main.BackgroundInstanceStart._position_rects_default()
                                    self.background_main.BackgroundInstanceStart.play_button_rect.x -= self.settings.screen_width
                                    self.background_main.BackgroundInstanceStart.settings_button_rect.x -= self.settings.screen_width
                                    self.background_main.BackgroundInstanceStart.score_button_rect.x -= self.settings.screen_width
                                    self.background_main.BackgroundInstanceStart.logo_image_rect.x -= self.settings.screen_width
                                self.background_main.BackgroundInstanceSettings._create_region()

                            # Check if collision between achievement_option
                            if self.background_main.BackgroundInstanceSettings.achievement_option_rect.collidepoint(mouse):
                                if self.settings.settings_save_dict['achievements'] == True:
                                    self.settings.settings_save_dict['achievements'] = False
                                else:
                                    self.settings.settings_save_dict['achievements'] = True
                                self.background_main.BackgroundInstanceSettings._create_region()

                            # Check if collision between key_rebind
                            if self.background_main.BackgroundInstanceSettings.key_rebind_surface_rect.collidepoint(mouse):
                                self.background_main.BackgroundInstanceSettings.reset_keybind_recent = True
                                self.background_main.BackgroundInstanceSettings._create_region()

                            # Check if collision between reset gravity_rebind
                            if self.background_main.BackgroundInstanceSettings.gravity_rebind_surface_rect.collidepoint(mouse):
                                self.background_main.BackgroundInstanceSettings.reset_gravity_recent = True
                                self.settings.settings_save_dict['gravity'] = ''
                                self.background_main.BackgroundInstanceSettings._create_region()

                            # Check if collision between yellow_bird
                            if self.background_main.BackgroundInstanceSettings.yellow_bird_option_image_rect.collidepoint(mouse):
                                self.settings.settings_save_dict['bird_color'] = 'yellow'
                                self.background_main.BackgroundInstanceGame.bird.change_bird_color()
                                self.background_main.BackgroundInstanceSettings._create_region()

                            # Check if collision between red_bird
                            if self.background_main.BackgroundInstanceSettings.red_bird_option_image_rect.collidepoint(mouse):
                                self.settings.settings_save_dict['bird_color'] = 'red'
                                self.background_main.BackgroundInstanceGame.bird.change_bird_color()
                                self.background_main.BackgroundInstanceSettings._create_region()

                            # Check if collision between blue_bird
                            if self.background_main.BackgroundInstanceSettings.blue_bird_option_image_rect.collidepoint(mouse):
                                self.settings.settings_save_dict['bird_color'] = 'blue'
                                self.background_main.BackgroundInstanceGame.bird.change_bird_color()
                                self.background_main.BackgroundInstanceSettings._create_region()

                # Keystroke Event
                if event.type == pygame.KEYDOWN:

                    # Check if game screen or tutorial screen
                    if self.game_screen or self.tutorial_screen:
                        if event.key == self.settings.keybinds[self.settings.settings_save_dict['jump']]:

                            # Close out of the tutorial screen
                            if self.tutorial_screen:
                                self.tutorial_screen = False
                                self.game_screen = True
                                self.settings.start_time = pygame.time.get_ticks()
                                self.background_main.BackgroundInstanceGame.bird.jump = True

                            # If game is running
                            elif self.game_screen:
                                self.background_main.BackgroundInstanceGame.bird.jump = True

                    # Check if settings screen
                    if self.settings_screen:

                        # Check if reset keybind
                        if self.background_main.BackgroundInstanceSettings.reset_keybind_recent:
                            self.changes = False
                            for key, item in self.settings.keybinds.items():
                                if event.key == item:
                                    self.settings.settings_save_dict['jump'] = key
                                    self.changes = True
                            if not self.changes:
                                self.settings.settings_save_dict['jump'] = 'space'
                            self.background_main.BackgroundInstanceSettings.reset_keybind_recent = False
                            self.background_main.BackgroundInstanceSettings._create_region()

                        # Check if changing gravity
                        if self.background_main.BackgroundInstanceSettings.reset_gravity_recent:
                            self.changes = False
                            for key, item in self.settings.keybinds_number.items():
                                if event.key == item:
                                    if key == 'backspace':
                                        self.settings.settings_save_dict['gravity'] = self.settings.settings_save_dict['gravity'][0:len(self.settings.gravity)-1]
                                    else:
                                        self.settings.settings_save_dict['gravity'] += key
                                    self.changes = True
                            if not self.changes:
                                try:
                                    self.settings.settings_save_dict['gravity'] = float(self.settings.settings_save_dict['gravity'])
                                except ValueError:
                                    self.settings.settings_save_dict['gravity'] = 0.3
                                self.background_main.BackgroundInstanceSettings.reset_gravity_recent = False
                            self.background_main.BackgroundInstanceSettings._create_region()


if __name__ == '__main__':
    instance = FlappyMain()
    instance.main_loop()
