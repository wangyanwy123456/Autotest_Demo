from selenium.webdriver.common.by import By

#该页面记录的是所有页面的元素的定位方式

"""
登录页面
"""
login_username = By.XPATH,".//input[@id='username']"      #账号
login_pwd = By.XPATH,".//input[@id='password']"      #密码
login_code= By.XPATH,".//input[@id='code']"    #验证码
login_in_btn = By.XPATH,".//input[@name='submit']"    #登录按钮
accout_fig = By.XPATH,".//label/img"    #账号头像
login_out_btn = By.XPATH,"//a[contains(text(),'退出登录')]"    #退出登录


#管理中心
mc_center = By.LINK_TEXT,'管理中心'   #管理中心菜单









