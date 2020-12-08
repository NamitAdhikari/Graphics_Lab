from tkinter import Tk, Canvas, Frame, BOTH
from math import pi, cos, sin
import ctypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
height, width = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(f'Resolution is: {height} x {width}')

k, l, m, n, o=479, 180, 465, 232, 347

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.master.title("Flag of Nepal")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)


        def SunShape(x, y, r, e, l, b):
            p, a, h=[], 2*pi/e, r*l
            c, d=[0, -a/2][b], [a/2, 0][b]
            for i in range(e):
                p+=[(x+r*cos(i*a+c), y+r*sin(i*a+c)), (x+h*cos(i*a+d), y+h*sin(i*a+d))]
            canvas.create_polygon(p, fill="white")

        #outer polygon with blue color
        canvas.create_polygon((0, 0), (393, 246), (144, 246), (375, k), (0, k), fill="#003893") 
        # inner polygon with red color over blue polygon
        canvas.create_polygon((14, 25), (o, n), (110, n), (o, m), (14, m), fill="#DC143C") 
        #Sun Shape at lower part
        SunShape(96, o, 68, 12, .6, 0) 
        #Semi cricle for the moon
        canvas.create_arc(31, 90, 163, 221, start=-180, extent=l, fill="#ffffff", outline="#ffffff")
        #another smaller semicircle with red color over the provious semicircle to make it small
        canvas.create_arc(28, 68, 166, 200, start=-180, extent=l, fill="#DC143C", outline="#DC143C")
        #Sun shape above the moon semicicle
        SunShape(96, 178, 40, 16, .7, 1) 

        canvas.pack(fill=BOTH, expand=1)



root = Tk()
ex = Example()
root.geometry("400x500")
root.mainloop()
