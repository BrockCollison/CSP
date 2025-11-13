import turtle as trtl

#Screen setup
wn = trtl.Screen()
wn.setup(width=800, height =600)
wn.bgpic("bg.gif")
wn.title("Veteran Letter")

wn.addshape("envv.gif")
wn.addshape("open_envv.gif")
wn.addshape("airforce.gif")
wn.addshape("spaceforce.gif")
wn.addshape("coastguard.gif")
wn.addshape("army.gif")
wn.addshape("marine.gif")
wn.addshape("navy.gif")


#Setup envelope
setup = trtl.Turtle(shape= "envv.gif")
setup.shapesize()

def open_envelope(x,y):
    envelope.shape("open_envv.gif")
    user_message = wn.textinput("Name", "What's your name?")

    if user_message:
        writer = trtl.Turtle()
        envelope.hideturtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(-395, 140)
        writer.write(f"Thank you for your service, {user_message}!", font=("Airborne 86", 40, "bold"))
        writer.hideturtle()
        writer.penup()
        writer.goto(-395,70)
        writer.write("Choose a branch...", font =("Airborne 86", 40, "bold"))

        positions = [(-270, -100), (-150, -150), (-30, -100), (70, -150), (170, -100), (270, -150)]
        branch_images = ["marine.gif", "navy.gif", "army.gif", "airforce.gif", "coastguard.gif", "spaceforce.gif"]

         
        for i in range(len(branch_images)):
            emblem = trtl.Turtle(shape=branch_images[i])
            emblem.penup()
            emblem.goto(positions[i])

envelope.onclick(open_envelope)

wn.mainloop()
