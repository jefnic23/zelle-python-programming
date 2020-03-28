# Write a program to convert an image to its color negative. The general
# form fo the program will be similar to that of the previous problem. The
# negative of a pixel is formed by subtracting each color value from 255. So
# the new pixel color is color_rgb(255-r, 255-g, 255-b).


from graphics import *


def main():
    win = GraphWin("Color Negative Converter", 400, 400)
    win.setCoords(-5, -5, 5, 5)
    Text(Point(-2, 0), "Enter image filename to import: ").draw(win)
    file = Entry(Point(2.25, 0), 12).draw(win)
    Rectangle(Point(-1, -2), Point(1, -3)).draw(win)
    Text(Point(0, -2.5), "Import").draw(win)
    win.getMouse()
    file.undraw()
    image = Image(Point(0, 0), file.getText())
    image.draw(win)
    convert = Text(Point(0, 4.5), "Click anywhere to convert to color negative").draw(win)
    win.getMouse()
    convert.undraw()
    for x in range(image.getWidth()):
        for y in range(image.getHeight()):
            r, g, b = image.getPixel(x, y)
            image.setPixel(x, y, color_rgb(255-r, 255-g, 255-b))
            win.update()
    Text(Point(-2, 0), "Enter filename to store image in: ").draw(win)
    file = Entry(Point(2.25, 0), 12).draw(win)
    Rectangle(Point(-1, -2), Point(1, -3)).draw(win)
    Text(Point(0, -2.5), "Export").draw(win)
    win.getMouse()
    image.save(file.getText())
    win.close()


main()
