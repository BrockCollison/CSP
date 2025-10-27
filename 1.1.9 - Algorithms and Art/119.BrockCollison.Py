import turtle as trtl

trtl.addshape("paint_brush", ((-5,-20), (5,-20),(5,0),(8,10),(0,20),(-8,10),(0,20),(-8,10),(-5,0)))
painter = trtl.Turtle(shape="paint_brush")

screen = trtl.Screen() #How do I set the screen measurements so I could create a drawing more easily?
screen.setup(width=600, height=400) 

#Make list of months and seasons 
Months = ["January", "Feburary", "March", "April", "May","June","July", "August", "September","October", "November", "December"]
Seasons = ["Winter", "Spring","Summer","Fall"]


  
#---------------------------------------------------------

#Create different drawings based on the seasons
def Fall_Draw():
    painter.speed(10)
    painter.penup()
    painter.goto(-300, -20)
    painter.color("brown")
    painter.pendown()
    painter.begin_fill()
    for i in range(2):
        painter.forward(600)
        painter.right(90)
        painter.forward(180)
        painter.right(90)
    
    painter.end_fill()
    painter.penup()
    painter.goto(0,-20)
    painter.color("orange")
    painter.pendown()
    painter.begin_fill()
    radius = 40
    painter.circle(radius)
    painter.end_fill()
    painter.penup()
    painter.goto(15,15)
    painter.color("black")
    painter.pendown()
    painter.begin_fill()
    radius = 5
    painter.circle(radius)
    painter.end_fill()
    painter.penup()
    painter.goto(-15,15)
    painter.color("black")
    painter.pendown()
    painter.begin_fill()
    radius = 5
    painter.circle(radius)
    painter.end_fill()
    painter.penup()
    painter.goto(-5,60)
    painter.left(90)
    painter.color("green")
    painter.pendown()
    painter.begin_fill()
    for i in range(2):
          painter.forward(20)
          painter.right(90)
          painter.forward(10)
          painter.right(90)
    painter.end_fill()
    painter.penup()
    painter.goto(-10, 0)
    painter.color("black")
    painter.setheading(-60)
    painter.pendown()
    painter.circle(10, 120)
    painter.penup()
    painter.goto(-300,0)

#----------------------------------------

def Winter_Draw():
    painter.speed(10)
    painter.penup()
    painter.goto(-300, -20)
    painter.color("white")
    painter.pendown()
    painter.begin_fill()
    for i in range(2):
        painter.forward(600)
        painter.right(90)
        painter.forward(180)
        painter.right(90)
    
    painter.end_fill()
    painter.penup()
    painter.goto(0,-20)
    painter.color("white")
    painter.pendown()
    painter.begin_fill()
    radius = 40
    painter.circle(radius)
    painter.end_fill()
    painter.penup()
    painter.goto(0,60)
    painter.color("white")
    painter.pendown()
    painter.begin_fill()
    radius = 30
    painter.circle(radius)
    painter.end_fill()
    painter.penup()
    painter.goto(0,120)
    painter.color("white")
    painter.pendown()
    painter.begin_fill()
    radius = 20
    painter.circle(radius)
    painter.end_fill()
    painter.penup()
    painter.goto(-5,160)
    painter.left(90)
    painter.color("black")
    painter.pendown()
    painter.begin_fill()
    for i in range(2):
          painter.forward(20)
          painter.right(90)
          painter.forward(10)
          painter.right(90)
    painter.end_fill()
    painter.left(90)
    painter.forward(15)
    painter.right(180)
    painter.forward(40)
    painter.penup()
    painter.goto(20, 145)
    painter.color("orange")
    painter.pendown()
    painter.begin_fill()
   
    painter.left(30)
    painter.forward(10)
    painter.right(120)
    painter.forward(10)
    painter.right(30)
    
    painter.end_fill()
    painter.penup()
    painter.goto(-100,-20)
    
   
 #------------------------------------------         
    

def Spring_Draw():
    painter.penup()
    painter.goto(-300, -20)
    painter.color("green")
    painter.pendown()
    painter.begin_fill()
    for i in range(2):
        painter.forward(600)
        painter.right(90)
        painter.forward(180)
        painter.right(90)
    
    painter.end_fill()
    painter.penup()
    painter.goto(0,-20)
    painter.color("orange")
    painter.pendown()
    painter.begin_fill()
    radius = 40
    painter.circle(radius)
    painter.end_fill()
    painter.penup()
    painter.goto(15,15)
    painter.color("black")
    painter.pendown()
    painter.begin_fill()
    radius = 5
    painter.circle(radius)
    painter.end_fill()
    painter.penup()
    painter.goto(-15,15)
    painter.color("black")
    painter.pendown()
    painter.begin_fill()
    radius = 5
    painter.circle(radius)
    painter.end_fill()
    painter.penup()
    painter.goto(-5,60)
    painter.left(90)
    painter.color("green")
    painter.pendown()
    painter.begin_fill()
    for i in range(2):
          painter.forward(20)
          painter.right(90)
          painter.forward(10)
          painter.right(90)
    painter.end_fill()
    painter.penup()
    painter.goto(-10, 0)
    painter.color("black")
    painter.setheading(-60)
    painter.pendown()
    painter.circle(10, 120)
    painter.penup()
    painter.goto(-300,0)
#---------------------------------------------------------------

def Summer_Draw():
    painter.penup()
    painter.goto(-300, -20)
    painter.color("yellow")
    painter.pendown()
    painter.begin_fill()
    for i in range(2):
        painter.forward(600)
        painter.right(90)
        painter.forward(180)
        painter.right(90)
    
    painter.end_fill()
    painter.penup()
    painter.goto(0,-20)
    painter.color("orange")
    painter.pendown()
    painter.begin_fill()
    radius = 40
    painter.circle(radius)
    painter.end_fill()
    painter.penup()
    painter.goto(15,15)
    painter.color("black")
    painter.pendown()
    painter.begin_fill()
    radius = 5
    painter.circle(radius)
    painter.end_fill()
    painter.penup()
    painter.goto(-15,15)
    painter.color("black")
    painter.pendown()
    painter.begin_fill()
    radius = 5
    painter.circle(radius)
    painter.end_fill()
    painter.penup()
    painter.goto(-5,60)
    painter.left(90)
    painter.color("green")
    painter.pendown()
    painter.begin_fill()
    for i in range(2):
          painter.forward(20)
          painter.right(90)
          painter.forward(10)
          painter.right(90)
    painter.end_fill()
    painter.penup()
    painter.goto(-10, 0)
    painter.color("black")
    painter.setheading(-60)
    painter.pendown()
    painter.circle(10, 120)
    painter.penup()
    painter.goto(-300,0)
#------------------------------------------------

sky_color = screen.textinput("Sky Color", "Day or Night?").lower() #Option to change the time(Day or night)
if sky_color == ("day"):
      screen.bgcolor("sky blue")

else:
      screen.bgcolor("midnight blue")


def ask_draw(season):
       answer = trtl.textinput("Draw season","Would you like me to draw "+season+"? Yes or no?...")
       if answer == "yes":
              if season.lower() == "fall":
                     Fall_Draw()
              elif season.lower() == "winter":
                     Winter_Draw()
              elif season.lower() == "spring":
                     Spring_Draw()
              elif season.lower() == "summer":
                     Summer_Draw()
              else:
                    trtl.write("No drawing then ok.")   
              


#Ask what month they want 
while True:
    x = (trtl.textinput("month", "Choose a month?...")) #Enter a Month
    x= x.capitalize()

    if not x:
          trtl.bye()
          break

    if x not in Months:
            trtl.clear()
            
            continue

    
    valid = False
    if x in ["October", "November", "September"]:
            Season_Ask = (trtl.textinput("season", "Choose a season..."))
            Season_Ask = Season_Ask.capitalize()
            if Season_Ask == "Fall":
                    valid = True
            else:
                
                continue

            
                    
    elif x in ["June", "July", "August"]:
            Season_Ask = (trtl.textinput("season", "Choose a season..."))
            Season_Ask = Season_Ask.capitalize()
            if Season_Ask == "Summer":
                    valid = True
            else:
                    
                    continue


    elif x in ["November", "December", "January"]:
            Season_Ask = (trtl.textinput("season", "Choose a season..."))
            Season_Ask = Season_Ask.capitalize()
            if Season_Ask == "Winter":
                    valid = True
            else:
                
                continue

    elif x in ["March", "Feburary", "April", "May"]:
            Season_Ask = (trtl.textinput("season","Choose a season..."))
            Season_Ask = Season_Ask.capitalize()
            if Season_Ask == "Spring":
                    valid = True
            else:
                trtl.write("That's not part of the Spring season...")
                continue
    

    if valid :
           print(f"{Season_Ask} is a nice season!")
           ask_draw(Season_Ask)

    else:
           trtl.clear()
           trtl.write(f"{Season_Ask} is not the correct season for {x}. Try again.")


    retry = trtl.textinput("Try Again?", "Would you like to try again? (yes/no)")

    if not retry or retry.lower() != "yes":
        
        trtl.bye()
        break
    else:
          trtl.resetscreen()
          screen = trtl.Screen()
          screen.setup(width=600, height=400)
          
          
          sky_color = screen.textinput("Sky Color", "Day or Night?").lower() #Option to change the time(Day or night)
          if sky_color == ("day"):
                screen.bgcolor("sky blue")

          else:
                screen.bgcolor("midnight blue")


           
           



#-------------------------------------------




    

        






       

       






wn = trtl.Screen()
wn.mainloop()