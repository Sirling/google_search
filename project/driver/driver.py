import os

from selenium import webdriver

import utilities
from utilities import settings


class Driver(object):
    __instance = None

    @classmethod
    def get_instance(cls):
        webdrivers_path = os.path.dirname(utilities.__file__)

        if cls.__instance is None:
            if settings.browser_name == "chrome":
                cls.__instance = webdriver.Chrome(executable_path=os.path.join(webdrivers_path,
                                                                               "driver_executables/chromedriver.exe"))
            if settings.browser_name == "firefox":
                cls.__instance = webdriver.Firefox(executable_path=os.path.join(webdrivers_path,
                                                                                "driver_executables/geckodriver.exe"))
        cls.__instance.set_page_load_timeout(10)
        return cls.__instance

    @classmethod
    def close(cls):
        cls.__instance.close()

    @classmethod
    def quit(cls):
        cls.__instance.quit()
        cls.__instance = None
