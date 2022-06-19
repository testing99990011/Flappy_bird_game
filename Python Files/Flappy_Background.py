import pygame, Flappy_Achievements
from Flappy_Base_and_Background import BaseAndBackground
from Flappy_Background_Start import FlappyBackgroundStart
from Flappy_Background_Game import FlappyBackgroundGame
from Flappy_Background_Tutorial import FlappyBackgroundTutorial
from Flappy_Background_Gameover import FlappyBackgroundGameoverscreen
from Flappy_Background_Scorescreen import FlappyBackgroundScorescreen
from Flappy_Background_Settings import FlappyBackgroundSettings

class FlappyBackground:
    """Background logic for the game. Controls all the screens."""

    def __init__(self, MainInstance):
        """Default values called on creation."""

        # Instances of screens and other classes used
        self.MainInstance = MainInstance
        self.settings = self.MainInstance.settings
        self.screen = self.MainInstance.screen
        self._create_achievements_instances()
        self.BackgroundAndBaseInstance = BaseAndBackground(MainInstance)
        self.BackgroundInstanceStart = FlappyBackgroundStart(self, MainInstance)
        self.BackgroundInstanceGame = FlappyBackgroundGame(self, MainInstance)
        self.BackgroundInstanceTutorial = FlappyBackgroundTutorial(self, MainInstance)
        self.BackgroundInstanceGameOver = FlappyBackgroundGameoverscreen(self, MainInstance)
        self.BackgroundInstanceScorescreen = FlappyBackgroundScorescreen(self, MainInstance)
        self.BackgroundInstanceSettings = FlappyBackgroundSettings(self, MainInstance)

        # Animation flags and values
        self.animation_distance = 0
        self.animation_running = False
        self.animation_start_game = False
        self.animation_start_scores = False
        self.animation_scores_start = False
        self.animation_start_settings = False
        self.animation_settings_start = False


    def _create_achievements_instances(self):
        # Create the achievements list
        self.all_achievements = [Flappy_Achievements.NewPlayer(self.MainInstance), Flappy_Achievements.TheJumperI(self.MainInstance),
                                 Flappy_Achievements.TheExplorerI(self.MainInstance), Flappy_Achievements.TheBeginner(self.MainInstance),
                                 Flappy_Achievements.TheNovice(self.MainInstance), Flappy_Achievements.TheJumperII(self.MainInstance),
                                 Flappy_Achievements.ItHappens(self.MainInstance), Flappy_Achievements.Gravity(self.MainInstance)]

        # Cant use a generator because generators dont return a single value
        [achiv.update_req_val() for achiv in self.all_achievements]


    def BackgroundLogic(self):
        # Main logic function called from Flappy_Main class

        # Fill the screen
        self.screen.fill((0, 0, 0))

        # Priority for animations between screens
        if self.animation_running:
            self._run_background_switch_animations()

        # If background screen
        elif self.MainInstance.start_screen:
            self.BackgroundInstanceStart.draw_start_background()

        # If tutorial screen
        elif self.MainInstance.tutorial_screen:
            self.BackgroundInstanceTutorial.draw_tutorial_screen()

        # If game screen
        elif self.MainInstance.game_screen:
            self.BackgroundInstanceGame._pipe_logic()
            self.BackgroundInstanceGame.pipe_group.update()
            self.BackgroundAndBaseInstance._update_base()
            self.BackgroundInstanceGame.bird.update_y_position()
            self.BackgroundInstanceGame.draw_game_background()
            self.BackgroundInstanceGame.achievement_logic()
            self.BackgroundInstanceGame.draw_achievements_logic()
            self.BackgroundInstanceGame.check_collisions()

        # If gameover screen
        elif self.MainInstance.gameover_screen:
            self.BackgroundInstanceGameOver.draw_gameover_background()

        # If score screen
        elif self.MainInstance.scores_screen:
            self.BackgroundInstanceScorescreen.draw_scorescreen()

        # If settings screen
        elif self.MainInstance.settings_screen:
            self.BackgroundInstanceSettings.draw_settings_background()

        # Update the pygame display
        pygame.display.flip()



    def _run_background_switch_animations(self):
        # Function for animation logic

        # Check for start screen to play screen
        if self.animation_start_game:

            # Move the screen over by animation speed
            if self.settings.settings_save_dict['animations'] == True:
                self.BackgroundInstanceStart.play_button_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceStart.settings_button_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceStart.score_button_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceStart.logo_image_rect.x -= self.settings.animation_speed

            # Blit the start screen
            self.BackgroundAndBaseInstance.draw_background()
            self.BackgroundAndBaseInstance.draw_base()
            self.screen.blit(self.BackgroundInstanceStart.play_button, \
                            self.BackgroundInstanceStart.play_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.settings_button, \
                            self.BackgroundInstanceStart.settings_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.score_button, \
                            self.BackgroundInstanceStart.score_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.logo_image, \
                            self.BackgroundInstanceStart.logo_image_rect)

            # Check if animation is over. If so, start the screens
            self.animation_distance += self.settings.animation_speed
            if self.animation_distance >= self.settings.screen_width or self.settings.settings_save_dict['animations'] ==False:
                self.animation_distance = 0
                self.BackgroundInstanceStart._position_rects_default()
                self.MainInstance.start_screen = False
                self.MainInstance.tutorial_screen = True
                self.animation_running = False
                self.animation_start_game = False

        # Check for start screen to score screen
        elif self.animation_start_scores:

            # Move the start screen to the left
            if self.settings.settings_save_dict['animations'] == True:
                self.BackgroundInstanceStart.play_button_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceStart.settings_button_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceStart.score_button_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceStart.logo_image_rect.x -= self.settings.animation_speed

            # Blit the start screen
            self.BackgroundAndBaseInstance.draw_background()
            self.BackgroundAndBaseInstance.draw_base()
            self.screen.blit(self.BackgroundInstanceStart.play_button, \
                            self.BackgroundInstanceStart.play_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.settings_button, \
                            self.BackgroundInstanceStart.settings_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.score_button, \
                            self.BackgroundInstanceStart.score_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.logo_image, \
                            self.BackgroundInstanceStart.logo_image_rect)

            # Move the score screen to the left
            if self.settings.settings_save_dict['animations'] == True:
                self.BackgroundInstanceScorescreen.region_surface_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceScorescreen.menu_button_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceScorescreen.left_arrow_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceScorescreen.right_arrow_rect.x -= self.settings.animation_speed

            # Blit the score screen
            self.screen.blit(self.BackgroundInstanceScorescreen.region_surface, \
                            self.BackgroundInstanceScorescreen.region_surface_rect)
            self.screen.blit(self.BackgroundInstanceScorescreen.menu_button, \
                            self.BackgroundInstanceScorescreen.menu_button_rect)
            self.screen.blit(self.BackgroundInstanceScorescreen.left_arrow, \
                            self.BackgroundInstanceScorescreen.left_arrow_rect)
            self.screen.blit(self.BackgroundInstanceScorescreen.right_arrow, \
                            self.BackgroundInstanceScorescreen.right_arrow_rect)

            # Check if animation is over. If so, start the score screen.
            # Do NOT reset start screen to default because we need to reverse it later for animations
            self.animation_distance += self.settings.animation_speed
            if self.animation_distance >= self.settings.screen_width or self.settings.settings_save_dict['animations'] == False:
                self.animation_distance = 0
                self.BackgroundInstanceScorescreen._position_rects_default()    # Default score screen
                self.MainInstance.start_screen = False
                self.MainInstance.scores_screen = True
                self.animation_running = False
                self.animation_start_scores = False

        # Check if scores screen to start screen
        elif self.animation_scores_start:

            # Move the start screen to the right
            if self.settings.settings_save_dict['animations'] == True:
                self.BackgroundInstanceStart.play_button_rect.x += self.settings.animation_speed
                self.BackgroundInstanceStart.settings_button_rect.x += self.settings.animation_speed
                self.BackgroundInstanceStart.score_button_rect.x += self.settings.animation_speed
                self.BackgroundInstanceStart.logo_image_rect.x += self.settings.animation_speed

            # Blit the start screen
            self.BackgroundAndBaseInstance.draw_background()
            self.BackgroundAndBaseInstance.draw_base()
            self.screen.blit(self.BackgroundInstanceStart.play_button, \
                            self.BackgroundInstanceStart.play_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.settings_button, \
                            self.BackgroundInstanceStart.settings_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.score_button, \
                            self.BackgroundInstanceStart.score_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.logo_image, \
                            self.BackgroundInstanceStart.logo_image_rect)

            # Move the score screen to the right
            if self.settings.settings_save_dict['animations'] == True:
                self.BackgroundInstanceScorescreen.region_surface_rect.x += self.settings.animation_speed
                self.BackgroundInstanceScorescreen.menu_button_rect.x += self.settings.animation_speed
                self.BackgroundInstanceScorescreen.left_arrow_rect.x += self.settings.animation_speed
                self.BackgroundInstanceScorescreen.right_arrow_rect.x += self.settings.animation_speed

            # Blit the score screen
            self.screen.blit(self.BackgroundInstanceScorescreen.region_surface, \
                            self.BackgroundInstanceScorescreen.region_surface_rect)
            self.screen.blit(self.BackgroundInstanceScorescreen.menu_button, \
                            self.BackgroundInstanceScorescreen.menu_button_rect)
            self.screen.blit(self.BackgroundInstanceScorescreen.left_arrow, \
                            self.BackgroundInstanceScorescreen.left_arrow_rect)
            self.screen.blit(self.BackgroundInstanceScorescreen.right_arrow, \
                            self.BackgroundInstanceScorescreen.right_arrow_rect)

            # Check if animation is over. If so, start the score screen. Reset to default at end
            self.animation_distance += self.settings.animation_speed
            if self.animation_distance >= self.settings.screen_width or self.settings.settings_save_dict['animations'] == False:
                self.animation_distance = 0
                self.BackgroundInstanceScorescreen._position_rects_default()    # Default score screen
                self.BackgroundInstanceScorescreen._push_right()                # Push scores to right
                self.BackgroundInstanceStart._position_rects_default()          # Default start screen
                self.MainInstance.start_screen = True
                self.MainInstance.scores_screen = False
                self.animation_running = False
                self.animation_scores_start = False

        # Check if start screen to settings screen
        elif self.animation_start_settings:

            # Move the start screen to the left
            if self.settings.settings_save_dict['animations'] == True:
                self.BackgroundInstanceStart.play_button_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceStart.settings_button_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceStart.score_button_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceStart.logo_image_rect.x -= self.settings.animation_speed

            # Blit the start screen
            self.BackgroundAndBaseInstance.draw_background()
            self.BackgroundAndBaseInstance.draw_base()
            self.screen.blit(self.BackgroundInstanceStart.play_button, \
                            self.BackgroundInstanceStart.play_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.settings_button, \
                            self.BackgroundInstanceStart.settings_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.score_button, \
                            self.BackgroundInstanceStart.score_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.logo_image, \
                            self.BackgroundInstanceStart.logo_image_rect)

            # Move the settings screen to the left
            if self.settings.settings_save_dict['animations'] == True:
                self.BackgroundInstanceSettings.region_surface_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceSettings.menu_button_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceSettings.reset_settings_button_rect.x -= self.settings.animation_speed
                self.BackgroundInstanceSettings.reset_data_button_rect.x -= self.settings.animation_speed

            # Blit the score screen
            self.screen.blit(self.BackgroundInstanceSettings.region_surface, \
                            self.BackgroundInstanceSettings.region_surface_rect)
            self.screen.blit(self.BackgroundInstanceSettings.menu_button, \
                            self.BackgroundInstanceSettings.menu_button_rect)
            self.screen.blit(self.BackgroundInstanceSettings.reset_settings_button, \
                            self.BackgroundInstanceSettings.reset_settings_button_rect)
            self.screen.blit(self.BackgroundInstanceSettings.reset_data_button, \
                            self.BackgroundInstanceSettings.reset_data_button_rect)

            # Check if animation is over. If so, start the settings screen. No reset of start screen.
            self.animation_distance += self.settings.animation_speed
            if self.animation_distance >= self.settings.screen_width or self.settings.settings_save_dict['animations'] == False:
                self.animation_distance = 0
                self.BackgroundInstanceSettings._position_rects_default()    # Default score screen
                self.MainInstance.start_screen = False
                self.MainInstance.settings_screen = True
                self.animation_running = False
                self.animation_start_settings = False

        # Check if settings screen to start screen
        elif self.animation_settings_start:

            # Force a stop for the reset button lights. (Gets overwritten either way by draw screen priority)
            self.BackgroundInstanceSettings.reset_settings_recent = False

            # Move the start screen to the right
            if self.settings.settings_save_dict['animations'] == True:
                self.BackgroundInstanceStart.play_button_rect.x += self.settings.animation_speed
                self.BackgroundInstanceStart.settings_button_rect.x += self.settings.animation_speed
                self.BackgroundInstanceStart.score_button_rect.x += self.settings.animation_speed
                self.BackgroundInstanceStart.logo_image_rect.x += self.settings.animation_speed

            # Blit the start screen
            self.BackgroundAndBaseInstance.draw_background()
            self.BackgroundAndBaseInstance.draw_base()
            self.screen.blit(self.BackgroundInstanceStart.play_button, \
                            self.BackgroundInstanceStart.play_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.settings_button, \
                            self.BackgroundInstanceStart.settings_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.score_button, \
                            self.BackgroundInstanceStart.score_button_rect)
            self.screen.blit(self.BackgroundInstanceStart.logo_image, \
                            self.BackgroundInstanceStart.logo_image_rect)

            # Move the settings screen to the right
            if self.settings.settings_save_dict['animations'] == True:
                self.BackgroundInstanceSettings.region_surface_rect.x += self.settings.animation_speed
                self.BackgroundInstanceSettings.menu_button_rect.x += self.settings.animation_speed
                self.BackgroundInstanceSettings.reset_settings_button_rect.x += self.settings.animation_speed
                self.BackgroundInstanceSettings.reset_data_button_rect.x += self.settings.animation_speed

            # Blit the score screen
            self.screen.blit(self.BackgroundInstanceSettings.region_surface, \
                            self.BackgroundInstanceSettings.region_surface_rect)
            self.screen.blit(self.BackgroundInstanceSettings.menu_button, \
                            self.BackgroundInstanceSettings.menu_button_rect)
            self.screen.blit(self.BackgroundInstanceSettings.reset_settings_button, \
                            self.BackgroundInstanceSettings.reset_settings_button_rect)
            self.screen.blit(self.BackgroundInstanceSettings.reset_data_button, \
                            self.BackgroundInstanceSettings.reset_data_button_rect)

            # Check if animation is over. If so, start the start screen.
            self.animation_distance += self.settings.animation_speed
            if self.animation_distance >= self.settings.screen_width or self.settings.settings_save_dict['animations'] == False:
                self.animation_distance = 0
                self.BackgroundInstanceSettings._position_rects_default()
                self.BackgroundInstanceSettings._push_right()
                self.BackgroundInstanceStart._position_rects_default()
                self.MainInstance.start_screen = True
                self.MainInstance.settings_screen = False
                self.animation_running = False
                self.animation_settings_start = False
