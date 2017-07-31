

import turtle
turtle.shape('turtle')
square=turtle.clone()
square.shape('square')
square.goto(100,100)
square.penup()
square.goto(100,150)
square.pendown()
square.goto(100,100)
square.goto(150,100)
square.goto(150,150)
square.goto(100,150)

triangle=turtle.clone()
triangle.shape('triangle')
triangle.penup()
triangle.goto(-100,-100)
triangle.pendown()
triangle.goto(-150,-100)
triangle.goto(-150,-150)
triangle.goto(-100,-100)


import turtle
turtle.shape('turtle')
square=turtle.clone()
square.shape('square')
square.goto(100,100)
square.goto(300,300)
square.stamp()
square.goto(100,100)

turtle.shape('turtle')
triangle=turtle.clone()
triangle.shape('triangle')
triangle.goto(-70,-70)
triangle.goto(-85,-85)
triangle.stamp()
triangle.goto(-70,-70)








