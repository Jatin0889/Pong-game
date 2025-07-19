from turtle import Turtle

class Center_line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.goto(0, 300)
        self.setheading(270)

        while self.ycor() - 10 > -300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        self.penup()

