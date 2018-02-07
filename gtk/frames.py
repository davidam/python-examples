try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

ventana = Tk()
ventana.minsize(200, 200)
ventana.maxsize(300, 300)

zona1 = Frame(ventana, background='green', width=50, height=50)
zona1.pack(side=TOP, expand=True, fill=BOTH)
eti = Label(zona1, text="arriba", bg="yellow")
eti.pack()
Label(zona1, text="abajo", bg="yellow").pack(side=BOTTOM)

zona2 = Frame(ventana, background="blue", width=30, height=30)
zona2.pack(side=BOTTOM, expand=True, fill=BOTH)
Label(zona2, text="izquierda", bg='red').pack(side=LEFT)
Label(zona2, text="derecha", bg='red').pack(side=RIGHT)

ventana.mainloop()
