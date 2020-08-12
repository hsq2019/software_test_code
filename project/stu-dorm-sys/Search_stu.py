from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
import sys, csv


def getCsv(file_name):
    rows=[]
    path=sys.path[0]

    with open(path+'/data/'+file_name, 'rt') as f:
        readers = csv.reader(f, delimiter=',', quotechar='|')
        next(readers, None)
        for row in readers:
            temprows=[]
            for i in row:
                temprows.append(i)
            rows.append(temprows)
        return rows

class Search_stu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://localhost:8080/sds/public/index.html")
        self.driver.maximize_window()
        time.sleep(3)
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

    def test_search_stu(self):
        driver=self.driver
        driver.find_element_by_name("username").send_keys("abc")
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("123")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='login_form']/div[6]/input[2]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='main_fail_modal_dialog']/div/div[3]/button").click()
        time.sleep(1)
        driver.find_element_by_link_text("学生管理").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='stu_panel']/div[1]/div[1]/div[3]/input").send_keys("黄庆庆")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='stu_panel']/div[1]/div[1]/div[3]/input").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='stu_panel']/div[1]/div[1]/div[3]/input").clear()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='stu_panel']/div[1]/div[1]/div[3]/input").send_keys("罗")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='stu_panel']/div[1]/div[1]/div[3]/input").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='stu_panel']/div[1]/div[1]/div[3]/input").clear()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='stu_panel']/div[1]/div[1]/div[3]/input").send_keys("luo")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='stu_panel']/div[1]/div[1]/div[3]/input").send_keys(Keys.ENTER)
        time.sleep(5)


if __name__=="__main__":
    unittest.main()
