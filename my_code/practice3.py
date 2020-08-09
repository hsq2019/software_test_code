from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import io
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("https://passport.bilibili.com/login")
driver.find_element_by_id("login-username").send_keys("666")
#使用tab键定位到密码格子，但是没有相应函数，所以输入密码还是得自己再用属性定位
driver.find_element_by_id("login-username").send_keys(Keys.TAB)
driver.find_element_by_id("login-passwd").send_keys("666")
time.sleep(2)
#使用enter键去登录
# driver.find_element_by_id("login-passwd").send_keys(Keys.ENTER)

#右击登录
su=driver.find_element_by_xpath("//*[@id='geetest-wrap']/div/div[5]/a[1]")
ActionChains(driver).context_click(su).perform()
time.sleep(5)
driver.quit()

