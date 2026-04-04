#Coreonte Bishop
#4/3/2026
#P4Lab1
#Use turtle and loops to draw a square and a triangle

#Import the library
import turtle

#Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()
win.bgcolor("lightblue")


#Set turtle options
pen.pensize(5)
pen.pencolor("green")
pen.shape("arrow")

#Code to draw the shapes
pen.fillcolor("magenta")
pen.begin_fill()

for side in range(4):
    pen.forward(200)
    pen.left(90)

pen.end_fill()

#Move turtle to top of the square
pen.left(90)
pen.forward(200)
pen.right(90)

#Draw triangle (filled)
pen.fillcolor("orange")
pen.begin_fill()

#Write loop that executes 3 times
sides = 3

while sides > 0:
    pen.forward(200)
    pen.left(120)
    sides = sides - 1

pen.end_fill()

#Wait for user to close window
win.mainloop()

