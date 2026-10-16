from pathlib import Path
from turtle import Turtle

FONT = ("Courier", 20, "bold")
MESSAGE_FONT = ("Courier", 28, "bold")
STARTING_LIVES = 3
HIGH_SCORE_FILE = Path(__file__).parent / "high_score.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = STARTING_LIVES
        self.high_score = self.load_high_score()
        self.messenger = Turtle()
        self.messenger.hideturtle()
        self.messenger.penup()
        self.messenger.color("white")
        self.update_scoreboard()

    def load_high_score(self):
        try:
            return int(HIGH_SCORE_FILE.read_text().strip())
        except (OSError, ValueError):
            return 0

    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            try:
                HIGH_SCORE_FILE.write_text(str(self.high_score))
            except OSError:
                pass
            self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 340)
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.goto(0, 340)
        self.write(f"High: {self.high_score}", align="center", font=FONT)
        self.goto(280, 340)
        self.write(f"Lives: {self.lives}", align="right", font=FONT)

    def add_points(self, points):
        self.score += points
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def show_message(self, text):
        self.messenger.clear()
        self.messenger.goto(0, -100)
        self.messenger.write(text, align="center", font=MESSAGE_FONT)

    def clear_message(self):
        self.messenger.clear()

    def game_over(self):
        self.show_message("GAME OVER")

    def you_win(self):
        self.show_message("YOU WIN!")
