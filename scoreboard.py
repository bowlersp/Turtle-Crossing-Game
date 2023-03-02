from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.score = 0
        self.color("black")
        self.updatescoreboard()


    def updatescoreboard(self):
        self.penup()
        self.write(f"Level {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.penup()
        self.clear()
        self.score += 1
        self.updatescoreboard()


    def you_lose(self):
        self.penup()
        self.goto(0, 0)
        self.color("black")
        self.write(f"NICE TRY BUT YOU SUCK!!\n "
                   f"      TRY AGAIN!!", align="center", font=FONT)
