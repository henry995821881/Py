# coding = utf-8 
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://192.168.80.249:8080/etrade/login.shtml?ref_url=/etrade/ucenter.shtml")
time.sleep(0.3)
browser.find_element_by_name("username").send_keys("yy888888")
browser.find_element_by_name("password").send_keys("888888")
browser.find_element_by_id("login_bt").click()
time.sleep(2)
#browser.find_elements_by_class_name("nav_icon1").click()
browser.get("http://192.168.80.249:8080/etrade/mall/mallDetail.shtml?order_id=4931")
time.sleep(2)
browser.find_element_by_id("count_number").clear();
browser.find_element_by_id("count_number").send_keys("2");
browser.find_element_by_id("buy").click()
time.sleep(2)
#browser.find_elements_by_class_name("k").submit()
browser.find_element_by_id("cx1").click()
browser.find_element_by_id("submitAll").click()
browser.find_elements_by_class_name("btn-primary")[0].click()
time.sleep(1)
browser.get("http://192.168.80.249:8080/gzql/contract/contract_mgr_buy.shtml?menu_no=801102")
time.sleep(1)
browser.find_elements_by_class_name("pay_order")[0].click()
time.sleep(1)
browser.find_element_by_id("password_3").send_keys("888888")
browser.find_element_by_id("vcode_3").send_keys("jlkf");
browser.find_element_by_id("payButton").click()
time.sleep(1)
browser.get("http://192.168.80.249:8080/gzql/contract/td_make.shtml?menu_no=802103")
time.sleep(1)
browser.find_elements_by_class_name("btn-success")[0].click()
time.sleep(10)
browser.quit()
