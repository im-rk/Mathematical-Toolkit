import math
from  tkinter import *
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
import numpy as np 
from matplotlib.figure import Figure

'''
root=Tk()
root.title('math')
root.geometry('500x500')
menu= StringVar()
menu.set("Select Any Operation")

#Create a dropdown Menu
drop= OptionMenu(root, menu,"roots of quadraic equations", "Add of matrix","Sub of matrix","Mult of matrix","Det of matrix")
drop.pack()

b1=Button(root, text="submit",
                command=lambda m="pressed": which_buttonnn(m)).place(x=200,y=200)

def which_buttonnn(button_press):
    selected =menu.get()
    print(type(selected))
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
    
root.mainloop()
'''
######################################################################################

# ROOTS OF A QUADRATIC EQUATIONS
def quadraticroots():
    root=Tk()
    root.title('solving quadratic equation')
    root.geometry('500x300')
    root.config(bg='green')
    #labels
    l1=Label(root,text='enter the coefficient of x^2:',bg='green').place(x=40,y=60)
    l2=Label(root,text='enter the coeeficient of x:',bg='green').place(x=40,y=80)
    l3=Label(root,text='enter the constant:',bg='green').place(x=40,y=100)

    #entry
    e1=Entry(root,width=30)
    e1.place(x=200,y=60)
    e2=Entry(root,width=30) 
    e2.place(x=200,y=80)
    e3=Entry(root,width=30)
    e3.place(x=200,y=100)
    #button1
    b1=Button(root, text="SUBMIT",fg='red', bg='yellow',
                command=lambda m="pressed": which_button(m)).place(x=200,y=150)


    #logic
    def which_button(button_press):
        
        a=e1.get()
        b=e2.get()
        c=e3.get()
        
        if a.isdigit() ==False:
            messagebox.showinfo('warning','PLEASE ENTER A VALUE,ONLY DIGITS ARE ALLOWED')
        elif b.isdigit()==False:
            messagebox.showinfo('warning','PLEASE ENTER A VALUE,ONLY DIGITS ARE ALLOWED')
        elif c.isdigit()==False:
            messagebox.showinfo('warning','PLEASE ENTER A VALUE,ONLY DIGITS ARE ALLOWED')
        
        
        discriminant=int(b)**2 - 4 *int(a)*int(c)
        if discriminant > 0:
            root1 = (-int(b) + math.sqrt(discriminant)) / (2 * int(a))
            root2 = (-int(b) - math.sqrt(discriminant)) / (2 * int(a))
            print("Roots are real and distinct")
            l4=Label(root,text='roots are real and distinct',bg='green').place(x=170,y=200)
            l5=Label(root,text=root1,bg='green').place(x=170,y=220)
            l6=Label(root,text=root2,bg='green').place(x=170,y=235)
            print("Root 1:", root1)
            print("Root 2:", root2)

        elif discriminant == 0:
            r = -int(b) / (2 * int(a))
            l7=Label(root,text='roots are real and same',bg='green').place(x=170,y=200)
            l8=Label(root,text=r).place(x=100,y=150)
            print("Roots are real and same")
            print("Root:", r)

        else:
            realPart = -int(b)/ (2 * int(a))
            imaginaryPart = math.sqrt(-discriminant) / (2 * int(a))
            l9=Label(root,text='Roots are complex and different',bg='green').place(x=170,y=200)
            
            print("Roots are complex and different")
            print("Root 1:", realPart, "+", imaginaryPart, "i")
            print("Root 2:", realPart, "-", imaginaryPart, "i")
        
    root.mainloop()


#################################################################################################################


#determinant of a matrix
def detofamatrix():
    root=Tk()
    
    root.title('Determinant of a matrix')
    root.geometry('400x400')
    root.config(bg='green')
    #label
    l1=Label(root,text='enter the order of matrix:',bg='green').place(x=40,y=60)
    
    #entery1
    e1=Entry(root,width=30)
    e1.place(x=200,y=60)
    #button
    b1=Button(root, text="SUBMIT",fg='red', bg='yellow',
                command=lambda m="pressed": which_button(m)).place(x=200,y=100)
    
    #to check wheather 2by2 matrix or 3by3 matrix...
    def which_button(button_press):
        a=e1.get()
        print(a)
        if int(a)==2:
            det2()
        elif int(a)==3:
            det3()
    l=[]
    def det2():
        root.destroy() 
        master=Tk()
        master.title('ELEMENTS OF A MATRIX')
        master.geometry('300x350')
        master.config(bg='green')
        l=[]
        #new window is created 
        #all the elements are appended in a list
        
        def something():
            k=[]
            for i in l:
                x=i.get()
                k.append(x[18:])
            ans=int(k[0])*int(k[3])-int(k[1])*int(k[2])
            l3=Label(master,text='Deteminant=',bg='green').place(x=100,y=300)
            l4=Label(master,text=ans,bg='green').place(x=170,y=300)
            print(k)

        for i in range(4):
            e2=Entry(master,width=30)
            e2.insert(0, "enter the element:")
            e2.grid(row=i,column=0,padx=5,pady=20)
            l.append(e2)
        b2=Button(master,text='SUBMIT',fg='red', bg='yellow',width=10,command=something)
        b2.grid(row=5,column=0,pady=20)
       
        master.mainloop()
        
    def det3():   
        root.destroy() 
        master=Tk()
        master.title('ELEMENTS OF A MATRIX')
        master.geometry('600x600')
        master.config(bg='blue')
        l=[]
        #new window is created 
        #all the elements are appended in a list
        
        def something():
            k=[]
            for i in l:
                x=i.get()
                k.append(x[18:])
            ans=(int(k[0]) * ( int(k[4])*int(k[8]) - int(k[5]) * int(k[7]) ))  - ( int(k[1]) * ( int(k[3])*int(k[8]) - int(k[5])*int(k[6])) ) + int(k[2]) * ( int(k[3])*int(k[7]) - int(k[4])*int(k[6]))
            
            l3=Label(master,text='det=',bg='blue').place(x=100,y=300)
            l4=Label(master,text=ans,bg='blue').place(x=130,y=300)
            print(k)

        for i in range(9):
            e2=Entry(master,width=30)
            e2.insert(0, "enter the element:")
            e2.grid(row=i,column=0,padx=5,pady=20)
            l.append(e2)
        b2=Button(master,text='submit',width=10,command=something)
        b2.grid(row=5,column=7,pady=20)
       
        master.mainloop()

    
    root.mainloop()

#############################################################################################################
#ADDITION OF TWO MATRIX
def addofmatrix():
    root=Tk()
    
    root.title('Addition of a matrix')
    root.geometry('400x400')
    root.config(bg='green')
    #getting m,n values for matrix 1
    l1=Label(root,text='enter the order of matrix 1:',bg='green').place(x=40,y=60)
    l2=Label(root,text='m:',bg='green').place(x=40,y=80)
    l3=Label(root,text='n:',bg='green').place(x=40,y=100)
    e2=Entry(root,width=30)
    e2.place(x=70,y=80)
    e3=Entry(root,width=30)
    e3.place(x=70,y=100)

    #getting n,m values for matrix 2
    l4=Label(root,text='enter the order of matrix 2:',bg='green').place(x=40,y=150)
    l5=Label(root,text='m:',bg='green').place(x=40,y=170)
    l6=Label(root,text='n:',bg='green').place(x=40,y=190)
    e5=Entry(root,width=30)
    e5.place(x=70,y=170)
    e6=Entry(root,width=30)
    e6.place(x=70,y=190)

    #button
    b1=Button(root, text="SUBMIT",fg='red', bg='yellow',
                command=lambda m="pressed": which_button(m)).place(x=200,y=250)
    def which_button(button_press):
        
        a=e2.get()
        b=e3.get()
        c=e5.get()
        d=e6.get()
        if a.isdigit()==False or b.isdigit()==False or c.isdigit()==False or d.isdigit()==False:
            messagebox.showinfo("showinfo", "order should not be empty!!!")

        elif int(a)==int(c)==int(b)==int(d)==2:
            add2()
        elif int(a)==int(c)==int(b)==int(d)==3:
            add3()
        elif int(a)!=int(c) or int(b)!=int(d) :
            messagebox.showinfo("showinfo", "order of matrx 1 and matrix 2 should be equal!!!")
        elif int(a)!=2 and int(c)!=2 and int(b)!=2 and int(d)!=2 or int(a)!=3 and int(c)!=3 and int(b)!=3 and int(d)!=3:
            messagebox.showinfo("showinfo", "only 2by2 and 3by3 matrix is allowed!!!")
        elif a.isspace() or b.isspace() or c.isspace() or d.isspace():
            messagebox.showinfo("showinfo", "order should not be empty!!!")


        else:
            None
         
        
    def add2():
        root.destroy() 
        master=Tk()
        master.title('ELEMENTS OF A MATRIX')
        master.geometry('500x500')
        master.config(bg='green')
        l=[]
        #new window is created 
        #all the elements are appended in a list
        def something():
            k=[]
            for i in l:
                x=i.get()
                k.append(x[30:])
                print(k)
            ans1=int(k[0])+int(k[4])
            ans2=int(k[1])+int(k[5])
            ans3=int(k[2])+int(k[6])
            ans4=int(k[3])+int(k[7])
            ans_list=[str(ans1),str(ans2),str(ans3),str(ans4)]
            txt_output = Text(master, height=4, width=10)
            txt_output.grid(column=6, row=6)
            txt_output.insert(END,'answer:')
            for i in range(0,3,2):
                txt_output.insert(END, "\n"+ans_list[i] +"  "+ans_list[i+1])


        for i in range(8):
            e7=Entry(master,width=30)
            if i<4:
               e7.insert(0, "enter the element of matrix 1:")
            else:
               e7.insert(0, "enter the element of matrix 2:") 
            e7.grid(row=i,column=0,padx=5,pady=20)
            l.append(e7)
        b2=Button(master,text='SUBMIT',fg='red', bg='yellow',width=10,command=something)
        b2.grid(row=5,column=2,pady=20)

        master.mainloop()
    def add3():
        root.destroy() 
        master=Tk()
        master.title('ELEMENTS OF A MATRIX')
        master.geometry('800x800')
        master.config(bg='blue')
        l=[]
        #new window is created 
        #all the elements are appended in a list
        def something():
            k=[]
            for i in l:
                x=i.get()
                k.append(x[30:])
                print(k)
            ans1=int(k[0])+int(k[9])
            ans2=int(k[1])+int(k[10])
            ans3=int(k[2])+int(k[11])
            ans4=int(k[3])+int(k[12])
            ans5=int(k[4])+int(k[13])
            ans6=int(k[5])+int(k[14])
            ans7=int(k[6])+int(k[15])
            ans8=int(k[7])+int(k[16])
            ans9=int(k[8])+int(k[17])

            ans_list=[str(ans1),str(ans2),str(ans3),str(ans4),str(ans5),str(ans6),str(ans7),str(ans8),str(ans9)]
            txt_output = Text(master, height=4, width=10)
            txt_output.grid(column=6, row=6)
            txt_output.insert(END,'answer:')
            for i in range(0,9,3):
                txt_output.insert(END, "\n"+ans_list[i] +"  "+ans_list[i+1]+"  "+ans_list[i+2])


        for i in range(18):
            e7=Entry(master,width=30)
            if i<9:
               e7.insert(0, "enter the element of matrix 1:")
               e7.grid(row=i,column=0,padx=5,pady=20)
            else:
               e7.insert(0, "enter the element of matrix 2:") 
               e7.grid(row=i-9,column=3,padx=5,pady=20)
            l.append(e7)
        b2=Button(master,text='submit',width=10,command=something)
        b2.grid(row=5,column=2,pady=20)

        master.mainloop()
    root.mainloop()
    


###########################################################################################################
#sub of matrix
def subofmatrix():
    root=Tk()
    
    root.title('Subtraction of a matrix')
    root.geometry('500x500')
    root.config(bg='green')
    #getting m,n values for matrix 1
    l1=Label(root,text='enter the order of matrix 1:',bg='green').place(x=40,y=60)
    l2=Label(root,text='m:',bg='green').place(x=40,y=80)
    l3=Label(root,text='n:',bg='green').place(x=40,y=100)
    e2=Entry(root,width=30)
    e2.place(x=70,y=80)
    e3=Entry(root,width=30)
    e3.place(x=70,y=100)

    #getting n,m values for matrix 2
    l4=Label(root,text='enter the order of matrix 2:',bg='green').place(x=40,y=150)
    l5=Label(root,text='m:',bg='green').place(x=40,y=170)
    l6=Label(root,text='n:',bg='green').place(x=40,y=190)
    e5=Entry(root,width=30)
    e5.place(x=70,y=170)
    e6=Entry(root,width=30)
    e6.place(x=70,y=190)

    #button
    b1=Button(root, text="SUBMIT",fg='red', bg='yellow',
                command=lambda m="pressed": which_button(m)).place(x=200,y=250)
    def which_button(button_press):
        a=e2.get()
        b=e3.get()
        c=e5.get()
        d=e6.get()
        if a.isdigit()==False or b.isdigit()==False or c.isdigit()==False or d.isdigit()==False:
            messagebox.showinfo("showinfo", "order should not be empty!!!")

        elif int(a)==int(c)==int(b)==int(d)==2:
            add2()
        elif int(a)==int(c)==int(b)==int(d)==3:
            add3()
        elif int(a)!=int(c) or int(b)!=int(d) :
            messagebox.showinfo("showinfo", "order of matrx 1 and matrix 2 should be equal!!!")
        elif int(a)!=2 and int(c)!=2 and int(b)!=2 and int(d)!=2 or int(a)!=3 and int(c)!=3 and int(b)!=3 and int(d)!=3:
            messagebox.showinfo("showinfo", "only 2by2 and 3by3 matrix is allowed!!!")
        elif a.isspace() or b.isspace() or c.isspace() or d.isspace():
            messagebox.showinfo("showinfo", "order should not be empty!!!")


        else:
            None
        
    def add2():
        root.destroy() 
        master=Tk()
        master.title('ELEMENTS OF A MATRIX')
        master.geometry('500x500')
        master.config(bg='green')
        l=[]
        #new window is created 
        #all the elements are appended in a list
        def something():
            k=[]
            for i in l:
                x=i.get()
                k.append(x[30:])
                print(k)
            ans1=int(k[0])-int(k[4])
            ans2=int(k[1])-int(k[5])
            ans3=int(k[2])-int(k[6])
            ans4=int(k[3])-int(k[7])
            ans_list=[str(ans1),str(ans2),str(ans3),str(ans4)]
            txt_output = Text(master, height=4, width=10)
            txt_output.grid(column=6, row=6)
            txt_output.insert(END,'answer:')
            for i in range(0,3,2):
                txt_output.insert(END, "\n"+ans_list[i] +"  "+ans_list[i+1])


        for i in range(8):
            e7=Entry(master,width=30)
            if i<4:
               e7.insert(0, "enter the element of matrix 1:")
            else:
               e7.insert(0, "enter the element of matrix 2:") 
            e7.grid(row=i,column=0,padx=5,pady=20)
            l.append(e7)
        b2=Button(master,text='SUBMIT',fg='red', bg='yellow',width=10,command=something)
        b2.grid(row=5,column=2,pady=20)

        master.mainloop()
    def add3():
        root.destroy() 
        master=Tk()
        master.title('ELEMENTS OF A MATRIX')
        master.geometry('600x600')
        master.config(bg='blue')
        l=[]
        #new window is created 
        #all the elements are appended in a list
        def something():
            k=[]
            for i in l:
                x=i.get()
                k.append(x[30:])
                print(k)
            ans1=int(k[0])-int(k[9])
            ans2=int(k[1])-int(k[10])
            ans3=int(k[2])-int(k[11])
            ans4=int(k[3])-int(k[12])
            ans5=int(k[4])-int(k[13])
            ans6=int(k[5])-int(k[14])
            ans7=int(k[6])-int(k[15])
            ans8=int(k[7])-int(k[16])
            ans9=int(k[8])-int(k[17])

            ans_list=[str(ans1),str(ans2),str(ans3),str(ans4),str(ans5),str(ans6),str(ans7),str(ans8),str(ans9)]
            txt_output = Text(master, height=4, width=10)
            txt_output.grid(column=6, row=6)
            txt_output.insert(END,'answer:')
            for i in range(0,9,3):
                txt_output.insert(END, "\n"+ans_list[i] +"  "+ans_list[i+1]+"  "+ans_list[i+2])


        for i in range(18):
            e7=Entry(master,width=30)
            if i<9:
               e7.insert(0, "enter the element of matrix 1:")
               e7.grid(row=i,column=0,padx=5,pady=20)
            else:
               e7.insert(0, "enter the element of matrix 2:") 
               e7.grid(row=i-9,column=3,padx=5,pady=20)
            l.append(e7)
        b2=Button(master,text='submit',width=10,command=something)
        b2.grid(row=5,column=2,pady=20)

        master.mainloop()
    root.mainloop()


    

###############################################################################################################
#multiplication of matrix
def multofmatrix():
    root=Tk()
    
    root.title('Multiplication of a matrix')
    root.geometry('400x400')
    root.config(bg='green')
    #getting m,n values for matrix 1
    l1=Label(root,text='enter the order of matrix 1:',bg='green').place(x=40,y=60)
    l2=Label(root,text='m:',bg='green').place(x=40,y=80)
    l3=Label(root,text='n:',bg='green').place(x=40,y=100)
    e2=Entry(root,width=30)
    e2.place(x=70,y=80)
    e3=Entry(root,width=30)
    e3.place(x=70,y=100)

    #getting n,m values for matrix 2
    l4=Label(root,text='enter the order of matrix 2:',bg='green').place(x=40,y=150)
    l5=Label(root,text='m:',bg='green').place(x=40,y=170)
    l6=Label(root,text='n:',bg='green').place(x=40,y=190)
    e5=Entry(root,width=30)
    e5.place(x=70,y=170)
    e6=Entry(root,width=30)
    e6.place(x=70,y=190)

    #button
    b1=Button(root, text="SUBMIT",fg='red', bg='yellow',
                command=lambda m="pressed": which_button(m)).place(x=200,y=225)
    def which_button(button_press):
        global a,b,c,d
        a=e2.get()
        b=e3.get()
        c=e5.get()
        d=e6.get()
        if a.isdigit()==False or b.isdigit()==False or c.isdigit()==False or d.isdigit()==False:
            messagebox.showinfo("showinfo", "order should not be empty!!!")

        elif int(b)==int(c):
            mult()
        elif int(a)!=int(c) :
            messagebox.showinfo("showinfo", "column of matrx 1 and column order 2 should be equal!!!")
        else:
            None
        
    def mult():
        root.destroy() 
        master=Tk()
        master.title('ELEMENTS OF A MATRIX')
        master.geometry('525x600')
        master.config(bg='green')
        l=[]
        m=[]
        ans=[]
        
        for i in range(int(a)):
            l.append([])
        for i in range(int(c)):
            m.append([])
        
        count=0
        sum=1
        for i in range(int(d)):
            ans.append([])
        for i in range(int(a)*int(d)):
            ans[count].append(0)
            if i==int(d)*sum-1:
                count+=1
                sum+=1
        print(l,m,ans)
        #new window is created 
        #all the elements are appended in a list
        def something():
            m1=[]
            m2=[]
            u=0
            o=0
            for i in range(int(a)):
               m1.append([])
            for i in range(int(c)):
               m2.append([])
            for i in l:
                for j in i:
                  x=j.get()
                  m1[u].append(int(x[30:]))
                u+=1
            for i in m:
                for j in i:
                   y=j.get()
                   m2[o].append(int(y[30:]))
                o+=1
            print(m1)
            print(m2)    
            for i in range(len(m1)):
                for j in range(len(m2[0])):
                    for k in range(len(m2)):
                        ans[i][j] += m1[i][k] * m2[k][j]
            print(ans)
            txt_output = Text(master, height=4, width=10)
            txt_output.grid(column=2, row=6)
            txt_output.insert(END,'answer:')
            for i in range(len(ans)):
                txt_output.insert(END, "\n"+str(ans[i][:]))

        z=0
        t=0
        v=0
        g=0
        for i in range(int(a)*int(b)+int(c)*int(d)):
            e7=Entry(master,width=30)
            if i<int(a)*int(b):
               e7.insert(0, "enter the element of matrix 1:")
               e7.grid(row=i,column=0,padx=5,pady=20)
               if i<int(b)+z:
                    l[t].append(e7)
                    if i==int(b)+z-1:
                       z=z+int(b)
                       t+=1
            else:
               e7.insert(0, "enter the element of matrix 2:")
               e7.grid(row=i-int(a)*int(b)+int(c)*int(d)%2,column=3,padx=5,pady=20)
               if i<int(a)*int(b)+1+int(d)+v:
                   m[g].append(e7)
                   if i==int(a)*int(b)+int(d)+v-1:
                      v=v+int(d)
                      g+=1
        

        '''    
        if i<int(b)+z:
                l[t].append(e7)
                if i==int(b)+z-1:
                    z=z+int(b)
                    t+=1
        else:
            if i<int(a)*int(b)+1+int(d)+v:
                m[g].append(e7)
                if i==int(a)*int(b)+1+int(d)+v-1:
                    v=v+int(d)
                    g+=1
        '''
        b2=Button(master,text='SUBMIT',fg='red', bg='yellow',width=10,command=something)
        b2.grid(row=5,column=2,pady=20)

        master.mainloop()
    
    root.mainloop()

#########################################################################################################################
def graph_representation():
    root=Tk()
    root.title('graph plotter')
    root.geometry('400x400')
    root.config(bg='green')
    
    
    def which_button(button_press):
        a=e2.get()
        b=e3.get()
        c=e4.get()
        d=e5.get()
        l1=[]
        l2=[]
        for i in a.split(','):
            l1.append(int(i))
        for i in b.split(','):
            l2.append(int(i))
        print(l1)
        print(l2) 
  
        # the figure that will contain the plot 
        fig = Figure(figsize = (10, 10), 
                    dpi = 100) 
     
        
        # adding the subplot 
        plot1 = fig.add_subplot(111) 
    
        # plotting the graph 
        plot1.plot(l1,l2)
        
    
        # creating the Tkinter canvas 
        # containing the Matplotlib figure 
        canvas = FigureCanvasTkAgg(fig, 
                                master = root)   
        canvas.draw() 
    
        # placing the canvas on the Tkinter window 
        canvas.get_tk_widget().pack() 
    
        # creating the Matplotlib toolbar 
        toolbar = NavigationToolbar2Tk(canvas, 
                                    root) 
        toolbar.update() 
    
        # placing the toolbar on the Tkinter window 
        canvas.get_tk_widget().pack() 

        #
        #plot1.set_title('Top 5 Programming Languages')
        plot1.set_ylabel(str(d))
        plot1.set_xlabel(str(c))


    l2=Label(root,text='x:',bg='green').place(x=40,y=80)
    l4=Label(root,text='label of x:',bg='green').place(x=40,y=100)
    l3=Label(root,text='y:',bg='green').place(x=40,y=140)
    l5=Label(root,text='label of y:',bg='green').place(x=40,y=160)
    e2=Entry(root,width=30)
    e2.place(x=120,y=80)
    e3=Entry(root,width=30)
    e3.place(x=120,y=140)
    e4=Entry(root,width=30)
    e4.place(x=120,y=100)
    e5=Entry(root,width=30)
    e5.place(x=120,y=160)
    
    b1=Button(root,text='Plot Graph',fg='red', bg='yellow',command=lambda m="pressed": which_button(m)).place(x=200,y=200)
    
    root.mainloop()
