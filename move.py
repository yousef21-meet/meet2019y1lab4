import turtle

ycord = ycor()
xcord = xcor()

def up():
    turtle.goto(xcor(), ycord + 10)
    
def down():
    minus_y = turtle.ycor()
    minus_y = minus_y - 10

def left():
    minus_x = turtle.xcor()
    minus_x = minus_x - 10

def right():
    add_x = turtle.xcor()
    add_x = add_x + 10

turtle.onkeypress(up, "w")
turtle.onkeypress(down, "s")
turtle.onkeypress(left, "a")
turtle.onkeypress(right, "d")

turtle.listen()

turtle.mainloop()
