import turtle
import figures
# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Side length
side_length = 50
length_a = 50
length_b = 100
figures.draw_square(side_length)

figures.draw_rectangle(length_a, length_b)

figures.draw_triangle(side_length)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()