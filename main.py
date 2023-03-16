import turtle

t=turtle.Turtle()

t.penup()
t.goto(10,-200)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(250)
t.end_fill()

t.width(40)

def logo(x,y,c):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(c)
    t.left(180)
    t.circle(50,270)
    t.forward(180)
    t.left(180)
    t.circle(50,90)

logo(0,40,"#DB0F3C")
logo(-5,53,"#50EBE7")
t.width(30)
logo(-5,45,"#FFFFFF")
t.penup()
t.goto(10,-350)
t.pendown()
t.pencolor("black")
t.write("TikTok", align="center", font=("Arial", 90, "bold"))
turtle.done()
