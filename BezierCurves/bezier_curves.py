import tkinter as tk
import curves
import time

WWidth = 1000
WHeight = 650
REFRESH = 5


class GUI(tk.Canvas):
    def __init__(self, parent: tk.Tk) -> None:
        super().__init__(parent)
        self.configure(width=WWidth, height=WHeight, bg='white')
        self.binder = parent
        self.curve_type = None
        self.binder.bind('<KeyPress>', self.keystrokes)
        self.points_to_curves = {2: curves.linear, 3: curves.quadratic, 4: curves.cubic}
        self.control_points = []
        self.points_num = 0
        self.t = 0
        self.dt = 0.007

    def make_points(self, event):
        dotsize = 9
        if len(self.control_points) < 2:
            self.create_oval(event.x - dotsize/2, event.y - dotsize/2,
                             event.x + dotsize/2, event.y + dotsize/2,
                             outline='coral', fill='lightsalmon',
                             tags='controls')
        else:
            self.create_oval(event.x - dotsize/2, event.y - dotsize/2,
                             event.x + dotsize/2, event.y + dotsize/2,
                             outline='coral', tags='controls')
        self.control_points.append((event.x, event.y))
        if len(self.control_points) == self.points_num:
            end2 = self.control_points[1]
            self.control_points.append(end2)
            self.control_points.remove(end2)
            self.unbind('<Button 1>')
            self.delete(self.curve_type)
            self.binder.bind('<Return>', self.show_curve)
            self.binder.bind('<Tab>', self.animate_line)

    def show_curve(self, event):
        coords = []
        self.t = 0
        self.delete('line')
        while self.t <= 1.005:
            new = self.points_to_curves[self.points_num](self.control_points, self.t, False)
            coords.append((new[0][0], new[0][1], new[0][0], new[0][1]))
            line_seg = self.create_line(coords, fill='deepskyblue')
            self.tag_lower(line_seg)
            self.t += self.dt
        self.delete('controls')

    def connect_points(self):
        for i in range(len(self.control_points) - 1):
            x0, y0, x1, y1 = self.control_points[i][0], \
                             self.control_points[i][1], \
                             self.control_points[i + 1][0], \
                             self.control_points[i + 1][1]
            self.create_line(x0, y0, x1, y1, fill='blue', tags='connectors')
            self.tag_lower('connectors')

    def animation_objects(self, coords):
        colors = ['darkgreen', 'purple']
        points = self.points_to_curves[self.points_num](self.control_points,
                                                        self.t, True)
        if self.points_num == 2:
            p_bezier = points
        else:
            p_bezier = points[0]
            for group in points[1:]:
                c = str(colors[points.index(group) - 1])
                for i in range(len(group) - 1):
                    self.create_line(group[i][0], group[i][1], group[i + 1][0],
                                     group[i + 1][1], fill=c, width=1,
                                     tags='guidelines')
                    self.create_oval(group[i][0] - 4, group[i][1] - 4,
                                     group[i][0] + 4, group[i][1] + 4,
                                     fill=c, tags='guidelines')
                    self.create_oval(group[i + 1][0] - 4, group[i + 1][1] - 4,
                                     group[i + 1][0] + 4, group[i + 1][1] + 4,
                                     fill=c, tags='guidelines')
        coords.append((p_bezier[0], p_bezier[1], p_bezier[0], p_bezier[1]))
        self.create_line(coords, fill='deepskyblue', tags='curve_trace')
        self.create_oval(p_bezier[0] - 6, p_bezier[1] - 6, p_bezier[0] + 6,
                         p_bezier[1] + 6, fill='deepskyblue', tags='mover')
        self.create_text(WWidth/2, WHeight-15, text=f't = {round(self.t, 2)}',
                         justify='left', fill='black', font='hussar 18 italic',
                         tags='guidelines')

    def animate_line(self, event):
        self.t = 0
        curve_coords = []
        if self.points_num != 2:
            self.connect_points()
        while self.t <= 1.005:
            self.after(REFRESH, self.animate(curve_coords))
        self.delete('guidelines')
        self.delete('mover')
        self.delete('connectors')

    def animate(self, curve_coords):
        self.delete('guidelines')
        self.delete('mover')
        self.delete('curve_trace')
        self.animation_objects(curve_coords)
        self.tag_lower('mover')
        self.tag_lower('guidelines')
        self.tag_lower('curve_trace')
        self.tag_lower('connectors')
        self.update()
        self.t += self.dt

    def keystrokes(self, event):
        self.delete('controls')
        self.delete('mover')
        self.delete('connectors')
        self.delete('guidelines')
        self.control_points = []
        self.t = 0
        key_map = {'l': ['Linear Bezier Curve', 2],
                   'q': ['Quadratic Bezier Curve', 3],
                   'c': ['Cubic Bezier Curve', 4]}
        if event.char in key_map:
            if self.curve_type is not None:
                self.delete(self.curve_type)
            self.curve_type = self.create_text(WWidth / 2, WHeight - 15,
                                               text=key_map[event.char][0],
                                               justify='center', fill='black',
                                               font='hussar 18 italic')
            self.tag_raise(self.curve_type)
            self.points_num = key_map[event.char][1]
            self.bind("<Button 1>", self.make_points)

        elif event.char == 'r':
            self.delete('all')


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Bezier Curves')
    p_right = int(root.winfo_screenwidth() / 2 - WWidth / 2)
    p_down = int(root.winfo_screenheight() / 2 - WHeight / 2)
    root.geometry("+{}+{}".format(p_right, p_down))
    root.resizable(0, 0)
    canvas = GUI(root)
    canvas.pack()
    root.mainloop()
