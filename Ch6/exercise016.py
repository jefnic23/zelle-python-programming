from graphics import *

win = GraphWin()
win.setCoords(0.0, 0.0, 10.0, 10.0)

infile = input('Enter image filename: ')
faces  = eval(input('Enter number of faces: '))
image  = Image(Point(5.0, 5.0), infile)
image.draw(win)

def drawFace(center, size, win):
    face = Circle(center, size)
    face.setFill('white')
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
    mouth.setFill('white')
    mouth.draw(win)

for i in range(faces):
    p1 = win.getMouse()
    p2 = win.getMouse()
    center = Point(p1.getX(), p1.getY())
    size   = p2.getY() - p1.getY()

    drawFace(center, size, win)

win.getMouse()
win.close()
