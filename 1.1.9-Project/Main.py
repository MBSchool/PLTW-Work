import turtle as trtl
wn = trtl.Screen()
# Setup Varibles and Make them easier to edit

creator = trtl.Turtle()
bg_color = "#3289a8"
bowl_color = "white"
yougurt_color = "pink"
bowl_size = 10
banana_pos1 = (-150, 10)
banana_shape = "BaNANANN.gif"
bannaa_size = 0.5


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

# Adding TIttle Text
reset1()
creator.goto(-350,300)
creator.write("The Yogurt Shop", font=("Impact", "80", "normal"))


# Adding Black RIm to Bowl
reset1()
creator.pensize(505)
creator.goto(0, 0,)
creator.pencolor("black")
creator.pendown()
creator.circle(bowl_size)

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



# Add First topping
banana = "y"    # input("Banana? (y/n):  ")
wn.register_shape('BaNANANN.gif')
if banana == "y":
    reset1()
    creator.goto(banana_pos1)
    creator.pendown()
    creator.shape(banana_shape)
    creator.shapesize(bannaa_size)
    creator.stamp()


#  Looping Screen
    
wn.mainloop()
