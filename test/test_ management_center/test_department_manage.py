import pytest
from page.management_center_page import MCPage
from page.login_page import LoginPage
import time
from utils import DriverUtils
from base.read_json_data import read_json_data

import os, sys
sys.path.append(os.getcwd())


# 模拟新增部门的json数据
def get_add_first_department_data():
    data_list = []
    data = read_json_data("management_center","department_manage.json")
    test_add_first_department_list = data.get("test_add_first_department")
    for i in test_add_first_department_list:
        chirld_menuName = i.get("chirld_menuName")
        first_menuName = i.get("first_menuName")
        department_name = i.get("department_name")
        # same_department_name = data2.get("same_department_name")
        data_list.append((chirld_menuName,first_menuName,department_name))
    return data_list


# 模拟不能新增相同部门的json数据
def get_unable_add_same_first_department():
    data_list = []
    data = read_json_data("management_center","department_manage.json")
    test_unable_add_same_first_department_list = data.get("test_unable_add_same_first_department")
    for i in test_unable_add_same_first_department_list:
        chirld_menuName = i.get("chirld_menuName")
        first_menuName = i.get("first_menuName")
        # department_name = i.get("department_name")
        same_department_name = i.get("same_department_name")
        data_list.append((chirld_menuName,first_menuName,same_department_name))
    return data_list


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
    @pytest.mark.parametrize("chirld_menuName,first_menuName,department_name", get_add_first_department_data())
    def test_add_first_department(self,chirld_menuName,first_menuName,department_name):
        self.mcpage.click_MC()
        self.mcpage.click_menu(chirld_menuName,first_menuName)
        self.mcpage.add_first_department(department_name)


    #验证不能添加同名部门
    @pytest.mark.parametrize("chirld_menuName,first_menuName,same_department_name", get_unable_add_same_first_department())
    def test_unable_add_same_first_department(self,chirld_menuName,first_menuName,same_department_name):
        self.mcpage.click_MC()
        self.mcpage.click_menu(chirld_menuName,first_menuName)
        self.mcpage.unable_add_same_first_department(same_department_name)


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