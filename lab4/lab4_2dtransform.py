import tkinter as tk
import numpy as np

width = 3840
height = 2160

centerX, centerY = width/2, height/2

class TkTransform(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Transformation")


    def create_widgets(self):
        self.canvas = tk.Canvas(self)
        self.pack(expand=1, fill=tk.BOTH)

        # setting axes
        self.canvas.create_line((width/2, 0), (width/2, height), fill='#ffffff')
        self.canvas.create_line((0, height/2), (width, height/2), fill='#ffffff')


    def canvas_draw(self, tranMat, choice):

        x_0, x_1, x_2, x_3 = [x for x in tranMat[0]]
        y_0, y_1, y_2, y_3 = [y for y in tranMat[1]]

        if choice == 1:
            points = [[ (x0+centerX, height-(y0+centerY)), 
                        (x1+centerX, height-(y1+centerY))],
                        [(x_0+centerX, height-(y_0+centerY)), 
                        (x_1+centerX, height-(y_1+centerY))
                    ]]
            
            self.canvas.create_line(points[0], fill='#ffffff')
            self.canvas.create_line(points[1], fill='#ffffff')

        elif choice == 2:
            points = [[ (x0+centerX, height-(y0+centerY)), 
                        (x1+centerX, height-(y1+centerY)),
                        (x2+centerX, height-(y2+centerY))],
                        [(x_0+centerX, height-(y_0+centerY)), 
                        (x_1+centerX, height-(y_1+centerY)),
                        (x_2+centerX, height-(y_2+centerY))
                    ]]

            self.canvas.create_polygon(points[0], outline='#ffffff')
            self.canvas.create_polygon(points[1], outline='#ffffff')

        elif choice == 3:
            points = [[ (x0+centerX, height-(y0+centerY)), 
                        (x1+centerX, height-(y1+centerY)),
                        (x2+centerX, height-(y2+centerY)),
                        (x3+centerX, height-(y3+centerY))],
                        [(x_0+centerX, height-(y_0+centerY)), 
                        (x_1+centerX, height-(y_1+centerY)),
                        (x_2+centerX, height-(y_2+centerY)),
                        (x_3+centerX, height-(y_3+centerY))
                    ]]

            self.canvas.create_polygon(points[0], outline='#ffffff')
            self.canvas.create_polygon(points[1], outline='#ffffff')
        
        self.canvas.pack(expand=1, fill=tk.BOTH)


    def translate(self, choice, tx, ty, x0, y0, x1, y1, x2=0, y2=0, x3=0, y3=0):

        self.pack(expand=1, fill=tk.BOTH)

        arrPoint = np.array([[x0, x1, x2, x3], 
                        [y0, y1, y2, y3], 
                        [1, 1, 1, 1]])

        arrMat = np.array([[1, 0, tx], 
                            [0, 1, ty], 
                            [0, 0, 1]])

        tranMat = np.dot(arrMat, arrPoint)

        self.canvas_draw(tranMat, choice)


    def rotate(self, choice, angle, x0, y0, x1, y1, x2=0, y2=0, x3=0, y3=0):
        self.pack(expand=1, fill=tk.BOTH)

        arrPoint = np.array([[x0, x1, x2, x3], 
                        [y0, y1, y2, y3], 
                        [1, 1, 1, 1]])

        arrMat = np.array([[np.cos(np.deg2rad(angle)), -np.sin(np.deg2rad(angle)), 0], 
                            [np.sin(np.deg2rad(angle)), np.cos(np.deg2rad(angle)), 0], 
                            [0, 0, 1]])

        tranMat = np.dot(arrMat, arrPoint)

        self.canvas_draw(tranMat, choice)


    def scale(self, choice, sx, sy, x0, y0, x1, y1, x2=0, y2=0, x3=0, y3=0):
        self.pack(expand=1, fill=tk.BOTH)

        arrPoint = np.array([[x0, x1, x2, x3], 
                        [y0, y1, y2, y3], 
                        [1, 1, 1, 1]])

        arrMat = np.array([[sx, 0, 0], 
                            [0, sy, 0], 
                            [0, 0, 1]])

        tranMat = np.dot(arrMat, arrPoint)

        self.canvas_draw(tranMat, choice)


    def reflect(self, choice, reflect, x0, y0, x1, y1, x2=0, y2=0, x3=0, y3=0):
        self.pack(expand=1, fill=tk.BOTH)

        arrPoint = np.array([[x0, x1, x2, x3], 
                        [y0, y1, y2, y3], 
                        [1, 1, 1, 1]])

        if reflect in list(['x-axis', 'X-axis', 'y=0', 'Y=0']):
            arrMat = np.array([[1, 0, 0], 
                                [0, -1, 0], 
                                [0, 0, 1]])

        elif reflect in list(['y-axis', 'Y-axis', 'x=0', 'X=0']):
            arrMat = np.array([[-1, 0, 0], 
                                [0, 1, 0], 
                                [0, 0, 1]])

        elif reflect in list(['x=y', 'X=y', 'x=Y', 'X=Y']):
            arrMat = np.array([[0, 1, 0], 
                                [1, 0, 0], 
                                [0, 0, 1]])

        elif reflect in list(['origin', 'o', 'O', '0,0']):
            arrMat = np.array([[-1, 0, 0], 
                                [0, -1, 0], 
                                [0, 0, 1]])


        tranMat = np.dot(arrMat, arrPoint)

        print(tranMat)

        self.canvas_draw(tranMat, choice)


    def shear(self, choice, shx, shy, x0, y0, x1, y1, x2=0, y2=0, x3=0, y3=0):
        self.pack(expand=1, fill=tk.BOTH)

        arrPoint = np.array([[x0, x1, x2, x3], 
                            [y0, y1, y2, y3], 
                            [1, 1, 1, 1]])

        if shx:
            arrMat = np.array([[1, shx, 0], 
                                [0, 1, 0], 
                                [0, 0, 1]])

        if shy:
            arrMat = np.array([[1, 0, 0], 
                                [shy, 1, 0], 
                                [0, 0, 1]])

        tranMat = np.dot(arrMat, arrPoint)

        self.canvas_draw(tranMat, choice)



if __name__ == "__main__":

    print("1. Translation\n2. Rotation\n3. Scaling\n4. Reflection\n5. Shearing")
    choiceTransform = int(input("Enter your choice of transformation: "))

    print("\n1. Line\n2. Triangle\n3. Rectangle")
    choiceShape = int(input("Enter your choice of shape for transformation: "))

    if choiceShape == 1:
        x0, y0, x1, y1 = [int(x) for x in input("\nEnter two endpoints of line: ").split()]

    elif choiceShape == 2:
        x0, y0, x1, y1, x2, y2 = [int(x) for x in input("Enter three vertices of triangle: ").split()]

    elif choiceShape == 3:
        x0, y0, x1, y1, x2, y2, x3, y3 = [int(x) for x in input("\nEnter four vertices of rectangle: ").split()]

    else:
        print("Enter valid choice of shape for transformation")


    if choiceTransform == 1:

        tx, ty = [int(x) for x in input("Enter tx and ty: ").split()]

        root = tk.Tk()
        app = TkTransform(root)
        app.create_widgets()

        if choiceShape == 1:
            app.translate(choiceShape, tx, ty, x0, y0, x1, y1)
        elif choiceShape == 2:
            app.translate(choiceShape, tx, ty, x0, y0, x1, y1, x2, y2)
        elif choiceShape == 3:
            app.translate(choiceShape, tx, ty, x0, y0, x1, y1, x2, y2, x3, y3)

    
    elif choiceTransform == 2:

        angle = float(input("Enter angle to rotate: "))

        root = tk.Tk()
        app = TkTransform(root)
        app.create_widgets()

        if choiceShape == 1:
            app.rotate(choiceShape, angle, x0, y0, x1, y1)
        elif choiceShape == 2:
            app.rotate(choiceShape, angle, x0, y0, x1, y1, x2, y2)
        elif choiceShape == 3:
            app.rotate(choiceShape, angle, x0, y0, x1, y1, x2, y2, x3, y3)


    elif choiceTransform == 3:

        sx, sy = [int(x) for x in input("Enter scaling factors Sx and Sy: ").split()]

        root = tk.Tk()
        app = TkTransform(root)
        app.create_widgets()

        if choiceShape == 1:
            app.scale(choiceShape, sx, sy, x0, y0, x1, y1)
        elif choiceShape == 2:
            app.scale(choiceShape, sx, sy, x0, y0, x1, y1, x2, y2)
        elif choiceShape == 3:
            app.scale(choiceShape, sx, sy, x0, y0, x1, y1, x2, y2, x3, y3)


    elif choiceTransform == 4:

        reflect = input("Reflection about: ")

        root = tk.Tk()
        app = TkTransform(root)
        app.create_widgets()

        if choiceShape == 1:
            app.reflect(choiceShape, reflect, x0, y0, x1, y1)
        elif choiceShape == 2:
            app.reflect(choiceShape, reflect, x0, y0, x1, y1, x2, y2)
        elif choiceShape == 3:
            app.reflect(choiceShape, reflect, x0, y0, x1, y1, x2, y2, x3, y3)


    elif choiceTransform == 5:

        print("\n1. Shearing on x\n2. Shearing on y")
        choiceShear = int(input("Enter choice on shearing: "))

        sh = int(input("Enter shearing factor: "))

        if choiceShear == 1:
            shx = sh
            shy = 0
        elif choiceShear == 2:
            shx = 0
            shy = sh

        root = tk.Tk()
        app = TkTransform(root)
        app.create_widgets()

        if choiceShape == 1:
            app.shear(choiceShape, shx, shy, x0, y0, x1, y1)
        elif choiceShape == 2:
            app.shear(choiceShape, shx, shy, x0, y0, x1, y1, x2, y2)
        elif choiceShape == 3:
            app.shear(choiceShape, shx, shy, x0, y0, x1, y1, x2, y2, x3, y3)


    else:
        print("Please enter a valid choice of transormation")


    root.geometry(f"{height}x{width}")
    root.mainloop()        
