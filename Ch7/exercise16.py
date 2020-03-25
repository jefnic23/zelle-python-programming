# Archery Scorer. Write a program that draws an archery target (see
# Programming Exercise 2 from Chapter 4) and allows the user to click five
# times to represent arrows shot at the target. Using five-band scoring, a
# bulls-eye (yellow) is worth 9 points and each successive ring is worth 2
# fewer points down to 1 for white. The program should output a score for
# each click and keep track of a running sum for the entire series.


from graphics import *
import math


def target(color, radius, win):
    shape = Circle(Point(0, 0), radius)
    shape.setFill(color)
    return shape.draw(win)


def main():
    win = GraphWin("Archery Scorer")
    win.setCoords(-5, -5, 5, 5)
    colors = ["white", "black", "blue", "red", "yellow"]
    radius = 5
    for c in colors:
        target(c, radius, win)
        radius -= 1
    points = 0
    for i in range(5):
        arrow = win.getMouse()
        arrow.setFill("green")
        arrow.draw(win)
        x = arrow.getX()
        y = arrow.getY()
        z = math.sqrt(x ** 2 + y ** 2)
        if 5 >= z > 4:
            print("one point for white")
            points += 1
        elif 4 >= z > 3:
            print("three points for black")
            points += 3
        elif 3 >= z > 2:
            print("five points for blue")
            points += 5
        elif 2 >= z > 1:
            print("seven points for red")
            points += 7
        elif 1 > z:
            print("nine points for bullseye")
            points += 9
        else:
            print("you missed!")
    print("points: {}".format(points))
    win.getMouse()
    win.close()


main()
