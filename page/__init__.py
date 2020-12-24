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
# sys_mc = By.XPATH,".//span[contains(text(),'系统管理')]"    #左侧系统管理菜单
sys_mc =  By.XPATH,".//i/../span[contains(text(),'系统管理')]"    #左侧系统管理菜单
role_preserve = By.XPATH,".//span[contains(text(),'角色维护')]"   #左侧角色维护菜单
add_role_btn = By.XPATH,".//button/span[contains(text(),'角色录入')]"    #角色录入按钮

select_role_input = By.XPATH,".//input[@class='ant-input']"      #查询角色输入框
select_btn = By.XPATH,".//i/../span[contains(text(),'查询')]"      #查询按钮
reset_btn = By.XPATH,".//i/../span[contains(text(),'重置')]"      #重置按钮

#角色维护模块---新增角色页面
add_title = By.XPATH,".//div[contains(text(),'新增')]"       #新增页面标题
role_name_input = By.XPATH,".//input[@placeholder='请输入角色名称']"       #角色名称输入框
role_code_input = By.XPATH,".//input[@placeholder='请输入角色编码']"       #角色编码输入框
description_input = By.XPATH,".//textarea[@id='description']"       #描述输入框
close_btn = By.XPATH,".//button/span[contains(text(),'关 闭')]"       #关闭按钮
confirm_btn = By.XPATH,".//button/span[contains(text(),'确 定')]"       #确定按钮









