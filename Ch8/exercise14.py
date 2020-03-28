# Write a program that converts a color image to grayscale. The user
# supplies the name of a file containing a GIF or PPM image, and the program
# loads the image and displays the file. At the click of the mouse, the
# program converts the image to grayscale. The user is then prompted for a
# filename to store the grayscale image in.
# You will probably want to go back and review the Image object from the
# graphics library (Section 4.8.4). The basic idea for converting the image
# is to go through it pixel by pixel and convert each one from color to an
# appropriate shade of gray. A gray pixel created by setting its red, green, and
# blue components to have the same brightness. So, color_rgb(0, 0, ) is
# black, color_rgb(255, 255, 255) is white, and color_rbg(127, 127, 127)
# is a gray "halfway" between. You should use a weighted average of the
# original RBG values to determine the brightness of the gray. Here is the
# pseudocode for the grayscale algorithm:
#
# for each row in the image:
#   for each column in the image:
#       r, g, b = get pixel information for current row and column
#       brightness = int(round(0.299r + 0.587g + 0.114b))
#       set pixel to color_rgb(brightness, brightness, brightness)
#   update the image # to see progress row by row

# Note: the pixel operations in the Image class are rather slow, so you will
# want to use relatively small images (not 12 megapixels) to test your program.


from graphics import *


def main():
    win = GraphWin("Grayscale Converter", 400, 400)
    win.setCoords(-5, -5, 5, 5)
    Text(Point(-2, 0), "Enter image filename to import: ").draw(win)
    file = Entry(Point(2.25, 0), 12).draw(win)
    Rectangle(Point(-1, -2), Point(1, -3)).draw(win)
    Text(Point(0, -2.5), "Import").draw(win)
    win.getMouse()
    file.undraw()
    image = Image(Point(0, 0), file.getText())
    image.draw(win)
    convert = Text(Point(0, 4.5), "Click anywhere to convert to grayscale").draw(win)
    win.getMouse()
    convert.undraw()
    for x in range(image.getWidth()):
        for y in range(image.getHeight()):
            r, g, b = image.getPixel(x, y)
            brightness = int(round(0.299*r + 0.587*g + 0.114*b))
            image.setPixel(x, y, color_rgb(brightness, brightness, brightness))
            win.update()
    Text(Point(-2, 0), "Enter filename to store image in: ").draw(win)
    file = Entry(Point(2.25, 0), 12).draw(win)
    Rectangle(Point(-1, -2), Point(1, -3)).draw(win)
    Text(Point(0, -2.5), "Export").draw(win)
    win.getMouse()
    image.save(file.getText())
    win.close()


main()
