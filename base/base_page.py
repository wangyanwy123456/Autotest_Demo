from utils import DriverUtils
import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import yaml, os



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



    # 找到一组元素对象并返回其中一个
    def find_elements(self, loc,num):
        time.sleep(1)
        ele = self.driver.find_elements(loc[0], loc[1])
        return ele[num]


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


    #对被覆盖的元素执行点击操作
    def click_cover_ele(self,loc):
        ele = self.find_ele(loc)
        self.driver.execute_script("arguments[0].click();",ele)


    #判断当前页面是否是预期页面
    def get_page_title(self,cur_title,loc):
        title = self.driver.title
        if cur_title == title:
            return cur_title
        else:
            self.click_ele(loc)

    #刷新页面并增加等待时间
    def refresh_page(self):
        self.driver.refresh()
        time.sleep(3)


# if __name__ == "__main__":
#     base = Base('http://10.194.188.76/homePage')
#     base.send_text([By.XPATH,".//input[@id='username']"],'admin')
#     base.send_text([By.XPATH,".//input[@id='password']"],'20202020')
#     base.send_text([By.XPATH,".//input[@id='code']"],'')
#     time.sleep(10)
#     base.click_ele([By.XPATH,".//input[@name='submit']"],)








