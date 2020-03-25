# Write a program to animate a circle bouncing around a window. The basic
# idea is to start the circle somewhere in the interior of the window. Use
# variables dx and dy (both initialized to 1) to control the movement of the
# circle. Use a large counted loop (say 10000 iterations), and each time
# through the loop move the circle using dx and dy. When the x-value of the
# center of the circle gets too high (it hits an edge), change dx to -1. When
# it gets too low, change dx back to 1. Use a similar approach for dy.
# Note: Your animation will probably run too fast. You can slow it down by
# using the sleep function from the time library module.


from time import sleep
from graphics import *


def main():
    win = GraphWin("Bouncing Circle")
    p1 = win.getMouse()
    circle = Circle(Point(p1.getX(), p1.getY()), 35)
    circle.setFill("red")
    circle.draw(win)
    dx = 1
    dy = 1
    for i in range(5000):
        circle.move(dx, dy)
        sleep(0.005)
        if circle.getP1().getX() == 0 or circle.getP2().getX() == 200:
            dx = -dx
        if circle.getP1().getY() == 0 or circle.getP2().getY() == 200:
            dy = -dy
    win.getMouse()
    win.close()


main()
