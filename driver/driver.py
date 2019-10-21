import os
from selenium import webdriver

import conftest
from utilities import drivers_executables


class Driver(object):
    __instance = None

    @classmethod
    def get_instance(cls):
        webdrivers_path = os.path.dirname(drivers_executables.__file__)
        browser = conftest.CONFIG['BROWSER'].lower()

        if cls.__instance is None:
            if browser == "chrome":
                cls.__instance = webdriver.Chrome(executable_path=os.path.join(webdrivers_path, "chromedriver.exe"))
            if browser == "firefox":
                cls.__instance = webdriver.Firefox(executable_path=os.path.join(webdrivers_path,
                                                                                "utilities/drivers_executables/"
                                                                                "geckodriver.exe"))
        cls.__instance.set_page_load_timeout(10)
        return cls.__instance

    @classmethod
    def close(cls):
        cls.__instance.close()

    @classmethod
    def quit(cls):
        cls.__instance.quit()
        cls.__instance = None
