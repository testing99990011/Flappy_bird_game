import pygame

class FlappyBackgroundSettings:
    """Background for settings screen."""

    def __init__(self, BackgroundInstanceLogic, MainInstance):
        """Default values used in instance."""
        self.BackgroundInstanceLogic = BackgroundInstanceLogic
        self.MainInstance = MainInstance
        self.screen = self.MainInstance.screen
        self.settings = self.MainInstance.settings

        # For the menu button
        self.menu_button = pygame.image.load('Images/Buttons/menu.png').convert()
        self.menu_button.set_colorkey((255, 255, 255))
        self.menu_button = pygame.transform.scale(self.menu_button, \
            (self.settings.button_width_settings, self.settings.button_height_settings))
        self.menu_button_rect = self.menu_button.get_rect()

        # For the reset settings button
        self.reset_settings_button = pygame.image.load('Images/Buttons/settings_reset_off.PNG').convert()
        self.reset_settings_button.set_colorkey((255, 255, 255))
        self.reset_settings_button = pygame.transform.scale(self.reset_settings_button, \
            (self.settings.button_width_smaller_settings, self.settings.button_height_smaller_settings))
        self.reset_settings_button_rect = self.reset_settings_button.get_rect()

        # For the reset data button
        self.reset_data_button = pygame.image.load('Images/Buttons/data_reset_off.PNG').convert()
        self.reset_data_button.set_colorkey((255, 255, 255))
        self.reset_data_button = pygame.transform.scale(self.reset_data_button, \
            (self.settings.button_width_smaller_settings, self.settings.button_height_smaller_settings))
        self.reset_data_button_rect = self.reset_data_button.get_rect()

        # For the menu button highlight
        self.menu_button_highlight = pygame.image.load('Images/Buttons/menu.PNG').convert()
        self.menu_button_highlight.set_colorkey((255, 255, 255))
        self.menu_button_highlight = pygame.transform.scale(self.menu_button_highlight, \
            (int(self.settings.button_width_settings * (1+self.settings.button_expansion_rate_settings)), \
            int(self.settings.button_height_settings * (1+self.settings.button_expansion_rate_settings))))
        self.menu_button_highlight_rect = self.menu_button_highlight.get_rect()

        # For the reset settings button highlight
        self.reset_settings_button_highlight = pygame.image.load('Images/Buttons/settings_reset_off.PNG').convert()
        self.reset_settings_button_highlight.set_colorkey((255, 255, 255))
        self.reset_settings_button_highlight = pygame.transform.scale(self.reset_settings_button_highlight, \
            (int(self.settings.button_width_smaller_settings * (1+self.settings.button_expansion_rate_settings)), \
            int(self.settings.button_height_smaller_settings * (1+self.settings.button_expansion_rate_settings))))
        self.reset_settings_button_highlight_rect = self.reset_settings_button_highlight.get_rect()

        # For the reset data button highlight
        self.reset_data_button_highlight = pygame.image.load('Images/Buttons/data_reset_off.PNG').convert()
        self.reset_data_button_highlight.set_colorkey((255, 255, 255))
        self.reset_data_button_highlight = pygame.transform.scale(self.reset_data_button_highlight, \
            (int(self.settings.button_width_smaller_settings * (1+self.settings.button_expansion_rate_settings)), \
            int(self.settings.button_height_smaller_settings * (1+self.settings.button_expansion_rate_settings))))
        self.reset_data_button_highlight_rect = self.reset_data_button_highlight.get_rect()

        # For the reset settings button light
        self.reset_settings_button_light = pygame.image.load('Images/Buttons/settings_restart_on.PNG').convert()
        self.reset_settings_button_light.set_colorkey((255, 255, 255))
        self.reset_settings_button_light = pygame.transform.scale(self.reset_settings_button_light, \
            (self.settings.button_width_smaller_settings, self.settings.button_height_smaller_settings))

        # For the reset data button light
        self.reset_data_button_light = pygame.image.load('Images/Buttons/data_restart_on.PNG').convert()
        self.reset_data_button_light.set_colorkey((255, 255, 255))
        self.reset_data_button_light = pygame.transform.scale(self.reset_data_button_light, \
            (self.settings.button_width_smaller_settings, self.settings.button_height_smaller_settings))

        # For the reset key button popup
        self.reset_key_surface = pygame.Surface((self.settings.screen_width, self.settings.screen_height))
        self.reset_key_surface.set_alpha(200)
        self.reset_key_surface_text = self.settings.settings_font_info.render("Press any Key", True,
            self.settings.rebind_key_surface_color)
        self.reset_key_surface_text_rect = self.reset_key_surface_text.get_rect()
        self.reset_key_surface_text_rect.center = self.MainInstance.screen.get_rect().center

        # For the on and off button rects
        self.reference_height = self.settings.settings_font_info.render("O", True,
            self.settings.settings_font_options_color)
        self.reference_height_rect = self.reference_height.get_rect().height
        self.circle_center = (self.reference_height_rect//2, self.reference_height_rect//2)
        self.circle_radius = self.reference_height_rect//2
        self.circle_width = self.settings.settings_circle_thickness

        # Load the on button
        self.on_button = pygame.Surface((self.reference_height_rect, self.reference_height_rect), \
         pygame.SRCALPHA, 32)
        self.on_button = self.on_button.convert_alpha()
        pygame.draw.circle(self.on_button, self.settings.settings_font_options_color, \
         self.circle_center, self.circle_radius, self.circle_width)
        pygame.draw.circle(self.on_button, self.settings.settings_text_color_fill, \
         self.circle_center, self.circle_radius - self.circle_width)

        # Load the orange button
        self.orange_button = pygame.Surface((self.reference_height_rect, self.reference_height_rect), \
         pygame.SRCALPHA, 32)
        self.orange_button = self.orange_button.convert_alpha()
        pygame.draw.circle(self.orange_button, self.settings.settings_text_color_orange, \
         self.circle_center, self.circle_radius//2)

        # Load the off button
        self.off_button = pygame.Surface((self.reference_height_rect, self.reference_height_rect), \
         pygame.SRCALPHA, 32)
        self.off_button = self.off_button.convert_alpha()
        pygame.draw.circle(self.off_button, self.settings.settings_font_options_color, \
         self.circle_center, self.circle_radius, self.circle_width)
        self.button_rect = self.on_button.get_rect()

        # Flags for dynamic highlighting
        self.menu_button_highlighted = False
        self.reset_settings_button_highlighted = False
        self.reset_data_button_highlighted = False

        # Flags for resets
        self.reset_settings_recent = False
        self.reset_data_recent = False
        self.reset_keybind_recent = False
        self.reset_gravity_recent = False

        # Create the region and push to right
        self._create_region()
        self._position_rects_default()
        self._push_right()


    def _create_region(self):
        # Create region
        self.region_surface = pygame.Surface(
            ((self.settings.screen_width - self.settings.region_side_gap_settings * 2),
            (self.settings.region_height_settings)),
            pygame.SRCALPHA)

        # Region position
        self.region_surface_rect = self.region_surface.get_rect()
        self.region_surface_rect.right = self.settings.screen_width - self.settings.region_side_gap_settings
        self.region_surface_rect.y = self.settings.region_side_gap_settings

        # Blit the background onto the region
        self.region_image_background = pygame.image.load('Images/Driver/region.PNG').convert()
        self.region_image_background.set_colorkey((255, 255, 255))
        self.region_image_background = pygame.transform.scale(self.region_image_background, \
            (self.region_surface_rect.width, self.region_surface_rect.height))
        self.region_surface.blit(self.region_image_background, (0, 0))

        # First setting for dynamic hitbox
        self.hitbox_text = self.settings.settings_font_info.render("Hitbox Type:", True, \
            self.settings.settings_font_info_color)
        self.hitbox_text_rect = self.hitbox_text.get_rect()
        self.hitbox_text_rect.x = self.settings.settings_x_gap
        self.hitbox_text_rect.top = self.settings.settings_x_gap
        self.region_surface.blit(self.hitbox_text, self.hitbox_text_rect)

        # First option for default hitbox
        self.hitbox_default_off = self.settings.settings_font_options.render("Default", True, \
            self.settings.settings_font_options_color)
        self.hitbox_default_on = self.settings.settings_font_options.render("Default", True, \
            self.settings.settings_font_options_color_on)
        self.hitbox_default_rect = self.hitbox_default_off.get_rect()
        self.hitbox_default_rect.x = self.hitbox_text_rect.right + self.settings.settings_x_gap
        self.hitbox_default_rect.bottom = self.hitbox_text_rect.bottom

        # Second option for default box
        self.hitbox_default_box_off = self.settings.settings_font_options.render("Default Box", True, \
            self.settings.settings_font_options_color)
        self.hitbox_default_box_on = self.settings.settings_font_options.render("Default Box", True, \
            self.settings.settings_font_options_color_on)
        self.hitbox_default_box_rect = self.hitbox_default_box_off.get_rect()
        self.hitbox_default_box_rect.left = self.hitbox_default_rect.left
        self.hitbox_default_box_rect.top = self.hitbox_default_rect.bottom + self.settings.settings_y_gap

        # Third option for adaptive box
        self.hitbox_adaptive_off = self.settings.settings_font_options.render("Transform Box", True, \
            self.settings.settings_font_options_color)
        self.hitbox_adaptive_on = self.settings.settings_font_options.render("Transform Box", True, \
            self.settings.settings_font_options_color_on)
        self.hitbox_adaptive_rect = self.hitbox_adaptive_off.get_rect()
        self.hitbox_adaptive_rect.left = self.hitbox_default_rect.left
        self.hitbox_adaptive_rect.top = self.hitbox_default_box_rect.bottom + self.settings.settings_y_gap

        # Dict for hitbox options
        self.hitbox_options = \
            {'default': {'off': self.hitbox_default_off, 'on': self.hitbox_default_on, 'rect': self.hitbox_default_rect},\
            'default_box': {'off': self.hitbox_default_box_off, 'on': self.hitbox_default_box_on, 'rect': self.hitbox_default_box_rect},\
            'hitbox_adaptive': {'off': self.hitbox_adaptive_off, 'on': self.hitbox_adaptive_on, 'rect': self.hitbox_adaptive_rect}
            }

        # Blit the hitbox option with corresponding value
        for key, value in self.hitbox_options.items():
            if key == self.settings.settings_save_dict['hitbox']:
                self.region_surface.blit(self.hitbox_options[key]['on'], self.hitbox_options[key]['rect'])
            else:
                self.region_surface.blit(self.hitbox_options[key]['off'], self.hitbox_options[key]['rect'])

        # For key rebind text
        self.rebind_jump_text = self.settings.settings_font_info.render("Jump Keybind:", True, \
            self.settings.settings_font_info_color)
        self.rebind_jump_text_rect = self.rebind_jump_text.get_rect()
        self.rebind_jump_text_rect.right = self.hitbox_text_rect.right
        self.rebind_jump_text_rect.top = self.hitbox_adaptive_rect.bottom + self.settings.settings_y_gap_big
        self.region_surface.blit(self.rebind_jump_text, self.rebind_jump_text_rect)

        # For the key rebind option
        self.key_rebind_surface = pygame.Surface(
            (self.settings.rebind_surface_width,
            self.settings.rebind_surface_height),
            pygame.SRCALPHA)
        pygame.draw.rect(self.key_rebind_surface, self.settings.region_outline_color,
            (0, 0, self.settings.rebind_surface_width, self.settings.rebind_surface_height), 1)
        self.key_rebind_surface_rect = self.key_rebind_surface.get_rect()

        # Blit the key rebind (no key if currently in rebind mode)
        if not self.reset_keybind_recent:
            self.rebind_current_key_text = self.settings.settings_font_options.render(self.settings.settings_save_dict['jump'], True,
                self.settings.settings_font_options_color)
            self.rebind_current_key_text_rect = self.rebind_current_key_text.get_rect()
            self.rebind_current_key_text_rect.center = self.key_rebind_surface_rect.center
            self.key_rebind_surface.blit(self.rebind_current_key_text, self.rebind_current_key_text_rect)
        self.key_rebind_surface_rect.left = self.rebind_jump_text_rect.right + self.settings.settings_x_gap
        self.key_rebind_surface_rect.top = self.rebind_jump_text_rect.top
        self.region_surface.blit(self.key_rebind_surface, self.key_rebind_surface_rect)

        # For the gravity change text
        self.change_gravity_text = self.settings.settings_font_info.render('Gravity:', True,
            self.settings.settings_font_options_color)
        self.change_gravity_text_rect = self.change_gravity_text.get_rect()
        self.change_gravity_text_rect.right = self.hitbox_text_rect.right
        self.change_gravity_text_rect.top = self.rebind_jump_text_rect.bottom + self.settings.settings_y_gap_big
        self.region_surface.blit(self.change_gravity_text, self.change_gravity_text_rect)

        # For the gravity rebind option
        self.gravity_rebind_surface = pygame.Surface(
            (self.settings.rebind_surface_width,
            self.settings.rebind_surface_height),
            pygame.SRCALPHA)
        pygame.draw.rect(self.gravity_rebind_surface, self.settings.region_outline_color,
            (0, 0, self.settings.rebind_surface_width, self.settings.rebind_surface_height), 1)
        self.gravity_rebind_surface_rect = self.gravity_rebind_surface.get_rect()

        # Blit the gravity rebind option
        self.reset_gravity_value = self.settings.settings_font_options.render(str(self.settings.settings_save_dict['gravity']), True,
            self.settings.settings_font_options_color)
        self.reset_gravity_value_rect = self.reset_gravity_value.get_rect()
        self.reset_gravity_value_rect.center = self.gravity_rebind_surface_rect.center
        self.gravity_rebind_surface.blit(self.reset_gravity_value, self.reset_gravity_value_rect)
        self.gravity_rebind_surface_rect.left = self.change_gravity_text_rect.right + self.settings.settings_x_gap
        self.gravity_rebind_surface_rect.top = self.change_gravity_text_rect.top
        self.region_surface.blit(self.gravity_rebind_surface, self.gravity_rebind_surface_rect)

        # Draw the light for gravity reset
        if self.reset_gravity_recent:
            self.gravity_light_rect = self.button_rect.copy()
            self.gravity_light_rect.left = self.gravity_rebind_surface_rect.right + self.settings.settings_x_gap
            self.gravity_light_rect.center = (self.gravity_light_rect.center[0], self.gravity_rebind_surface_rect.center[1])
            self.region_surface.blit(self.orange_button, self.gravity_light_rect)

        # For the animation option text
        self.animation_option_text = self.settings.settings_font_info.render("Animations:", True,
            self.settings.settings_font_info_color)
        self.animation_option_text_rect = self.animation_option_text.get_rect()
        self.animation_option_text_rect.right = self.hitbox_text_rect.right
        self.animation_option_text_rect.top = self.change_gravity_text_rect.bottom + self.settings.settings_y_gap_big
        self.region_surface.blit(self.animation_option_text, self.animation_option_text_rect)

        # For the animation option
        self.animation_option_rect = self.button_rect.copy()
        self.animation_option_rect.left = self.animation_option_text_rect.right + self.settings.settings_x_gap
        self.animation_option_rect.bottom = self.animation_option_text_rect.bottom
        if self.settings.settings_save_dict['animations'] == True:
            self.region_surface.blit(self.on_button, self.animation_option_rect)
        else:
            self.region_surface.blit(self.off_button, self.animation_option_rect)

        # For the achievement progress text
        self.achievement_option_text = self.settings.settings_font_info.render("Achievements:", True,
            self.settings.settings_font_info_color)
        self.achievement_option_text_rect = self.achievement_option_text.get_rect()
        self.achievement_option_text_rect.right = self.hitbox_text_rect.right
        self.achievement_option_text_rect.top = self.animation_option_rect.bottom + self.settings.settings_y_gap_big
        self.region_surface.blit(self.achievement_option_text, self.achievement_option_text_rect)

        # For the achievement option
        self.achievement_option_rect = self.button_rect.copy()
        self.achievement_option_rect.left = self.achievement_option_text_rect.right + self.settings.settings_x_gap
        self.achievement_option_rect.bottom = self.achievement_option_text_rect.bottom
        if self.settings.settings_save_dict['achievements'] == True:
            self.region_surface.blit(self.on_button, self.achievement_option_rect)
        else:
            self.region_surface.blit(self.off_button, self.achievement_option_rect)

        # For the bird options (red bird at center, so used as reference)
        self.red_bird_option_on_image = pygame.image.load('Images/Driver/redbird-midflap.png')
        self.red_bird_option_off_image = pygame.image.load('Images/Driver/redbird-midflap - Grey.png')
        self.red_bird_option_image_rect = self.red_bird_option_on_image.get_rect()
        self.red_bird_option_image_rect.top = self.achievement_option_text_rect.bottom + self.settings.settings_y_gap_big
        self.red_bird_option_image_rect.center = (self.region_surface_rect.width//2, self.red_bird_option_image_rect.center[1])

        # For the yellow bird
        self.yellow_bird_option_on_image = pygame.image.load('Images/Driver/yellowbird-midflap.png')
        self.yellow_bird_option_off_image = pygame.image.load('Images/Driver/yellowbird-midflap - Grey.png')
        self.yellow_bird_option_image_rect = self.yellow_bird_option_on_image.get_rect()
        self.yellow_bird_option_image_rect.top = self.achievement_option_text_rect.bottom + self.settings.settings_y_gap_big
        self.yellow_bird_option_image_rect.right = self.red_bird_option_image_rect.left - self.settings.settings_x_gap

        # For the blue bird
        self.blue_bird_option_on_image = pygame.image.load('Images/Driver/bluebird-midflap.png')
        self.blue_bird_option_off_image = pygame.image.load('Images/Driver/bluebird-midflap - Grey.png')
        self.blue_bird_option_image_rect = self.blue_bird_option_on_image.get_rect()
        self.blue_bird_option_image_rect.top = self.achievement_option_text_rect.bottom + self.settings.settings_y_gap_big
        self.blue_bird_option_image_rect.left = self.red_bird_option_image_rect.right + self.settings.settings_x_gap

        # Blit all the bird options. Blit first all grey then colored on top
        self.region_surface.blit(self.yellow_bird_option_off_image, self.yellow_bird_option_image_rect)
        self.region_surface.blit(self.red_bird_option_off_image, self.red_bird_option_image_rect)
        self.region_surface.blit(self.blue_bird_option_off_image, self.blue_bird_option_image_rect)
        if self.settings.settings_save_dict['bird_color'] == 'yellow':
            self.region_surface.blit(self.yellow_bird_option_on_image, self.yellow_bird_option_image_rect)
        if self.settings.settings_save_dict['bird_color'] == 'red':
            self.region_surface.blit(self.red_bird_option_on_image, self.red_bird_option_image_rect)
        if self.settings.settings_save_dict['bird_color'] == 'blue':
            self.region_surface.blit(self.blue_bird_option_on_image, self.blue_bird_option_image_rect)


    def _position_rects_default(self):
        # For the region surface
        self.region_surface_rect.x = self.settings.region_side_gap_settings

        # For menu button
        self.menu_button_rect.center = self.BackgroundInstanceLogic.BackgroundAndBaseInstance.base_rect.center
        self.menu_button_rect.x = self.settings.button_gap_settings
        self.menu_button_highlight_rect.center = self.menu_button_rect.center

        # For the reset settings button
        self.reset_settings_button_rect.center = self.BackgroundInstanceLogic.BackgroundAndBaseInstance.base_rect.center
        self.reset_settings_button_rect.left = self.menu_button_rect.right + self.settings.button_gap_settings
        self.reset_settings_button_highlight_rect.center = self.reset_settings_button_rect.center

        # For the reset data button
        self.reset_data_button_rect.center = self.BackgroundInstanceLogic.BackgroundAndBaseInstance.base_rect.center
        self.reset_data_button_rect.left = self.reset_settings_button_rect.right + self.settings.button_gap_settings
        self.reset_data_button_highlight_rect.center = self.reset_data_button_rect.center


    def _push_right(self):
        # Push everything right to prepare for animation
        self.region_surface_rect.x += self.settings.screen_width
        self.menu_button_rect.x += self.settings.screen_width
        self.reset_settings_button_rect.x += self.settings.screen_width
        self.reset_data_button_rect.x += self.settings.screen_width


    def _draw_highlights(self):
        # Draw the highlights
        mouse = pygame.mouse.get_pos()

        # Check if collision between mouse and menu button
        if self.menu_button_rect.collidepoint(mouse) or \
            self.menu_button_highlight_rect.collidepoint(mouse) and self.menu_button_highlighted:
                self.screen.blit(self.menu_button_highlight, self.menu_button_highlight_rect)
                self.menu_button_highlighted = True
        else:
            self.menu_button_highlighted = False

        # Check settings collision. Allow for highlighting if no recent reset for settings
        if not self.reset_settings_recent:
            if self.reset_settings_button_rect.collidepoint(mouse) or\
                self.reset_settings_button_highlight_rect.collidepoint(mouse) and self.reset_settings_button_highlighted:
                    self.screen.blit(self.reset_settings_button_highlight, self.reset_settings_button_highlight_rect)
                    self.reset_settings_button_highlighted = True
            else:
                self.reset_settings_button_highlighted = False

        # Check data collision. Allow for highlighting if no recent reset for data
        if not self.reset_data_recent:
            if self.reset_data_button_rect.collidepoint(mouse) or\
                self.reset_data_button_highlight_rect.collidepoint(mouse) and self.reset_data_button_highlighted:
                    self.screen.blit(self.reset_data_button_highlight, self.reset_data_button_highlight_rect)
                    self.reset_data_button_highlighted = True
            else:
                self.reset_data_button_highlighted = False


    def draw_settings_background(self):
        # Draw the settings background
        self.BackgroundInstanceLogic.BackgroundAndBaseInstance.draw_background()
        self.BackgroundInstanceLogic.BackgroundAndBaseInstance.draw_base()

        # Draw the region
        self.screen.blit(self.region_surface, self.region_surface_rect)

        # For the menu button
        self.screen.blit(self.menu_button, self.menu_button_rect)

        # Draw the reset button for settings
        if not self.reset_settings_recent:
            self.screen.blit(self.reset_settings_button, self.reset_settings_button_rect)
        else:
            self.screen.blit(self.reset_settings_button_light, self.reset_settings_button_rect)
            if self.MainInstance.reset_settings_start + self.settings.button_light_delay <= pygame.time.get_ticks() / 1000:
                self.reset_settings_recent = False

        # Draw the reset button for data
        if not self.reset_data_recent:
            self.screen.blit(self.reset_data_button, self.reset_data_button_rect)
        else:
            self.screen.blit(self.reset_data_button_light, self.reset_data_button_rect)
            if self.MainInstance.reset_data_start + self.settings.button_light_delay <= pygame.time.get_ticks() / 1000:
                self.reset_data_recent = False

        # For the reset jump key (gray screen)
        if self.reset_keybind_recent:
            self.reset_key_surface.blit(self.reset_key_surface_text, self.reset_key_surface_text_rect)
            self.screen.blit(self.reset_key_surface, self.reset_key_surface.get_rect())

        # Check highlights
        if not self.reset_keybind_recent and not self.reset_gravity_recent:
            self._draw_highlights()
