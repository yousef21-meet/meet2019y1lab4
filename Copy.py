import turtle
turtle.pensize(5)
turtle.shape('circle')
arrow = turtle.clone()
arrow.pensize(10)
arrow.shape('arrow')
arrow.color('green')
turtle.color('yellow')
arrow.left(90)
arrow.goto(0,-150)
turtle.goto(0,150)
arrow.goto(75,-150)
turtle.goto(-75,150)
arrow.color('blue')
turtle.color('white')
arrow.goto(75,0)
turtle.goto(-75,0)
turtle.bgcolor('purple')
turtle.mainloop()
