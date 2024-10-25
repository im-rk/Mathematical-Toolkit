from tkinter import *
from codes import *

root=Tk()
root.title('math')
root.geometry('350x350')
menu= StringVar()
menu.set("Select Any Operation")
l=Label(root,text='MATHEMATICAL TOOLKIT',font='AERIAL',bg='#856ff8')
l.place(x=65,y=40)
#Create a dropdown Menu
drop= OptionMenu(root,menu,"roots of quadraic equations", "Add of matrix","Sub of matrix","Mult of matrix","Det of matrix","Graph Representation")
drop.place(x=100,y=95)

root.config(bg='#856ff8')
b1=Button(root, text="SUBMIT", fg='red', bg='yellow',
                command=lambda m="pressed": which_button(m)).place(x=150,y=249)

def which_button(button_press):
    selected =menu.get()
    #print(type(selected))
    if selected=='roots of quadraic equations':
        quadraticroots()
    if selected=='Add of matrix':
        addofmatrix()
    if selected=="Sub of matrix":
        subofmatrix()
    if selected=="Mult of matrix":
        multofmatrix()
    if selected=="Det of matrix":
        detofamatrix()
    if selected=='Graph Representation':
        graph_representation()
root.mainloop()