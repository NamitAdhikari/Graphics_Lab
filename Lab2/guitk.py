import tkinter as tk
from blaTk import drawBLA
from ddaTk import drawDDA
from midTk import drawMid

arrayPoint = []

class GuiTK(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("GUI Line Algo Generation")
        self.geometry("500x500")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        self.show_frame("LineAlgoGUI", container)

    def show_frame(self, page_name, container):
        page_name = eval(page_name)
        for F in (page_name,):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def show_frame1(self, page_name, ent1, ent2, choice, container):
        def getPoint(ent1, ent2, choice):
            global arrayPoint
            p1 = ent1.get()
            p2 = ent2.get()
            x1, y1 = [int(x) for x in p1.split()]
            x2, y2 = [int(x) for x in p2.split()]
            print(x1, y1, x2, y2, choice)
            if choice == 1:
                arrayPoint.clear()
                arrayPoint = drawDDA(x1, y1, x2, y2)
                print(arrayPoint)
            elif choice == 2:
                arrayPoint.clear()
                arrayPoint = drawBLA(x1, y1, x2, y2)
                print(arrayPoint)
            else:
                arrayPoint.clear()
                arrayPoint = drawMid(x1, y1, x2, y2)
                print(arrayPoint)

        getPoint(ent1, ent2, choice)

        self.show_frame(page_name, container)



class LineAlgoGUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self)

        canvas.create_text((180, 150), text="Enter the start point: ", font="Tahoma 15")
        ent1 = tk.Entry(self)
        canvas.create_window(335, 150, window=ent1)

        canvas.create_text((180, 190), text="Enter the end point: ", font="Tahoma 15")
        ent2 = tk.Entry(self)
        canvas.create_window(333, 190, window=ent2)

        btn1 = tk.Button(self, text="DDA", font="Helvetica 13", command=lambda: controller.show_frame1("LineAlgo", ent1, ent2, 1, parent))
        canvas.create_window(130, 250, window=btn1)

        btn2 = tk.Button(self, text="BLA", font="Helvetica 13", command=lambda: controller.show_frame1("LineAlgo", ent1, ent2, 2, parent))
        canvas.create_window(220, 250, window=btn2)

        btn3 = tk.Button(self, text="Midpoint", font="Helvetica 13", command=lambda: controller.show_frame1("LineAlgo", ent1, ent2, 3, parent))
        canvas.create_window(320, 250, window=btn3)

        canvas.pack(fill=tk.BOTH, expand=1)


class LineAlgo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = tk.Canvas(self)
        canvas.create_line(arrayPoint)
        btn1 = tk.Button(self, text="Home", font="Helvetica 13", command=lambda: controller.show_frame("LineAlgoGUI", parent))
        canvas.create_window(450, 20, window=btn1)
        canvas.pack(fill=tk.BOTH, expand=1)




if __name__ == "__main__":
    app = GuiTK()
    app.mainloop()

