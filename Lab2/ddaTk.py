import numpy as np
from tkinter import Tk, Canvas, Frame, BOTH

arrayPoint = []

class DDA(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("DDA Line generation")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        canvas.create_line(arrayPoint)
        canvas.pack(fill=BOTH, expand=True)


def drawDDA(x1, y1, x2, y2):
    x,y = x1,y1
    dx = (x2-x1)
    dy = (y2-y1)
    step = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    Xin = dx/float(step)
    Yin = dy/float(step)

    while (step+1):
        putPixel(x, (1000-y))
        x += Xin
        y += Yin
        step = step - 1


def putPixel(x, y):
    global arrayPoint
    arrayPoint.append((x, y))
    

if __name__ == "__main__":
    x1, y1 = [int(x) for x in input("Enter the starting point: ").split()]
    x2, y2 = [int(x) for x in input("Enter the end point: ").split()]

    drawDDA(x1, y1, x2, y2)

    print(arrayPoint)

    window = Tk()
    dda = DDA()
    window.geometry("1000x1000")
    window.mainloop()
