import numpy as np
from tkinter import Tk, Canvas, Frame, BOTH

arrayPoint = []

class Mid(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Midpoint Line generation")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        canvas.create_line(arrayPoint)
        canvas.pack(fill=BOTH, expand=True)


def drawMid(x1, y1, x2, y2):
    dx = (x2-x1)
    dy = (y2-y1)
    m = abs(dy/dx)
    if m < 1:
        step = dx
        do = abs(dy) - abs(dx)/2.0
        nextPoint(do, x1, y1, dx, dy, step, m)
    else:
        step = dy
        do = abs(dx) - abs(dy)/2.0
        nextPoint(do, y1, x1, dy, dx, step, m)

        
def nextPoint(do, x, y, dx, dy, step, m):
    step = abs(step)

    while(step+1):
        if m < 1:
            putPixel(x, (1000-y))
        else:
            putPixel(y, (1000-x))

        x += np.sign(dx)
        if (do < 0):
            dk = do + abs(dy)
        else:
            dk = do + abs(dy) - abs(dx)
            y += np.sign(dy)
        
        do = dk
        step = step - 1


def putPixel(x, y):
    global arrayPoint
    arrayPoint.append((x,y))
    


if __name__ == "__main__":
    x1, y1 = [int(x) for x in input("Enter the starting point: ").split()]
    x2, y2 = [int(x) for x in input("Enter the end point: ").split()]

    drawMid(x1, y1, x2, y2)

    window = Tk()
    mid = Mid()
    window.geometry("1000x1000")
    window.mainloop()