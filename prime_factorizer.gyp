import tkinter as tk

root = tk.Tk()
root.title("Prime Factors")
canvas = tk.Canvas(root, width = 400, height = 300, bg = 'lightskyblue')
canvas.pack()
p_right = int(root.winfo_screenwidth()/2 - 200)
p_down = int(root.winfo_screenheight()/2 - 200)
root.geometry('+{}+{}'.format(p_right, p_down))

canvas.create_text(200, 60, fill = 'black', font = 'verdana 45', text = 'Prime Factors')
entry = tk.Entry(root, width = 15)
canvas.create_window(200, 120, window = entry)

def textorg(txt):
    exptext = ''
    text2 = sorted(set(txt))
    for i in text2:
        exptext += str(i) + 'exp(' + str(txt.count(i)) + ') ' 
    
    translation = str(exptext).maketrans({1: '\u00b9' , 2: '\u00b8'})
    print(exptext.translate(translation))

def primeFactors(event):
    canvas.delete('factors')
    num = int(eval(entry.get())) 
    num2 = str(int(eval(entry.get())))
    factors = []
    while num % 2 == 0: 
        factors.append(2)
        num = int(num/2)
          
    for i in range(3,int(num**0.5)+1,2): 
        while num % i == 0: 
            factors.append(i)
            num = int(num/i)
        
    if num > 2:
        factors.append(num)

    textorg(factors)
    fulltext = str(num2) + ' = ' + str(factors)[1:-1].replace(',', ' \u00D7')
    canvas.create_text(200, 180, fill = 'black', font = 'verdana 20', text = fulltext, width = 360, justify = 'center', anchor = 'n', tag = 'factors')

root.bind("<Return>", primeFactors)

root.mainloop()