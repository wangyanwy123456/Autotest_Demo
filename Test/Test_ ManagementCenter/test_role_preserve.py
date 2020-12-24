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
        self.driver.quit()

    #查询角色
    def test_select_role(self):
         self.mcpage.click_MC()
         self.mcpage.click_menu("角色维护")
         self.mcpage.select_role("新增")



if __name__ == "__main__":
    test = TestRoleProserve()
    test.setup_class()
    test.test_select_role()
    test.teardown_class()



