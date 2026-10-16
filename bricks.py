from turtle import Turtle

COLORS = ["red", "orange red", "orange", "gold", "yellow", "green yellow"]
COLUMNS = 10
BRICK_WIDTH = 56
BRICK_HEIGHT = 20
GAP = 4
BALL_RADIUS = 10
FIRST_X = -270
FIRST_Y = 300


class Brick(Turtle):
    def __init__(self, x, y, color, points):
        super().__init__()
        self.points = points
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=BRICK_HEIGHT / 20, stretch_len=BRICK_WIDTH / 20)
        self.penup()
        self.goto(x, y)
        self.width_px = BRICK_WIDTH
        self.height_px = BRICK_HEIGHT


class Bricks:
    def __init__(self):
        self.all_bricks = []
        self.create_bricks()

    def check_collision(self, ball):
        """Знищує цеглинку, у яку влучив м'яч, і відбиває м'яч. Повертає очки за цеглинку (0, якщо влучання не було)."""
        for brick in self.all_bricks:
            half_w = brick.width_px / 2 + BALL_RADIUS
            half_h = brick.height_px / 2 + BALL_RADIUS
            dx = abs(ball.xcor() - brick.xcor())
            dy = abs(ball.ycor() - brick.ycor())
            if dx < half_w and dy < half_h:
                # відбиваємо по осі з меншим проникненням
                if half_w - dx < half_h - dy:
                    ball.bounce_x()
                else:
                    ball.bounce_y()
                brick.hideturtle()
                self.all_bricks.remove(brick)
                return brick.points
        return 0

    def create_bricks(self):
        for row, color in enumerate(COLORS):
            y = FIRST_Y - row * (BRICK_HEIGHT + GAP)
            for col in range(COLUMNS):
                x = FIRST_X + col * (BRICK_WIDTH + GAP)
                points = len(COLORS) - row  # верхні рядки дають більше очок
                self.all_bricks.append(Brick(x, y, color, points))
