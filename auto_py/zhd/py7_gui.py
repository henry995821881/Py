#-*- encoding=UTF-8 -*-  
import  Tkinter as Tk
import os
 

#url_base=/gzql/sfjlko
#username=yy888888
#passwd=888888
#buy_num=2
#make_num=2
#order_id=8212
#cal_way=2

class mygui():

	def __init__(self):

		self.master = Tk()
		self.param=self.master.StringVar()
		self.param1=TK.StringVar()
		self.param2=TK.StringVar()
		self.param3=TK.StringVar()
		self.param4=Tk.StringVar()
		self.param5=TK.StringVar()
		self.param6=TK.StringVar()
		
		self.master.title("友邻港自动测试")
		filename = "history.txt" 
		if not os.path.exists(filename):
			f = open("history.txt","w")
			f.close()
		a_dict = {}
		f = open("history.txt","r")
		str_line = f.readlines()
		for s in str_line:
			li = s.split("=")
			a_dict[li[0]]=''.join(li[1]).strip('\n')
		f.close()
		print str_line
		self.a_dict = a_dict


	def get_param(self,key,dict_):
		if a_dict.has_key(key):
			val=a_dict[key]
		else:
			val=""
		return val







	def clear_text(self):
	 	self.param.set("")
	 	self.param1.set("")
	 	self.param2.set("")
	 	self.param3.set("")
	 	self.param4.set("")
	 	self.param5.set("")
	 	self.param6.set("")





	def write_new_param(self):
		os.remove("history.txt")
		f = open("history.txt","w")
		dict1 = get_all_text()
		li_for_write=[]
		for k,v in dict1.items():
			li_for_write.append(k+"="+v+"\n")

		f.writelines(li_for_write)	
		f.close






	def get_all_text(self):
		b_dict ={}
		b_dict["url_base"]=self.e.get()
		b_dict["username"]=self.e1.get()
		b_dict["passwd"]=self.e2.get()
		b_dict["buy_num"]=self.e3.get()
		b_dict["make_num"]=self.e4.get()
		b_dict["order_id"]=self.e5.get()
		b_dict["cal_way"]=self.e6.get()
		return b_dict





	def paint_gui(self):	

		dict_ = self.a_dict

		Label(self.master,text="url_base:").grid(row=0)
		e = Entry(self.master,textvariable=self.param)
		e.focus_set()
		e.grid(row=0,column=1)
		self.param.set(get_param("url_base",dict_))
		self.e = e

		Label(self.master,text="username:").grid(row=1)
		e1 = Entry(self.master,textvariable=self.param1)
		e1.grid(row=1,column=1)
		self.param1.set(get_param("username",dict_))
		self.e1 = e1

		Label(self.master,text="passwd:").grid(row=2)
		e2 = Entry(self.master,textvariable=self.param2)
		e2.grid(row=2,column=1)
		self.param2.set(get_param("passwd",dict_))
		self.e2 = e2

		Label(self.master,text=u"商品购买数量:").grid(row=3)
		e3 = Entry(self.master,textvariable=self.param3)
		e3.grid(row=3,column=1)
		self.param3.set(get_param("buy_num",dict_))
		self.e3 =e3


		Label(self.master,text=u"商品制作数量:").grid(row=4)
		e4 = Entry(self.master,textvariable=self.param4)
		e4.grid(row=4,column=1)
		self.param4.set(get_param("make_num",dict_))
		self.e4=e4


		Label(self.master,text=u"商品orderId:").grid(row=5)
		e5 = Entry(self.master,textvariable=self.param5)
		e5.grid(row=5,column=1)
		self.param5.set(get_param("order_id",dict_))
		self.e5 =e5


		Label(self.master,text=u"理计2or磅计购买1:").grid(row=6)
		e6 = Entry(self.master,textvariable=self.param6)
		e6.grid(row=6,column=1)
		self.param6.set(get_param("cal_way",dict_))
		self.e6=e6



		clear_btn =Button(self.master,text="重置参数",command=self.clear_text)
		clear_btn.grid(row=7)
		self.clear_btn = clear_btn


		submit_btn=Button(self.master,text="执行浏览器",command=self.write_new_param)
		submit_btn.grid(row=7,column=1)
		self.submit_btn=submit_btn




gui1 = mygui()
#gui1.paint_gui()
#gui1.master.mainloop()
