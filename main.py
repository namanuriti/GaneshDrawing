#imports
import turtle as t
#variables
screen = t.Screen()
ganesh = t.Turtle()
blue = '#10557d'
white = '#ffffff'
red = '#ff0004'
black = '#000000'
yellow = '#ffb700'

screen.title('Ganesh Drawing')
ganesh.shape('turtle')

# pentagon
ganesh.color(blue, blue)
ganesh.begin_fill()
ganesh.left(angle=130)
ganesh.forward(distance=55)
ganesh.right(90)
ganesh.forward(70)
ganesh.right(65)
ganesh.forward(70)
ganesh.right(80)
ganesh.forward(55)
ganesh.right(70)
ganesh.forward(66)
ganesh.end_fill()

ganesh.penup()
ganesh.forward(10)
ganesh.left(90)
ganesh.forward(12.5)
ganesh.pendown()

#square
ganesh.color(yellow, yellow)
ganesh.begin_fill()
ganesh.forward(90)
for _ in range(3):
    ganesh.left(90)
    ganesh.forward(90)
ganesh.end_fill()

ganesh.penup()
ganesh.forward(10)
ganesh.pendown()

#rectangle 1
ganesh.color(red, red)
ganesh.begin_fill()
for _ in range(2):
    ganesh.forward(27.5)
    ganesh.right(90)
    ganesh.backward(90)
    ganesh.right(90)

ganesh.penup()
ganesh.right(180)
ganesh.forward(137.5)
ganesh.pendown()

#rectangle 2
for _ in range(2):
    ganesh.backward(27.5)
    ganesh.right(90)
    ganesh.forward(90)
    ganesh.right(90)
ganesh.end_fill()

ganesh.penup()
ganesh.left(180)
ganesh.forward(57.5)
ganesh.left(90)
ganesh.forward(5)
ganesh.left(90)
ganesh.pendown()

# Bindi line 1
ganesh.color(white)
ganesh.backward(50)

ganesh.penup()
ganesh.right(90)
ganesh.forward(5)
ganesh.left(90)
ganesh.pendown()

#Bindi line 2
ganesh.forward(50)

ganesh.penup()
ganesh.right(90)
ganesh.forward(5)
ganesh.left(90)
ganesh.pendown()

#Bindi line 3
ganesh.backward(50)

ganesh.penup()
ganesh.right(90)
ganesh.forward(10)
ganesh.pendown()

#Eye 1
ganesh.color(black, black)
ganesh.begin_fill()
ganesh.circle(5)

ganesh.penup()
ganesh.left(90)
ganesh.forward(50)
ganesh.pendown()

#Eye 2
ganesh.circle(5)
ganesh.end_fill()

ganesh.penup()
ganesh.right(180)
ganesh.forward(30)
ganesh.left(90)
ganesh.forward(25)
ganesh.pendown()

#Nose
ganesh.color(red, red)
ganesh.begin_fill()
ganesh.forward(100)
ganesh.left(90)
ganesh.forward(50)
ganesh.left(90)
ganesh.forward(20)
ganesh.left(90)
ganesh.forward(30)
ganesh.right(90)
ganesh.forward(80)
ganesh.end_fill()

# finisher
ganesh.penup()
ganesh.forward(1000)

screen.mainloop()