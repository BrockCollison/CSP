import turtle as trtl
import random as rand

#Intializing
car_image = ""
wn = trtl.Screen() 
wn.setup(width=600, height=400)
wn.bgcolor("lightgrey")

cars = []
car_colors = ["red", "green", "blue", "yellow"]
player_colors = ["red","blue","yellow","green","orange"]

setup = trtl.Turtle()

#TODO Create a leaderboard that displays a score based on how long the user has lasted.

#TODO  Incorporate randomly placed  cars that will try to hit the player.

#TODO  Make a collide feature where the game ends if the player comes in contact with a car.

#TODO  Create the actual game layout where there are three columns in which the player can move 

setup.pencolor("yellow")
setup.pensize(4)
setup.speed(0)
setup.penup()
setup.goto(-100,-200)
setup.left(90)
setup.pendown()
setup.forward(400)
setup.penup()
setup.goto(100,-200)
setup.pendown()
setup.forward(400)
setup.hideturtle()

#Make a player 
player = trtl.Turtle(shape = "turtle")
player_colors = wn.textinput("Player color", "Choose a color...").lower() 
if player_colors == ("red"):
      player.color("red")
elif player_colors == ("blue"):
      player.color("blue")
elif player_colors == ("yellow"):
      player.color("yellow")
elif player_colors == ("orange"):
      player.color("orange")
elif player_colors == ("green"):
      player.color("green")
elif player_colors == ("black"):
      player.color("black")
elif player_colors == ("white"):
      player.color("white")
elif player_colors == ("lightgrey"):
      player.color("lightgrey")

player.shapesize(2.5)
player.speed(0)
player.penup()
player.goto(0,-150)
player.left(90)

def go_left():
    x = player.xcor()
    x -= 200
    if x >= -200:
      player.setx(x)

def go_right():
    x = player.xcor()
    x += 200
    if x <= 200:
       player.setx(x)



wn.listen()
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")






wn = trtl.Screen()
wn.mainloop()
