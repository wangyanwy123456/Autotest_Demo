from base.base_page import Base
import page
from selenium.webdriver.common.by import By
import time


"""
负责管理中心模块的逻辑
"""

class MCPage(Base):
    # 初始化函数  动态把driver传入
    def __init__(self, driver):
        Base.__init__(self, driver)

    # 点击进入管理中心模块
    def click_MC(self):
        # 1.点击管理中心菜单
        self.click_ele(page.mc_center)
        # 2.切换到管理中心新窗口
        self.switch_window(1)


    def click_menu(self,menuName):
        # 1.点击左侧系统管理菜单
        time.sleep(5)
        # self.click_ele(page.sys_mc)
        # 2.点击进入对应的二级菜单
        ele = self.find_ele(([By.XPATH,".//*[contains(text(),'{}')]".format(menuName)]))
        self.Action.move_to_element(ele).click(ele).perform()


   #新增角色
    def add_role(self,role_name,role_code,description):
        # 1.点击角色维护
        # self.click_menu(page.role_preserve)
        # 2.点击角色录入
        ele = self.find_ele(page.add_role_btn)
        self.Action.move_to_element(ele).click(ele).perform()
        # self.click_ele(page.add_role_btn)
        # # 3.新增角色
        self.find_ele(page.add_title)
        self.send_text(page.role_name_input,role_name)        #输入角色名称
        self.send_text(page.role_code_input,role_code)        #输入角色编码
        self.send_text(page.description_input,description)        #输入角色描述
        # 点击确定按钮
        self.click_cover_ele(page.confirm_btn)
        time.sleep(1)


    #查询角色
    def select_role(self,role_name):
        # 输入查询内容
        self.send_text(page.select_role_input,role_name)
        #点击查询按钮
        self.click_cover_ele(page.select_btn)
        time.sleep(1)
        self.click_cover_ele(page.reset_btn)
        time.sleep(1)


    #编辑角色
    def edit_role(self,roleName,newRoleName,newRoleDescrip):
        #选择某一角色
        self.click_ele([By.XPATH,".//td[contains(text(),'{}')]//..//input[@ type = 'radio']".format(roleName)])
        # 点击"角色编辑"
        self.click_cover_ele(page.edit_role)
        #编辑角色名称
        self.send_text(page.edit_role_name_input,newRoleName)
        #编辑角色描述
        self.send_text(page.edit_role_descrip_input, newRoleDescrip)
        #点击确定
        self.click_cover_ele(page.edit_role_confirm_btn)
        self.find_ele(page.edit_role_success)
        time.sleep(5)


    #删除角色
    def delete_role(self,role_name):
        self.driver.refresh()
        self.click_cover_ele([By.XPATH,".//td[contains(text(),name)]/../td//a[contains(text(),'删除')]" .format(role_name)])  #删除
        self.find_ele(page.cofirm_del_tile)    #定位到确认删除标题
        time.sleep(1)
        self.click_cover_ele(page.edit_role_confirm_btn)  #确定
        time.sleep(1)
        self.find_ele(page.role_delete_success)    #删除成功
        time.sleep(1)
