import turtle


def customize_turtle(name, shape, color, speed):
    name.shape(shape)
    name.color(color)
    name.speed(speed)


def draw_square(who, size):
    for i in range(4):
        who.forward(size)
        who.right(90)


def draw_circle(who, size):
    who.circle(size)


def draw_triangle(who, size):
    for i in range(3):
        who.left(120)
        who.forward(size)


def run_program():
    # Creates window object for turtles to play on
    window = turtle.Screen()
    window.bgcolor("#4286f4")

    # Creating some turtles
    lark = turtle.Turtle()
    customize_turtle(lark, "turtle", "#19c438", 2)
    sporty = turtle.Turtle()
    customize_turtle(sporty, "turtle", "#8dc419", 4)
    mud = turtle.Turtle()
    customize_turtle(mud, "turtle", "#996a15", 8)

    # Go magical artistic turtles! Draw things!
    draw_square(lark, 100)
    draw_circle(sporty, 150)
    draw_triangle(mud, 250)

    window.exitonclick()


run_program()