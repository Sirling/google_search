from project.driver.driver import Driver


class BasePage:

    def __init__(self):
        self.driver = Driver().get_instance()

