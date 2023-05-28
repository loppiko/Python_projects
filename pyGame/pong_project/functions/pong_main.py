import random
import pygame
import sys
import functions.pong_functions as pong_functions

pygame.init()
pygame.display.set_caption("Python Pong")

window_size = [900, 600]
window = pygame.display.set_mode((window_size[0], window_size[1]))
font = pygame.font.Font('freesansbold.ttf', 32)
main_color = (160, 160, 160)
special_light_blue_color = (51, 153, 255)
special_dark_blue_color = (0, 102, 204)
special_light_green_color = (7, 194, 105)
special_white_color = (250, 250, 250)
background_color = (10, 10, 10)
margin = 75
# Ball
ball_width = 10
ball_velocity_x = 0.6
ball_velocity_y = 0.6
ball_x_coordinates = window_size[0] // 2
ball_y_coordinates = random.randint(margin, window_size[1] - margin)
# Paddle
paddle_width = 15
paddle_height = 50
paddle_velocity = 2.5
paddle_y_user = window_size[1] // 2
paddle_y_computer = window_size[1] // 2
# Difficulty
difficulty = 0.9
# Pong data
pong_data = {}
user_text = ''
computer_wins = 0
user_wins = 0
input_rect = pygame.Rect(200, 200, 140, 32)
game = True
enter = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pong_data = {"nick": user_text, "rekord": user_wins, "rekord-computer": computer_wins}
            pong_functions.file_managment('write', pong_data)
            game = False
    # USER INPUT and RECORDS
    text = (pong_functions.writing_text('Podaj nick: ', font, main_color, background_color))
    window.blit(text, (margin + 125, margin + 300))
    while not enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pong_data = {"nick": user_text, "rekord": user_wins, "rekord-computer": computer_wins}
                pong_functions.file_managment('write', pong_data)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                    text = (pong_functions.writing_text(user_text, font, main_color, background_color))
                    window.blit(text, (margin + 325, margin + 300))
                elif event.key == pygame.K_RETURN:
                    enter = True
                    break
                else:
                    user_text += event.unicode
        window.fill(background_color)
        text = (pong_functions.writing_text('Podaj nick: ', font, main_color, background_color))
        window.blit(text, (margin + 125, margin + 300))
        text = (pong_functions.writing_text('Tabela wyników: ', font, main_color, background_color))
        window.blit(text, (margin, margin))
        dictionary = pong_functions.file_managment("read", pong_data)
        text = (
            pong_functions.writing_text(('nick:        ' + str(dictionary["nick"])), font, special_light_blue_color,
                                        background_color))
        window.blit(text, (margin, margin + 100))
        text = (
            pong_functions.writing_text(('record:    ' + str(dictionary["rekord"])), font, special_dark_blue_color,
                                        background_color))
        window.blit(text, (margin, margin + 135))
        # pygame.display.update()
        text = (pong_functions.writing_text(user_text, font, main_color, background_color))
        window.blit(text, (margin + 325, margin + 300))
        pygame.display.update()
        pong_data = {"nick": user_text, "rekord": user_wins, "rekord-computer": computer_wins}

    # MAIN GAME
    window.fill(background_color)
    pygame.draw.line(window, main_color, (0, 0), (window_size[0], 0), margin)
    pygame.draw.line(window, main_color, (0, window_size[1]), (window_size[0], window_size[1]), margin)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and paddle_y_user > margin + 25:
        paddle_y_user -= paddle_velocity
    if keys[pygame.K_DOWN] and paddle_y_user < window_size[1] - margin - 25:
        paddle_y_user += paddle_velocity
    window.fill(background_color)
    pygame.draw.line(window, special_light_green_color, (0, 0), (window_size[0], 0), margin)
    pygame.draw.line(window, special_light_green_color, (0, window_size[1]), (window_size[0], window_size[1]), margin)
    # dashed_line
    dashed_line_y = 0
    dashed_line_height = 10
    while dashed_line_y < window_size[1]:
        pygame.draw.line(window, main_color, (window_size[0] // 2, dashed_line_y),
                         (window_size[0] // 2, dashed_line_y + dashed_line_height), 5)
        dashed_line_y = dashed_line_y + (dashed_line_height * 2)
    # paddle_user
    pygame.draw.line(window, main_color, (window_size[0] - margin, paddle_y_user - paddle_height),
                     (window_size[0] - margin, paddle_y_user + paddle_height), paddle_width)
    # paddle_computer
    paddle_y_computer = pong_functions.computer(ball_y_coordinates, paddle_y_computer, difficulty, margin, window_size)
    pygame.draw.line(window, main_color, (0 + margin, paddle_y_computer - paddle_height),
                     (0 + margin, paddle_y_computer + paddle_height), paddle_width)
    ball_velocity_x = pong_functions.ball_coordinates(ball_velocity_x, ball_velocity_y, ball_width, ball_x_coordinates,
                                                      ball_y_coordinates,
                                                      paddle_y_user,
                                                      paddle_y_computer, paddle_width, paddle_height, margin,
                                                      window_size, user_wins, computer_wins, pong_data)[0]
    ball_velocity_y = pong_functions.ball_coordinates(ball_velocity_x, ball_velocity_y, ball_width, ball_x_coordinates,
                                                      ball_y_coordinates,
                                                      paddle_y_user,
                                                      paddle_y_computer, paddle_width, paddle_height, margin,
                                                      window_size, user_wins, computer_wins, pong_data)[1]
    ball_x_coordinates += ball_velocity_x
    ball_y_coordinates += ball_velocity_y
    pygame.draw.circle(window, special_white_color, (ball_x_coordinates, ball_y_coordinates), ball_width)
    text = (pong_functions.writing_text((str(user_wins)), font, special_white_color, background_color))
    window.blit(text, (window_size[0] // 2 + 45, 100))
    text = (pong_functions.writing_text((str(computer_wins)), font, special_white_color, background_color))
    window.blit(text, (window_size[0] // 2 - 60, 100))
    # Drawing result
    if pong_functions.ball_coordinates(ball_velocity_x, ball_velocity_y, ball_width, ball_x_coordinates,
                                       ball_y_coordinates,
                                       paddle_y_user,
                                       paddle_y_computer, paddle_width, paddle_height, margin,
                                       window_size, user_wins, computer_wins, pong_data)[3]:
        pong_data = pong_functions.ball_coordinates(ball_velocity_x, ball_velocity_y, ball_width, ball_x_coordinates,
                                                    ball_y_coordinates,
                                                    paddle_y_user,
                                                    paddle_y_computer, paddle_width, paddle_height, margin,
                                                    window_size, user_wins, computer_wins, pong_data)[2]
        user_wins = pong_data["rekord"]
        computer_wins = pong_data["rekord-computer"]
        ball_velocity_x = 0.5
        ball_velocity_y = 0.5
        ball_x_coordinates = window_size[0] // 2
        ball_y_coordinates = random.randint(margin, window_size[1] - margin)
        paddle_y_user = window_size[1] // 2
        paddle_y_computer = window_size[1] // 2
        window.fill(background_color)

    pygame.display.update()
