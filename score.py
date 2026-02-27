from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"Score is: {self.score} ", False,"center",("Arial", 8, "normal") )