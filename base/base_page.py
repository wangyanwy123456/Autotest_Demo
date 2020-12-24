from utils import DriverUtils
import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



#对象基类
class Base():


    # 当类初始化的时候这个方法就执行
    def __init__(self,driver):
        self.driver = driver
        self.Action = ActionChains(self.driver)

    #定位元素
    def find_ele(self,loc):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(loc[0], loc[1])


    #点击元素
    def click_ele(self, loc):
        self.find_ele(loc).click()
        time.sleep(1)


    #输入文本
    def send_text(self,loc,text):
        self.find_ele(loc).clear()
        self.find_ele(loc).send_keys(text)
        time.sleep(1)

    #切换窗口
    def switch_window(self,index):
        new_window = self.driver.window_handles[index]
        self.driver.switch_to.window(new_window)






# if __name__ == "__main__":
#     base = Base('http://10.194.188.76/homePage')
#     base.send_text([By.XPATH,".//input[@id='username']"],'admin')
#     base.send_text([By.XPATH,".//input[@id='password']"],'20202020')
#     base.send_text([By.XPATH,".//input[@id='code']"],'')
#     time.sleep(10)
#     base.click_ele([By.XPATH,".//input[@name='submit']"],)








