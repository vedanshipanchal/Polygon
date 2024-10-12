import turtle

turtle.Screen().bgcolor("green")
turtle.Screen().setup(500,500)

pencil = turtle.Turtle()

#1 triangle
pencil.forward(200)

pencil.left(120)
pencil.forward(200)

pencil.left(120)
pencil.forward(200)

#move pencil
pencil.penup()
pencil.right(150)
pencil.forward(100)

#2 triangle start draw
pencil.pendown()
pencil.right(90)
pencil.forward(200)

pencil.right(120)
pencil.forward(200)

pencil.right(120)
pencil.forward(200)





turtle.done()