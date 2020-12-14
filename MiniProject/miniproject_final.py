import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from tkinter import ttk, BOTH, Tk, BOTTOM, TOP, Frame, Button, Canvas, StringVar, IntVar, Entry, Label, INSERT
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.animation as animation
from matplotlib.widgets import Slider



sine       = lambda f,n:   np.sin(np.arange(n) * np.pi * 2 * f / float(n))

sawtooth   = lambda f,n:   np.mod(np.arange(n) * 2.0 * f/n + f/2.0, 2) - 1

square     = lambda f,n:   (sawtooth(f,n) >= 0) * 2.0 - 1

def tri(f,n):
    osc = 2 * sawtooth(f,n) * square(f,n) - 1
    # This needs a phase shift on top:
    sh = int(n / f / 4.0)
    return np.concatenate((osc[sh:], osc[:sh]))

whiteNoise = lambda n:     np.random.random(n) * 2.0 - 1

sineClip   = lambda f,n,r: np.clip(sine(f,n), -r, r)

def sineTrunc(f, n, t0, t1):
    r = np.arange(n) / float(n)
    envelope = (r > t0) * (r <= t1) * 1
    return sine(f,n) * envelope


is_manual = False


def initVar(rate=48000, plotN=128, f=750):

    plotF = f * plotN / rate

    plots = (
        (sine(plotF, plotN), "Sine, pure"),
        (-sine(plotF, plotN), "Sine, inverted"),
        (sineClip(plotF, plotN, 0.7), "Sine, clipped (70%)"),
        (sineTrunc(plotF, plotN, 0.1, 0.9), "Sine, truncated"),
        (square(plotF, plotN), "Square wave"),
        (tri(plotF, plotN), "Triangle wave"),
        (sawtooth(plotF, plotN), "Sawtooth wave"),
        (whiteNoise(plotN), "White Noise"),
    )

    return plots




# Seperated out config of plot to just do it once
class matplotlibSwitchGraphs:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.config_plot()
        self.canvas = FigureCanvasTkAgg(self.fig, self.master)
        self.config_window()
        self.switch_graphs(1, 48000, 128, 750)
        self.frame.pack(expand=True, fill=BOTH)

    def config_plot(self):
        self.fig, self.ax = plt.subplots(2)
        self.fig.subplots_adjust(hspace=0.3, wspace=0.3)
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)


    def config_window(self):
        toolbar = NavigationToolbar2Tk(self.canvas, self.master)
        toolbar.update()
        self.canvas.get_tk_widget().pack(expand=True, fill=BOTH)
        self.button = Button(self.master, text="Quit", command=self._quit)
        self.button.pack(side=BOTTOM)


        rateAxis = plt.axes([0.25, .03, 0.50, 0.02])
        self.rateSlider = Slider(rateAxis ,'Rate', 0, 192000, valinit=48000)

        plotn_var = IntVar()
        plotn_var.set(128)
        lbl2 = Label(self.master, text="Enter Samples to Plot: ").pack()
        ent2 = Entry(self.master, textvariable=plotn_var, width=20).pack()

        f_var = IntVar()
        f_var.set(750)
        lbl3 = Label(self.master, text="Enter Frequency: ").pack()
        ent3 = Entry(self.master, textvariable=f_var, width=20).pack()

        v = StringVar(self.master, "1")

        values = {
            "Sine, Pure": "1",
            "Sine, Inverted": "2",
            "Sine, clipped (70%)": "3",
            "Sine, Truncated": "4",
            "Square Wave": "5",
            "Triangle Wave": "6",
            "Sawtooth Wave": "7",
            "White Noise": "8"
        }

        for (text, val) in values.items():
            ttk.Radiobutton(self.master, text = text, variable = v, value = val, command=lambda: self.switch_graphs(v.get(), self.rateSlider.val, plotn_var.get(), f_var.get())).pack(side=BOTTOM)


    def draw_graph(self, timeSeries, name, rate):

        n = len(timeSeries)
        timesMsec = np.arange(n) * 1000.0 / rate
        self.ax[0].clear() # clear current axes
        self.ax[0].grid(True)
        self.ax[0].plot(timesMsec, timeSeries)
        self.ax[0].set(title=name)
        self.ax[0].set_xlim([0, max(timesMsec)])
        self.ax[0].set_ylim([-1.2, 1.2])
        self.ax[0].set_xlabel("Time (ms)")
        self.ax[0].grid(True)


        spectrum = np.abs(np.fft.rfft(timeSeries)) / n
        specFreq = np.fft.rfftfreq(n, 1.0 / rate)
        # Note that for the bar plot, we set the width to the size of each
        # frequency bin:
        self.ax[1].clear()
        self.ax[1].bar(specFreq, spectrum, width = rate / n, linewidth = 0)
        #axs[1].set_title("Frequency spectrum")
        # Limit the X axis to the given frequencies:
        self.ax[1].set_xlim([0, max(specFreq)])
        self.ax[1].set_ylim([0, 1])
        self.ax[1].set_xlabel("Frequency (Hz)")
        self.ax[1].set_ylabel("Intensity")

        print("Plotting: \"%s\"" % (name,))


        animation.FuncAnimation(self.fig, self.update_plot, interval=100)

        self.canvas.draw()


    def _quit(self):
        self.master.quit()  # stops mainloop
        self.master.destroy()

    def switch_graphs(self, value, rate, plotN, f):
        # Need to call the correct draw, whether we're on graph one or two
        print(rate, plotN, f)
        plots = initVar(rate, plotN, f)

        for index, (wavePlot, name) in enumerate(plots):
            if index+1 == int(value):
                self.draw_graph(wavePlot, name, rate)


    def update_slider(self, val):
        global is_manual
        is_manual=True
        self.update(val)

    def update(self, val):        
        # redraw canvas while idle
        self.fig.canvas.draw_idle()

        return val

    def update_plot(self, num):
        global is_manual
        if is_manual:
            return self.ax # don't change

        scale = 100 / 1000 / 5.0
        val = (self.rateSlider.val + scale) % self.rateSlider.valmax
        self.rateSlider.set_val(val)
        is_manual = False # the above line called update_slider, so we need to reset this
        return self.ax

    def on_click(self, event):
        # Check where the click happened
        (xm,ym),(xM,yM) = self.rateSlider.label.clipbox.get_points()
        if xm < event.x < xM and ym < event.y < yM:
            # Event happened within the slider, ignore since it is handled in update_slider
            return
        else:
            # user clicked somewhere else on canvas = unpause
            global is_manual
            is_manual=False


def main():
    root = Tk()
    app = matplotlibSwitchGraphs(root)

    app.rateSlider.on_changed(app.update_slider)

    root.geometry("3840x2160")
    root.mainloop()

if __name__ == '__main__':
    main()
