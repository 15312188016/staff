from utils.mySetting import chromeDriver,taidiiPath
from selenium import webdriver

class Driver:
    # driver初始化为None
    _driver = None

    @classmethod
    def get_driver(cls,browserName = "Chrome"):
        """
        如果浏览器驱动不存在，则创建浏览器驱动对象，并将其作为值返回
        如果，浏览器驱动对象存在，直接返回
        :param browserName: 默认Chrome为默认浏览器
        :return:
        """
        if cls._driver is None:
            if browserName == "Chrome":
                cls._driver = webdriver.Chrome(chromeDriver)
            elif browserName == "Firox":
                cls._driver = webdriver.Firefox()

            #访问默认网址
            cls._driver.get(taidiiPath)
            cls._driver.maximize_window()
            # 执行登录
            # cls.__login()

        return cls._driver

    # @classmethod
    # def __login(cls):
    #     """
    #     私有方法，只能在类内部使用
    #     绕过登录
    #     :return:
    #     """
    #     pass

if __name__ == "__main__":
    Driver.get_driver()