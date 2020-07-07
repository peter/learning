# You can edit this code and run it right here in the browser!
# First we'll import some turtles and shapes:
from turtle import *
from shapes import *

# Create a turtle named Tommy:
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(7)

# Draw three circles:
draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)

# Write a little message:
tommy.penup()
tommy.goto(0,-50)
tommy.color("black")
tommy.write("Teach With Code!", None, "center", 16)
tommy.goto(0,-80)

done()
# Try changing draw_circle to draw_square, draw_triangle, or draw_star
