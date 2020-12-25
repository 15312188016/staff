from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(r"D:\chromeDriver\chromedriver.exe")
driver.get("https://dev.taidii.cn/")
driver.maximize_window()
driver.find_element_by_id("id_username").send_keys("demochina_cn")
driver.find_element_by_id("id_password").send_keys("123456")
driver.find_element_by_id("submit").click()

ele = driver.find_element_by_css_selector(".td-sidebar ul>li:nth-of-type(3)")
ActionChains(driver).move_to_element(ele).perform()
driver.find_element_by_css_selector(".td-sidebar ul>div:nth-of-type(3) li:nth-child(4)").click()