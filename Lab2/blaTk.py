import numpy as np
from tkinter import Tk, Canvas, Frame, BOTH

arrayPoint = []

class BLA(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("BLA Line generation")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas (self)
        canvas.create_line(arrayPoint)
        canvas.pack(fill=BOTH, expand=True)


def drawBLA(x1, y1, x2, y2):
    dx = (x2-x1)
    dy = (y2-y1)
    m = abs(dy/dx)
    if m < 1:
        step = dx
        Po = 2*abs(dy) - abs(dx)
        nextPoint(Po, x1, y1, dx, dy, step, m)
    else:
        step = dy
        Po = 2*abs(dx) - abs(dy)
        nextPoint(Po, y1, x1, dy, dx, step, m)


def nextPoint(Po, x, y, dx, dy, step, m):
    step = abs(step)
    while (step+1):
        if m < 1:
            putPixel(x, (1000-y))
        else:
            putPixel(y, (1000-x))

        x += np.sign(dx)
        if (Po < 0):
            Pk = Po + 2*abs(dy)
        else:
            Pk = Po + 2*abs(dy) - 2*abs(dx)
            y += np.sign(dy)
        
        Po = Pk
        step = step - 1

def putPixel(x, y):
    global arrayPoint
    arrayPoint.append((x, y))
    


if __name__ == "__main__":
    x1, y1 = [int(x) for x in input("Enter the starting point: ").split()]
    x2, y2 = [int(x) for x in input("Enter the end point: ").split()]

    drawBLA(x1, y1, x2, y2)

    print(arrayPoint)

    window = Tk()
    bla = BLA()
    window.geometry("1000x1000")
    window.mainloop()
