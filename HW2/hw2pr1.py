from turtle import *

t = Turtle()

t.shape('turtle')  # or 'arrow'

t.speed(10)  # fastest speed!

t.color("green")
t.width(1)
t.forward(100)
t.left(90)

t.color("blue")
t.width(2)
t.forward(100)
t.left(90)

t.color('red')
t.width(1)
t.forward(100)
t.left(90)

t.color("purple")
t.width(4)
t.forward(100)
t.left(90)

##########################

from turtle import *

t = Turtle()

def tri(n):
    """Draws n 100-pixel sides of an equilateral triangle.
       Note that n doesn't have to be 3 (!)
    """
    if n == 0:
        return      # No sides to draw, so stop drawing
    else:
        t.dot(10, 'red')
        t.pencolor('darkgreen')
        t.pensize(10)
        t.forward(100)
        t.left(120)
        tri(n-1)   # Recur to draw the rest of the sides!

#
# here, run tri(3)   
#
t.fillcolor('blue')
t.begin_fill()
tri(3)
t.end_fill()

##########################################################

# import turtle
import turtle
 
# defining colors
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']
 
# setup turtle pen
t= turtle.Pen()
 
# changes the speed of the turtle
t.speed(10)
 
# changes the background color
turtle.bgcolor("black")
 
# make spiral_web
for x in range(200):
    t.pencolor(colors[x%6]) # setting color
    t.width(x/200 + 1) # setting width
    t.forward(x) # moving forward
    t.left(42) # moving left
 
turtle.done()
t.speed(10)
 
turtle.bgcolor("black") # changes the background color
 
# make spiral_web
for x in range(200):
    t.pencolor(colors[x%6]) # setting color
    t.width(x/200 + 1) # setting width
    t.forward(x) # moving forward
    t.left(42) # moving left
 
turtle.done()

###############################################################

import turtle as t

colors = ['white','green']

def svtree(trunklength, levels):
    """svtree: draws a side-view tree
       trunklength = the length of the first line drawn ("the trunk")
       levels = the depth of recursion to which it continues branching
    """
    if (levels==0): 
        return
    else:
        for x in range(100):
          t.bgcolor('black')
          t.pencolor(colors[x%2])
          t.forward(trunklength)
          t.left(45)

          svtree(trunklength/2, levels-1)

          t.right(45)
          svtree(trunklength/2, levels-1)
          t.right(45)
          svtree(trunklength/2, levels-1)

          t.left(45)
          t.backward(trunklength)
          return

svtree(100,6)

###################################################

import turtle
import random

# Setup the window with a background color
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(0)

# Create a list of colors
sfcolor = ["white", "blue", "purple", "grey", "magenta"]

# Define a function to create different sized snowflakes
def snowflake(size):
  # move the pen into starting position
  t.penup()
  t.forward(5 * size)
  t.left(45)
  t.pendown()
  t.color(random.choice(sfcolor))
  # draw branch 8 times to make a snowflake
  for i in range(10):
    branch(size)   
    t.left(45)
    
# This function creates one branch of the snowflake
def branch(size):
  for i in range(3):
    for i in range(3):
      t.forward(10.0 * size / 3)
      t.back(10.0 * size / 3)
      t.right(45)
    t.left(90)
    t.back(10.0 * size / 3)
    t.left(45)
  t.right(90) 
  t.forward(10.0 * size)

# Loop to create 20 snowflakes of different sizes and at 
# different starting locations
for i in range(20):
  x = random.randint(-200, 200)
  y = random.randint(-200, 200)
  sfsize = random.randint(1, 4)
  t.penup()
  t.goto(x, y)
  t.pendown()
  snowflake(sfsize)