from selenium import webdriver
import time
import unittest
from ddt import ddt,data,unpack,file_data
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
@ddt
class Sign_in(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://localhost:8080/sds/public/index.html")
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(2)
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    @data(("abc","123"),("abc","1234"),("666","123"),("abc1","123"))
    @unpack
    def test_signIn(self,value1,value2):
        driver=self.driver
        driver.find_element_by_name("username").send_keys(value1)
        time.sleep(1)
        driver.find_element_by_name("password").send_keys(value2)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='login_form']/div[6]/input[2]").click()
        time.sleep(5)

if __name__=="__main__":
    unittest.main()

