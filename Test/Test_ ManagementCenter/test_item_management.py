import pytest
from page.management_center_page import MCPage
from page.login_page import LoginPage
import time
from utils import DriverUtils

import os, sys
sys.path.append(os.getcwd())


class TestItemManage:

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

    # 新增项目
    def test_add_item(self):
        self.mcpage.click_MC()
        self.mcpage.click_menu("项目管理","项目管理")
        self.mcpage.add_item("新增项目测试","item001")


