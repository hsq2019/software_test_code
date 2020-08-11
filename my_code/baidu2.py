from selenium import webdriver
import unittest
import time
from ddt import ddt, unpack, data, file_data
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
class baidu2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.verificationErrors=[]
        self.accept_next_alert = True
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

    #@file_data('test_baidu_data.json')
    #@data(*getCsv('test_baidu_data.txt'))
    #([周迅,周迅_百度搜索],[张国荣,张国荣_百度搜索])
    #@unpack
    @data("王凯", "Lisa", "特朗普", "蒋欣")
    def test_baidu(self, value):
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        driver = self.driver
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(6)


if __name__ == "__main__":
    unittest.main()