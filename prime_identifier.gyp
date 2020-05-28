import tkinter as tk
window = tk.Tk()
window.title("Prime Identifier")
window.geometry("268x160")
pright = int(window.winfo_screenwidth()/2 - 268/2)
pdown = int(window.winfo_screenheight()/2.4 - 160/2)
window.geometry("+{}+{}".format(pright,pdown))

intro = tk.Label(window, text = "Prime Identifier", font = ("Cambria", 40))
intro.grid(column=1, row=0)

txt = tk.Entry(window, width = 10)
txt.grid(column=1, row = 1)

lbl = tk.Label(window, text = "Enter a number")
lbl.grid(column=1, row = 2)

def check():
    if '.' in txt.get():
        lbl.configure(text = "Please enter a positive whole number")
    else:
        num = int(eval(txt.get()))
    if num <= 0:
        lbl.configure(text = "Please enter a positive whole number")
    elif num == 1:
        lbl.configure(text = "The number is not a prime")
    elif num == 2 or num == 3:
        lbl.configure(text = "The number is a prime!!!")
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            lbl.configure(text = "The number is not a prime")
            break
        else:
            lbl.configure(text = "The number is a prime!!!")

btn = tk.Button(window, text = "Click to check", command = check)
btn.grid(column=1, row = 3)

window.mainloop()
