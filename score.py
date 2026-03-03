from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hi_score = self.get_hi_score()
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score is: {self.score}, Hi Score:{self.hi_score} ", False,"center",("Courier", 8, "normal") )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def keep_score(self):
        if self.score > self.hi_score:
            self.hi_score = self.score
            with open("data.txt", "w") as f:
                f.write(str(self.hi_score))
        self.score = 0
        self.update_score()

    def get_hi_score(self):
        with open("data.txt") as f:
            return int(f.readline())

    # def display_game_over(self):
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write(f"GAME OVER", False,"center",("Courier", 8, "normal") )