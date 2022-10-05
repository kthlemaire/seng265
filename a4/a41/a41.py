#!/usr/bin/env python3
'''Assignment 4 Part 1 template'''
from typing import IO
print(__doc__)

'''
    Class: Circle
    Description: Creates an Circle object 
    Input: 
        - cir: a tuple containing the x and y coordinates of the circle center and the radius of the circle
        - col: a tuple of the RGB and opacity 
'''


class Circle:
    '''Circle class'''

    def __init__(self, cir: tuple, col: tuple) -> None:
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]


'''
    Class: Rectangle
    Description: Creates an Rectangle object 
    Input: 
        - x: x coordinate of the rectangle's top left corner
        - y: y coordinate of the rectangle's top left corner
        - w: width of the rectangle
        - h: height of the rectangle
        - col: a tuple of the RGB and opacity 
'''


class Rectangle:
    '''Rectangle class'''

    def __init__(self, x: int, y: int, w: int, h: int, col: tuple) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]


'''
    Class: Ellipse
    Description: Creates an Ellipse object 
    Input: 
        - ex: x coordinate of the ellipse center
        - ey: y coordinate of the ellipse center
        - rx: radius small range
        - ry: radius
        - col: a tuple of the RGB and opacity 
'''


class Ellipse:
    '''Ellipse class'''

    def __init__(self, ex: int, ey: int, rx: int, ry: int, col: tuple) -> None:
        self.ex = ex
        self.ey = ey
        self.rx = rx
        self.ry = ry
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]


'''
    Class: ProEpilogue
    Description: Generates the prologue and the epilogue of an html page
    Input: 
        - fileName: the name of the file to be written to
        - title: the title of the html file
        - width: the width of the page
        - height: the height of the page
'''


class ProEpilogue:
    '''ProEpilogue class'''

    def __init__(self, fileName: str, title: str, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.fileName = fileName
        self.title = title

    def writePrologue(self) -> None:
        self.fileName = open(self.fileName, "w")
        self.fileName.write(f"<html>\n")
        self.fileName.write(f"<head>\n")
        ts = "   " * 1
        self.fileName.write(f"{ts}<title>{self.title}</title>\n")
        self.fileName.write(f"<head>\n")
        self.fileName.write(f"<body>\n")
        ts = "   " * 1
        self.fileName.write(f'{ts}<!--Define SVG drawing box-->\n')
        self.fileName.write(
            f'{ts}<svg width="{self.width}" height="{self.height}">\n')

    def writeEpilogue(self) -> None:
        ts: str = "   " * 1
        self.fileName.write(f'{ts}</svg>\n')
        self.fileName.write(f'</body>\n')
        self.fileName.write(f'</html>\n')
        self.fileName = self.fileName.close()

    def getFile(self) -> None:
        return self.fileName


def writeHTMLcomment(f: IO[str], t: int, com: str):
    '''writeHTMLcomment method'''
    ts: str = "   " * t
    f.write(f'{ts}<!--{com}-->\n')


'''
    Function: drawCircleLine
    Description: takes a Circle object and a file, writes the shape in SVG form to the file
    Input: 
        - f: file to be written to 
        - t: tabs before SVG line
        - c: Circle object
    Output:
        - None
'''


def drawCircleLine(f: IO[str], t: int, c: Circle):
    '''drawCircleLine method'''
    ts: str = "   " * t
    line: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></circle>'
    f.write(f"{ts}{line}\n")


'''
    Function: drawRectangle
    Description: takes a Rectangle object and a file, writes the rectangle in SVG form to the file
    Input: 
        - f: file to be written to 
        - t: tabs before SVG line
        - r: Rectangle object
    Output:
        - None
'''


def drawRectangle(f: IO[str], t: int, r: Rectangle):
    '''drawRectangle method'''
    ts: str = "   " * t
    line: str = f'<rect x="{r.x}" y="{r.y}" width="{r.w}" height="{r.h}" fill="rgb({r.red}, {r.green}, {r.blue})" fill-opacity="{r.op}"></rect>'
    f.write(f"{ts}{line}\n")


'''
    Function: drawEllipse
    Description: takes a Ellipse object and a file, writes the ellipse in SVG form to the file
    Input: 
        - f: file to be written to 
        - t: tabs before SVG line
        - e: Ellipse object
    Output:
        - None
'''


def drawEllipse(f: IO[str], t: int, e: Ellipse):
    '''drawEllipse method'''
    ts: str = "   " * t
    line: str = f'<ellipse cx="{e.ex}" cy="{e.ey}" rx="{e.rx}"ry="{e.ry}" fill="rgb({e.red}, {e.green}, {e.blue})" fill-opacity="{e.op}"></ellipse>'
    f.write(f"{ts}{line}\n")


'''
    Function: genArt
    Description: creates different shape objects and calls other functions to draw them
    Input: 
        - f: file to be written to 
        - t: tabs before SVG line
    Output:
        - None
'''


def genArt(f: IO[str], t: int):
    '''genART method'''
    drawCircleLine(f, t, Circle((50, 50, 50), (255, 0, 0, 1.0)))
    drawCircleLine(f, t, Circle((150, 50, 50), (255, 0, 0, 1.0)))
    drawCircleLine(f, t, Circle((250, 50, 50), (255, 0, 0, 1.0)))
    drawCircleLine(f, t, Circle((350, 50, 50), (255, 0, 0, 1.0)))
    drawCircleLine(f, t, Circle((450, 50, 50), (255, 0, 0, 1.0)))
    drawCircleLine(f, t, Circle((50, 250, 50), (0, 0, 255, 1.0)))
    drawCircleLine(f, t, Circle((150, 250, 50), (0, 0, 255, 1.0)))
    drawCircleLine(f, t, Circle((250, 250, 50), (0, 0, 255, 1.0)))
    drawCircleLine(f, t, Circle((350, 250, 50), (0, 0, 255, 1.0)))
    drawCircleLine(f, t, Circle((450, 250, 50), (0, 0, 255, 1.0)))
    drawRectangle(f, t, Rectangle(5, 9, 50, 10, (0, 0, 255, 1.0)))
    drawRectangle(f, t, Rectangle(50, 70, 70, 90, (244, 8, 211, 0.6)))
    drawRectangle(f, t, Rectangle(250, 150, 100, 100, (255, 0, 255, 0.75)))
    drawEllipse(f, t, Ellipse(150, 150, 55, 70, (60, 100, 255, 0.85)))
    drawEllipse(f, t, Ellipse(385, 97, 70, 90, (100, 200, 255, 0.75)))


def openSVGcanvas(f: IO[str], t: int, canvas: tuple):
    '''openSVGcanvas method'''
    ts: str = "   " * t
    writeHTMLcomment(f, t, "Define SVG drawing box")
    f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')


def closeSVGcanvas(f: IO[str], t: int):
    '''closeSVGcanvas method'''
    ts: str = "   " * t
    f.write(f'{ts}</svg>\n')
    f.write(f'</body>\n')
    f.write(f'</html>\n')


def writeHTMLline(f: IO[str], t: int, line: str):
    '''writeLineHTML method'''
    ts = "   " * t
    f.write(f"{ts}{line}\n")


def writeHTMLHeader(f: IO[str], winTitle: str):
    '''writeHeadHTML method'''
    writeHTMLline(f, 0, "<html>")
    writeHTMLline(f, 0, "<head>")
    writeHTMLline(f, 1, f"<title>{winTitle}</title>")
    writeHTMLline(f, 0, "</head>")
    writeHTMLline(f, 0, "<body>")


def writeHTMLfile():
    '''writeHTMLfile method'''
    fnam: str = "a41.html"
    winTitle = "My Art"
    f: IO[str] = open(fnam, "w")
    writeHTMLHeader(f, winTitle)
    openSVGcanvas(f, 1, (500, 300))
    genArt(f, 2)
    closeSVGcanvas(f, 1)
    f.close()


def main():
    '''main method'''
    writeHTMLfile()


main()
