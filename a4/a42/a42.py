#!/usr/bin/env python3
import random
print(__doc__)


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
    Description: represents the entry point of the program, generates and prints a table of random shapes
    Inputs: 
       - None
'''


def main():
    randomNumbers = GenRandom(600, 400)
    test = ArtConfig(10, randomNumbers, [])
    test.generateTable()
    test.printTable()


if __name__ == '__main__':
    main()
