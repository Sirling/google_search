import os
from selenium import webdriver

import conftest
from utilities import drivers_executables


class Driver(object):
    __instance = None

    @classmethod
    def get_instance(cls):
        """
        Створення драйверу із застосуванням Singletone паттерну
        :return: інстанс драйверу
        """
        # створення шляху до папки з драйверами
        webdrivers_path = os.path.dirname(drivers_executables.__file__)
        # запис тип браузера у змінну
        browser = conftest.CONFIG['BROWSER'].lower()
        # створення опцій до хром браузера
        chromeoptions = webdriver.ChromeOptions()
        chromeoptions.add_argument('--start-maximized')
        chromeoptions.add_argument('--lang=en')

        if cls.__instance is None:
            # ініціалізація браузера в залежності від заданого браузеру
            if browser == "chrome":
                cls.__instance = webdriver.Chrome(options=chromeoptions, executable_path=os.path.join(
                    webdrivers_path, "chromedriver.exe"))
            if browser == "firefox":
                cls.__instance = webdriver.Firefox(executable_path=os.path.join(webdrivers_path, "geckodriver.exe"))
        # встановлення таймеру завантажєння сторінки
        cls.__instance.set_page_load_timeout(10)
        return cls.__instance

    @classmethod
    def close(cls):
        """
        Закриття вкладки
        """
        cls.__instance.close()

    @classmethod
    def quit(cls):
        """
        Закриття браузеру та присвоєння змінній значення None (видалення інстансу)
        """
        cls.__instance.quit()
        cls.__instance = None
