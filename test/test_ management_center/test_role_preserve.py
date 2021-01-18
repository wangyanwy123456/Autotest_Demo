import pytest
from page.management_center_page import MCPage
from page.login_page import LoginPage
import time
from utils import DriverUtils

import os, sys
sys.path.append(os.getcwd())


class TestRoleProserve:

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

    # 新增角色
    def test_add_role(self):
        self.mcpage.click_MC()
        self.mcpage.click_menu("角色维护","系统管理")
        self.mcpage.add_role("角色名称001", "code001", "1234角色描述角色描述角色描述角色描述角色描述1234")

    #查询角色
    def test_select_role(self):
         self.mcpage.click_MC()
         # self.mcpage.click_menu("角色维护")
         self.mcpage.select_role("角色名称001")

    def test_edit_role(self):
        self.mcpage.click_MC()
        # self.mcpage.click_menu("角色维护")
        self.mcpage.edit_role("角色名称001", "新角色名称", "新角色描述")

    def test_delete_role(self):
        self.mcpage.click_MC()
        # self.mcpage.click_menu("角色维护")
        self.mcpage.delete_role("新角色名称")


# if __name__ == "__main__":
#     test = TestRoleProserve()
#     test.setup_class()
#     test.test_delete_role()
#     test.teardown_class()



