from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
# driver.get("https://zhidao.baidu.com/question/1992997995037483147.html")
# driver.maximize_window()
# url=driver.current_url
# print(url)
# driver.quit()

#打印内容
text=driver.find_element_by_id("s-bottom-layer-right").text
print(text)

driver.find_element_by_id("kw").send_keys("火锅百度百科")
driver.find_element_by_id("su").click()
driver.implicitly_wait(2)
driver.find_element_by_link_text("火锅(中国美食)_百度百科").click()
#打印标题
title=driver.title
print("title="+title)
#打印url
url=driver.current_url
print("url="+url)
time.sleep(5)
driver.quit()