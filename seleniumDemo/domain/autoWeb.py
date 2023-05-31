from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager
################################
import module.test

class AutoWeb:
    chromedriver_version = ''
    driver = None
    chrome_option = webdriver.ChromeOptions()

    def __init__(self,chrome_location,data_dir) -> None:
        self.chrome_location = chrome_location
        self.data_dir = data_dir

    def init_driver(self):

        # 浏览器位置
        self.chrome_option.binary_location = self.chrome_location
        #设置浏览器数据保存位置
        self.chrome_option.add_argument(r"user-data-dir=" + self.data_dir)
        self._createDriver()

    def set_chromedriver_version(self,version):
        self.chromedriver_version = version
    
    def _createDriver(self):
        if(self.chromedriver_version):
            service = ChromeService(executable_path=ChromeDriverManager(version=self.chromedriver_version).install())
        else:
            service = ChromeService(executable_path=ChromeDriverManager().install())
        
        driver = webdriver.Chrome(service=service,chrome_options=self.chrome_option)
        self.driver = driver
        return self.driver

    def openUrl(self,url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()




# option = webdriver.ChromeOptions()
# # 浏览器位置
# chrome_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# option.binary_location = chrome_location

# # 设置浏览器数据保存位置
# data_dir = r'C:\Users\Public\Chrome\UserData'
# option.add_argument(r"user-data-dir=" + data_dir)

# # 加载chromedriver.exe,版本需要与浏览器版本相近的
# chromedriver_version = "113.0.5672.63"
# service = ChromeService(executable_path=ChromeDriverManager(version=chromedriver_version).install())

# # 实例化 driver
# driver = webdriver.Chrome(service=service,chrome_options=option)

# driver.implicitly_wait(10)

# # 打开页面，注意链接要完整
# driver.get('https://www.baidu.com')

# testObj = module.test.Test(driver)

# testObj.doAction()

# # 保持浏览器不退出
# input("selenium running...")