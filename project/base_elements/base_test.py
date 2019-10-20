from project.driver.driver import Driver


class BaseTest:

    def __init__(self):
        self.driver = Driver().get_instance()

    def setup(self):
        pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()
