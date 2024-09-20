import turtle as trtl
wn = trtl.Screen()

# Setup Varibles and Make them easier to edit

creator = trtl.Turtle()
wn.setup(1000, 900)  # Makes Window set height
creator.speed(10000)
bg_color = "#3289a8"
bg_shape = "shop.gif"
bowl_color = "white"
yougurt_color = "pink"
bowl_size = 10

# Adding Topping variables

# Banna
banana_pos1 = (-150, 10)
banana_pos2 = (-150, 15)
banana_pos3 = (-150, 20)
banana_pos4 = (-150, 25)
banana_pos5 = (-150, 30)

banana_shape = "BaNANANN.gif"
bannaa_size = 0.5

#strawberry
strawberry_pos1 = (0, 0)
strawberry_shape= "strawberry.gif"
strawberry_size = 0.1

# Def Reset


def banna():
    creator.pendown()
    creator.shape(banana_shape)
    creator.shapesize(bannaa_size)
    creator.stamp()

def strawberry():
    creator.pendown()
    creator.shape(strawberry_shape)
    creator.shapesize(strawberry_size)
    creator.stamp()


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

# Adding Title Text with Drop Shadow

reset1()
creator.goto(-350 + 5, 300 - 5)  # Offset position for shadow
creator.color("white")  # Shadow color
creator.write("The Yogurt Shop", font=("Impact", 80, "normal"))


# Main text (black color, original position)
reset1()
creator.goto(-350, 300)  # Original position
creator.color("black")  # Main text color
creator.write("The Yogurt Shop", font=("Impact", 80, "normal"))


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
    creator.goto()
    banna()
    creator.goto(banana_pos2)
    banana
else:
    print("Moving on!")

# Add Second Topping 
    
strawberry = input("Strawberry? (y/n):  ")
wn.register_shape('strawberry.gif')
if strawberry == "y":
    reset1()
    

#  Looping Screen
    
wn.mainloop()
