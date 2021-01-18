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
default_page = By.XPATH,".// li[contains(text(), '1-')]"     #重置之后的默认页面

#角色维护模块---新增角色页面
add_title = By.XPATH,".//div[contains(text(),'新增')]"       #新增页面标题
role_name_input = By.XPATH,".//input[@placeholder='请输入角色名称']"       #角色名称输入框
role_code_input = By.XPATH,".//input[@placeholder='请输入角色编码']"       #角色编码输入框
description_input = By.XPATH,".//textarea[@id='description']"       #描述输入框
close_btn = By.XPATH,".//button/span[contains(text(),'关 闭')]"       #关闭按钮
confirm_btn = By.XPATH,".//button/span[contains(text(),'确 定')]"       #确定按钮

#删除角色页面
# delete_role = ((By.XPATH,".//td[contains(text(),name)]/../td//a[contains(text(),'删除')]" .format(name)])) #删除角色
role_delete_success = (By.XPATH,".//span[contains(text(),'删除成功')]")
cofirm_del_tile = (By.XPATH,".//span[contains(text(),'确认删除')]")     #确认删除标题


#角色编辑
edit_role = (By.XPATH,".//button/span[contains(text(),'角色编辑')]")     #角色编辑按钮
edit_title = (By.XPATH,".//div[contains(text(),'编辑')]")       #编辑的标题
edit_role_name_input = (By.XPATH,".//input[@placeholder='请输入角色名称']")        #角色名称输入框
edit_role_descrip_input = (By.XPATH,".//textarea[@id='description']")        #角色描述输入框
edit_role_confirm_btn = By.XPATH,".//button/span[contains(text(),'确 定')]"       #确定按钮
edit_role_success = (By.XPATH,".//span[contains(text(),'修改成功')]")



#部门管理
btn_add_first_department = By.XPATH,".//button/span[contains(text(),'添加一级部门')]"      #添加一级部门
btn_add_child_department = By.XPATH,".//button/span[contains(text(),'添加子部门')]"        #添加子部门
select_department_input = By.XPATH,".//input[@placeholder='请输入部门名称']"      #查询部门输入框
select_department_btn = By.XPATH,".//i[@class='anticon anticon-search ant-input-search-icon']"       #查询部门按钮
batch_delete = By.XPATH,".//button[@title='删除多条数据']"     #批量删除
basic_info = By.XPATH,".//div[@role='tab'][contains(text(),'基本信息')]"     #基本信息tab


#新增部门页面
department_input = By.XPATH,".//input[@placeholder='请输入机构/部门名称']"
department_tel_input = By.XPATH,".//input[@placeholder='请输入电话']"
add_department_success = (By.XPATH,".//span[contains(text(),'添加成功')]")     #添加部门成功的提示
add_same_department_msg = (By.XPATH,".//i/../span[contains(text(),'同父部门下重复的部门名称或重复的一级部门名')]")    #添加同级部门的提示


#项目管理
add_btn = By.XPATH,".//button/span[contains(text(),'新增')]"   #新增按钮
item_name_input = By.XPATH,".//input[@placeholder='请输入项目名称']"   #项目名称输入框
item_num_input = By.XPATH,".//input[@placeholder='请输入项目编号']"   #项目编号输入框
item_edit_title = By.XPATH,".//div[@id='rcDialogTitle0'][contains(text(),'编辑')]"     #编辑的标题
batch_act = By.XPATH,".//button/span[contains(text(),'批量操作')]"      #批量操作按钮
delete_item = By.XPATH,".//li[contains(text(),'删除')]"      #删除


