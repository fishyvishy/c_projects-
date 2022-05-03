#n-body simulation
import tkinter as tk
from random import uniform, randint
from body_vectors import Body, Vector
from color_map import gen_color_map

WWidth = 1000
WHeight = 650
REFRESH = 1
G = 5

color_map = gen_color_map()

class sim(tk.Canvas):
    """n-body simulation class. Subclass of tkinter Canvas class"""

    def __init__(self, parent: tk.Tk) -> None:
        super().__init__(parent)
        self.configure(width=WWidth, height=WHeight, bg='white')
        self.bodies = {}
        self.dt = 0.1
        self.softening = 2

    def populate(self, n) -> None:
        for _ in range(n):
            b = Body(randint(10, 50), Vector(uniform(0, 1000), uniform(0, 650)))
            color = color_map[randint(3, 94)]
            self.create_oval(b.position.x - b.mass/2, b.position.y - b.mass/2, b.position.x + b.mass/2, b.position.y + b.mass/2, fill = color, tag = 'bodies')
            self.bodies[b] = color
    
    def redraw(self) -> None:
        self.delete('bodies')
        for body in self.bodies:
            self.create_oval(body.position.x - body.mass/2, body.position.y - body.mass/2, body.position.x + body.mass/2, body.position.y + body.mass/2, fill = self.bodies[body], tag = 'bodies')

    def get_accelerations(self, body_i, body_j) -> None:
        r = body_j.position - body_i.position
        mag = G * body_j.mass / (r.norm()**2 + self.softening**2)**(3/2)
        return r * mag

    def update_accelerations(self) -> None:
        for body in self.bodies:
            body.acceleration *= 0
            for other in self.bodies:
                if other != body:
                    acc = self.get_accelerations(body, other)
                    body.acceleration += acc
        self.update_positions()

    def update_positions(self) -> None:
        for b in self.bodies:
            b.velocity += b.acceleration * self.dt
            b.position += b.velocity * self.dt
            self.redraw()
        self.after(REFRESH, self.update_accelerations)


if __name__ == "__main__":
    system_size = int(input('Enter number of bodies: '))
    root = tk.Tk()
    root.title('n-body Simulation')
    p_right = int(root.winfo_screenwidth() / 2 - WWidth / 2)
    p_down = int(root.winfo_screenheight() / 2 - WHeight / 2)
    root.geometry("+{}+{}".format(p_right, p_down))
    root.resizable(0, 0)
    canvas = sim(root)
    canvas.pack()
    canvas.populate(system_size)
    canvas.update_positions()
    root.mainloop()