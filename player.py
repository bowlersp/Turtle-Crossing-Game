from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90
DOWN = 270



class Player(Turtle):
    
  def __init__(self,STARTING_POSITION):
    super().__init__()
    self.penup()
    self.shape("turtle")
    self.color("black")
    self.shapesize(stretch_wid=1, stretch_len=1)
    self.goto(STARTING_POSITION)

  def go_up(self):
    self.setheading(UP)
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)

  def go_down(self):
    self.setheading(DOWN)
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)
