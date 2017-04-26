#-*- encoding=UTF-8 -*-  

import os
import Tkinter as tk  

class Application(tk.Frame):  
    def __init__(self,master=None):  
        tk.Frame.__init__(self,master)  
        self.pack()  
        self.createWidgets()  
    def createWidgets(self):  
        self.btnSayHi=tk.Button(self)  
        self.btnSayHi["text"]="Hello"  
        self.btnSayHi["command"]=self.sayHi   
        self.btnSayHi.pack() 
        self.btnQuit=tk.Button(self,text="Quit",command=root.destroy) 
        self.btnQuit.pack()  
  
    def sayHi(self):  
        tk.messagebox.showinfo("Message","Hello World!") 
  
root=tk.Tk()  
app=Application(master=root)  
app.mainloop() 