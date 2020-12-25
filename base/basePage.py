from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from  utils.myDriver import Driver,taidiiPath
from selenium.webdriver.common.action_chains import ActionChains
import win32com.client
import time


class Basepage():
    """所有页面封装方法"""
    def __init__(self):
        self.driver = Driver.get_driver()
        self.url = taidiiPath

    def get_element(self,locator):
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_elements(self,locator):
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    # 元素输入内容
    def ele_input(self,locator,info):
        return self.get_element(locator).send_keys(info)

    # 元素点击
    def ele_click(self,locator):
        return self.get_element(locator).click()

    def move_to_ele(self,locator):
        return ActionChains(self.driver).move_to_element(self.get_element(locator)).perform()

    #js执行
    def js_execute(self,js):
        return self.driver.execute_script(js)

        # 上传文件操作

    def upload_text(self, locator, path):
        self.ele_click(locator)
        sh = win32com.client.Dispatch("WScript.shell")
        time.sleep(1)
        sh.sendkeys(path)



