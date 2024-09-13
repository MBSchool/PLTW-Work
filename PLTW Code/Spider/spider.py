#   a116_buggy_image.py
import turtle as trtl

#    Sets the turtle to spider for easier use | Setting up body

spider = trtl.Turtle()
spider.circle(20)

#   Configure spider legs

rightlegs = 4
leftlegs = 4 
length = 70
angle = 120 / rightlegs
spider.pensize(5)
# - - - - - -


#     Draw Right Legs

rightcounter = 0
while (rightcounter < rightlegs):
  spider.goto(0,20)
  spider.setheading(angle*rightcounter - 45)
  print(angle*rightcounter - 45)
  spider.forward(length)
  rightcounter = rightcounter + 1
  print(rightcounter)
# - - - - - -
  
# Draw Left Legs
  
leftcounter = 0
while (leftcounter < leftlegs):
  spider.goto(0,20)
  spider.setheading(angle*leftcounter+135)
  spider.forward(length)
  leftcounter = leftcounter + 1
# - - - - - -

#    End and looping visual
spider.hideturtle()
wn = trtl.Screen() 
wn.mainloop()