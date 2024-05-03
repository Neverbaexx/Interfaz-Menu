from tkinter import*
ventana=Tk()

menu=Menu(ventana)
ventana.config( menu = menu)


File=Menu(menu, tearoff=0)
File.add_command (label= "New Project...")
File.add_command (label= "Open")
File.add_command (label= "Save")
File.add_separator ()
File.add_command (label= "Exit")

Edit=Menu (menu, tearoff=0)
Edit.add_command (label="copy")
Edit.add_command (label="cut")
Edit.add_command (label="paste")

help=Menu (menu, tearoff=0)
help.add_command(label="Help")
help.add_separator() 
help.add_command (label= "About")


menu.add_cascade (label= "file", menu=File)
menu.add_cascade (label= "Edit", menu=File)
menu.add_cascade (label= "Help", menu=File)

ventana.mainloop ()

