from turtle import Turtle

STARTING_POSITION = (0, -350)
MOVE_DISTANCE = 40
X_LIMIT = 240  # екран 600 шириною, платформа 120: половина екрана 300 - половина платформи 60


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.penup()
        self.goto(STARTING_POSITION)

    def go_left(self):
        new_x = max(self.xcor() - MOVE_DISTANCE, -X_LIMIT)
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = min(self.xcor() + MOVE_DISTANCE, X_LIMIT)
        self.goto(new_x, self.ycor())
