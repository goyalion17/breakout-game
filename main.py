import time
from turtle import Screen

import sounds
from ball import Ball
from bricks import Bricks
from paddle import Paddle
from scoreboard import Scoreboard

MAX_LEVEL = 3

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Breakout - Level 1")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard()

level = 1
running = False  # гра стоїть на паузі, поки не натиснуто пробіл
game_is_on = True


def toggle_pause():
    global running
    running = not running
    if running:
        scoreboard.clear_message()
    else:
        scoreboard.show_message("PAUSED - press SPACE")


def next_level():
    global level, running
    level += 1
    screen.title(f"Breakout - Level {level}")
    bricks.create_bricks()
    ball.set_level(level)
    ball.reset_position()
    running = False
    scoreboard.show_message(f"LEVEL {level} - press SPACE")


screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(toggle_pause, "space")

scoreboard.show_message("Press SPACE to start")

while game_is_on:
    screen.update()
    if not running:
        time.sleep(0.05)
        continue

    time.sleep(ball.move_speed)
    ball.move()

    # бічні стіни (екран 600 шириною, м'яч 20: 300 - 10 - запас)
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    # стеля (екран 800 висотою: 400 - 10 - запас)
    if ball.ycor() > 380:
        ball.bounce_y()

    # платформа (верх платформи -340, радіус м'яча 10, половина платформи 60)
    if ball.y_move < 0 and ball.ycor() < -330 and abs(ball.xcor() - paddle.xcor()) < 70:
        ball.bounce_off_paddle((ball.xcor() - paddle.xcor()) / 70)
        ball.speed_up()
        sounds.play("Tink")

    # цеглинки
    points = bricks.check_collision(ball)
    if points:
        sounds.play("Pop")
        scoreboard.add_points(points)
        if not bricks.all_bricks:
            if level == MAX_LEVEL:
                sounds.play("Glass")
                scoreboard.you_win()
                game_is_on = False
            else:
                next_level()

    # м'яч впав нижче платформи
    if ball.ycor() < -390:
        sounds.play("Basso")
        scoreboard.lose_life()
        ball.reset_position()
        if scoreboard.lives == 0:
            sounds.play("Sosumi")
            scoreboard.game_over()
            game_is_on = False
        else:
            running = False
            scoreboard.show_message("Press SPACE")

scoreboard.save_high_score()
screen.update()
screen.exitonclick()
