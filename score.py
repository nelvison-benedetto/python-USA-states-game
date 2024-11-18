from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Times New Roman", 25, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("blue")
        self.hideturtle()
        self.penup()
        self.goto(120,245)
        self.high_score = self.get_high_score()

    def get_high_score(self):
        try:
            with open("scores.txt", mode="r") as file_scores:
                return int(file_scores.read().strip())
        except(FileNotFoundError, ValueError):
            return 0

    def update_scoreboard(self):
        with open("scores.txt", mode="r") as file_scores:
            self.content = file_scores.read()
        self.write(f"Score: {self.score}\nHight Score: {self.content}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        if(self.score > self.high_score):
            self.high_score = self.score
            with open("scores.txt", mode="w") as file_scores:
                file_scores.seek(0)
                file_scores.write(str(self.high_score))
                file_scores.truncate()
        self.update_scoreboard()