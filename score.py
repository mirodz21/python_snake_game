from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score is: {self.score} ", False,"center",("Courier", 8, "normal") )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def display_game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER", False,"center",("Courier", 8, "normal") )