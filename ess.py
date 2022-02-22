from curses import window
from tkinter import *
from PIL import ImageTk



    
root= Tk()
root.title("slider")
root.geometry("2000x2000")

        

        
    #=====image====
image1=ImageTk.PhotoImage(file="img1.jpeg")
lbl1=Label(root,image=image1,bd=0)
lbl1.place(x=20,y=100)

image2=ImageTk.PhotoImage(file="img2.jpeg")
lbl2=Label(root,image=image2,bd=0)
lbl2.place(x=500,y=100)
x=500

scrol= Scrollbar(orient=VERTICAL,width=25)
scrol.pack(side=RIGHT,fill= Y)
scrol= Scrollbar(root,orient=HORIZONTAL)
scrol.pack(side=BOTTOM,fill=X)

def slider_fonct():
    global image1,image2  
    x =-1
    if x==0:
        x=500

        #new_im=image1
        image1=image2
        image2=image1
    lbl2.place(x,y=0)
    lbl2.after(1,slider_fonct)       
obj=slider_fonct
root.mainloop()


    