# Write a program that graphically plots a regression line, that is, the line
# with the best fit through a collection of points. First ask the user to specify
# the data points by clicking on them in a graphics window. To find the end
# of input, place a small rectangle labeled "Done" in the lower left corner of
# the window; the program will stop gathering points when the user clicks
# inside that rectangle.
# The regression line is the line with the following equation:
#           y = avg(y) + m(x - avg(x))
# where
#           m = sum(xi*yi - n*avg(x)*avg(y)) / sum(xi**2 - n*avg(x)**2)
# and n is the number of points.
# As the user clicks on points, the program should draw them in the graphics
# window and keep track of the count of input values and the running sum
# of x, y, x**2 and xy values. When the user clicks inside the "Done" rectangle,
# the program then computes value of y (using the equations above)
# corresponding to the x values at the left and right edges of the window to
# compute the endpoints of the regression line spanning the window. After
# the line is drawn, the program will pause for another mouse click before
# closing the window and quitting.


from graphics import *


def main():
    win = GraphWin("Linear Regression", 400, 400)
    win.setCoords(-5, -5, 5, 5)
    Text(Point(0, 4.5), "Click anywhere to place a data point").draw(win)
    box = Rectangle(Point(-4.5, -3.5), Point(-3.5, -4.5))
    box.draw(win)
    Text(Point(-4, -4), "Done").draw(win)
    n = 0
    x = []
    y = []
    xy = []
    x2 = []
    done = False
    while not done:
        click = win.getMouse()
        if box.getP1().getX() < click.getX() < box.getP2().getX():
            if box.getP2().getY() < click.getY() < box.getP1().getY():
                break
        else:
            data = Circle(Point(click.getX(), click.getY()), 0.05)
            data.setFill("cyan")
            data.draw(win)
            n += 1
            x.append(click.getX())
            y.append(click.getY())
            xy.append(click.getX()*click.getY())
            x2.append(click.getX()**2)
    avg_x = sum(x) / len(x)
    avg_y = sum(y) / len(y)
    top = -n * avg_x * avg_y
    bottom = -2 * avg_x ** 2
    for i in range(n):
        top += x[i] * y[i]
        bottom += x[i] ** 2
    m = top / bottom
    left = avg_y + m * (-5 - avg_x)
    right = avg_y + m * (5 - avg_x)
    line = Line(Point(-5, left), Point(5, right))
    line.setOutline("red")
    line.draw(win)
    Text(Point(0, -4.5), "Click anywhere to exit").draw(win)
    win.getMouse()
    win.close()


main()
