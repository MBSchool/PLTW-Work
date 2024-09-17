import turtle as trtl
wn = trtl.Screen()
# Setup Varibles and Make them easier to edit

creator = trtl.Turtle()
bg_color = "#3289a8"
bowl_color = "white"
yougurt_color = "pink"
bowl_size = 10
banana_pos1 = (10, 10)
banana_shape = "BaNANANN.gif"
bannaa_


# Def Reset

def reset1():
    creator.color("black")
    creator.shapesize(0.2)
    creator.pensize(1)
    creator.penup()

# Make Background a color 
    
creator.goto(0,0)
creator.shapesize(90)
creator.shape("circle")
creator.color(bg_color)
creator.stamp()

# Draw Bowl
reset1()
creator.pensize(500)
creator.goto(0, 0,)
creator.pencolor(bowl_color)
creator.pendown()
creator.circle(bowl_size)

# Add yogurt
reset1()
creator.pensize(400)
creator.goto(0, 0,)
creator.pencolor(yougurt_color)
creator.pendown()
creator.circle(8)

# Adding TIttle Text
reset1()
creator.goto(-400,300)
creator.write("The Yogurt Shop", font=("Arial", "80", "normal"))

# Add First topping
banana = input("Banana? (y/n)")
wn.register_shape('BaNANANN.gif')
if banana == "y":
    reset1
    creator.goto(banana_pos1)
    creator.pendown()
    creator.shape(banana_shape)
    creator.shapesize(1)
    creator.stamp()


#  Looping Screen
    
wn.mainloop()
