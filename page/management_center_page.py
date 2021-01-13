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
        # 判断当前页面是否是管理中心页面
        cur_title = self.driver.title
        if cur_title == "统一管理平台":
            return cur_title
        # 2.切换到管理中心新窗口
        else:
            self.click_ele(page.mc_center)
            self.switch_window(1)


    # def click_menu001(self,menuName):
    #     # 1.点击左侧系统管理菜单
    #     time.sleep(5)
    #     # self.click_ele(page.sys_mc)
    #     # 2.点击进入对应的二级菜单
    #     ele = self.find_ele(([By.XPATH,".//*[contains(text(),'{}')]".format(menuName)]))
    #     self.Action.move_to_element(ele).click(ele).perform()

    def click_menu(self, chirld_menuName,first_menuName):
        # 1.点击左侧系统管理菜单
        time.sleep(5)
        # self.click_ele(page.sys_mc)
        # 2.点击进入对应的二级菜单
        if self.find_ele(([By.XPATH, ".//*[contains(text(),'{}')]".format(chirld_menuName)])):
            self.click_cover_ele(([By.XPATH, ".//*[contains(text(),'{}')]".format(chirld_menuName)]))
        else:
            #点击对应的一级菜单
            self.click_cover_ele(([By.XPATH, ".//*[contains(text(),'{}')]".format(first_menuName)]))
            #点击对应的二级菜单
            self.click_cover_ele(([By.XPATH, ".//*[contains(text(),'{}')]".format(chirld_menuName)]))


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
        #点击重置按钮
        self.click_cover_ele(page.reset_btn)
        time.sleep(1)
        self.find_ele(page.default_page)
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


    #以下是部门管理的页面公共方法
    #验证添加一级部门
    def add_first_department(self,department_name):
        #点击添加一级部门
        self.click_cover_ele(page.btn_add_first_department)
        self.find_ele(page.add_title)
        self.ele = self.find_elements(page.department_input,1)    #定位到输入部门的输入框
        self.ele.send_keys(department_name)   # 输入部门名称
        time.sleep(1)
        # 点击确定按钮
        self.click_cover_ele(page.confirm_btn)
        time.sleep(1)
        #验证添加成功弹窗
        self.find_ele(page.add_department_success)


    #验证不能添加重名部门
    def unable_add_same_first_department(self, same_department_name):
        # 点击添加一级部门
        self.click_cover_ele(page.btn_add_first_department)
        self.find_ele(page.add_title)
        self.ele = self.find_elements(page.department_input, 1)  # 定位到输入部门的输入框
        self.ele.send_keys(same_department_name)  # 输入部门名称
        time.sleep(1)
        # 点击确定按钮
        self.click_cover_ele(page.confirm_btn)
        time.sleep(1)
        # 显示部门名称不能重复的弹窗
        self.find_ele(page.add_same_department_msg)

    # 验证添加子部门
    def add_child_department(self,first_department_name,child_department_name):
        # 点击对应的一级部门
        self.click_cover_ele([By.XPATH,".//span[@title='{}']".format(first_department_name)])
        #点击添加子部门
        self.click_cover_ele(page.btn_add_child_department)
        #定位到新增子部门页面的上级部门
        self.find_ele([By.XPATH, ".//label[@title = '上级部门'] //../../ div //span[@title='{}']".format(first_department_name)])
        self.ele = self.find_elements(page.department_input, 1)  # 定位到输入部门的输入框
        self.ele.send_keys(child_department_name)  # 输入子部门名称
        time.sleep(1)
        # 点击确定按钮
        self.click_cover_ele(page.confirm_btn)
        time.sleep(1)
        # 添加成功的弹窗
        self.find_ele(page.add_department_success)


    # 验证不能添加重名子部门
    def unable_add_same_child_department(self,first_department_name,same_child_department_name):
        # 点击对应的一级部门
        self.click_cover_ele([By.XPATH, ".//span[@title='{}']".format(first_department_name)])
        # 点击添加子部门
        self.click_cover_ele(page.btn_add_child_department)
        # 定位到新增子部门页面的上级部门
        self.find_ele(
            [By.XPATH, ".//label[@title = '上级部门'] //../../ div //span[@title='{}']".format(first_department_name)])
        self.ele = self.find_elements(page.department_input, 1)  # 定位到输入部门的输入框
        self.ele.send_keys(same_child_department_name)  # 输入子部门名称
        time.sleep(1)
        # 点击确定按钮
        self.click_cover_ele(page.confirm_btn)
        time.sleep(1)
        # 显示部门名称不能重复的弹窗
        self.find_ele(page.add_same_department_msg)


    #查询部门
    def select_department(self,department_name):
        # 输入查询内容
        self.send_text(page.select_department_input,department_name)
        #点击查询按钮
        self.click_cover_ele(page.select_department_btn)
        time.sleep(1)
        #因查询的结果只是样式发生了变化,故无法通过自动化测试查询条件是否和查询结果相匹配


    #删除子部门
    def delete_child_department(self,first_department_name,child_department_name):
        self.refresh_page()
        # 点击对应的一级部门前面的缩略图标
        self.click_cover_ele([By.XPATH, ".//span[@title='{}']/../span/i".format(first_department_name)])
        #点击子部门前面的选择框
        self.click_cover_ele(
            [By.XPATH, ".//span[@title='{}']/../span[@class='ant-tree-checkbox']".format(child_department_name)])
        self.click_cover_ele(page.batch_delete)      #点击批量删除按钮
        self.find_ele(page.cofirm_del_tile)  # 定位到确认删除标题
        time.sleep(1)
        self.click_cover_ele(page.edit_role_confirm_btn)  # 确定
        time.sleep(1)
        self.find_ele(page.role_delete_success)  # 删除成功
        time.sleep(1)

    def delete_first_department(self,first_department_name):
        self.refresh_page()
        #点击一级部门前面的选择框
        self.click_cover_ele(
            [By.XPATH, ".//span[@title='{}']/../span[@class='ant-tree-checkbox']".format(first_department_name)])
        self.click_cover_ele(page.batch_delete)      #点击批量删除按钮
        self.find_ele(page.cofirm_del_tile)  # 定位到确认删除标题
        time.sleep(1)
        self.click_cover_ele(page.edit_role_confirm_btn)  # 确定
        time.sleep(1)
        self.find_ele(page.role_delete_success)  # 删除成功
        time.sleep(1)


    #项目管理
    def add_item(self,item_name,item_num):
        #点击新增
        self.click_cover_ele(page.add_btn)
        self.find_ele(page.add_title)
        item_name_ele = self.find_elements(page.item_name_input,1)
        item_name_ele.send_keys(item_name)   #输入项目名称
        item_num_ele = self.find_elements(page.item_num_input,1)
        item_num_ele.send_keys(item_num)    #输入项目编号
        time.sleep(1)
        # 点击确定按钮
        self.click_cover_ele(page.confirm_btn)
        time.sleep(1)
        #验证添加成功弹窗
        self.find_ele(page.add_department_success)




