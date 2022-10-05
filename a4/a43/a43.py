#!/usr/bin/env python3
'''Assignment 4 Part 3'''
import random
from typing import IO
import sys
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


'''
    Class: ArtConfig
    Description: Generates a table of random Circle, Rectangle and Ellipses
    Input: 
        - cnt: the number of shapes to be generated
        - randomNums: GenRandom type to generate numbers for the table
        - table: empty list
'''


class ArtConfig:
    '''ArtConfig class'''

    def __init__(self, cnt: int, randomNums: "GenRandom", table: list) -> None:
        self.cnt = cnt
        self.randomNums = randomNums
        self.table = table

    def generateTable(self) -> None:
        self.table.append(["CNT", "SHA", "X", "Y", "RAD", "RX",
                          "RY", "W", "H", "R", "G", "B", "OP"])
        for shapes in range(self.cnt):
            shape = []
            shape.append(shapes + 1)
            shape.append(self.randomNums.randomShape())
            shape.append(self.randomNums.randomX())
            shape.append(self.randomNums.randomY())
            shape.append(self.randomNums.randomRAD())
            shape.append(self.randomNums.randomRXY())
            shape.append(self.randomNums.randomRXY())
            shape.append(self.randomNums.randomWH())
            shape.append(self.randomNums.randomWH())
            shape.append(self.randomNums.randomColour())
            shape.append(self.randomNums.randomColour())
            shape.append(self.randomNums.randomColour())
            shape.append(self.randomNums.randomOP())
            self.table.append(shape)

    def printTable(self) -> None:
        for items in self.table:
            print(f"{items[0]:>3} {items[1]:>3} {items[2]:>3} {items[3]:>3} {items[4]:>3} {items[5]:>3} {items[6]:>3} {items[7]:>3} {items[8]:>3} {items[9]:>3} {items[10]:>3} {items[11]:>3} {items[12]:>3}")

    def getTable(self) -> list:
        return self.table


'''
    Class: GenRandom
    Description: generates random values that can be used to create Circle, Rectangle or Ellipses
    Input: 
        - width: the width of the page
        - height: the height of the page
'''


class GenRandom:
    '''GenRandom class'''

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def randomShape(self) -> int:
        return random.randrange(0, 3)

    def randomX(self) -> int:
        return random.randrange(0, self.width)

    def randomY(self) -> int:
        return random.randrange(0, self.height)

    def randomRAD(self) -> int:
        return random.randrange(0, 101)

    def randomRXY(self) -> int:
        return random.randrange(10, 31)

    def randomWH(self) -> int:
        return random.randrange(10, 101)

    def randomColour(self) -> int:
        return random.randrange(0, 256)

    def randomOP(self) -> float:
        return round(random.uniform(0.0, 1.1), 1)


'''
Function: main
    Description: represents the entry point of the program.
    Inputs: 
        - argc: indicates the number of arguments to be passed to the program.
        - argv: an array of strings containing the arguments passed to the program.
        - Three arguments passed to the program
            - number of symbols to be printed
            - width of the page
            - height of the page
    Output: an integer describing the result of the execution of the program:
        - 0: Successful execution.
        - 1: Erroneous execution.
'''


def main():
    '''main'''
    if len(sys.argv) < 4:
        print("Please include the number of symbols to be generated, and the width and height of the page as arguments.")
        print("Example: ./a43.py 1000 600 400")
        sys.exit(1)

    numSymbols = int(sys.argv[1])
    width = int(sys.argv[2])
    height = int(sys.argv[3])

    randomNumbers = GenRandom(width, height)
    getRandomShapes = ArtConfig(numSymbols, randomNumbers, [])
    getRandomShapes.generateTable()
    tableOfShapes = getRandomShapes.getTable()
    openFile = ProEpilogue("myPart3Art.html", "My Art", width, height)
    openFile.writePrologue()
    fileName = openFile.getFile()
    getShapes(tableOfShapes, fileName)
    openFile.writeEpilogue()


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


def drawCircleLine(f: IO[str], t: int, c: Circle) -> None:
    '''drawCircle method'''
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


def drawRectangle(f: IO[str], t: int, r: Rectangle) -> None:
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


def drawEllipse(f: IO[str], t: int, e: Ellipse) -> None:
    '''drawEllipse method'''
    ts: str = "   " * t
    line: str = f'<ellipse cx="{e.ex}" cy="{e.ey}" rx="{e.rx}"ry="{e.ry}" fill="rgb({e.red}, {e.green}, {e.blue})" fill-opacity="{e.op}"></ellipse>'
    f.write(f"{ts}{line}\n")


'''
    Function: getShapes
    Description: takes a table of shapes, determines what type of shape they are (Circle, Rectangle, Ellipse), calls other functions to create the correct object type
    Input: 
        - table: table of shape information
        - fileName: file to be written to
    Output:
        - None
'''


def getShapes(table, fileName) -> None:
    '''getShapes method'''
    for shapes in range(1, len(table)):
        temp = table[shapes]
        if temp[1] == 0:
            makeCircle(temp, fileName)
        elif temp[1] == 1:
            makeRectangle(temp, fileName)
        else:
            makeEllipse(temp, fileName)


'''
    Function: makeRectangle
    Description: takes a table with information about a rectangle, creates a rectangle object based on the information, calls drawRectangle
    Input: 
        - table: information of a rectangle
        - fileName: file to be written to
    Output:
        - None
'''


def makeRectangle(table, fileName) -> None:
    '''makeRectangle method'''
    x = table[2]
    y = table[3]
    w = table[7]
    h = table[8]
    colour = (table[9], table[10], table[11], table[12])
    rectangle = Rectangle(x, y, w, h, colour)
    drawRectangle(fileName, 2, rectangle)


'''
    Function: makeCircle
    Description: takes a table with information about a circle, creates a circle object based on the information, calls drawCircleLine
    Input: 
        - table: information of a circle
        - fileName: file to be written to
    Output:
        - None
'''


def makeCircle(table, fileName) -> None:
    '''makeCircle method'''
    cir = (table[2], table[3], table[4])
    colour = (table[9], table[10], table[11], table[12])
    circle = Circle(cir, colour)
    drawCircleLine(fileName, 2, circle)


'''
    Function: makeEllipse
    Description: takes a table with information about a ellipse, creates a ellipse object based on the information, calls drawEllipse
    Input: 
        - table: information of a ellipse
        - fileName: file to be written to
    Output:
        - None
'''


def makeEllipse(table, fileName) -> None:
    '''makeEllipse method'''
    x = table[2]
    y = table[3]
    rx = table[5]
    ry = table[6]
    colour = (table[9], table[10], table[11], table[12])
    ellipse = Ellipse(x, y, rx, ry, colour)
    drawEllipse(fileName, 2, ellipse)


if __name__ == '__main__':
    main()
