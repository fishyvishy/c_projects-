from tkinter import *
window = Tk()
window.title("Prime Identifier")
window.geometry('268x175')
intro = Label(window, text = "Prime Identifier", font = ("Cambria", 40))
intro.grid(column=1, row=0)

txt = Entry(window, width = 10)
txt.grid(column=1, row = 1)

lbl = Label(window, text = "Enter a number")
lbl.grid(column=1, row = 2)

def check():
    num = int(txt.get())
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            lbl.configure(text = "The number is not a prime")
            break
        else:
            lbl.configure(text = "The number is a prime!!")

btn = Button(window, text = "Click to check", command = check)
btn.grid(column=1, row = 3)

window.mainloop()


