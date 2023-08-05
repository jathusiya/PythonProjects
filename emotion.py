import turtle

emo = turtle.Turtle()

#center of circle--face
emo.up()
emo.goto(0,-100)
emo.down()

#fill yellow color circle
emo.begin_fill()
emo.pendown()
emo.fillcolor('yellow')
emo.circle(100)
emo.end_fill()

#smile
emo.up()
emo.goto(-67,-40)
emo.setheading(-60)
emo.width(5)
emo.down()
emo.circle(80,120)
emo.fillcolor("black")

#to make eyes
for i in range(-35,105,70):
    emo.up()
    emo.goto(i,35)
    emo.setheading(0)
    emo.begin_fill()
    emo.circle(10)
    emo.end_fill()
emo.penup()
emo.goto(0,-150)

turtle.mainloop()