from selenium import webdriver


class DriverUtils:
    _driver = None
    _auto_quit = True


    #获取驱动
    @classmethod
    def get_driver(cls,url):
        if cls._driver is None:
            cls._driver = webdriver.Firefox()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(30)
            cls._driver.get(url)
        return cls._driver

    #退出驱动
    @classmethod
    def quit_driver(cls):
        if cls._auto_quit:
            if cls._driver:
                cls._driver.quit()
                cls._driver = None


if __name__ == "__main__":
    driverutils = DriverUtils()
    driverutils.get_driver("http://10.194.188.76/homePage")
    driverutils.quit_driver()
    driverutils.get_driver("http://10.194.188.76/homePage")


