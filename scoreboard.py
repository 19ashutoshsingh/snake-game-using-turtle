from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Ariel", 24, "normal")
FONT2 = ("Ariel", 18, "normal")
FONT3 = ("Ariel", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.h_score = self.load_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()

        # self.goto(200, 290)
        # self.update_h_score()

        self.goto(0, 290)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # def update_h_score(self):
    #     self.clear()
    #     self.write(f"HS: {self.h_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
        # self.update_h_score()

    def game_over(self):
        screen = Screen()
        screen.title("Game Over.")
        msg = f"GAME OVER.\nScore: {self.score}    |    Previous HS: {self.h_score}"
        lines = msg.split("\n")
        x, y = 0, 30

        for line in lines:
            self.goto(x, y)
            self.write(line, align=ALIGNMENT, font=FONT2)
            y -= 30
        self.goto(x, y)
        self.write("Press 'r' to restart the game.", align=ALIGNMENT, font=FONT3)

        self.check_high_score()

    def check_high_score(self):
        if self.score > self.h_score:
            self.h_score = self.score
            self.save_high_score()

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.h_score))

