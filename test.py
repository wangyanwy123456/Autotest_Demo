from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
def find_ele():
    ele = driver.find_element_by_id("kw")
    return ele
if find_ele():
    print("11111")
else:
    driver.quit()