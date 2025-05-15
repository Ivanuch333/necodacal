import turtle

class Draw:
  
  def __init__(self):
    self.t = turtle.Turtle()
    self.t.hideturtle()
    self.screen = self.t.getscreen()
    self.screen.tracer(0)

  def setcolor(self, color = "RED"):
    self.t.color(color)
    self.t.penpown(color)
    

  def teleport(self, x, y):
    self.t.penup()
    self.t.goto(x, y)
    self.t.pendown()
  
  def circle(self, ball):
    self.teleport(ball.x, ball.y)
    self.t.circle(ball.radius)

  def pen(self, size):
    self.t.pensize(size)
    
    

    self.t.begin_fill()
    self.t.end_fill()
