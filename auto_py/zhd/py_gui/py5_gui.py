#-*- encoding=UTF-8 -*-  
from Tkinter import *
import os
 

#url_base=/gzql/sfjlko
#username=yy888888
#passwd=888888
#buy_num=2
#make_num=2
#order_id=8212
#cal_way=2


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
print a_dict



master = Tk()
master.title("友邻港自动测试")

def get_param(key):
	if a_dict.has_key(key):
		val=a_dict[key]
	else:
		val=""
	return val
	
 
def clear_text():
 	param.set("")
 	param1.set("")
 	param2.set("")
 	param3.set("")
 	param4.set("")
 	param5.set("")
 	param6.set("")

def write_new_param():
	os.remove("history.txt")
	f = open("history.txt","w")
	dict1 = get_all_text()
	li_for_write=[]
	for k,v in dict1.items():
		li_for_write.append(k+"="+v+"\n")

	f.writelines(li_for_write)	
	f.close




def get_all_text():
	b_dict ={}
	b_dict["url_base"]=e.get()
	b_dict["username"]=e1.get()
	b_dict["passwd"]=e2.get()
	b_dict["buy_num"]=e3.get()
	b_dict["make_num"]=e4.get()
	b_dict["order_id"]=e5.get()
	b_dict["cal_way"]=e6.get()
	return b_dict


Label(master,text="url_base:").grid(row=0)
param = StringVar()
e = Entry(master,textvariable=param)
e.focus_set()
e.grid(row=0,column=1)
param.set(get_param("url_base"))

param1 = StringVar()
Label(master,text="username:").grid(row=1)
e1 = Entry(master,textvariable=param1)
e1.grid(row=1,column=1)
param1.set(get_param("username"))

param2= StringVar()
Label(master,text="passwd:").grid(row=2)
e2 = Entry(master,textvariable=param2)
e2.grid(row=2,column=1)
param2.set(get_param("passwd"))


param3 = StringVar()
Label(master,text=u"商品购买数量:").grid(row=3)
e3 = Entry(master,textvariable=param3)
e3.grid(row=3,column=1)
param3.set(get_param("buy_num"))

param4=StringVar()
Label(master,text=u"商品制作数量:").grid(row=4)
e4 = Entry(master,textvariable=param4)
e4.grid(row=4,column=1)
param4.set(get_param("make_num"))


param5=StringVar()
Label(master,text=u"商品orderId:").grid(row=5)
e5 = Entry(master,textvariable=param5)
e5.grid(row=5,column=1)
param5.set(get_param("order_id"))


param6=StringVar()
Label(master,text=u"理计2or磅计购买1:").grid(row=6)
e6 = Entry(master,textvariable=param6)
e6.grid(row=6,column=1)
param6.set(get_param("cal_way"))



clear_btn =Button(master,text="重置参数",command=clear_text)
clear_btn.grid(row=7)


submit_btn=Button(master,text="执行浏览器",command=write_new_param)
submit_btn.grid(row=7,column=1)



mainloop()
