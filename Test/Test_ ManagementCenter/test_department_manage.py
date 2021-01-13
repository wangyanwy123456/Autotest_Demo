import pytest
from page.management_center_page import MCPage
from page.login_page import LoginPage
import time
from utils import DriverUtils

import os, sys
sys.path.append(os.getcwd())


class TestDepartmentManage:

    # 登陆数据中台平台
    def setup_class(self):
        self.url = "http://10.194.188.76/homePage"
        self.driver = DriverUtils.get_driver(self.url)
        self.mcpage = MCPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login_in('admin', '20202020', '', '管理员1')

    #退出数据中台平台
    def teardown_class(self):
        time.sleep(5)
        DriverUtils.quit_driver()

    # 新增部门
    def test_add_first_department(self):
        self.mcpage.click_MC()
        self.mcpage.click_menu("部门管理","系统管理")
        self.mcpage.add_first_department("添加一级部门测试001")


    #验证不能添加同名部门
    def test_unable_add_same_first_department(self):
        self.mcpage.click_MC()
        self.mcpage.click_menu("部门管理","系统管理")
        self.mcpage.unable_add_same_first_department("添加一级部门测试001")


    #验证添加子部门
    def test_add_child_department(self):
        self.mcpage.click_MC()
        self.mcpage.click_menu("部门管理","系统管理")
        self.mcpage.add_child_department("添加一级部门测试001","添加一级的子部门测试")


    #验证不能添加重名子部门
    def test_unable_add_same_child_department(self):
        self.mcpage.click_MC()
        self.mcpage.click_menu("部门管理","系统管理")
        self.mcpage.unable_add_same_child_department("添加一级部门测试001","添加一级的子部门测试")


    #查询部门
    def test_select_department(self):
        self.mcpage.click_MC()
        self.mcpage.click_menu("部门管理", "系统管理")
        self.mcpage.select_department("添加一级")


    #删除子部门的数据
    # def test_delete_child_department(self):
    #     self.mcpage.delete_child_department("添加一级部门测试001","添加一级的子部门测试")


    #删除一级部门
    def test_delete_first_department(self):
        self.mcpage.delete_first_department("添加一级部门测试001")