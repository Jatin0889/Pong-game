from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=0.5)
        self.penup()
        self.goto(position)

    def center_line(self):
         self.shape("square")
         self.color("white")
         self.goto(0,0)
         self.shapesize(stretch_wid=0.5,stretch_len=0.5)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
