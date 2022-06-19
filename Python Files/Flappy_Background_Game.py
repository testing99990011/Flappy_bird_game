import pygame, time, datetime, copy
from Flappy_Pipe_Pair import PipePair
from Flappy_Bird import FlappyBird
from Flappy_Scoreboard import ScoreBoard

class FlappyBackgroundGame:
    """Background for the start screen."""

    def __init__(self, BackgroundInstanceLogic, MainInstance):
        """Default values called on creation of instance."""

        self.BackgroundInstanceLogic = BackgroundInstanceLogic
        self.MainInstance = MainInstance
        self.settings = self.MainInstance.settings
        self.screen = self.MainInstance.screen

        # Group for pipes
        self.pipe_group = pygame.sprite.Group()

        # Bird and Scoreboard instance
        self.bird = FlappyBird(self, self.MainInstance)
        self.scoreboard = ScoreBoard(self.MainInstance)

        # For the achievement queue
        self.achievement_draw_queue = []


    def achievement_logic(self):
        # Check if achievements completed. Add them to queue if completed.
        if self.settings.settings_save_dict['achievements']:
            for achievement in self.BackgroundInstanceLogic.all_achievements:
                if achievement.check_completion() and not self.settings.achiv_save_dict[achievement.name+'_finished']:
                    self.settings.achiv_save_dict[achievement.name+'_finished'] = True
                    self.achievement_running_instance = achievement
                    self.achievement_draw_queue.append(achievement)


    def draw_achievements_logic(self):
        # Draw the achievements in queue to the screen
        if self.achievement_draw_queue:
            if self.achievement_draw_queue[0].draw_logic():
                self.achievement_draw_queue.pop(0)


    def check_collisions(self):
        # Collision detection function

        # Defualt hitbox
        if self.settings.settings_save_dict['hitbox'] == 'default':
            if self.bird.bird_rect.y <= 0 or self.bird.bird_rect.bottom  >= self.BackgroundInstanceLogic.BackgroundAndBaseInstance.base_rect.y:
                self.collision_flag = True
            else:
                self.collision_flag = False
            for pipe in self.pipe_group:
                if pipe.top_pipe_rect.colliderect(self.bird.bird_rect) or \
                pipe.bottom_pipe_rect.colliderect(self.bird.bird_rect):
                    self.collision_flag = True

        # Box hitbox
        if self.settings.settings_save_dict['hitbox'] == 'default_box':
            if self.bird.bird_hitbox_rect.y <= 0 or self.bird.bird_hitbox_rect.bottom  >= self.BackgroundInstanceLogic.BackgroundAndBaseInstance.base_rect.y:
                self.collision_flag = True
            else:
                self.collision_flag = False
            for pipe in self.pipe_group:
                if pipe.top_pipe_rect.colliderect(self.bird.bird_hitbox_rect) or \
                pipe.bottom_pipe_rect.colliderect(self.bird.bird_hitbox_rect):
                    self.collision_flag = True

        # Adaptive hitbox
        if self.settings.settings_save_dict['hitbox'] == 'hitbox_adaptive':
            if self.bird.bird_hitbox_advanced_rect.y <= 0 or self.bird.bird_hitbox_advanced_rect.bottom  >= self.BackgroundInstanceLogic.BackgroundAndBaseInstance.base_rect.y:
                self.collision_flag = True
            else:
                self.collision_flag = False
            for pipe in self.pipe_group:
                if pipe.top_pipe_rect.colliderect(self.bird.bird_hitbox_advanced_rect) or \
                pipe.bottom_pipe_rect.colliderect(self.bird.bird_hitbox_advanced_rect):
                    self.collision_flag = True

        # If collision flag
        if self.collision_flag:
            # Flags for screens
            self.MainInstance.game_screen = False
            self.MainInstance.gameover_screen = True

            # Reset the bird position, clear the pipes list, reset the scores
            self._reset_game_background_default()

            # Update the gameover info screen with the new score values
            self.settings.end_time = pygame.time.get_ticks()
            self.BackgroundInstanceLogic.BackgroundInstanceGameOver._create_region()

            # Save and reset the values
            self.achievement_draw_queue.clear()
            self._add_match_leaderboard()
            self._add_match_data()
            self.settings._reset_match_scores()

            # Sleep (So player sees where collision occurred). Must update display before so that collision is shown.
            pygame.display.flip()
            time.sleep(2)


    def _add_match_leaderboard(self):
        # Add match to leaderboard dict

        for i in range(1, 4):
            if self.settings.dynamic_score > self.settings.matches_save_dict[i]['score'] and self.settings.dynamic_score != 0:
                # Shift over all the scores down by one if not last
                if i != 3:
                    self._shift_leaderboard(i)

                # Add the new value to the leaderboard
                now = datetime.datetime.now()
                current_time = now.strftime('%m/%d/%y')
                self.copy_dict[i]['score'] = self.settings.dynamic_score
                self.copy_dict[i]['time'] = int((self.settings.end_time - self.settings.start_time)/1000)
                self.copy_dict[i]['date'] = current_time

                # Change the dict. Break statement since shift would have occurred
                self.settings.matches_save_dict = self.copy_dict
                break


    def _shift_leaderboard(self, start_value):
        # Shift the leaderboard down. End value of 3 (actually 2) because 3 is replaced not shifted
        self.copy_dict = copy.deepcopy(self.settings.matches_save_dict)
        for i in range(start_value, 3):
            self.copy_dict[i+1]['score'] = self.settings.matches_save_dict[i]['score']
            self.copy_dict[i+1]['time'] = self.settings.matches_save_dict[i]['time']
            self.copy_dict[i+1]['date'] = self.settings.matches_save_dict[i]['date']


    def _add_match_data(self):
        # Add the most recent match data to the dictionary
        self.settings.achiv_save_dict['jumps'] += self.settings.jumps
        self.settings.achiv_save_dict['deaths'] += 1
        self.settings.achiv_save_dict['score'] += self.settings.dynamic_score
        self.settings.achiv_save_dict['total_sessions'] += 1
        self.settings.achiv_save_dict['play_time'] += int((self.settings.end_time - self.settings.start_time)/1000)
        self.settings.achiv_save_dict['distance_x'] += self.settings.distance_x
        self.settings.achiv_save_dict['distance_y'] += self.settings.distance_y

        # Update the requirements for the achievements
        if self.settings.settings_save_dict['achievements']:
            for achievement in self.BackgroundInstanceLogic.all_achievements:
                achievement.update_req_val()


    def _pipe_logic(self):
        # Add a new pipe to the group if room exists
        try:
            if list(self.pipe_group)[-1].top_pipe_rect.x \
            + (self.settings.pipe_distance_between + self.settings.pipe_width) \
            < self.settings.screen_width:
                self.pipe_group.add(PipePair(self, self.MainInstance))
        # Generate a first pipe if pipe_group is empty
        except IndexError:
            self.pipe_group.add(PipePair(self, self.MainInstance))


    def _draw_pipes(self):
        # Draw the pipes individually. Remove pipes that are out of screen
        for pipe in self.pipe_group:
            if pipe.top_pipe_rect.x <= (-pipe.top_pipe_rect.width):
                self.pipe_group.remove(pipe)
                self.settings.dynamic_score += 1
            else:
                pipe.draw_pipe()


    def _reset_game_background_default(self):
        # Reset the game background
        self.bird.reset_bird_default()
        self.pipe_group.empty()


    def draw_game_background(self):
        # Draw the game background. Pipes then background because pipes full height screen
        self.BackgroundInstanceLogic.BackgroundAndBaseInstance.draw_background()
        self._draw_pipes()
        self.bird.draw_bird()
        self.scoreboard.draw_score()
        self.BackgroundInstanceLogic.BackgroundAndBaseInstance.draw_base()
