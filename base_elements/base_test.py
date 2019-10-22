from driver.driver import Driver


class BaseTest:

    def setup(self):
        self.driver = Driver().get_instance()

    def teardown(self):
        Driver().close()
        Driver().quit()
