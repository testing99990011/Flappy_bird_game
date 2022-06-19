import pygame, time

class Achievements:
    """Achievements used in the game."""

    def __init__(self, MainInstance, achievement_image):
        """Default values used in all instances."""
        self.screen = MainInstance.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = MainInstance.settings

        # Flags and MainInstance
        self.MainInstance = MainInstance
        self.achievement_finished = False

        # Screen Rects
        self.achievement_image = achievement_image
        self.achievement_image.set_colorkey((255, 255, 255))
        self.achievement_image = pygame.transform.scale(self.achievement_image,
            ((self.settings.width_achievements), self.settings.height_achievements))
        self.achievement_image_rect = self.achievement_image.get_rect()
        self.achievement_image_rect.bottom = self.screen_rect.top

    def draw_logic(self):
        # Draw achievement onto screen
        if not self.achievement_image_rect.top >= self.screen_rect.top:
            self._position_update()
        else:
            if time.time() >= self.reference_time + self.settings.achievement_duration:
                self.screen.blit(self.achievement_image, self.achievement_image_rect)
                return True     # Return True if achievement expired and complete
        self.screen.blit(self.achievement_image, self.achievement_image_rect)

    def _position_update(self):
        # Update position of draw
        self.achievement_image_rect.y += self.MainInstance.settings.achievement_speed
        self.reference_time = time.time()


class NewPlayer(Achievements):
    """NewPlayer achievement"""
    def __init__(self, MainInstance):
        achievement_image = pygame.image.load('Images/Achiv/NewPlayer.PNG').convert()
        super().__init__(MainInstance, achievement_image)

        # Name and descirption
        self.name = 'NewPlayer'
        self.description = 'Start a game for the very first time.'

        """
        Requirements:
                    1. Start the game for the very first time
        """

    def update_req_val(self):
        # Update requirements values
        self.requirements = {0: {'description': 'Start a game: ', 'current': self.settings.achiv_save_dict['jumps'], 'required': 1}}

    def check_completion(self):
        # Check if achievement is completed
        if self.settings.achiv_save_dict['jumps'] + self.settings.jumps >= 1:
            return True


class TheJumperI(Achievements):
    """TheJumperI achievement"""
    def __init__(self, MainInstance):
        achievement_image = pygame.image.load('Images/Achiv/TheJumperI.PNG').convert()
        super().__init__(MainInstance, achievement_image)

        # Name and descirption
        self.name = 'TheJumperI'
        self.description = 'Jumping a lot? (Includes tutorial jumps).'

        """
        Requirements:
                    1. Jump 100 times
        """

    def update_req_val(self):
        # Update requirements values
        self.requirements = {0: {'description': 'Jumps: ', 'current': self.settings.achiv_save_dict['jumps'],
                            'required': 100}}

    def check_completion(self):
        # Check if achievement is completed
        if self.settings.achiv_save_dict['jumps'] + self.settings.jumps == 100:
            return True


class TheExplorerI(Achievements):
    """TheExplorerI achievement"""
    def __init__(self, MainInstance):
        achievement_image = pygame.image.load('Images/Achiv/TheExplorerI.PNG').convert()
        super().__init__(MainInstance, achievement_image)

        # Name and descirption
        self.name = 'TheExplorerI'
        self.description = 'Exploring the map.'

        """
        Requirements:
                    1. Travel a horizontal distance of 500
        """

    def update_req_val(self):
        # Update requirements values
        self.requirements = {0: {'description': 'Dist x: ',
                            'current': self.settings.achiv_save_dict['distance_x'], 'required': 500}}

    def check_completion(self):
        # Check if achievement is completed
        if self.settings.achiv_save_dict['distance_x'] + self.settings.distance_x == 500:
            return True


class TheBeginner(Achievements):
    """The Beginner achievement"""
    def __init__(self, MainInstance):
        achievement_image = pygame.image.load('Images/Achiv/TheBeginner.PNG').convert()
        super().__init__(MainInstance, achievement_image)

        # Name and descirption
        self.name = 'TheBeginner'
        self.description = 'Getting the hang of it.'

        """
        Requirements:
                    1. Jump 100 times
                    2. travel 500 distance
                    3. die 5 times
        """

    def update_req_val(self):
        # Update requirements values
        self.requirements = {0: {'description': 'Jumps: ',
                            'current': self.settings.achiv_save_dict['jumps'], 'required': 100},
                            1: {'description': 'Dist x: ',
                            'current': self.settings.achiv_save_dict['distance_x'], 'required': 500},
                            2: {'description': 'Deaths: ',
                            'current': self.settings.achiv_save_dict['deaths'], 'required': 5}}

    def check_completion(self):
        # Check if the achievement is completed
        if self.settings.achiv_save_dict['jumps'] + self.settings.jumps == 50 and\
            self.settings.achiv_save_dict['distance_x'] + self.settings.distance_x == 500 and\
            self.settings.achiv_save_dict['deaths'] == 5:
                return True


class TheNovice(Achievements):
    """The Novice achievement"""
    def __init__(self, MainInstance):
        achievement_image = pygame.image.load('Images/Achiv/TheNovice.PNG').convert()
        super().__init__(MainInstance, achievement_image)

        # Name and descirption
        self.name = 'TheNovice'
        self.description = 'You\'re improving.'

        """
        Requirements:
                    1. Jump 250 times
                    2. travel 1500 distance
                    3. die 15 times
        """

    def update_req_val(self):
        # Update requirements values
        self.requirements = {0: {'description': 'Jumps: ',
                            'current': self.settings.achiv_save_dict['jumps'], 'required': 250},
                            1: {'description': 'Dist x: ',
                            'current': self.settings.achiv_save_dict['distance_x'], 'required': 1500},
                            2: {'description': 'Deaths: ',
                            'current': self.settings.achiv_save_dict['deaths'], 'required': 15}}

    def check_completion(self):
        # Check if the achievement is completed
        if self.settings.achiv_save_dict['jumps'] + self.settings.jumps == 250 and\
            self.settings.achiv_save_dict['distance_x'] + self.settings.distance_x == 1500 and\
            self.settings.achiv_save_dict['deaths'] == 15:
                return True


class TheJumperII(Achievements):
    """The Jumper II achievement"""
    def __init__(self, MainInstance):
        achievement_image = pygame.image.load('Images/Achiv/TheJumperII.PNG').convert()
        super().__init__(MainInstance, achievement_image)

        # Name and descirption
        self.name = 'TheJumperII'
        self.description = 'Pressing the jump key a lot?'

        """
        Requirements:
                    1. Jump 300 times
        """

    def update_req_val(self):
        # Update requirements values
        self.requirements = {0: {'description': 'Jumps: ',
                            'current': self.settings.achiv_save_dict['jumps'], 'required': 300}}

    def check_completion(self):
        # Check if completed
        if self.settings.achiv_save_dict['jumps'] + self.settings.jumps == 300:
            return True


class ItHappens(Achievements):
    """It Happens achievement"""
    def __init__(self, MainInstance):
        achievement_image = pygame.image.load('Images/Achiv/ItHappens.PNG').convert()
        super().__init__(MainInstance, achievement_image)

        # Name and descirption
        self.name = 'ItHappens'
        self.description = 'Restarting is always hard.'

        """
        Requirements:
                    1. Die 20 times
        """

    def update_req_val(self):
        # Update requirements values
        self.requirements = {0: {'description': 'Deaths: ',
                            'current': self.settings.achiv_save_dict['deaths'], 'required': 20}}

    def check_completion(self):
        # Check if completed
        if self.settings.achiv_save_dict['deaths'] == 20:
            return True


class Gravity(Achievements):
    """Gravity Achievement"""
    def __init__(self, MainInstance):
        achievement_image = pygame.image.load('Images/Achiv/Gravity.PNG').convert()
        super().__init__(MainInstance, achievement_image)

        # Name and descirption
        self.name = 'Gravity'
        self.description = 'Pulling you downnnnnn!'

        """
        Requirements:
                    1. Fall 1000 meters
        """

    def update_req_val(self):
        # Update requirements values
        self.requirements = {0: {'description': 'Fall dist: ',
                            'current': self.settings.achiv_save_dict['distance_y'], 'required': 1000}}

    def check_completion(self):
        # Check if completed
        if self.settings.achiv_save_dict['distance_y'] + self.settings.distance_y == 1000:
            return True
