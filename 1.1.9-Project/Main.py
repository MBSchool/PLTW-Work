import turtle as trtl
wn = trtl.Screen()

# Setup Varibles and Make them easier to edit

creator = trtl.Turtle()
bg_color = "#3289a8"
bg_shape = "shop.gif"
bowl_color = "white"
yougurt_color = "pink"
bowl_size = 10

# Adding Topping variables

# Banna
banana_pos1 = (-150, 10)
banana_shape = "BaNANANN.gif"
bannaa_size = 0.5

#strawberry
strawberry_pos1 = (100, 30)
strawberry_shape= "strawberry.gif"
strawberry_size = 0.5

# Def Reset

def reset1():
    creator.color("black")
    creator.shapesize(0.2)
    creator.shape("arrow")
    creator.pensize(1)
    creator.penup()
    print("Creator Reset Made")

# Adding a background image
    
wn.register_shape('shop.gif')

reset1()
creator.goto(0,0)
creator.pendown()
creator.shape(bg_shape)
creator.shapesize(100)
creator.stamp()
reset1()

'''# Make Background a color 
    
creator.goto(0,0)
creator.shapesize(90)
creator.shape("circle")
creator.color(bg_color)
creator.stamp()
print("Background Made")
'''
# Adding TIttle Text

reset1()
creator.goto(-350,300)
creator.write("The Yogurt Shop", font=("Impact", "80", "normal"))
print("Tittle Text made")

# Adding Black RIm to Bowl

reset1()
creator.pensize(505)
creator.goto(0, 0,)
creator.pencolor("black")
creator.pendown()
creator.circle(bowl_size)
print("Bowl Rim Made")
# Draw Bowl

reset1()
creator.pensize(500)
creator.goto(0, 0,)
creator.pencolor(bowl_color)
creator.pendown()
creator.circle(bowl_size)
print("Bowl Rim Made")
# Add yogurt

reset1()
creator.pensize(400)
creator.goto(0, 0,)
creator.pencolor(yougurt_color)
creator.pendown()
creator.circle(8)
print("Yogurt Made")
# Add First topping

banana = input("Banana? (y/n):  ")
wn.register_shape('BaNANANN.gif')
if banana == "y":
    reset1()
    creator.goto(banana_pos1)
    creator.pendown()
    creator.shape(banana_shape)
    creator.shapesize(bannaa_size)
    creator.stamp()
elif banana == "n":
        print("Moving on!")

# Add Second Topping 
    
strawberry = input("Strawberry? (y/n):  ")
wn.register_shape('strawberry.gif')
if strawberry == "y":
    reset1()
    creator.goto(strawberry_pos1)
    creator.pendown()
    creator.shape(strawberry_shape)
    creator.shapesize(strawberry_size)
    creator.stamp()

#  Looping Screen
    
wn.mainloop()
