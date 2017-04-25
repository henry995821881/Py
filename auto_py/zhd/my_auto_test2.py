# coding = utf-8 
from selenium import webdriver
import time


class test_chrome:

     
     def login(self,browser,name,pwd):
     	browser.get("http://localhost/trade/login.shtml?ref_url=/etrade/ucenter.shtml")
     	browser.find_element_by_name("username").send_keys(name)
        browser.find_element_by_name("password").send_keys(pwd)
        browser.find_element_by_id("login_bt").click()


    
	 def addmycart(self,browser,orderid,num):
	    browser.get("http://localhost/etrade/mall/mallDetail.shtml?order_id="+orderid)
	    browser.find_element_by_id("count_number").clear()
        browser.find_element_by_id("count_number").send_keys(num)
        browser.find_element_by_id("buy").click()

		
       
     def mycart(self,browser):
    	browser.find_element_by_id("cx1").click()
        browser.find_element_by_id("submitAll").click()
        browser.find_elements_by_class_name("btn-primary")[0].click()


     def payorder(self,browser):
     	browser.get("http://localhost/gzql/contract/contract_mgr_buy.shtml?menu_no=801102")
        browser.find_elements_by_class_name("pay_order")[0].click()
        browser.find_element_by_id("password_3").send_keys("888888")
        browser.find_element_by_id("vcode_3").send_keys("jlkf")
        browser.find_element_by_id("payButton").click()


      def makerprovide(self,browser):
      	browser.get("http://localhost/gzql/contract/td_make.shtml?menu_no=802103")
      	browser.find_elements_by_class_name("btn-success")[0].click()





if __name__ == "__main__"
	
	browser = webdriver.Chrome()
	browser.implicitlyWait(10)
	browser.pageLoadTimeout(10)
    test_case = test_chrome()

    test_case.login(browser,"yy888888","88888")

    test_case.addmycart(browser,"4931","2")

    test_case.mycart(browser)

    test_case.payorder(browser)

    test_case.makerprovide(browser)
    time.sleep(10)
    browser.quit()
