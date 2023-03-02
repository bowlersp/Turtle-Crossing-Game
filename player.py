from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90
DOWN = 270


class Player(Turtle):

    def __init__(self, STARTING_POSITION):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.go_to_start()

    def go_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)
        #self.setheading(DOWN)
        #new_y = self.ycor() - 10
        #self.goto(self.xcor(), new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            pass
