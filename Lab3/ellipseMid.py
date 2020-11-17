import numpy as np
from tkinter import Tk, Canvas, Frame, BOTH

arrayPoint = [[] for i in range(4)]

class MidEllipse(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Midpoint Ellipse generation")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        for i in range(4):
            canvas.create_line(arrayPoint[i])

        canvas.pack(fill=BOTH, expand=True)


def drawEllipseMid(xc, yc, rx, ry):
    x0, y0 = 0, ry           
    P10 = pow(ry, 2) - pow(rx, 2)*ry + (1/4)*pow(rx, 2)
    nextPoint(x0, y0, xc, yc, rx, ry, P10)

def nextPoint(x, y, xc, yc, rx, ry, Pk):
    dx = 2*pow(ry, 2)*x
    dy = 2*pow(rx, 2)*y

    while (dx < dy):
        putPixel(x, y, xc, yc)
        x += 1
        if (Pk < 0):
            dx = dx + 2*pow(ry, 2)
            Pk = Pk + dx + pow(ry, 2)
        else:
            y -= 1
            dx = dx + 2*pow(ry, 2)
            dy = dy - 2*pow(rx, 2)
            Pk = Pk + dx - dy + pow(ry, 2)


    P20 = pow(ry, 2)*pow((x + 0.5), 2) + pow(rx, 2)*pow(y - 1, 2) - pow (rx * ry, 2)

    while (y >= 0):
        putPixel(x, y, xc, yc)
        y -= 1
        if (P20 > 0):
            dy = dy - 2*pow(rx, 2)
            P20 = P20 + pow(rx, 2) - dy
        else:
            x += 1
            dx = dx + 2*pow(ry, 2)
            dy = dy - 2*pow(rx, 2)
            P20 = P20 + dx - dy + pow(rx, 2)

def putPixel(x, y, xc, yc):
    global arrayPoint
    arrayPoint[0].append((x + xc, y + yc))
    arrayPoint[1].append((-x + xc, y+yc))
    arrayPoint[2].append((x + xc, -y + yc))
    arrayPoint[3].append((-x + xc, -y + yc))



if __name__ == "__main__":
    xc, yc = [int(x) for x in input("Enter the center of ellipse: ").split()]
    radX, radY = [int(x) for x in input("Enter the radius of ellipse along x-axis and y-axis: ").split()]

    drawEllipseMid(xc, yc, radX, radY)

    window = Tk()
    mid = MidEllipse()
    window.geometry("500x500")
    window.mainloop()
