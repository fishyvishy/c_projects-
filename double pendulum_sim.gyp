import tkinter as tk
import math
import random

r1, r2 = 100, 100
m1, m2 = 10, 10
g = 9.81

class main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Double Pendulum System")
        self.canvas = tk.Canvas(self, width = 440, height = 420)
        self.canvas.pack()
        p_right = int(self.winfo_screenwidth()/2 - 250)
        p_down = int(self.winfo_screenheight()/2 - 300)
        self.geometry("+{}+{}".format(p_right, p_down))


        self.ang1 = random.random()*2*math.pi
        self.ang2 = random.random()*2*math.pi
        self.ang1_v, self.ang2_v = 0, 0
        self.delt_t = 0.1
        self.trace_coord = []
        self.z = 1
        self.after(1, self.movement)

    def movement(self):
        self.canvas.delete('Pendulum')
        self.canvas.delete('tracer')
        self.canvas.delete('angle')

        num1 = (-g*(2*m1 + m2)*math.sin(self.ang1))
        num2 = (-m2*g*math.sin(self.ang1-2*self.ang2))
        num3 = (-2*math.sin(self.ang1-self.ang2)*m2)
        num4 = (self.ang2_v*self.ang2_v*r2+self.ang1_v*self.ang1_v*r1*math.cos(self.ang1-self.ang2))
        den1 = (r1*(2*m1+m2-m2*math.cos(2*self.ang1-2*self.ang2)))
        ang1_a = (num1+num2+(num3*num4))/den1

        num5 = (2*math.sin(self.ang1-self.ang2))
        num6 = (self.ang1_v*self.ang1_v*r1*(m1+m2))
        num7 = (g*(m1+m2)*math.cos(self.ang1))
        num8 = (self.ang2_v*self.ang2_v*r2*m2*math.cos(self.ang1-self.ang2))
        den2 = (r2*(2*m1+m2-m2*math.cos(2*self.ang1-2*self.ang2)))
        ang2_a = (num5*(num6+num7+num8))/den2 

    
        self.ang1_v += ang1_a * self.delt_t
        self.ang2_v += ang2_a * self.delt_t
        self.ang1 += self.ang1_v * self.delt_t
        self.ang2 += self.ang2_v * self.delt_t
        
        x1 = r1*math.sin(self.ang1)
        y1 = r1*math.cos(self.ang1)

        x2 = x1 + r2*math.sin(self.ang2)
        y2 = y1 + r2*math.cos(self.ang2)

        self.trace_coord.append((220 + x2, 150 + y2, 220 + x2 , 150 + y2))
        self.canvas.create_line(self.trace_coord, fill = 'lightskyblue', tag = 'tracer')
        self.canvas.create_line(220, 150, 220 + x1, 150 + y1, fill = 'coral2', tag = 'Pendulum')
        self.canvas.create_line(220 + x1, 150 + y1, 220 + x2, 150 + y2, fill = 'coral2', tag = 'Pendulum')
        self.canvas.create_oval(210 + x1, 160 + y1, 230 + x1, 140 + y1, fill = 'coral2', outline = '', tag = 'Pendulum')
        self.canvas.create_oval(210 + x2, 160 + y2, 230 + x2, 140 + y2, fill = 'coral2', outline = '', tag = 'Pendulum')
    
        def keypress(event):
            self.canvas.delete('intro')
            self.after(1, self.movement)

        def pass_ev(event):
            pass

        if self.z > 0:
            print(self.ang1, self.ang2)
            self.canvas.create_text(220, 400, fill = 'gray30', font = 'hussar 20 italic', text = "Press return", tag = 'intro')
            self.bind("<Return>", keypress)
            self.z -= 1
        
        else:
            self.canvas.create_text(175, 400, fill = 'gray30', font = 'hussar 15 italic', text = '\u03B8\u2081 = ' + str(round(self.ang1, 1)), tag = 'angle')
            self.canvas.create_text(265, 400, fill = 'gray30', font = 'hussar 15 italic', text = '\u03B8\u2082 = ' + str(round(self.ang2, 1)), tag = 'angle')
            self.bind("<Return>", pass_ev)
            self.after(1, self.movement)
               
sim = main()
sim.mainloop()
