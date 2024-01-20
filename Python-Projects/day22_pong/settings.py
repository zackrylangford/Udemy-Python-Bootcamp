# settings.py

# Game speed settings
BALL_MOVE_SPEED = 5
GAME_UPDATE_INTERVAL = 40  # in milliseconds
PADDLE_MOVE_DISTANCE = 20

def increase_ball_speed():
    """ Increase the ball speed """
    global BALL_MOVE_SPEED, GAME_UPDATE_INTERVAL
    BALL_MOVE_SPEED = BALL_MOVE_SPEED * 2
    GAME_UPDATE_INTERVAL = int(GAME_UPDATE_INTERVAL / 2)  # Convert to integer
    print(f"Ball speed increased to {BALL_MOVE_SPEED}, Update interval: {GAME_UPDATE_INTERVAL}")

def reset_ball_speed():
    """ Reset the ball speed """
    global BALL_MOVE_SPEED, GAME_UPDATE_INTERVAL
    BALL_MOVE_SPEED = 5
    GAME_UPDATE_INTERVAL = int(40)  # Ensure it's an integer
    print(f"Ball speed reset to {BALL_MOVE_SPEED}, Update interval: {GAME_UPDATE_INTERVAL}")
