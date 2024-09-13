#   a116_buggy_image.py
import turtle as trtl
spider = trtl.Turtle()
#    Variable Setup

bodysize = 2
eyesize = 0.5
innereye = 0.1
rightlegs = 4
leftlegs = 4 
length = 70
angle = 120 / rightlegs
rightcounter = 0
leftcounter = 0
pencolor = "yellow"


# - - - - - -

#  Drawing Spider body

spider.shapesize(bodysize)
spider.shape("circle")
spider.stamp()
# - - - - - -

#   Configure painter for spider legs
spider.shapesize(1)
spider.shape()
spider.pensize(5)
# - - - - - -

#     Draw Right Legs

while (rightcounter < rightlegs):
  spider.goto(0,0)
  spider.setheading(angle*rightcounter - 45)
  print(angle*rightcounter - 45)
  spider.forward(length)
  rightcounter = rightcounter + 1
  print(rightcounter)
# - - - - - -

# Draw Left Legs
  
while (leftcounter < leftlegs):
  spider.goto(0,0)
  spider.setheading(angle*leftcounter+135)
  spider.forward(length)
  leftcounter = leftcounter + 1
# - - - - - -
  
# Setting up shape for eyes
  
spider.penup()
spider.shape("circle")
spider.shapesize(eyesize)
spider.color(pencolor)

# Right Eye 

spider.goto(10,0)
spider.pendown()
spider.stamp()
spider.shapesize(innereye)
spider.color("red")
spider.stamp()
spider.penup()


# Left eye
spider.color("yellow")
spider.shapesize(eyesize)
spider.goto(-10,0)
spider.pendown()
spider.stamp()
spider.shapesize(innereye)
spider.color("red")
spider.stamp()


#    End and looping visual
spider.hideturtle()
wn = trtl.Screen() 
wn.mainloop()

# - - - - - -