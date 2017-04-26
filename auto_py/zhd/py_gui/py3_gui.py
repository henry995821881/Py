#-*- encoding=UTF-8 -*-  
from Tkinter import *
 
master = Tk()
 
e = Entry(master)
 
e.pack()
 
e.focus_set()
 
a=[]
 
global a
 
def clr_text():
 
    e.delete(0, END)
 
    #a.pop()删除最后一个元素
 
def callback():
 
    n = e.get()
    print n
 
    a.append(n)
 
def list_n():
 
    print a
 
b1 = Button(master, text="get", width=10, command=callback)
 
b1.pack()
 
b2 = Button(master, text="clear", width=10, command=clr_text)
 
b2.pack()
 
b3 = Button(master, text="comfirm", width=10, command=list_n)
 
b3.pack()
 
mainloop()