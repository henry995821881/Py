#-*- encoding=UTF-8 -*-  

import os
import Tkinter as tk  
from selenium import webdriver
import time

class Application(tk.Frame):  
    def __init__(self,master=None): 

        self.read_file_param()

        tk.Frame.__init__(self,master)  
        self.pack()  
        self.createWidgets()  




    def get_param(self,key):
        if self.a_dict.has_key(key):
            val=self.a_dict[key]
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




    def read_file_param(self):
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
        self.a_dict =a_dict


    def write_new_param(self):
        os.remove("history.txt")
        f = open("history.txt","w")
        dict1 = self.get_all_text()
        li_for_write=[]
        for k,v in dict1.items():
            li_for_write.append(k+"="+v+"\n")

        f.writelines(li_for_write)  
        f.close
        #执行浏览器
        self.run_chrome()





    def run_chrome(self):
        #url_base = "http://192.168.80.249:8080"
         url_base=self.e.get()
         username = self.e1.get()
         passwd = self.e2.get()
         #商品购买数量
         num = self.e3.get()
         #商品制作数量
         num2=self.e4.get()

         browser = webdriver.Chrome()
         browser.implicitly_wait(10)
         test_case = test_chrome()
         test_case.login(browser,username,passwd,url_base)
        
         # 可以多次调用加入购物车商品，前提是注意要相同卖家的。否则后面付款走不过去
         #4931的商品加入购物车 数量为3，
         orderid = self.e5.get()
         cacul_way = self.e6.get()# 理计购买2  磅计购买1
         
         test_case.addmycart(browser,orderid,num,cacul_way,url_base)



         #提交购物车中所有商品
         test_case.mycart(browser,url_base)
         #付定金批量支付
         test_case.payorder(browser,url_base)
         #制作提单
         test_case.makerprovide(browser,url_base)
         
         test_case.makerprovide2(browser,num2,url_base)
         #print
         test_case.printprovide(browser,url_base)
         time.sleep(10)
         browser.quit()




    def createWidgets(self):  
        
        tk.Label(self,text="url_base:").grid(row=0)
        self.param = tk.StringVar()
        self.e = tk.Entry(self,textvariable=self.param)
        self.e.focus_set()
        self.e.grid(row=0,column=1)
        self.param.set(self.get_param("url_base"))

        self.param1 = tk.StringVar()
        tk.Label(self,text="username:").grid(row=1)
        self.e1 = tk.Entry(self,textvariable=self.param1)
        self.e1.grid(row=1,column=1)
        self.param1.set(self.get_param("username"))

        self.param2= tk.StringVar()
        tk.Label(self,text="passwd:").grid(row=2)
        self.e2 = tk.Entry(self,textvariable=self.param2)
        self.e2.grid(row=2,column=1)
        self.param2.set(self.get_param("passwd"))


        self.param3 = tk.StringVar()
        tk.Label(self,text=u"商品购买数量:").grid(row=3)
        self.e3 = tk.Entry(self,textvariable=self.param3)
        self.e3.grid(row=3,column=1)
        self.param3.set(self.get_param("buy_num"))

        self.param4=tk.StringVar()
        tk.Label(self,text=u"商品制作数量:").grid(row=4)
        self.e4 = tk.Entry(self,textvariable=self.param4)
        self.e4.grid(row=4,column=1)
        self.param4.set(self.get_param("make_num"))


        self.param5=tk.StringVar()
        tk.Label(self,text=u"商品orderId:").grid(row=5)
        self.e5 = tk.Entry(self,textvariable=self.param5)
        self.e5.grid(row=5,column=1)
        self.param5.set(self.get_param("order_id"))


        self.param6=tk.StringVar()
        tk.Label(self,text=u"理计2or磅计购买1:").grid(row=6)
        self.e6 = tk.Entry(self,textvariable=self.param6)
        self.e6.grid(row=6,column=1)
        self.param6.set(self.get_param("cal_way"))



        self.clear_btn =tk.Button(self,text="重置参数",command=self.clear_text)
        self.clear_btn.grid(row=7)


        self.submit_btn=tk.Button(self,text="执行浏览器",command=self.write_new_param)
        self.submit_btn.grid(row=7,column=1)
                    
  

class test_chrome:

     #登陆
     def login(self,browser,name,pwd,url_base):
          browser.get(url_base+"/etrade/login.shtml?ref_url=/etrade/ucenter.shtml")
          time.sleep(1)
          browser.find_element_by_name("username").send_keys(name)
          browser.find_element_by_name("password").send_keys(pwd)
          browser.find_element_by_id("login_bt").click()
          time.sleep(5)


     #加入购物车 
     def addmycart(self,browser,orderid,num,way,url_base):
          browser.get(url_base+"/etrade/mall/mallDetail.shtml?order_id="+orderid)
          time.sleep(1)
          
          radios = browser.find_elements_by_class_name("price_type_class")
          if (len(radios) > 1 and way ==1):
            browser.find_element_by_css_selector("input[class='price_type_class'][value='1']").click()

          browser.find_element_by_id("count_number").clear()
          browser.find_element_by_id("count_number").send_keys(num)
          browser.find_element_by_id("buy").click()
          time.sleep(1)
        
       #提交购物车
     def mycart(self,browser,url_base):
          browser.get(url_base+"/gzql/mycart/mycart.shtml?menu_no=801101")
          time.sleep(1)
          browser.find_element_by_id("cx1").click()
          browser.find_element_by_id("submitAll").click()
          browser.find_elements_by_class_name("btn-primary")[0].click()
          time.sleep(1)

      #定金付款 付款所有定金订单
     def payorder(self,browser,url_base):
          browser.get(url_base+"/gzql/contract/contract_mgr_buy.shtml?menu_no=801102")
          time.sleep(1)
          #browser.find_elements_by_class_name("pay_order")[0].click()
          check_one_s = browser.find_elements_by_class_name("checkbox_one")
          if len(check_one_s) < 1:
               return
          for one in check_one_s:
                one.click()
                time.sleep(0.3)

          browser.find_element_by_id("batch_makeBill").click()
          time.sleep(1)
          browser.find_element_by_id("password_3").send_keys("888888")
          browser.find_element_by_id("vcode_3").send_keys("jlkf")
          browser.find_element_by_id("payButton").click()
          time.sleep(1)


      #提单制作列表 制作所有提单
     def makerprovide(self,browser,url_base):
          browser.get(url_base+"/gzql/contract/td_make.shtml?menu_no=802103")
          #checkbox_all = browser.find_element_by_id("maker_check_all")
          #print checkbox_all
          #checkbox_all.click()
          #time.sleep(60)
          #browser.find_element_by_id("batch_makeBill").click();
          #####browser.find_elements_by_class_name("btn-success")[0].click()
          check_one_s = browser.find_elements_by_class_name("checkbox_one");
          print len(check_one_s)
          for checkbox_one in check_one_s:
               checkbox_one.click();
               time.sleep(0.3);

          browser.find_element_by_id("batch_makeBill").click()              
          time.sleep(1)
          
          
     #提单制作页面 
     def makerprovide2(self,browser,num,url_base):
          check_inputs = browser.find_elements_by_class_name("check_input")
          for inp in check_inputs:
               inp.click()

          time.sleep(1)
          input_num_s = browser.find_elements_by_class_name("goods_input")

          #最多只有6条商品
          #for inu in input_num_s:
              # inu.clear()
               #inu.send_keys(num)
          x = 5
          if(len(input_num_s) < x):
                    x = len(input_num_s)
          print x
          for i in range(0,x):     
               input_num_s[i].clear()
               input_num_s[i].send_keys(num)

          #browser.find_element_by_id("create_many").click()
          browser.find_element_by_id("delivery_man_input").send_keys(u"sff")
          browser.find_element_by_id("phone_dv").send_keys("14725836998")
          browser.find_element_by_id("certificate_code").send_keys("330881199106229014")
          browser.find_element_by_id("vehicle_no_input").send_keys(u"苏d12345")
          #browser.find_element_by_name("str3").send_keys("yy888");
          #browser.find_element_by_name("str4").send_keys("14725836998");
          browser.find_element_by_id("tjButton").click()
          time.sleep(1)
          browser.find_element_by_css_selector("button[roles='btnDialog'][datas='ok']").click()
          time.sleep(1)

      # 打印对应身份证的第一个提单
     def printprovide(self,browser,url_base):
          browser.get(url_base+"/gzql/billladingprintmng/bladprtmngpage.shtml?menu_no=802102")
          time.sleep(1)
          browser.find_element_by_id("idcertificate").send_keys("330881199106229014")
          browser.find_element_by_css_selector(".y_search").click()
          time.sleep(1)
          browser.find_element_by_css_selector(".ck_print").click()
          time.sleep(1)
          browser.find_element_by_css_selector(".print_btn").click()






root=tk.Tk()  
root.title("友邻港自动测试")
app=Application(master=root)  
app.mainloop() 