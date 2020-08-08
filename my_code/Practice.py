from selenium import webdriver
import time
driver=webdriver.Chrome()
#输入网址
driver.get("https://www.baidu.com")
#最大化浏览器
driver.maximize_window()
#send_keys()输入啥
driver.find_element_by_id("kw").send_keys("第一")
time.sleep(2)
#click点击啥
driver.find_element_by_id("su").click()
time.sleep(2)
#清除
driver.find_element_by_id("kw").clear()
time.sleep(1)
driver.find_element_by_id("kw").send_keys("饿死了")
time.sleep(1)
#submit代替click，提交
driver.find_element_by_id("su").submit()
time.sleep(5)
driver.quit()

