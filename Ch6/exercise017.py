from graphics import *

win = GraphWin()
win.setCoords(0.0, 0.0, 10.0, 10.0)

shape = Circle(Point(5.0, 5.0), 1)
shape.setFill('red')
shape.draw(win)


def move_to(shape, new_center):
    old_center = shape.getCenter()
    new_x = new_center.getX() - old_center.getX()
    new_y = new_center.getY() - old_center.getY()
    shape.move(new_x, new_y)


for i in range(10):
    new_center = win.getMouse()
    move_to(shape, new_center)

win.getMouse()
win.close()
