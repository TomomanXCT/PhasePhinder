from tkinter import *

root = Tk()
root.title('PhasePhinder')
root.iconbitmap('phasy_new.ico')
root.geometry("490x250")

#def myClick():
#    hello = "Hello " + e.get()
#    myLabel = Label(root, text=hello)
#    e.delete(0, 'end')
#    myLabel.pack(pady=10)



#myButton = Button(root, text="Enter Your Name", command=myClick)
#myButton.pack(pady=10)

def show():
    myLabel = Label(root, text='.').grid(column=3,row=13)
    myLabel2 = Label(root, text='Special thanks to Francesco Iacoviello and Marco Endrizzi for providing the required data,').grid(column=1,row=15,columnspan=7)
    myLabel3 = Label(root, text='and thanks to Andrew Morrison saving the IF statments.').grid(column=1,row=16,columnspan=4)
    myLabel4 = Label(root, text='R. S. Young 2022').grid(column=2,row=17,columnspan=2)
    
instruct = Label(root,text="Voltage").grid(column=1,row=2)
instruct2 = Label(root,text="Optical Magnification").grid(column=1,row=4)
instruct3 = Label(root,text="Source to sample distance (mm)").grid(column=1,row=6)
instruct4 = Label(root,text="CAUTION: Be sure that the positions do not lead to a collision!").grid(column=1,row=11,columnspan=5)
instruct5 = Label(root,text="Plan before you scan.").grid(column=2,row=12,columnspan=2)

var = StringVar()

var.set("No")
var2 = StringVar()
var2.set("No")
x = None

c =Checkbutton(root, text="30-100kV", variable=var, onvalue="qq")
c.grid(column=3,row=2)
#c.deselect()
#c.pack()

d =Checkbutton(root, text="100-160kV", variable=var, onvalue="qp")
d.grid(column=4,row=2)
#d.deselect()
#d.pack()

f =Checkbutton(root, text="0.4X", variable=var2, onvalue="wa")
f.grid(column=3,row=4)
#f.deselect()
#f.pack()

g =Checkbutton(root, text="4X", variable=var2, onvalue="wb")
g.grid(column=4,row=4)
#g.deselect()
#g.pack()

h =Checkbutton(root, text="20X", variable=var2, onvalue="wc")
h.grid(column=5,row=4)
#h.deselect()
#h.pack()

j =Checkbutton(root, text="40X", variable=var2, onvalue="wd")
j.grid(column=6,row=4)
#j.deselect()
#j.pack()
En = Entry(root, width=10)
En.grid(column=4,row=6)


    
print('Im here')    
def EqWay():
    x=StringVar();
    if var.get()=="qq" and var2.get()=="wa":
        x=(float(En.get()))/0.0631
    
    if var.get()=="qq" and var2.get()=="wb":
        x=(float(En.get()))/0.3426
        
    if var.get()=="qq" and var2.get()=="wc":
        x=(float(En.get()))/0.5576
        
    if var.get()=="qq" and var2.get()=="wd":
        x=(float(En.get()))/0.7003
        
    if var.get()=="qp" and var2.get()=="wa":
        x=(float(En.get()))/0.0927
        
    if var.get()=="qp" and var2.get()=="wb":
        x=(float(En.get()))/0.431
        
    if var.get()=="qp" and var2.get()=="wc":
        x=(float(En.get()))/0.6474
        
    if var.get()=="qp" and var2.get()=="wd":
        x=(float(En.get()))/0.7766
    
    myLabel = Label(root, text='Move the detector '+str(round(x,2))+'mm from the sample.').grid(column=3,row=8,columnspan=4)

#myButton = Button(root, text="Confirm", command=EqWay).grid(column=1,row=10)
myButton2 = Button(root, text="Find phase region", command=EqWay).grid(column=3,row=10)

myButton3 = Button(root, text="?", command=show).grid(column=7,row=2)
    
    
root.mainloop()
