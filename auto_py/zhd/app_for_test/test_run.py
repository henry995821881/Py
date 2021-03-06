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
        self.param7.set("")
        self.param8.set("")
        self.param9.set("")
        self.param10.set("")
        self.param11.set("")
        self.param12.set("")





    def get_all_text(self):
        b_dict ={}
        b_dict["url_base"]=self.e.get()
        b_dict["username"]=self.e1.get()
        b_dict["passwd"]=self.e2.get()
        b_dict["buy_num"]=self.e3.get()
        b_dict["make_num"]=self.e4.get()
        b_dict["order_id"]=self.e5.get()
        b_dict["cal_way"]=self.e6.get()
        b_dict["process"] =self.e7.get()
        b_dict["ck_username"] =self.e8.get()
        b_dict["ck_passwd"] =self.e9.get()
        b_dict["weight"] =self.e10.get()
        b_dict["vehicle_no"]=self.e11.get()
        b_dict["count"] =self.e12.get()
        print b_dict
        return b_dict




    def read_file_param(self):
        filename = "history.conf" 
        if not os.path.exists(filename):
            f = open("history.conf","w")
            f.close()


        a_dict = {}
        f = open("history.conf","r")
        str_line = f.readlines()
        for s in str_line:
            li = s.split("=")
            a_dict[li[0]]=''.join(li[1]).strip('\n')
        f.close()
        print a_dict
        self.a_dict =a_dict


    def write_new_param(self):
        os.remove("history.conf")
        f = open("history.conf","w")
        dict1 = self.get_all_text()
        li_for_write=[]
        for k,v in dict1.items():
            li_for_write.append(k+"="+v.encode("utf-8")+"\n")

        f.writelines(li_for_write)  
        f.close
        #执行浏览器
        self.run_chrome()



    def run_addcart(self,browser,username,orderid,num,cacul_way,url_base,test_case):

        test_case.addmycart(browser,orderid,num,cacul_way,url_base)



    def run_cart_submit(self,browser,username,orderid,num,cacul_way,url_base,test_case):
          test_case.addmycart(browser,orderid,num,cacul_way,url_base)
          test_case.mycart(browser,url_base)

    
    def run_pay_order(self,browser,username,orderid,num,cacul_way,passwd,url_base,test_case):
          test_case.addmycart(browser,orderid,num,cacul_way,url_base)
         #提交购物车中所有商品
          test_case.mycart(browser,url_base)
         #付定金批量支付
          test_case.payorder(browser,passwd,url_base)     



    def run_make_provide(self,browser,username,orderid,num,cacul_way,passwd,num2,vehicle_no,url_base,test_case):
      
          test_case.addmycart(browser,orderid,num,cacul_way,url_base)
         #提交购物车中所有商品
          test_case.mycart(browser,url_base)
         #付定金批量支付
          test_case.payorder(browser,passwd,url_base)
         #制作提单
          test_case.makerprovide(browser,url_base)
         
          test_case.makerprovide2(browser,num2,vehicle_no,url_base)





    def run_out_warehouse(self,browser,username,orderid,num,cacul_way,passwd,num2,vehicle_no,ck_username,ck_passwd,weight,url_base,test_case):

          test_case.addmycart(browser,orderid,num,cacul_way,url_base)
         #提交购物车中所有商品
          test_case.mycart(browser,url_base)
         # #付定金批量支付
          test_case.payorder(browser,passwd,url_base)
         # #制作提单
          test_case.makerprovide(browser,url_base)
         
          test_case.makerprovide2(browser,num2,vehicle_no,url_base)
         #  #logout
          test_case.logout(browser,url_base)
          #login
          test_case.login(browser,ck_username,ck_passwd,url_base)
          test_case.out_warehouse(browser,weight,url_base)

       


    def run_print_out_warehouse(self,browser,username,orderid,num,cacul_way,passwd,num2,vehicle_no,ck_username,ck_passwd,weight,url_base,test_case):
      
          test_case.addmycart(browser,orderid,num,cacul_way,url_base)
         #提交购物车中所有商品
          test_case.mycart(browser,url_base)
         # #付定金批量支付
          test_case.payorder(browser,passwd,url_base)
         # #制作提单
          test_case.makerprovide(browser,url_base)
         
          test_case.makerprovide2(browser,num2,vehicle_no,url_base)
         #  #logout
          test_case.logout(browser,url_base)
          #login 出库
          test_case.login(browser,ck_username,ck_passwd,url_base)
          test_case.out_warehouse(browser,weight,url_base)

          #合同批量支付
          test_case.logout(browser,url_base)
          test_case.login(browser,username,passwd,url_base)
          test_case.pay_contract(browser,passwd,url_base)


          #打印出门证
          test_case.logout(browser,url_base)
          test_case.login(browser,ck_username,ck_passwd,url_base)
          test_case.print_outwarehouse(browser,vehicle_no,url_base)


    def run_confrim_rec(self,browser,username,orderid,num,cacul_way,passwd,num2,vehicle_no,ck_username,ck_passwd,weight,url_base,test_case):
      
          test_case.addmycart(browser,orderid,num,cacul_way,url_base)
         #提交购物车中所有商品
          test_case.mycart(browser,url_base)
         # #付定金批量支付
          test_case.payorder(browser,passwd,url_base)
         # #制作提单
          test_case.makerprovide(browser,url_base)
         
          test_case.makerprovide2(browser,num2,vehicle_no,url_base)
         #  #logout
          test_case.logout(browser,url_base)
          #login 出库
          test_case.login(browser,ck_username,ck_passwd,url_base)
          test_case.out_warehouse(browser,weight,url_base)

          #合同批量支付
          test_case.logout(browser,url_base)
          test_case.login(browser,username,passwd,url_base)
          test_case.pay_contract(browser,passwd,url_base)


          #打印出门证
          test_case.logout(browser,url_base)
          test_case.login(browser,ck_username,ck_passwd,url_base)
          test_case.print_outwarehouse(browser,vehicle_no,url_base)


          #提单确认收货
          test_case.logout(browser,url_base)
          test_case.login(browser,username,passwd,url_base)
          test_case.confirm_rec(browser,url_base)



    def run_busyness(self,url_base,username,passwd,num,num2,orderid,cacul_way,process,ck_username,ck_passwd,weight,vehicle_no,count,test_case,browser):



         for x in xrange(0,count):
            
         
           if process == 1:
             #login
            test_case.login(browser,username,passwd,url_base)
            self.run_addcart(browser,username,orderid,num,cacul_way,url_base,test_case)
            test_case.logout(browser,url_base)
           elif process == 2:
            #login
            test_case.login(browser,username,passwd,url_base)
            self.run_cart_submit(browser,username,orderid,num,cacul_way,url_base,test_case)
            test_case.logout(browser,url_base)
           
           elif process == 3:
            #login
            test_case.login(browser,username,passwd,url_base)
            self.run_pay_order(browser,username,orderid,num,cacul_way,passwd,url_base,test_case)
            test_case.logout(browser,url_base)
            
           elif process == 4:
            #login
            test_case.login(browser,username,passwd,url_base)
            self.run_make_provide(browser,username,orderid,num,cacul_way,passwd,num2,vehicle_no,url_base,test_case)
            test_case.logout(browser,url_base)

           elif process == 5:
            #login
            test_case.login(browser,username,passwd,url_base)
            self.run_out_warehouse(browser,username,orderid,num,cacul_way,passwd,num2,vehicle_no,ck_username,ck_passwd,weight,url_base,test_case)
            test_case.logout(browser,url_base)

           elif process == 6:
            #login
            test_case.login(browser,username,passwd,url_base)
            self.run_print_out_warehouse(browser,username,orderid,num,cacul_way,passwd,num2,vehicle_no,ck_username,ck_passwd,weight,url_base,test_case)
            test_case.logout(browser,url_base)

            #代码测试
           elif process ==10:
            test_case.logout(browser,url_base)
            #login
            test_case.login(browser,ck_username,ck_passwd,url_base)
            test_case.print_outwarehouse(browser,vehicle_no,url_base)
            test_case.logout(browser,url_base)

           elif process == 7:
            #login
            test_case.login(browser,username,passwd,url_base)
            self.run_confrim_rec(browser,username,orderid,num,cacul_way,passwd,num2,vehicle_no,ck_username,ck_passwd,weight,url_base,test_case)
            test_case.logout(browser,url_base)











    def run_chrome(self):
        #url_base = "http://192.168.80.249:8080"
         url_base=self.e.get()
         username = self.e1.get()
         passwd = self.e2.get()
         #商品购买数量
         num = self.e3.get()
         #商品制作数量
         num2=self.e4.get()
         # 可以多次调用加入购物车商品，前提是注意要相同卖家的。否则后面付款走不过去
         #4931的商品加入购物车 数量为3，
         orderid = self.e5.get()
         cacul_way = int(self.e6.get())# 理计购买2  磅计购买1
         process = int(self.e7.get()) # 步骤到哪一步
         ck_username =self.e8.get()
         ck_passwd = self.e9.get()
         weight = self.e10.get()
         vehicle_no = self.e11.get()
         count = int(self.e12.get())
         
         browser = webdriver.Chrome()
         browser.implicitly_wait(10)
         test_case = test_chrome()

         
         
         self.run_busyness(url_base,username,passwd,num,num2,orderid,cacul_way,process,ck_username,ck_passwd,weight,vehicle_no,count,test_case,browser)

         
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
        tk.Label(self,text=u"用户名:").grid(row=1)
        self.e1 = tk.Entry(self,textvariable=self.param1)
        self.e1.grid(row=1,column=1)
        self.param1.set(self.get_param("username"))

        self.param2= tk.StringVar()
        tk.Label(self,text=u"密码:").grid(row=2)
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


        self.param7=tk.StringVar()
        tk.Label(self,text=u"1到购物车",fg="red").grid(row=7,column=0)
        tk.Label(self,text=u"2提交订单",fg="red").grid(row=8,column=0)
        tk.Label(self,text=u"3付款订单",fg="red").grid(row=9,column=0)
        tk.Label(self,text=u"4制作提单",fg="red").grid(row=10,column=0)
        tk.Label(self,text=u"5仓库出库",fg="red").grid(row=11,column=0)

        tk.Label(self,text=u"6合同付款出门打印",fg="red").grid(row=7,column=1)
        tk.Label(self,text=u"7提单确认收货",fg="red").grid(row=8,column=1)
        tk.Label(self,text=u"8备用",fg="red").grid(row=9,column=1)
        tk.Label(self,text=u"9备用",fg="red").grid(row=10,column=1)
        tk.Label(self,text=u"10测试代码",fg="red").grid(row=11,column=1)
        tk.Label(self,text=u"步骤到哪:",fg="blue").grid(row=12)
        self.e7 = tk.Entry(self,textvariable=self.param7)
        self.e7.grid(row=12,column=1)
        self.param7.set(self.get_param("process"))



        self.param8 = tk.StringVar()
        tk.Label(self,text=u"仓库用户名:").grid(row=13)
        self.e8 = tk.Entry(self,textvariable=self.param8)
        self.e8.grid(row=13,column=1)
        self.param8.set(self.get_param("ck_username"))

        self.param9= tk.StringVar()
        tk.Label(self,text=u"仓库密码:").grid(row=14)
        self.e9 = tk.Entry(self,textvariable=self.param9)
        self.e9.grid(row=14,column=1)
        self.param9.set(self.get_param("ck_passwd"))

        self.param10= tk.StringVar()
        tk.Label(self,text=u"出库吨数:").grid(row=15)
        self.e10 = tk.Entry(self,textvariable=self.param10)
        self.e10.grid(row=15,column=1)
        self.param10.set(self.get_param("weight"))

        self.param11= tk.StringVar()
        tk.Label(self,text=u"车牌号码:").grid(row=16)
        self.e11 = tk.Entry(self,textvariable=self.param11)
        self.e11.grid(row=16,column=1)
        self.param11.set(self.get_param("vehicle_no"))


        self.param12= tk.StringVar()
        tk.Label(self,text=u"循环次数:").grid(row=17)
        self.e12 = tk.Entry(self,textvariable=self.param12)
        self.e12.grid(row=17,column=1)
        self.param12.set(self.get_param("count"))



        self.clear_btn =tk.Button(self,text="重置参数",command=self.clear_text)
        self.clear_btn.grid(row=18)


        self.submit_btn=tk.Button(self,text="执行浏览器",command=self.write_new_param)
        self.submit_btn.grid(row=18,column=1)
                    
  

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
          time.sleep(2)
          
          radios = browser.find_elements_by_class_name("price_type_class")
          if (len(radios) > 1 and way == 1):
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
          time.sleep(1)
          browser.find_element_by_id("submitAll").click()
          browser.find_elements_by_class_name("btn-primary")[0].click()
          time.sleep(2)
          browser.find_elements_by_class_name("jx_btn")[1].click()
          time.sleep(1)

      #定金付款 付款所有定金订单
     def payorder(self,browser,passwd_,url_base):
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
          browser.find_element_by_id("password_3").send_keys(passwd_)
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
     def makerprovide2(self,browser,num,vehicle_no,url_base):
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
          browser.find_element_by_id("vehicle_no_input").send_keys(vehicle_no)
          #browser.find_element_by_name("str3").send_keys("yy888");
          #browser.find_element_by_name("str4").send_keys("14725836998");
          browser.find_element_by_id("tjButton").click()
          time.sleep(1)
          browser.find_element_by_css_selector("button[roles='btnDialog'][datas='ok']").click()
          time.sleep(6)
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


          #出库第一个提单
     def out_warehouse(self,browser,weight,url_base):
          browser.get(url_base+"/gzql/ladingBillManage/ladingBillManage_warehouse.shtml?menu_no=971101")
          time.sleep(1)
          browser.find_elements_by_class_name("operat")[0].click()
          time.sleep(1)
          input_all = browser.find_elements_by_class_name("weightBlur")
          for inn in input_all:
            if not inn.get_attribute("readonly"):
                inn.clear()
                inn.send_keys(weight)
                time.sleep(0.3)

          browser.find_element_by_id("OutWhBtn").click()
          time.sleep(6)
          browser.find_element_by_css_selector("button[roles='btnDialog'][datas='ok']").click()
          time.sleep(1)



     def logout(self,browser,url_base):
          browser.find_elements_by_class_name("s_reg")[0].click()
          time.sleep(1)


     def pay_contract(self,browser,passwd_,url_base):
          browser.get(url_base+"/gzql/contract/contract_show_buy.shtml?menu_no=801103&is_confirm=6")
          time.sleep(2)
          check_one_s = browser.find_elements_by_class_name("choose_check")
          if len(check_one_s) < 1:
            return
          browser.find_element_by_id("choose_check_all").click()
          time.sleep(0.5)
          browser.find_element_by_id("batch_pay").click()
          time.sleep(2)
          browser.find_element_by_id("password_3").send_keys(passwd_)
          browser.find_element_by_id("vcode_3").send_keys("wqer")
          browser.find_element_by_id("payButton").click()
          time.sleep(1)


          #打印出门证自提的
     def print_outwarehouse(self,browser,vehicle_no,url_base):
          browser.get(url_base+"/gzql/certfpntmng/certfpntmngckpage.shtml?menu_no=972101")
          time.sleep(1)
          browser.find_element_by_id("vehicle_no").send_keys(vehicle_no)
          browser.find_elements_by_class_name("y_search")[0].click()
          time.sleep(1)
          ck = browser.find_elements_by_class_name("ck_print")
          if len(ck) < 1:
            return
          ck[0].click()
          time.sleep(1)
          browser.find_element_by_id("prn_btn").click()
          time.sleep(1)


      #第一个确认收货
     def confirm_rec(self,browser,url_base):
          browser.get(url_base+"/gzql/billmgr/bill_mgr_buy.shtml?menu_no=802101")
          time.sleep(2)
          browser.find_elements_by_class_name("receiptBtn")[0].click()
          time.sleep(1)
          browser.find_element_by_id("receiptBtn").click()
          time.sleep(1)
          browser.find_element_by_css_selector("button[roles='btnDialog'][datas='ok']").click()
          time.sleep(1)




       




if __name__ =="__main__":
  root=tk.Tk()  
  root.title("友邻港自动测试")
  app=Application(master=root)  
  app.mainloop() 
