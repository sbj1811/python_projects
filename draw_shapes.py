import turtle


def draw_square(sq):
        index = 0
        while index < 4:
                sq.forward(100)
                sq.right(90)
                index += 1

def draw_shape():
        window = turtle.Screen()
        window.bgcolor("red")
        index = 0
        cr = turtle.Turtle()
        cr.shape("circle")
        cr.color("blue")
        cr.speed('normal')
        while index < 36:
                draw_square(cr)
                cr.right(10)
                index += 1
        window.exitonclick()

draw_shape()
