import ast
from os.path import exists


def file_managment(game_status, pong_data):
    if game_status == 'read':
        file_exists = exists("results/pong_results.txt")
        if file_exists:
            with open('results/pong_results.txt') as file:
                data = file.read()
            file.close()
            old_pong_data = ast.literal_eval(data)
            file.close()
            return old_pong_data
        else:
            temp_dictionary = {"nick": 'no one', "rekord": 0, "rekord-computer": 0}
            with open('results/pong_results.txt', 'w') as file:
                file.write(str(temp_dictionary))
            return temp_dictionary
    elif game_status == 'write':
        with open('results/pong_results.txt') as file:
            data = file.read()
        file.close()
        old_pong_data = ast.literal_eval(data)
        if int(old_pong_data["rekord"]) < int(pong_data["rekord"]):
            with open('results/pong_results.txt', 'w') as file:
                file.write(str(pong_data))
        file.close()
    else:
        pass
    return 0


def writing_text(text_data, font, main_color, background_color):
    text = font.render(text_data, True, main_color, background_color)
    return text


def ball_coordinates(ball_velocity_x, ball_velocity_y, ball_width, ball_x_coordinates, ball_y_coordinates,
                     paddle_y_user,
                     paddle_y_computer, paddle_width, paddle_height, margin, window_size, user_wins, computer_wins,
                     pong_data):
    if ball_x_coordinates < 0 + margin:
        pong_data = {"rekord": user_wins + 1, "rekord-computer": computer_wins}
        return ball_velocity_x, ball_velocity_y, pong_data, True
    if ball_x_coordinates > window_size[0] - margin:
        pong_data = {"rekord": user_wins, "rekord-computer": computer_wins + 1}
        return ball_velocity_x, ball_velocity_y, pong_data, True
    if ball_x_coordinates + ball_width >= window_size[0] - (paddle_width + margin) and (
            ball_y_coordinates < paddle_y_user + paddle_height and ball_y_coordinates > paddle_y_user - paddle_height):
        ball_velocity_x = -abs(ball_velocity_x) - 0.05  # DO IT QUCIKLY :)
        if ball_velocity_y < 0:
            ball_velocity_y = ball_velocity_y - 0.05
        else:
            ball_velocity_y = ball_velocity_y + 0.05
        return ball_velocity_x, ball_velocity_y, pong_data, False
    elif ball_x_coordinates - ball_width <= paddle_width + margin and (
            ball_y_coordinates < paddle_y_computer + paddle_height and ball_y_coordinates > paddle_y_computer - paddle_height):
        ball_velocity_x = abs(ball_velocity_x) + 0.05
        if ball_velocity_y < 0:
            ball_velocity_y = ball_velocity_y - 0.05
        else:
            ball_velocity_y = ball_velocity_y + 0.05
        return ball_velocity_x, ball_velocity_y, pong_data, False
    elif ball_y_coordinates >= window_size[1] - margin:
        ball_velocity_y = -abs(ball_velocity_y)
        return ball_velocity_x, ball_velocity_y, pong_data, False
    elif ball_y_coordinates <= margin:
        ball_velocity_y = abs(ball_velocity_y)
        return ball_velocity_x, ball_velocity_y, pong_data, False
    else:
        return ball_velocity_x, ball_velocity_y, pong_data, False


def computer(ball_y_coordinates, paddle_y_computer, difficulty, margin, window_size):
    if ball_y_coordinates > paddle_y_computer and paddle_y_computer < window_size[1] - margin - 25:
        paddle_y_computer = paddle_y_computer + difficulty
        return paddle_y_computer
    if ball_y_coordinates < paddle_y_computer and paddle_y_computer > margin + 25:
        paddle_y_computer = paddle_y_computer - difficulty
        return paddle_y_computer
    return paddle_y_computer
