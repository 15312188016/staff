from base.basePage import Basepage
from selenium.webdriver.common.by import By

class Login(Basepage):
    def __init__(self):
        super().__init__()
        self.login_name = (By.ID,"id_username")
        self.login_password = (By.ID,"id_password")
        self.login_button = (By.ID,"submit")

    def login_sys(self,username = "demochina_cn",password = "123456"):
        self.ele_input(self.login_name,username)
        self.ele_input(self.login_password,password)
        self.ele_click(self.login_button)

# login_sys = Login()

if __name__ =="__main__":
    # login = Login()
    # login_sys.login()
    # login_sys.action_chains()




    pass
