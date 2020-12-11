import tkinter as tk

# assigning region codes
inside = 0  #0000
left = 1    #0001
right = 2   #0010
bottom = 4  #0100
top = 8     #1000

# assigning clip window
x_max = 1920
y_max = 1440
x_min = 360
y_min = 480

# screen height and width
width = 3840
height = 2160


class ClipperTk(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Cohen-Sutherland Line Clipping")

    def clipUI(self, x0, y0, x1, y1):
        self.canvas = tk.Canvas(self)
        self.pack(expand=1, fill=tk.BOTH)

        self.canvas.create_rectangle((x_max, height - y_max), (x_min, height - y_min), outline='#000000', width=2, dash=(3,6))
        button = tk.Button(self.canvas, text="Clip Line", command=lambda: self.lineClipAlgo(x0, y0, x1, y1))
        button.pack(side='right', padx='300', ipadx='50')

        self.canvas.create_line((x0, height - y0), (x1, height - y1), width=2, fill='#000000', tags='init_line')
        self.canvas.pack(fill=tk.BOTH, expand=1)


    def computeCode(self, x, y):
        code = inside

        if x < x_min:
            code |= left
        elif x > x_max:
            code |= right

        if y < y_min:
            code |= bottom
        elif y > y_max:
            code |= top

        return code


    def lineClipAlgo(self, x0, y0, x1, y1):

        self.canvas.delete('init_line')

        code1 = self.computeCode(x0, y0)
        code2 = self.computeCode(x1, y1)

        while(True):
            if code1 == 0 and code2 == 0:
                break

            elif (code1 & code2) != 0:
                break

            else:
                x = 1
                y = 1

                code_out = code1 if code1 != 0 else code2

                if code_out & top:
                    x = x0 + (x1 - x0) * (y_max - y0) / (y1 - y0)
                    y = y_max

                elif code_out & bottom:
                    x = x0 + (x1 - x0) * (y_min-y0) / (y1 - y0)
                    y = y_min

                elif code_out & right:
                    y = y0 + (y1 - y0) * (x_max - x0) / (x1 - x0)
                    x = x_max

                elif code_out & left:
                    y = y0 + (y1 - y0) * (x_min - x0) / (x1 - x0)
                    x = x_min


                if code_out == code1:
                    x0 = x
                    y0 = y
                    code1 = self.computeCode(x0, y0)

                else:
                    x1 = x
                    y1 = y
                    code2 = self.computeCode(x1, y1)


        self.canvas.create_line((x0, height - y0), (x1, height - y1), width=2, fill='#000000')
        self.canvas.pack(fill=tk.BOTH, expand=1)


if __name__ == "__main__":
    
    x0, y0, x1, y1 = [int(x) for x in input("\nEnter two endpoints of line: ").split()]

    root = tk.Tk()
    app = ClipperTk(root)

    app.clipUI(x0, y0, x1, y1)

    root.geometry(f'{width}x{height}')
    root.mainloop()