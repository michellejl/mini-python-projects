import turtle


def customize_turtle(name, shape, color, pencolor, speed, width):
    name.shape(shape)
    name.speed(speed)
    name.width(width)
    name.pencolor(pencolor)
    name.fillcolor(color)


def draw_square(who, size):
    for i in range(4):
        who.forward(size)
        who.right(90)


def draw_circle_from_squares(who, size, num_of_squares):
    for i in range(num_of_squares):
        draw_square(who, size)
        who.right((360.0 / num_of_squares))


def run_program():
    # Creates window object for turtles to play on
    window = turtle.Screen()
    window.bgcolor("#4286f4")

    # Creating some turtles
    lark = turtle.Turtle()
    customize_turtle(lark, "turtle", "#19c438", "black", 8, 5)

    # Go magical artistic turtle! Draw me a circle from squares!
    draw_circle_from_squares(lark, 100, 20)
    lark.right(90)
    lark.forward(200)
    lark.right(-90)
    lark.circle(200)



    window.exitonclick()


run_program()