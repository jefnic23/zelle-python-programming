# Do Programming Exercise 8 from Chapter 4, but add a decision to
# prevent the program from dividing by zero if the line is vertical.


from graphics import *
import math


def main():
    win = GraphWin("Line Segment Information")
    p1 = win.getMouse()
    p2 = win.getMouse()
    Line(Point(p1.getX(), p1.getY()), Point(p2.getX(), p2.getY())).draw(win)
    midx = (p1.getX() + p2.getX()) / 2
    midy = (p1.getY() + p2.getY()) / 2
    midpoint = Point(midx, midy)
    midpoint.setFill("cyan")
    midpoint.draw(win)
    dx = p1.getX() - p2.getX()
    dy = p1.getY() - p2.getY()
    try:
        slope = dy / dx
        length = math.sqrt(dx ** 2 + dy ** 2)
        print("slope: {}".format(slope))
        print("length: {}".format(length))
    except ZeroDivisionError:
        print("line is vertical, no slope")
    win.getMouse()
    win.close()


main()
