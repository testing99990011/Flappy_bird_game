import pygame

class FlappyBackgroundGameoverscreen:
    """Background for game over screen"""

    def __init__(self, BackgroundInstanceLogic, MainInstance):
        """Default values used for game over screen"""
        self.BackgroundInstanceLogic = BackgroundInstanceLogic
        self.MainInstance = MainInstance
        self.screen = self.MainInstance.screen
        self.settings = self.MainInstance.settings

        # For the medals
        self.default_medal = pygame.image.load('Images/Driver/default_medal.PNG').convert()
        self.bronze_medal = pygame.image.load('Images/Driver/bronze_medal.PNG').convert()
        self.silver_medal = pygame.image.load('Images/Driver/silver_medal.PNG').convert()
        self.gold_medal = pygame.image.load('Images/Driver/gold_medal.PNG').convert()
        self.default_medal.set_colorkey((255, 255, 255))
        self.bronze_medal.set_colorkey((255, 255, 255))
        self.silver_medal.set_colorkey((255, 255, 255))
        self.gold_medal.set_colorkey((255, 255, 255))
        self.default_medal = pygame.transform.scale(self.default_medal, \
            (self.settings.medal_width, self.settings.medal_height))
        self.bronze_medal = pygame.transform.scale(self.bronze_medal, \
            (self.settings.medal_width, self.settings.medal_height))
        self.silver_medal = pygame.transform.scale(self.silver_medal, \
            (self.settings.medal_width, self.settings.medal_height))
        self.gold_medal = pygame.transform.scale(self.gold_medal, \
            (self.settings.medal_width, self.settings.medal_height))

        # For the logo game over
        self.game_over_logo = pygame.image.load('Images/Driver/gameover.png')
        self.game_over_logo = pygame.transform.scale(self.game_over_logo, \
            (self.settings.logo_width_gameover, self.settings.logo_height_gameover))
        self.game_over_logo_rect = self.game_over_logo.get_rect()
        self.game_over_logo_rect.center = self.BackgroundInstanceLogic.BackgroundInstanceStart.logo_image_rect.center

        # For the restart game
        self.restart_button = pygame.image.load('Images/Buttons/restart.png').convert()
        self.restart_button.set_colorkey((255, 255, 255))
        self.restart_button = pygame.transform.scale(self.restart_button, \
            (self.settings.button_width_gameover, self.settings.button_height_gameover))
        self.restart_button_rect = self.restart_button.get_rect()
        self.restart_button_rect.x = self.settings.button_gap_gameover
        self.restart_button_rect.y = self.settings.screen_height - \
            self.BackgroundInstanceLogic.BackgroundAndBaseInstance.base_rect.height - \
            self.settings.button_gap_gameover - self.restart_button_rect.height

        # For the menu button
        self.menu_button = pygame.image.load('Images/Buttons/menu.png').convert()
        self.menu_button.set_colorkey((255, 255, 255))
        self.menu_button = pygame.transform.scale(self.menu_button, \
            (self.settings.button_width_gameover, self.settings.button_height_gameover))
        self.menu_button_rect = self.menu_button.get_rect()
        self.menu_button_rect.x = self.settings.screen_width - self.menu_button_rect.width - \
            self.settings.button_gap_gameover
        self.menu_button_rect.y = self.settings.screen_height - \
            self.BackgroundInstanceLogic.BackgroundAndBaseInstance.base_rect.height - \
            self.settings.button_gap_gameover - self.restart_button_rect.height

        # For the restart button highlight
        self.restart_button_highlight = pygame.image.load('Images/Buttons/restart.png').convert()
        self.restart_button_highlight.set_colorkey((255, 255, 255))
        self.restart_button_highlight = pygame.transform.scale(self.restart_button_highlight, \
            (int(self.settings.button_width_gameover * (1 + self.settings.button_expansion_rate_gameover)),\
            int(self.settings.button_height_gameover * (1 + self.settings.button_expansion_rate_gameover)))
            )
        self.restart_button_highlight_rect = self.restart_button_highlight.get_rect()
        self.restart_button_highlight_rect.center = self.restart_button_rect.center

        # For the menu button highlight
        self.menu_button_highlight = pygame.image.load('Images/Buttons/menu.png').convert()
        self.menu_button_highlight.set_colorkey((255, 255, 255))
        self.menu_button_highlight = pygame.transform.scale(self.menu_button_highlight, \
            (int(self.settings.button_width_gameover * (1 + self.settings.button_expansion_rate_gameover)),\
            int(self.settings.button_height_gameover * (1 + self.settings.button_expansion_rate_gameover)))
            )
        self.menu_button_highlight_rect = self.menu_button_highlight.get_rect()
        self.menu_button_highlight_rect.center = self.menu_button_rect.center

        # Flags for dynamic highlighting
        self.restart_button_highlighted = False
        self.menu_button_highlighted = False

        # For the region
        self.region_image = pygame.image.load('Images/Driver/region.png').convert()
        self.region_image.set_colorkey((255, 255, 255))

        # For the fonts used
        self.font_info = self.settings.gameover_font
        self.text_color_info = self.settings.gameover_font_color
        self.font_data = self.settings.gameover_font_info
        self.font_data_color = self.settings.gameover_font_info_color


    def _create_region(self):
        # Create region for gameover screen
        self.region_surface = pygame.Surface(
            ((self.menu_button_rect.right - self.restart_button_rect.x),
            (self.settings.surface_height_gameover)),
            pygame.SRCALPHA)

        # Surface region rect
        self.region_surface_rect = self.region_surface.get_rect()
        self.region_surface_rect.x = self.restart_button_rect.x
        self.region_surface_rect.bottom = (self.restart_button_rect.top - self.settings.button_gap_gameover)

        # Background overlay
        self.region_image = pygame.transform.scale(self.region_image, \
            (self.region_surface_rect.width, self.region_surface_rect.height))
        self.region_surface.blit(self.region_image, self.region_image.get_rect())

        # Text for Score (Static)
        self.current_score_text = self.font_info.render("Score", True, self.text_color_info)
        self.current_score_text_rect = self.current_score_text.get_rect()
        self.current_score_text_rect.right = self.region_surface_rect.width - \
            self.settings.info_screen_text_gap_gameover
        self.current_score_text_rect.y = self.settings.info_screen_text_gap_gameover
        self.region_surface.blit(self.current_score_text, self.current_score_text_rect)

        # Text for top score (Static)
        self.top_score_text = self.font_info.render("Most", True, self.text_color_info)
        self.top_score_text_rect = self.top_score_text.get_rect()
        self.top_score_text_rect.right = self.current_score_text_rect.right
        self.top_score_text_rect.y = self.current_score_text_rect.bottom + self.settings.info_screen_text_gap_gameover * 2
        self.region_surface.blit(self.top_score_text, self.top_score_text_rect)

        # Text next to top score if its a new top score
        if self.settings.dynamic_score > self.settings.matches_save_dict[1]['score']:
            self.new_top_score_text = pygame.font.Font(None, 20).render("New!", True, (255,0,0))
            self.new_top_score_text_rect = self.new_top_score_text.get_rect()
            self.new_top_score_text_rect.right = self.top_score_text_rect.left - self.settings.number_gap_gameover
            self.new_top_score_text_rect.center = (self.new_top_score_text_rect.center[0], \
                self.top_score_text_rect.center[1])
            self.region_surface.blit(self.new_top_score_text, self.new_top_score_text_rect)

        # Text for the time (Static)
        self.current_time_text = self.font_info.render("Time", True, self.text_color_info)
        self.current_time_text_rect = self.current_time_text.get_rect()
        self.current_time_text_rect.right = self.current_score_text_rect.right
        self.current_time_text_rect.y = self.top_score_text_rect.bottom + self.settings.info_screen_text_gap_gameover * 2
        self.region_surface.blit(self.current_time_text, self.current_time_text_rect)

        # Text title for medal (Static)
        self.medal_title_text = self.font_info.render("MEDAL", True, self.text_color_info)
        self.medal_title_text_rect = self.medal_title_text.get_rect()
        self.medal_title_text_rect.top = self.settings.top_medal_title
        self.medal_title_text_rect.center = (self.settings.medal_width/2 + self.settings.side_gap), self.medal_title_text_rect.y
        self.region_surface.blit(self.medal_title_text, self.medal_title_text_rect)

        # Text for info below medal. Draw text from bottom upward with y, x, jumps. (Static)
        self.distance_y_text = self.font_data.render('Distance Y:', True, self.font_data_color)
        self.distance_x_text = self.font_data.render('Distance X:', True, self.font_data_color)
        self.jumps_match_text = self.font_data.render("Jumps:", True, self.font_data_color)
        self.distance_y_text_rect = self.distance_y_text.get_rect()
        self.distance_y_text_rect.x = self.settings.gameover_gap_from_side
        self.distance_y_text_rect.bottom = (self.settings.surface_height_gameover - self.settings.gameover_gap_from_bottom)
        self.distance_x_text_rect = self.distance_x_text.get_rect()
        self.distance_x_text_rect.right = self.distance_y_text_rect.right
        self.distance_x_text_rect.bottom = self.distance_y_text_rect.top - self.settings.gameover_gap_between
        self.jumps_match_text_rect = self.jumps_match_text.get_rect()
        self.jumps_match_text_rect.right = self.distance_y_text_rect.right
        self.jumps_match_text_rect.bottom = self.distance_x_text_rect.top - self.settings.gameover_gap_between
        self.region_surface.blit(self.distance_y_text, self.distance_y_text_rect)
        self.region_surface.blit(self.distance_x_text, self.distance_x_text_rect)
        self.region_surface.blit(self.jumps_match_text, self.jumps_match_text_rect)

        # Text for current score (Dynamic)
        self.current_score_data = self._return_score_surface(self.settings.dynamic_score)
        self.current_score_data_rect = self.current_score_data.get_rect()
        self.current_score_data_rect.right = self.current_score_text_rect.right
        self.current_score_data_rect.center = (self.current_score_data_rect.center[0], \
            self.current_score_text_rect.bottom + self.settings.info_screen_text_gap_gameover)
        self.region_surface.blit(self.current_score_data, self.current_score_data_rect)

        # Text for the top score (Dynamic)
        if self.settings.dynamic_score > self.settings.matches_save_dict[1]['score']:
            self.top_score_data = self._return_score_surface(self.settings.dynamic_score)
        else:
            self.top_score_data = self._return_score_surface(self.settings.matches_save_dict[1]['score'])
        self.top_score_data_rect = self.top_score_data.get_rect()
        self.top_score_data_rect.right = self.current_score_text_rect.right
        self.top_score_data_rect.center = (self.top_score_data_rect.center[0], \
            self.top_score_text_rect.bottom + self.settings.info_screen_text_gap_gameover)
        self.region_surface.blit(self.top_score_data, self.top_score_data_rect)

        # Text for the timer (Dynamic)
        self.current_time_data = self.font_data.render(self._convert_sec_to_normal(), True, self.font_data_color)
        self.current_time_data_rect = self.current_time_data.get_rect()
        self.current_time_data_rect.right = self.current_score_text_rect.right
        self.current_time_data_rect.center = (self.current_time_data_rect.center[0], \
            self.current_time_text_rect.bottom + self.settings.info_screen_text_gap_gameover)
        self.region_surface.blit(self.current_time_data, self.current_time_data_rect)

        # Data for info below medal. Draw data text from bottom upward with y, x, jumps. (Dynamic)
        self.distance_y_data = self.font_data.render(str(int(self.settings.distance_y)), True, self.font_data_color)
        self.distance_x_data =  self.font_data.render(str(int(self.settings.distance_x)), True, self.font_data_color)
        self.jumps_data = self.font_data.render(str(self.settings.jumps), True, self.font_data_color)
        self.distance_y_data_rect = self.distance_y_data.get_rect()
        self.distance_y_data_rect.left = self.distance_y_text_rect.right + self.settings.gameover_gap_between
        self.distance_y_data_rect.bottom = self.distance_y_text_rect.bottom
        self.distance_x_data_rect = self.distance_x_data.get_rect()
        self.distance_x_data_rect.left = self.distance_y_text_rect.right + self.settings.gameover_gap_between
        self.distance_x_data_rect.bottom = self.distance_x_text_rect.bottom
        self.jumps_data_rect = self.jumps_data.get_rect()
        self.jumps_data_rect.left = self.distance_y_text_rect.right + self.settings.gameover_gap_between
        self.jumps_data_rect.bottom = self.jumps_match_text_rect.bottom
        self.region_surface.blit(self.distance_y_data, self.distance_y_data_rect)
        self.region_surface.blit(self.distance_x_data, self.distance_x_data_rect)
        self.region_surface.blit(self.jumps_data, self.jumps_data_rect)

        # Rects for the medals
        self.default_medal_rect = self.default_medal.get_rect()
        self.default_medal_rect.x = self.settings.side_gap
        self.default_medal_rect.y = self.settings.top_gap
        self.bronze_medal_rect = self.default_medal_rect.copy()
        self.silver_medal_rect = self.default_medal_rect.copy()
        self.gold_medal_rect = self.default_medal_rect.copy()

        # Blit the correct medal
        if self.settings.dynamic_score >= self.settings.gold_requirement:
            self.region_surface.blit(self.gold_medal, self.gold_medal_rect)
        elif self.settings.gold_requirement > self.settings.dynamic_score >= self.settings.silver_requirement:
            self.region_surface.blit(self.silver_medal, self.silver_medal_rect)
        elif self.settings.silver_requirement > self.settings.dynamic_score >= self.settings.bronze_requirement:
            self.region_surface.blit(self.bronze_medal, self.bronze_medal_rect)
        else:
            self.region_surface.blit(self.default_medal, self.default_medal_rect)


    def _convert_sec_to_normal(self):
        # Convert the seconds played to a min, sec format
        total_seconds = (self.settings.end_time - self.settings.start_time)/1000
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds - (minutes * 60))
        time_string = f"{minutes}m {seconds}s"
        return time_string


    def _return_score_surface(self, score):
        # Returns a surface with score

        # Use the reference rect of a number from scoreboard to create the surface
        self.reference_rect = self.BackgroundInstanceLogic.BackgroundInstanceGame.scoreboard.basic_rect.copy()
        self.reference_surface = pygame.Surface(\
            ((self.reference_rect.width + self.settings.number_gap_gameover) * len(str(score)),
            self.reference_rect.height), \
            pygame.SRCALPHA)

        # Add the numbers to the surface
        for iteration, value in enumerate(str(score)):
            self.number = self.BackgroundInstanceLogic.BackgroundInstanceGame.scoreboard.score_dict[int(value)]
            self.reference_rect.x = iteration * (self.reference_rect.width + self.settings.number_gap_gameover)
            self.reference_surface.blit(self.number, self.reference_rect)

        # Scale the surface to fit into the info screen
        self.reference_surface_rect_width, self.reference_surface_rect_height = self.reference_surface.get_rect().size
        self.reference_surface_final = pygame.transform.smoothscale(self.reference_surface, \
            (int(self.reference_surface_rect_width * self.settings.ratio_score_gameover),\
            int(self.reference_surface_rect_height * self.settings.ratio_score_gameover)))
        return self.reference_surface_final


    def _draw_highlights(self):
        # Draw the highlights
        mouse = pygame.mouse.get_pos()

        # Check if collision between mouse and restart button
        if self.restart_button_rect.collidepoint(mouse) or \
            self.restart_button_highlight_rect.collidepoint(mouse) and self.restart_button_highlighted:
                self.screen.blit(self.restart_button_highlight, self.restart_button_highlight_rect)
                self.restart_button_highlighted = True
        else:
            self.restart_button_highlighted = False

        # Check the collision between mouse and menu button
        if self.menu_button_rect.collidepoint(mouse) or \
            self.menu_button_highlight_rect.collidepoint(mouse) and self.menu_button_highlighted:
                self.screen.blit(self.menu_button_highlight, self.menu_button_highlight_rect)
                self.menu_button_highlighted = True
        else:
            self.menu_button_highlighted = False


    def draw_gameover_background(self):
        # Draw the gameover screen. Draw background from GameInstance
        self.BackgroundInstanceLogic.BackgroundAndBaseInstance.draw_background()
        self.BackgroundInstanceLogic.BackgroundAndBaseInstance.draw_base()
        self.screen.blit(self.game_over_logo, self.game_over_logo_rect)

        # Draw the button
        self.screen.blit(self.restart_button, self.restart_button_rect)
        self.screen.blit(self.menu_button, self.menu_button_rect)

        # Draw the info screen
        self.screen.blit(self.region_surface, self.region_surface_rect)

        # Logic for highlights
        self._draw_highlights()
