import tkinter as tk
import random
from math import pi

class main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Monte Carlo Approximation of Pi")
        self.canvas = tk.Canvas(self, width = 400, height = 400)
        self.canvas.pack()
        p_right = int(self.winfo_screenwidth()/2 - 200)
        p_down = int(self.winfo_screenheight()/2 - 250)
        self.geometry("+{}+{}".format(p_right, p_down))
        self.total_count = 0
        self.circle_count = 0
        self.after(1, self.create_background)

    def create_background(self):
        self.canvas.create_rectangle(6, 400, 400, 6, fill = 'dodgerblue', outline = 'red3', width = 0)
        self.canvas.create_oval(6, 400, 400, 6, fill = 'coral1', outline = None, width = 0)
        self.canvas.create_text(197, 180, fill = 'gray30', font = 'hussar 20 italic', text = "Enter a Number", tag = 'intro')
        self.entry = tk.Entry(self, width = 15, bd = 0, highlightcolor = 'gray')
        self.canvas.create_window(197, 212, window = self.entry, tag = 'slot')

        def keypress(event):
            self.canvas.delete('intro')
            self.canvas.delete('slot')
            self.iterations = int(self.entry.get())
            self.t = int(4000/self.iterations)
            self.after(1, self.approximation)        
        self.bind("<Return>", keypress)

    def approximation(self):
        self.unbind("<Return>")
        self.x1 = random.uniform(6, 394)
        self.y1 = random.uniform(6, 394)
        self.coord = self.x1, self.y1, self.x1 + 4, self.y1 + 4
        self.dot = self.canvas.create_oval(self.coord, fill = 'gray25', width = 0)
        self.x_mid = float((self.x1 +2) - 203)
        self.y_mid = float(-((self.y1 + 2) - 203)) 
        self.dist = float((self.x_mid**2 + self.y_mid**2)**0.5)
 
        if self.dist <= 197:
            self.circle_count += 1
        self.total_count += 1
        self.iterations -= 1
        
        if self.iterations > 0:
            self.after(self.t, self.approximation)
        else:
            self.res = 4*(self.circle_count/self.total_count)
            self.error = (self.res - pi)*100/pi
            self.bind("<Return>", self.result)  

    def result(self, event):
        self.unbind('<Return>')
        self.text1 = '\u03C0 \u2248 ' + str(round(self.res,5))
        self.text2 = str(round(self.error, 5)) + '%'
        self.canvas.create_text(197, 177, fill = 'white', font = 'hussar 20 italic', text = self.text1)
        self.canvas.create_text(197, 212, fill = 'white', font = 'hussar 20 italic', text = self.text2)

sim = main()
sim.mainloop()