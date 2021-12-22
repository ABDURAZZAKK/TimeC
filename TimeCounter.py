import tkinter as tk 

def testVal(inStr,acttyp):
    if acttyp == '1':
        if not inStr.isdigit():
            return False
    return True
 
def pr(event):
    tim = int(entry.get())
    res = 0 
    speed = var.get()
    while tim >= 1:
        res+= tim
        if speed == 1:
            label["text"]+=f"min={int(res*100)/100} hour={int(((res/60)*100)/100)}\n"
            return
        tim/=speed
    entry.delete(0,tk.END)
    label["text"]=f"min={(res*100)/100:.{2}f} hour={((res/60)*100)/100:.{2}f}\n"
        
    
 
 
root = tk.Tk()
root.title("TimeCounter")
root.geometry("230x100-2500+200")


 
var = tk.DoubleVar()
var.set(1.0)

f_right = tk.Frame(root)
f_left = tk.Frame(root)

x1_5 = tk.Radiobutton(f_left, text="x1.5", variable=var, value=1.5)
x2 = tk.Radiobutton(f_left, text="x2", variable=var, value=2.0)
x2_5 = tk.Radiobutton(f_left, text="x2.5", variable=var, value=2.5)
x3 = tk.Radiobutton(f_left, text="x3", variable=var, value=3.0)

                   
entry = tk.Entry(f_right,validate="key")
entry['validatecommand'] = (entry.register(testVal),'%P','%d')
label = tk.Label(f_right, width=20, height=10)


f_right.pack(side=tk.LEFT)
f_left.pack(side=tk.RIGHT)

x1_5.pack(anchor=tk.NW)
x2.pack(anchor=tk.NW)
x2_5.pack(anchor=tk.NW)
x2_5.select()
x3.pack(anchor=tk.NW)
entry.pack(side=tk.TOP)
label.pack(side=tk.TOP)

entry.bind("<Return>", pr)
 
root.mainloop()
 