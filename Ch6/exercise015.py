from graphics import *

win = GraphWin()
win.setCoords(0.0, 0.0, 10.0, 10.0)

center = Point(2.5,5)
size   = 2
    
def drawFace(center, size, win):
    face = Circle(center, size)
    face.draw(win)

    left_x = center.getX() - 0.75
    right_x = center.getX() + 0.75
    eye_y = center.getY() + 0.5
    
    left_eye = Circle(Point(left_x,eye_y), size*0.125)
    left_eye.setFill('black')
    left_eye.draw(win)
    
    right_eye = Circle(Point(right_x,eye_y), size*0.125)
    right_eye.setFill('black')
    right_eye.draw(win)

    mouth_y = center.getY() - 0.5
    mouth = Polygon(Point(left_x, mouth_y),
                    Point(center.getX(), mouth_y - 0.5),
                    Point(right_x, mouth_y)
                    )
    mouth.draw(win)

drawFace(center, size, win)
win.getMouse()
win.close()
