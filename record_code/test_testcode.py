# Generated by Selenium IDE
#import unittest
# import pytest
# import time
# import json
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# class TestTestcode(unittest.TestCase):
#   def setUp(self):
#     self.driver = webdriver.Firefox()
#     self.vars = {}
#
#   def tearDown(self):
#     self.driver.quit()
#
#   def test_testcode(self):
#     self.driver.get("https://www.baidu.com/")
#     self.driver.set_window_size(1550, 838)
#     self.driver.find_element(By.ID, "kw").click()
#     self.driver.find_element(By.ID, "kw").send_keys("定军山")
#     self.driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
#     element = self.driver.find_element(By.CSS_SELECTOR, ".opr-recommends-merge-panel:nth-child(2) .c-span4:nth-child(2) .opr-recommends-merge-mask")
#     actions = ActionChains(self.driver)
#     actions.move_to_element(element).perform()
#     element = self.driver.find_element(By.CSS_SELECTOR, "body")
#     actions = ActionChains(self.driver)
#     actions.move_to_element(element, 0, 0).perform()
#
#
# if __name__=="__main__":
#     unittest.main()
#
#
# from selenium import webdriver
# import time
# browser=webdriver.Firefox()
# time.sleep(3)
# browser.get("https://www.baidu.com/")
# time.sleep(2)
# browser.maximize_window()
# # browser.find_element_by_id("kw").send_keys("selenium")
# # time.sleep(3)
# # browser.find_element_by_id("su").click()
# browser.find_element_by_link_text("高考加油").click()
# time.sleep(5)
# browser.quit()
#
# if __name__=="__main__":
#     unittest.main()

from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://localhost:8080/sds/public/index.html")
time.sleep(2)
driver.find_element_by_name("username").send_keys("abc")
time.sleep(1)
driver.find_element_by_name("password").send_keys("123")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='login_form']/div[6]/input[2]").click()
time.sleep(5)
driver.quit()