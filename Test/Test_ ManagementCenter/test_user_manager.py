import os, sys
import pytest

from page.management _center_page import MCPage

# from page. import NavigationPage
# from base.init_driver import get_driver
# from base.read_yaml_data import read_yaml_data
# import time
#
#
# # 获取模拟的yaml数据
# def get_data():
#     data_list = []
#     data = read_yaml_data("login_data.yaml")
#     # print(data)
#     for i in data.keys():
#         data2 = data.get(i)
#         name = data2.get("username")
#         passwd = data2.get("password")
#         tag = data2.get("tag")
#         except_msg = data2.get("except_msg")
#         get_toast_msg = data2.get("get_toast_msg")
#         data_list.append((name, passwd,tag,get_toast_msg,except_msg))
#     return data_list
#
# class TestLogin:
#     # 初始化导航类
#     def setup_class(self):
#         # 1.初始化driver对象
#         self.driver = get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
#         # 2.初始化导航对象
#         self.navigation_page = NavigationPage(self.driver)
#
#     def teardown_class(self):
#         time.sleep(5)
#         self.driver.quit()