import pygame
import json

class FlappySettings:
    """Settings class for game. Contains functions for JSON saving."""

    def __init__(self):
        """Default values used in the game."""

        # Global values used in many screens
        self.screen_width = 400
        self.screen_height = 650
        self.fps = 30
        self.animation_speed = 6

        # Create the key map
        self.keybinds = {'space': pygame.K_SPACE, 'a': pygame.K_a, 'b': pygame.K_b, 'c': pygame.K_c,
                        'd': pygame.K_d, 'e': pygame.K_e, 'f': pygame.K_f, 'g': pygame.K_g, 'h': pygame.K_h,
                        'i': pygame.K_i, 'j': pygame.K_j, 'k': pygame.K_k, 'l': pygame.K_l, 'm': pygame.K_m,
                        'n': pygame.K_n, 'o': pygame.K_o, 'p': pygame.K_p, 'q': pygame.K_q, 'r': pygame.K_r,
                        's': pygame.K_s, 't': pygame.K_t, 'u': pygame.K_u, 'v': pygame.K_v, 'w': pygame.K_w,
                        'x': pygame.K_x, 'y': pygame.K_y, 'z': pygame.K_z}
        self.keybinds_number = {'0': pygame.K_0, '1': pygame.K_1, '2': pygame.K_2, '3': pygame.K_3, '4': pygame.K_4,
                                '5': pygame.K_5, '6': pygame.K_6, '7': pygame.K_7, '8': pygame.K_8, '9': pygame.K_9,
                                '.': pygame.K_PERIOD, 'backspace': pygame.K_BACKSPACE}

        # Loading the matches
        self._load_matches()

        # Loading the achivement
        self._load_achiv_scores()

        # Loading the previous settings
        self._load_saved_settings()

        # Loading the achievement settings
        self._achievements_settings()

        # For the start screen
        self._start_background_settings()

        # For the tutorial screen
        self._tutorial_background_settings()

        # For the game screen
        self._game_background_settings()

        # For the game over screen
        self._gameover_background_settings()

        # For the score screen
        self._score_background_settings()

        # For the settings screen
        self._settings_background_settings()

        # For the bird
        self._bird_settings()

        # For the dynamic scores reset
        self._reset_match_scores()


    def _load_matches(self):
        # Load the previous matches
        self.total_possible_match_saves = 3

        # Load the scores using JSON
        self.matches_file_location = r'Game_Data\match_data.json'
        try:
            with open(self.matches_file_location, 'r') as file_object:
                matches_object = json.load(file_object)
                self.matches_save_dict = matches_object

            # Json changes to string, change back to int
            self.fixed_dict = {}
            for i in range(1, 4):
                self.fixed_dict[i] = self.matches_save_dict[str(i)]
            self.matches_save_dict = self.fixed_dict

        # If data does not exist, create new dict
        except FileNotFoundError:
            self.matches_save_dict = {1: {'score': 0, 'time': 0, 'date': None},
                                      2: {'score': 0, 'time': 0, 'date': None},
                                      3: {'score': 0, 'time': 0, 'date': None}
                                      }


    def _load_achiv_scores(self):
        # Load the achiv data using json
        self.achiv_save_location = r'Game_Data\achiv_data.json'
        try:
            with open(self.achiv_save_location) as file_object:
                achiv_save_object = json.load(file_object)
                self.achiv_save_dict = achiv_save_object
        except FileNotFoundError:
            self.achiv_save_dict = {'jumps': 0,
                                    'deaths': 0,
                                    'score': 0,
                                    'total_sessions': 0,
                                    'play_time': 0,
                                    'distance_x': 0,
                                    'distance_y': 0,
                                    'NewPlayer_finished': False,
                                    'TheJumperI_finished': False,
                                    'TheExplorerI_finished': False,
                                    'TheBeginner_finished': False,
                                    'TheNovice_finished': False,
                                    'TheJumperII_finished': False,
                                    'ItHappens_finished': False,
                                    'Gravity_finished': False
                                    }


    def reset_saved_data(self):
        # Reset the data saved if called
        self.matches_save_dict = {1: {'score': 0, 'time': 0, 'date': None},
                                  2: {'score': 0, 'time': 0, 'date': None},
                                  3: {'score': 0, 'time': 0, 'date': None}
                                  }
        self.achiv_save_dict = {'jumps': 0,
                                'deaths': 0,
                                'score': 0,
                                'total_sessions': 0,
                                'play_time': 0,
                                'distance_x': 0,
                                'distance_y': 0,
                                'NewPlayer_finished': False,
                                'TheJumperI_finished': False,
                                'TheExplorerI_finished': False,
                                'TheBeginner_finished': False,
                                'TheNovice_finished': False,
                                'TheJumperII_finished': False,
                                'ItHappens_finished': False,
                                'Gravity_finished': False
                                }


    def _load_saved_settings(self):
        # Load the saved setting
        self.settings_save_location = r'Game_Data\settings_data.json'
        try:
            with open(self.settings_save_location) as file_object:
                settings_data = json.load(file_object)
                self.settings_save_dict = settings_data
        except FileNotFoundError:
            self.reset_saved_settings()


    def reset_saved_settings(self):
        # Reset the settings saved if called
        self.settings_save_dict = {'hitbox': 'default', 'jump': 'space', 'gravity': 0.3,
                                   'animations': True, 'achievements': True, 'bird_color': 'yellow'}


    def _save_all_items(self):
        # Save all the variables

        # First file (matches)
        file = open(self.matches_file_location, 'w')
        json.dump(self.matches_save_dict, file)
        file.close()

        # Second file (achievements)
        file = open(self.achiv_save_location, 'w')
        json.dump(self.achiv_save_dict, file)
        file.close()

        # Third file (settings)
        file = open(self.settings_save_location, 'w')
        json.dump(self.settings_save_dict, file)
        file.close()


    def _achievements_settings(self):
        # Settings for the achievements that pop down
        self.width_achievements = 150
        self.height_achievements = 50
        self.achievement_speed = 1          # Speed drops down
        self.achievement_duration = 3       # In seconds ; duration on screen


    def _start_background_settings(self):
        # Settings for start screen
        self.button_width_start = round(self.screen_width * 0.3125)         # 125
        self.button_height_start = round(self.screen_height * 0.0769)       # 50
        self.button_gap_start = 40
        self.button_expansion_rate_start = .25
        self.logo_width_start = round(self.screen_width * 0.3125 * 2.5)
        self.logo_height_start = round(self.screen_height * 0.0769 * 2)
        self.logo_gap_start = 50


    def _tutorial_background_settings(self):
        # Settings for tutorial screen
        self.tutorial_font = pygame.font.Font(r'Images\Buttons\FSEX300.ttf', 40)
        self.tutorial_font_color = (0, 0, 0)
        self.tutorial_bird_oscillation = 30
        self.tutorial_bird_speed = 3


    def _game_background_settings(self):
        # Settings for game screen
        self.game_speed = 5
        self.pipe_gap = 150                 # Distance between top and bot pipe
        self.pipe_distance_between = 275    # Distance between pipes
        self.pipe_width = 52
        self.pipe_distance_border = 40      # Distance between pipe and top or bot border
        self.scoreboard_gap = 10


    def _gameover_background_settings(self):
        # Settings for gameover screen

        # For the logo at top
        self.logo_width_gameover = 313
        self.logo_height_gameover = 75

        # For the medals
        self.medal_width = 75
        self.medal_height = 75
        self.side_gap = 51
        self.top_gap = 40
        self.top_medal_title = 20
        self.bronze_requirement = 10
        self.silver_requirement = 25
        self.gold_requirement = 40

        # For the buttons
        self.button_width_gameover = round(self.screen_width * 0.3125)
        self.button_height_gameover = round(self.screen_height * 0.0769)
        self.button_expansion_rate_gameover = .25
        self.button_gap_gameover = 40

        # For the region
        self.surface_height_gameover = 250       # For info surface
        self.gameover_font = pygame.font.Font(r'Images\Buttons\FSEX300.ttf', 30)
        self.gameover_font_color = (255, 127, 39)
        self.gameover_font_info = pygame.font.Font(r'Images\Buttons\FSEX300.ttf', 22)
        self.gameover_font_info_color = (0, 0, 0)
        self.info_screen_text_gap_gameover = 20
        self.number_gap_gameover = 5
        self.ratio_score_gameover = .6

        # For the info below the region
        self.gameover_gap_from_side = 10
        self.gameover_gap_from_bottom = 10
        self.gameover_gap_between = 5


    def _score_background_settings(self):
        # Settings for the score screen
        self.region_side_gap = 40
        self.button_width_score = round(self.screen_width * 0.3125)
        self.button_height_score = round(self.screen_height * 0.0769)
        self.button_expansion_rate_score = .25
        self.button_base_gap_score = 20
        self.arrow_gap_score = 20


    def _settings_background_settings(self):
        # Settings for background of settings
        self.button_width_settings = round(self.screen_width * 0.3125)
        self.button_height_settings = round(self.screen_height * 0.0769)
        self.button_gap_settings = 20
        self.button_expansion_rate_settings = .20

        # For smaller buttons
        self.button_width_smaller_settings = 100
        self.button_height_smaller_settings = 50
        self.button_light_delay = 1

        # For the region
        self.region_height_settings = 460
        self.region_side_gap_settings = 40

        # For the region texts
        self.settings_font_info = pygame.font.Font(r'Images\Buttons\FSEX300.ttf', 22)
        self.settings_font_info_color = (0, 0, 0)
        self.settings_font_options = pygame.font.Font(r'Images\Buttons\FSEX300.ttf', 16)
        self.settings_font_options_color = (0, 0, 0)
        self.settings_font_options_color_on = (127, 255, 0)

        # For the region options
        self.settings_x_gap = 20
        self.settings_y_gap = 15
        self.settings_y_gap_big = 30

        # For the key rebind
        self.rebind_surface_width = 75
        self.rebind_surface_height = 25
        self.region_outline_color = (255,165,0)
        self.rebind_key_surface_color = (211,211,211)

        # For the on and off button
        self.settings_circle_thickness = 4
        self.settings_text_color_fill = (0,255,0)
        self.settings_text_color_orange = (255,69,0)


    def _bird_settings(self):
        # Settings for the bird
        self.jump_power = 5
        self.max_angle = 30             # For single jump rotation
        self.rotation_angle = 2

        # For the distance travelled
        self.distance_travel_factor_x = 0.03
        self.distance_travel_factor_y = 0.03


    def _reset_match_scores(self):
        # Dynamic scores
        self.dynamic_score = 0      # Score for a match
        self.start_time = 0         # Starts when tutorial ends
        self.end_time = 0           # Ends when collision occurs
        self.jumps = 0
        self.distance_x = 0
        self.distance_y = 0

