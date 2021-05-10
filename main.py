from turtle import *
from random import *
import turtle
import time

# SCREEN SETUP
import turtle
my_window = turtle.Screen() 
my_window.bgcolor("navy")      
color(800, 500)
print("\n \n Turtle Race")
color("chocolate")
print("By @YashasShah")
print("Instructions: Move the tutle with the key")
print("Cyan Turtle: Space Bar") 
print("Pink Turtle: Backspace Key ")
print("Brown turtle: Right Arrow Key")
speed(0)

# HEADING
penup()
goto(-100, 205)
color("white")
write("TURTLE RACE", font=("Arial", 20, "bold"))

# DIRT
goto(-350, 200)
pendown()
color("forestgreen")
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

# FINISH LINE
gap_size = 20
shape("square")
penup()

# WHITE SQUARES ROW 1
color("white")
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()

# WHITE SQUARES ROW 2
for i in range(10):
    goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
    stamp()

# BLACK SQUARES ROW 1
color("black")
for i in range(10):
    goto(250, (190 - (i * gap_size * 2)))
    stamp()

# BLACK SQUARES ROW 2
for i in range(10):
    goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
    stamp()
    
# TURTLE 1 - BLUE
blue_turtle = Turtle()
blue_turtle.color("cyan")
blue_turtle.shape("turtle")
blue_turtle.penup()
blue_turtle.goto(-300, 150)
blue_turtle.pendown()
    
# TURTLE 2 - PINK
pink_turtle = Turtle()
pink_turtle.color("magenta")
pink_turtle.shape("turtle")
pink_turtle.penup()
pink_turtle.goto(-300, 50)
pink_turtle.pendown()    
    
# TURTLE 3 - YELLOW
yellow_turtle = Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.penup()
yellow_turtle.goto(-300, -50)
yellow_turtle.pendown()    
  
# TURTLE 4 - GREEN
green_turtle = Turtle()
green_turtle.color("chocolate")
green_turtle.shape("turtle")
green_turtle.penup()
green_turtle.goto(-300, -150)
green_turtle.pendown()    

# PAUSE FOR 1 SECOND BEFORE RACING
time.sleep(1)
from turtle import *

def blueTurtle():
  blueDistance = 100
  blue_turtle.forward(blueDistance)
  b = blue_turtle.xpos()
  done()

def greenTurtle():
  greenDistance = 100 
  green_turtle.forward(greenDistance)
  g = green_turtle.xpos()
  done()

def yellowTurtle():
  yellowDistance = 100
  yellow_turtle.forward(yellowDistance)
  y = yellow_turtle.xpos()
  done()

def pinkTurtle():
  pinkDistance = 100
  pink_turtle.forward(pinkDistance)
  p = pink_turtle.xpos()
  done()


# KEY PRESS
screen = turtle.Screen()
screen.listen()
screen.onkey(blueTurtle, "space")
screen.onkey(greenTurtle, "right")
screen.onkey(yellowTurtle, "enter")
screen.onkey(pinkTurtle, "backspace")

#################################################################
