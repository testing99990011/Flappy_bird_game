import pygame
pygame.init()

title_font = pygame.font.Font(r'Images\Buttons\FSEX300.ttf', 24)
page_number_font = pygame.font.Font(r'Images\Buttons\FSEX300.ttf', 16)
text_info_font = pygame.font.Font(r'Images\Buttons\FSEX300.ttf', 18)
text_description = pygame.font.Font(r'Images\Buttons\FSEX300.ttf', 14)

gap = 20
gap_big = 40
text_gap = 10
number_gap = 5
ratio = .6
score_color = {1: (210, 186, 45), 2: (195, 195, 195), 3: (176, 141, 87)}


def create_region_info(page_number, total_pages, region_surface_rect, matches_dict, achiv_dict, BackgroundInstanceLogic):
    """Function that returns the region based on the page number."""

    # Base region
    region_surface_copy = pygame.Surface((region_surface_rect.width, region_surface_rect.height),\
        pygame.SRCALPHA)
    page_number_surface = _page_number_surface(page_number, total_pages, region_surface_rect, region_surface_copy)

    # For the page number
    _page_number_surface(page_number, total_pages, region_surface_rect, region_surface_copy)

    if page_number == 1:
        _create_page_one(region_surface_rect, region_surface_copy, matches_dict, achiv_dict, BackgroundInstanceLogic)
    else:
        # We use i-start to position the achievement correctly. If page two, then page 1 achievements above screen
        if page_number == 2:
            start = 0
        elif page_number == 3:
            start = 4
        else:
            start = 8
        for i in range(4 + start):

            # Loading and pasting Achievement logo
            try:
                loaded_achievement = BackgroundInstanceLogic.all_achievements[i]
            except IndexError:
                break
            achievement_image = loaded_achievement.achievement_image.copy()
            achievement_image_rect = achievement_image.get_rect()
            if not BackgroundInstanceLogic.settings.achiv_save_dict[loaded_achievement.name+'_finished']:
                surf = pygame.Surface((achievement_image_rect.width, achievement_image_rect.height))
                surf.set_alpha(200)
                achievement_image.blit(surf, surf.get_rect())
            achievement_image_rect.x = text_gap
            achievement_image_rect.y = text_gap + (120 * (i-start))
            region_surface_copy.blit(achievement_image, achievement_image_rect)

            # Line between achievements
            if i-start != 0:
                pygame.draw.line(region_surface_copy, (185,122,87), \
                    (5, achievement_image_rect.y), (region_surface_rect.width-5, achievement_image_rect.y))

            # Blit the descirption of achievement
            if i-start == 0:
                return_surface = _text_wrap_algo(loaded_achievement.description, text_description, 100)
            else:
                return_surface = _text_wrap_algo(loaded_achievement.description, text_description)
            return_surface_rect = return_surface.get_rect()
            return_surface_rect.left = achievement_image_rect.right
            return_surface_rect.top = achievement_image_rect.top
            region_surface_copy.blit(return_surface, return_surface_rect)

            # Draw the requirements below the achievement
            for x in range(len(loaded_achievement.requirements)):
                text = loaded_achievement.requirements[x]['description']
                current = int(loaded_achievement.requirements[x]['current'])
                required = loaded_achievement.requirements[x]['required']
                generated_progress_bar = _generate_score_progress(text, current, required)
                draw_requirements_progress_bar(x, generated_progress_bar, achievement_image_rect, region_surface_copy)

    return region_surface_copy


def _page_number_surface(page_number, total_pages, region_surface_rect, region_surface_copy):
    # Create the page number text. Goes at top right
    page_number_text = f'{page_number} / {total_pages}'
    page_number_render = page_number_font.render(page_number_text, True, (0,0,0))
    page_number_render_rect = page_number_render.get_rect()
    page_number_render_rect.topright = \
    (region_surface_rect.width - gap), (gap)
    region_surface_copy.blit(page_number_render, page_number_render_rect)


def _create_page_one(region_surface_rect, region_surface_copy, matches_dict, achiv_dict, BackgroundInstanceLogic):
    # Leaderboard page

    # Create the headers at the top
    text1 = 'Score'
    text2 = 'Time'
    text3 = 'Date'
    text1_render = title_font.render(text1, True, (0,0,0))
    text2_render = title_font.render(text2, True, (0,0,0))
    text3_render = title_font.render(text3, True, (0,0,0))
    text1_rect = text1_render.get_rect()

    text1_rect.topleft = (gap_big, gap_big)
    text2_rect = text1_rect.copy()
    text3_rect = text1_rect.copy()
    text2_rect.left = text1_rect.right + gap_big
    text3_rect.left = text2_rect.right + gap_big

    region_surface_copy.blit(text1_render, text1_rect)
    region_surface_copy.blit(text2_render, text2_rect)
    region_surface_copy.blit(text3_render, text3_rect)

    # For the leaderboard
    for score_id in range(1, 4):
        # Left side score number
        score_id_number = title_font.render(str(score_id), True, score_color[score_id])
        score_id_number_rect = score_id_number.get_rect()
        score_id_number_rect.x = (text1_rect.left - score_id_number_rect.width) / 2
        score_id_number_rect.top = text1_rect.bottom + gap_big * score_id
        region_surface_copy.blit(score_id_number, score_id_number_rect)

        # Score on the left side
        score_actual_value = _score_image(matches_dict[score_id]['score'], BackgroundInstanceLogic)
        score_actual_value_rect = score_actual_value.get_rect()
        score_actual_value_rect.center = text1_rect.center
        score_actual_value_rect.bottom = score_id_number_rect.bottom
        region_surface_copy.blit(score_actual_value, score_actual_value_rect)

        # Time of match
        total_time = matches_dict[score_id]['time']
        minutes, seconds = _return_min_seconds(total_time)
        formatted_time_msg = f'{minutes}m {seconds}s'
        time_msg_rendered = title_font.render(formatted_time_msg, True, score_color[score_id])
        time_msg_rendered_rect = time_msg_rendered.get_rect()
        time_msg_rendered_rect.center = text2_rect.center
        time_msg_rendered_rect.bottom = score_id_number_rect.bottom
        region_surface_copy.blit(time_msg_rendered, time_msg_rendered_rect)

        # Date info
        formatted_date = matches_dict[score_id]['date']
        formatted_date_rendered = title_font.render(formatted_date, True, score_color[score_id])
        formatted_date_rendered_rect = formatted_date_rendered.get_rect()
        formatted_date_rendered_rect.center = text3_rect.center
        formatted_date_rendered_rect.bottom = score_id_number_rect.bottom
        region_surface_copy.blit(formatted_date_rendered, formatted_date_rendered_rect)


    # For the averages at the bottom of screen
    jumps = achiv_dict['jumps']
    deaths = achiv_dict['deaths']
    total_pipes = achiv_dict['score']
    try:
        avg_time = int(achiv_dict['play_time'] / achiv_dict['total_sessions'])
    except ZeroDivisionError:
        avg_time = 0
    avg_min, avg_sec = _return_min_seconds(avg_time)
    avg_time = f"{avg_min}m:{avg_sec}s"
    minutes, seconds = _return_min_seconds(achiv_dict['play_time'])
    play_time = f"{minutes}m:{seconds}s"
    distance_x = int(achiv_dict['distance_x'])
    distance_y = int(achiv_dict['distance_y'])

    # For the text at the bottom
    text4 = 'Jumps:'
    text5 = 'Pipes:'
    text6 = 'Deaths:'
    text7 = 'Travel x:'
    text8 = 'Travel y:'
    text9 = 'Play Time:'
    text10 = 'Avg Time:'
    txt_lst = [text4, text5, text6, text7, text8, text9, text10]
    matching = {text4: jumps, text5: total_pipes, text6: deaths, text7: distance_x,
                text8: distance_y, text9: play_time, text10: avg_time}
    for i in range(len(txt_lst)):
        rendered_text = text_info_font.render(txt_lst[i], True, (0,0,0))
        rendered_text_rect = rendered_text.get_rect()
        rendered_text_rect.right = text2_rect.left + gap
        rendered_text_rect.top = (score_actual_value_rect.bottom + gap_big) \
            + (i * (text_gap + rendered_text_rect.height))
        answer_text = text_info_font.render(str(matching[txt_lst[i]]), True, (0,0,0))
        answer_text_rect = answer_text.get_rect()
        answer_text_rect.bottom = rendered_text_rect.bottom
        answer_text_rect.left = rendered_text_rect.right + gap_big
        region_surface_copy.blit(rendered_text, rendered_text_rect)
        region_surface_copy.blit(answer_text, answer_text_rect)


def _score_image(score, BackgroundInstanceLogic):
    # Return a surface with score on it

    # Use the reference rect of a number from scoreboard to create the surface
    reference_rect = BackgroundInstanceLogic.BackgroundInstanceGame.scoreboard.basic_rect.copy()
    reference_surface = pygame.Surface(\
        ((reference_rect.width + number_gap) * len(str(score)),
        reference_rect.height), \
        pygame.SRCALPHA)

    # Add the numbers to the surface
    for iteration, value in enumerate(str(score)):
        number = BackgroundInstanceLogic.BackgroundInstanceGame.scoreboard.score_dict[int(value)]
        reference_rect.x = iteration * (reference_rect.width + number_gap)
        reference_surface.blit(number, reference_rect)

    # Scale the surface to fit into the info screen
    reference_surface_rect_width, reference_surface_rect_height = reference_surface.get_rect().size
    reference_surface_final = pygame.transform.smoothscale(reference_surface, \
        (int(reference_surface_rect_width * ratio),\
        int(reference_surface_rect_height * ratio)))
    return reference_surface_final


def _return_min_seconds(total_time):
    # Return the minutes and seconds given the total time in seconds
    minutes = total_time // 60
    seconds = total_time - 60 * (total_time//60)
    return str(minutes), str(seconds)


def _text_wrap_algo(text, font_size, max_width=155, hyphens=False, periods=False):
    # Return a surface with word wrap based on width. Hypthens and periods optional
    words = text.split()
    current_width = 0
    generated_lines = []
    current_line = ''
    single_width, total_height = font_size.size(' ')

    for word in words:
        width, height = font_size.size(word)
        if current_width + width + single_width > max_width:
            # Add old line generated_lines
            total_height += height
            if hyphens:
                current_width += single_width
                current_line += '-'
            generated_lines.append(current_line)

            # If last word add single word to generated_lines. Else add to current_line
            if word == words[-1]:
                current_line = word
            else:
                current_line = word + ' '
                current_width = (width + single_width)
        else:
            current_width += (width + single_width)
            current_line += (word + ' ')
        if word == words[-1]:
            current_line.rstrip()
            if periods:
                current_line += '.'
            generated_lines.append(current_line)

    # Convert text to actual images
    text_surface = pygame.Surface((max_width, total_height), pygame.SRCALPHA)
    for i, line in enumerate(generated_lines):
        rendered_words = font_size.render(line, True, (0,0,0))
        rendered_words_rect = rendered_words.get_rect()
        rendered_words_rect.y = (rendered_words_rect.height * i)
        text_surface.blit(rendered_words, rendered_words_rect)
    return text_surface


def _generate_score_progress(text, current, total):
    # Function to generate the score progress

    # Main Surface
    region = pygame.Surface((145, 21), pygame.SRCALPHA)
    region_rect = region.get_rect()

    # Border rectangle
    pygame.draw.rect(region, (0,0,0), (0,0,145,21), 1)

    # Ratio and text
    ratio_completed = current / total
    if ratio_completed >= 1:
        color = (0,128,0,128)
        ratio_completed = 1
        text = text[:] + f'{total}/{total}'
    else:
        color = (255,128,64,128)
        text = text[:] + f'{current}/{total}'
    text = text_description.render(text, True, (0,0,0))
    text_rect = text.get_rect()
    text_rect.center = region_rect.center
    region.blit(text, text_rect)

    # The progress bar
    width = 143 * ratio_completed
    progress_bar = pygame.Surface((width, 19), pygame.SRCALPHA)
    progress_bar.fill(color)
    progress_bar_rect = progress_bar.get_rect()
    progress_bar_rect.center = region_rect.center
    progress_bar_rect.left = region_rect.left + 1
    region.blit(progress_bar, progress_bar_rect)

    return region


def draw_requirements_progress_bar(x, bar, achievement_image_rect, region_surface_copy):
    # Draw the progress bar
    surface_rect = bar.get_rect()
    if x == 0:
        surface_rect.x = text_gap
        surface_rect.y = achievement_image_rect.bottom + text_gap/2
    elif x == 1:
        surface_rect.x = text_gap
        surface_rect.y = achievement_image_rect.bottom + (text_gap) + surface_rect.height
    elif x == 2:
        surface_rect.x = (text_gap * 2) + surface_rect.width
        surface_rect.y = achievement_image_rect.bottom + text_gap/2
    else:
        surface_rect.x = (text_gap * 2) + surface_rect.width
        surface_rect.y = achievement_image_rect.bottom + (text_gap) + surface_rect.height
    region_surface_copy.blit(bar, surface_rect)
