import numpy as np
from tkinter import Tk, Canvas, Frame, BOTH

arrayPoint = [[] for i in range(8)]

class MidCircle(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Midpoint Circle generation")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)

        for i in range(8):
            canvas.create_line(arrayPoint[i])

        canvas.pack(fill=BOTH, expand=True)


def drawCircleMid(xc, yc, r):
    x0, y0 = 0, r
    P0 = (1 - r)
    putPixel(x0, y0, xc, yc)
    nextPoint(x0, y0, xc, yc, r, P0)


def nextPoint(x, y, xc, yc, r, Pk):
    while (x <= y):
        x += 1
        if (Pk < 0):
            Pk += (2*x + 1)
        else:
            y -= 1
            Pk += (2*x + 1 - 2*y)

        putPixel(x, y, xc, yc)


def putPixel(x, y, xc, yc):
    for i in range(2):
        global arrayPoint
        if (i != 0):
            x, y = y, x

        arrayPoint[i].append((x + xc, y + yc))
        arrayPoint[i+2].append((-x + xc, y+yc))
        arrayPoint[i+4].append((-x + xc, -y + yc))
        arrayPoint[i+6].append((x + xc, -y + yc))



if __name__ == "__main__":
    xc, yc = [int(x) for x in input("Enter the center of circle: ").split()]
    rad = int(input("Enter the radius of circle: "))

    drawCircleMid(xc, yc, rad)

    window = Tk()
    mid = MidCircle()
    window.geometry("500x500")
    window.mainloop()
