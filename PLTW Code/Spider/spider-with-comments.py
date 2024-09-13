#   a116_buggy_image.py
import turtle as trtl

#    Sets the turtle to spider for easier use | Setting up body

spider = trtl.Turtle()
spider.circle(20)

#   Configure spider legs

legs = 8
length = 70
angle = 360 / legs
spider.pensize(5)

#     Draw legs

counter = 0
while (counter < legs):
  spider.goto(0,20)
  spider.setheading(angle*counter)
  spider.forward(length)
  counter = counter + 1

#    End and looping visual
spider.hideturtle()
wn = trtl.Screen() 
wn.mainloop()