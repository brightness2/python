# 测试功能
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class Test:
    def __init__(self,driver) -> None:
        self.driver = driver
        pass
    # 不可见方法
    def __search(self,keyword):
        self.driver.find_element(By.ID,'kw').send_keys("selenium" + Keys.ENTER)
        
    
    def doAction(self):
        self.__search('selenium')