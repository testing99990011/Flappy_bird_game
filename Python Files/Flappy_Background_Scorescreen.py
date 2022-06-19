import Flappy_Region_Info
import pygame

class FlappyBackgroundScorescreen:
    """Background for score screen"""

    def __init__(self, BackgroundInstanceLogic, MainInstance):
        """Default values used for score screen"""
        self.MainInstance = MainInstance
        self.BackgroundInstanceLogic = BackgroundInstanceLogic
        self.settings = self.MainInstance.settings
        self.screen = self.MainInstance.screen

        # Region Surface
        self.width = self.settings.screen_width - (2*self.settings.region_side_gap)
        self.height = self.settings.screen_height - (4*self.settings.region_side_gap)
        self.region_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.region_surface_rect = self.region_surface.get_rect()

        # For the region background
        self.surface_background_image = pygame.image.load('Images/Driver/region.PNG').convert()
        self.surface_background_image.set_colorkey((255, 255, 255))
        self.surface_background_image = pygame.transform.scale(self.surface_background_image,
            (self.width, self.height ))
        self.surface_background_image_rect = self.surface_background_image.get_rect()

        # Menu button
        self.menu_button = pygame.image.load('Images/Buttons/menu.PNG').convert()
        self.menu_button.set_colorkey((255,255,255))
        self.menu_button = pygame.transform.scale(self.menu_button,
            (self.settings.button_width_score, self.settings.button_height_score))
        self.menu_button_rect = self.menu_button.get_rect()

        # Arrow buttons
        self.arrow_image = pygame.image.load('Images/buttons/arrow.PNG').convert()
        self.arrow_image.set_colorkey((255, 255, 255))
        self.arrow_image = pygame.transform.scale(self.arrow_image,
            (int(self.settings.button_width_score / 2), self.settings.button_height_score))
        self.left_arrow = self.arrow_image.copy()
        self.right_arrow = pygame.transform.rotate(self.arrow_image, 180)
        self.left_arrow_rect = self.left_arrow.get_rect()
        self.right_arrow_rect = self.right_arrow.get_rect()

        # Menu button highlight
        self.menu_button_highlight = pygame.image.load('Images/Buttons/menu.PNG').convert()
        self.menu_button_highlight.set_colorkey((255,255,255))
        self.menu_button_highlight = pygame.transform.scale(self.menu_button_highlight, \
            (int(self.settings.button_width_score * (1 + self.settings.button_expansion_rate_score)),\
            int(self.settings.button_height_score * (1 + self.settings.button_expansion_rate_score)))
            )
        self.menu_button_highlight_rect = self.menu_button_highlight.get_rect()

        # Arrow highlight
        self.arrow_image_highlight = pygame.image.load('Images/buttons/arrow.PNG').convert()
        self.arrow_image_highlight.set_colorkey((255, 255, 255))
        self.arrow_image_highlight = pygame.transform.scale(self.arrow_image_highlight,
            (
            int(self.settings.button_width_score / 2 * (1 + self.settings.button_expansion_rate_score)), \
            int(self.settings.button_height_score * (1 + self.settings.button_expansion_rate_score))
            ))
        self.left_arrow_highlight = self.arrow_image_highlight.copy()
        self.right_arrow_highlight = pygame.transform.rotate(self.arrow_image_highlight, 180)
        self.left_arrow_highlight_rect = self.left_arrow_highlight.get_rect()
        self.right_arrow_highlight_rect = self.right_arrow_highlight.get_rect()

        # Flags for highlights
        self.menu_button_highlighted = False
        self.left_arrow_highlighted = False
        self.right_arrow_highlighted = False

        # Flags for the region surface
        self.page = 1
        self.total_pages = 4

        # Call the default positions. Push needed right for animations
        self._position_rects_default()
        self._push_right()


    def _position_rects_default(self):
        # Default positions for the rects on scorescreen

        # For the region
        self.region_surface_rect.right = self.settings.screen_width - self.settings.region_side_gap
        self.region_surface_rect.y = self.settings.region_side_gap

        # For the menu button
        self.menu_button_rect.center = self.BackgroundInstanceLogic.BackgroundAndBaseInstance.base_rect.center
        self.menu_button_rect.left = self.region_surface_rect.left

        # For the arrows
        self.right_arrow_rect.center = self.BackgroundInstanceLogic.BackgroundAndBaseInstance.base_rect.center
        self.right_arrow_rect.right = self.region_surface_rect.right
        self.left_arrow_rect = self.right_arrow_rect.copy()
        self.left_arrow_rect.right = self.right_arrow_rect.left
        self.left_arrow_rect.x -= self.settings.arrow_gap_score / 2

        # For the highlights of menu and arrows
        self.menu_button_highlight_rect.center = self.menu_button_rect.center
        self.left_arrow_highlight_rect.center = self.left_arrow_rect.center
        self.right_arrow_highlight_rect.center = self.right_arrow_rect.center


    def _push_right(self):
        # Push all the rights to the far right for the animation
        self.region_surface_rect.x += self.settings.screen_width
        self.menu_button_rect.x += self.settings.screen_width
        self.right_arrow_rect.x += self.settings.screen_width
        self.left_arrow_rect.x += self.settings.screen_width


    def _draw_highlights(self):
        # Draw highlights if a collision between mouse and button occurs
        mouse = pygame.mouse.get_pos()

        # For menu button collision
        if self.menu_button_rect.collidepoint(mouse) or \
           self.menu_button_highlight_rect.collidepoint(mouse) and self.menu_button_highlighted:
               self.screen.blit(self.menu_button_highlight, self.menu_button_highlight_rect)
               self.menu_button_highlighted = True
        else:
            self.menu_button_highlighted = False

        # For settings button collision
        if self.left_arrow_rect.collidepoint(mouse) or \
           self.left_arrow_highlight_rect.collidepoint(mouse) and self.left_arrow_highlighted:
               self.screen.blit(self.left_arrow_highlight, self.left_arrow_highlight_rect)
               self.left_arrow_highlighted = True
        else:
            self.left_arrow_highlighted = False

        # For score button collision
        if self.right_arrow_rect.collidepoint(mouse) or \
           self.right_arrow_highlight_rect.collidepoint(mouse) and self.right_arrow_highlighted:
               self.screen.blit(self.right_arrow_highlight, self.right_arrow_highlight_rect)
               self.right_arrow_highlighted = True
        else:
            self.right_arrow_highlighted = False


    def update_region_surface(self):
        # Update the info on the region surface based on the page number (controlled from main)
        # Always blit the background
        self.region_surface.blit(self.surface_background_image, self.surface_background_image_rect)
        self.region_surface.blit(Flappy_Region_Info.create_region_info(self.page,\
                                                                        self.total_pages,\
                                                                        self.region_surface_rect,\
                                                                        self.settings.matches_save_dict,\
                                                                        self.settings.achiv_save_dict,\
                                                                        self.BackgroundInstanceLogic),
                                                                        (0,0))


    def draw_scorescreen(self):
        # Draw the background
        self.BackgroundInstanceLogic.BackgroundAndBaseInstance.draw_background()
        self.BackgroundInstanceLogic.BackgroundAndBaseInstance.draw_base()

        # Draw the actual region
        self.screen.blit(self.region_surface, self.region_surface_rect)

        # Draw the buttons
        self.screen.blit(self.menu_button, self.menu_button_rect)
        self.screen.blit(self.left_arrow, self.left_arrow_rect)
        self.screen.blit(self.right_arrow, self.right_arrow_rect)

        # Draw the highlights
        self._draw_highlights()
