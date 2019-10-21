import conftest
from driver.driver import Driver


class BasePage:

    def __init__(self):
        self.driver = Driver().get_instance()

    def open(self):
        self.driver.get(conftest.CONFIG["BASE_URL"])
