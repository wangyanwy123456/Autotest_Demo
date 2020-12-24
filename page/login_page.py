from base.base_page import Base
import page
from selenium.webdriver.common.by import By
import time

"""
负责登录页面的逻辑
"""

class LoginPage(Base):
    # 初始化函数  动态把driver传入
    def __init__(self,driver):
        Base.__init__(self,driver)


    #点击登录逻辑
    def login_in(self,userName,pwd,code,accoutName):
        #1.输入账号
        self.send_text(page.login_username,userName)
        # 2.输入密码
        self.send_text(page.login_pwd,pwd)
        # 3.输入验证码,需要开发协助提供下万能验证码
        time.sleep(10)
        self.send_text(page.login_pwd, pwd)
        #4.点击登录按钮
        self.click_ele(page.login_in_btn)
        # 5.定位到登录的账号
        self.find_ele([By.XPATH,".//*[contains(text(),'{}')]".format(accoutName)])


    #关闭登录页面
    def close_login_page(self):
        self.click_ele(page.accout_fig)
        self.click_ele(page.login_out_btn)

# if __name__ == "__main__":
#     loginpage = LoginPage("http://10.194.188.76/homePage")
#     loginpage.login_in('admin', '20202020', '', '管理员1')
#     loginpage.close_login_page()
