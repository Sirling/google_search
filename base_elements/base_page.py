import conftest
from driver.driver import Driver


class BasePage:

    def __init__(self):
        self.driver = Driver().get_instance()   # створення посилання на інстанс драйверу

    def open(self):
        """
        Відкриття урла з файлу конфігурації
        """
        self.driver.get(conftest.CONFIG["BASE_URL"])
