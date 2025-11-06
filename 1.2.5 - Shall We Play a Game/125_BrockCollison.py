
import turtle as trtl
import random as rand
import time

# --- SETUP WINDOW ---
wn = trtl.Screen()
wn.setup(width=600, height=400)
wn.bgcolor("lightgrey")
wn.title("Turtle Car Dodge Game. Use arrow keys only.")
wn.tracer(0)

# --- DRAW LANE LINES ---
setup = trtl.Turtle()
setup.hideturtle()
setup.speed(0)
setup.pencolor("yellow")
setup.pensize(4)

# Draw 4 lane lines (to create 5 lanes)
lane_positions = [-200, -100, 0, 100, 200]  # 5 lanes total, lines between them
for pos in [-150, -50, 50, 150]:
    setup.penup()
    setup.goto(pos, -200)
    setup.setheading(90)
    setup.pendown()
    setup.forward(400)

# --- PLAYER SETUP ---
player = trtl.Turtle(shape="turtle")
player.speed(0)
player.penup()
player.goto(0, -150)
player.setheading(90)
player.shapesize(2.5)

# Choose player color
color_choice = wn.textinput("Player Color", "Choose a color (red, blue, yellow, orange, green, black, white, lightgrey): ")
if color_choice:
    color_choice = color_choice.lower()
else:
    color_choice = "green"

valid_colors = ["red", "blue", "yellow", "orange", "green", "black", "white", "lightgrey"]
if color_choice in valid_colors:
    player.color(color_choice)
else:
    player.color("green")

# --- MOVEMENT CONTROLS ---
player_lanes = [-200, -100, 0, 100, 200]  

def go_left():
    x = player.xcor()
    current_index = min(range(len(player_lanes)), key=lambda i: abs(player_lanes[i]-x))
    if current_index > 0:
        player.setx(player_lanes[current_index-1])

def go_right():
    x = player.xcor()
    current_index = min(range(len(player_lanes)), key=lambda i: abs(player_lanes[i]-x))
    if current_index < len(player_lanes)-1:
        player.setx(player_lanes[current_index+1])

wn.listen()
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# --- CARS SETUP ---
car_colors = ["red", "green", "blue", "yellow", "orange", "purple"]
cars = []
car_speed = 40 # starting speed

def create_car():
    # Spawn 1-3 cars randomly across 5 lanes
    num_cars = rand.randint(1, 2)
    x_positions = player_lanes.copy()
    rand.shuffle(x_positions)

    for i in range(num_cars):
        car = trtl.Turtle("square")
        car.color(rand.choice(car_colors))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(x_positions[i], 200 + rand.randint(0, 50))
        cars.append(car)

    # Schedule next spawn WITHOUT pausing the game
    wn.ontimer(create_car, rand.randint(200, 1200))  # cars spawn asynchronously

# --- MOVE CARS ---
def move_cars():
    global car_speed
    for car in cars:
        car.sety(car.ycor() - car_speed)
        if car.ycor() < -250:
            cars.remove(car)
            car.hideturtle()
    car_speed += 0.1  # slowly increase difficulty
    wn.update()
    wn.ontimer(move_cars, 100)

# --- COLLISION DETECTION ---
def check_collision():
    for car in cars:
        if player.distance(car) < 40:
            game_over()
            return
    wn.ontimer(check_collision, 100)

# --- TIMER / SCOREBOARD ---
score_display = trtl.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-280, 170)
start_time = time.time()

def update_score():
    score_display.clear()
    elapsed = int(time.time() - start_time)
    score_display.write(f"Time: {elapsed}s", font=("Arial", 16, "bold"))
    wn.ontimer(update_score, 1000)


def game_over():
    wn.clearscreen()
    wn.bgcolor("black")
    over = trtl.Turtle()
    over.hideturtle()
    over.color("white")
    over.write(" GAME OVER ", align="center", font=("Arial", 24, "bold"))
    time_survived = int(time.time() - start_time)
    over.penup()
    over.goto(0, -40)
    over.write(f"You survived {time_survived} seconds!", align="center", font=("Arial", 18, "normal"))

 


create_car()
move_cars()
check_collision()
update_score()

wn.mainloop()
