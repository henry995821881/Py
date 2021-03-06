from Tkinter import *
class LabelDemo(Frame):
    """Demonstrate Labels """
   
    def __init__(self):
        """create three Labels and pack them """
       
        Frame.__init__(self)
        #frame fills all available space
        self.pack(expand=YES,fill=BOTH)
        self.master.title('Labels')
        self.Label1=Label(self,text='Label with text')
        #resize frame to acommodate Label
        self.Label1.pack()
       
        self.Label2=Label(self,text='Labels with text and a bitmap')
        #insert Label against left side of frame
        self.Label2.pack(side=LEFT)
        #using default bitmap image as label
        self.Label3=Label(self,bitmap="warning")
        self.Label3.pack(side=LEFT)
def main():
    LabelDemo().mainloop()#starts event loop

if __name__=='__main__':
    main()