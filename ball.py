from turtle import Turtle

STARTING_POSITION = (0, -300)
START_MOVE = 5
MAX_X_MOVE = 8
START_SPEED = 0.02  # пауза між кадрами: менше значення - швидший м'яч
MIN_SPEED = 0.005
SPEED_UP_FACTOR = 0.95
LEVEL_SPEED_FACTOR = 0.85


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = START_MOVE
        self.y_move = START_MOVE
        self.base_speed = START_SPEED
        self.move_speed = START_SPEED
        self.goto(STARTING_POSITION)

    def speed_up(self):
        self.move_speed = max(self.move_speed * SPEED_UP_FACTOR, MIN_SPEED)

    def set_level(self, level):
        self.base_speed = max(START_SPEED * LEVEL_SPEED_FACTOR ** (level - 1), MIN_SPEED)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def bounce_off_paddle(self, offset_ratio):
        # offset_ratio: від -1 (лівий край платформи) до 1 (правий край)
        offset_ratio = max(-1, min(1, offset_ratio))
        self.y_move = abs(self.y_move)
        self.x_move = offset_ratio * MAX_X_MOVE

    def reset_position(self):
        self.goto(STARTING_POSITION)
        self.x_move = START_MOVE
        self.y_move = START_MOVE
        self.move_speed = self.base_speed
