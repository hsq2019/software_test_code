import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class baidu1(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")
        self.verificationErrors = []
        self.accept_next_alert = True
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
    def test_baidu(self):

        self.driver.find_element_by_id("kw").send_keys(u"阴阳师")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        self.assertEqual("阴阳师_百度搜",self.driver.title,msg="不一样!!!")
        time.sleep(3)

    if __name__=="__main__":
        unittest.main(verbosity=2)