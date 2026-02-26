from turtle import Turtle, Screen
import time
START_POSITIONS = [(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in START_POSITIONS:
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.pu()
            snake_segment.goto(i)
            self.segments.append(snake_segment)

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[seg_num - 1].xcor()
            new_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcor, new_ycor)
        self.segments[0].fd(20)

