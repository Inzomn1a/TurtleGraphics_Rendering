from turtle import Turtle, Screen
import turtle as t
import random
import colorgram
t.colormode(255)  # change colordmode to "RGB 0 - 255"


def random_color():
    """Creates a random RGB Tuple to generate a random color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    generated_color = (r, g, b)
    return generated_color


# Turtle Setup
turtle = Turtle()
turtle.hideturtle()
turtle.shape("turtle")
turtle.color(random_color())
turtle.speed(0)  # 1 slow, 10 fast, 0 fastest


def make_shape():
    """Starts drawing a triangle, adding +1 side with each loop making a full 360° turn. INFINITE LOOP"""
    number_of_sides = 3
    for repeats in range(100):  # how many shapes?
        for _ in range(number_of_sides):
            angle = 360 / number_of_sides
            turtle.right(angle)
            turtle.forward(100)
        number_of_sides += 1
        turtle.color(random_color())


def random_walk():
    """Infinite Random walk, printed on screen using Turtle Graphics Library"""
    random_direction = [0, 90, 180, 270]
    turtle_move_range = 20
    turtle.pensize(10)

    while 0 < 1:
        turtle.color(random_color())
        turtle.right(random.choice(random_direction))
        turtle.forward(turtle_move_range)


def make_spirograph():
    """Spirograph Shape, rendered on screen using Turtle Graphics Library"""
    repeat = 0
    while repeat != 36:  # interval is 10, so at 36 we made 360° turn
        turtle.forward(0)  # increase value to create gap in middle (0 == Spirograph)
        turtle.left(10)
        turtle.circle(200)
        repeat += 1
        turtle.color(random_color())


# Extract Color Pallete from imported Image (used my draw_dot_picture Function)
extracted_RGB_colors = []
extracted_colors = colorgram.extract('DotImage.jpg', 20)
for color in extracted_colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    extracted_RGB_colors.append(new_color)


def draw_dot_picture():
    """Drawing a 'Hirst Inspired' Painting (10x10 Dots)"""
    turtle_y_position = 0
    turtle.setposition(0, turtle_y_position)
    turtle.penup()
    printed_dots = 0
    while printed_dots < 100:
        for _ in range(10):
            turtle.dot(20, (random.choice(extracted_RGB_colors)))
            turtle.forward(50)
            printed_dots += 1
            turtle_y_position += 5  # ATTENTION: Should be 50. But the spacing is correct with 5. dunno wtf is going on.
        turtle.setposition(0, turtle_y_position)

# draw_dot_picture()
# make_shape()
# random_walk()
# make_spirograph()


screen = Screen()
screen.exitonclick()
