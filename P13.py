from tkinter import*
def lenguajes (): 
    c=selC.get()
    cc=selCC.get()
    java=selJava.get()
    php=selPHP.get()
    python=selPython.get()
    
    
    print("valor de C...", c)
    print("Valor de C++...", cc)
    print("Valor de Java..", java )
    print("Valor de PHP...", php)
    print("Valor de Python...", python)
    global cadena 
    cadena = " "
    
    if c == 1 :
        cadena=cadena+"C"
    if cc == 1 : 
        cadena=cadena+"cc"  
    if java == 1 : 
        cadena=cadena+"java" 
    if php == 1: 
        cadena=cadena+"php" 
    if python == 1 : 
        cadena=cadena+"python" 
        
   
    

ventana=Tk()
ventana.geometry("170x300")
ventana.title("SoundFon")

lblPregunta= Label(ventana,text="¿que lenguaje de programacion conoces? ").place(x=100, y=40)

#crear Chekpoints
selC=IntVar()
selCC=IntVar()
selJava=IntVar()
selPHP=IntVar()
selPython=int()

chck=Checkbutton(ventana,text="C",variable=selC, onvalue=1, offvalue=0).place (x=100, y=60)
chck=Checkbutton(ventana,text="C++",variable=selC, onvalue=1, offvalue=0).place (x=100, y=80)
c=Checkbutton(ventana,text="java",variable=selC, onvalue=1, offvalue=0).place (x=100, y=100)
c=Checkbutton(ventana,text="PHP",variable=selC, onvalue=1, offvalue=0).place (x=100, y=120)
c=Checkbutton(ventana,text="Python",variable=selC, onvalue=1, offvalue=0).place (x=100, y=140)

btnlenguajes=Button(ventana,text="¿cuales selecciones?", command=lenguajes).place(x=100, y=220)





ventana.mainloop()

