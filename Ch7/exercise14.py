# Do Programming Exercise 7 from Chapter 4, but add a decision to
# handle the case where the line does not intersect the circle.


from graphics import *
import math


def main():
    win = GraphWin("Circle Intersection", 400, 400)
    win.setCoords(-10.0, -10.0, 10.0, 10.0)
    radius = eval(input("enter radius: "))
    intercept = eval(input("enter y-intercept: "))
    circle = Circle(Point(0.0, 0.0), radius)
    circle.setFill("cyan")
    circle.setOutline("cyan")
    circle.draw(win)
    line = Line(Point(-10, intercept), Point(10, intercept))
    line.draw(win)
    try:
        x = math.sqrt(radius ** 2 - intercept ** 2)
        p1 = Point(x, intercept)
        p1.setFill("red")
        p1.draw(win)
        p2 = Point(0 - x, intercept)
        p2.setFill("red")
        p2.draw(win)
        print("intersect x values: {0}, {1}".format(x, 0 - x))
    except ValueError:
        print("line does not intersect circle")
    win.getMouse()
    win.close()


main()
