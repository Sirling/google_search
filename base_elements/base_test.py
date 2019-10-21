import pytest

from driver.driver import Driver


@pytest.mark.usefixtures('get_config', 'try_new')
class BaseTest:
    #
    # def __init__(self):
    #     self.driver = Driver().get_instance()

    def setup(self):
        self.driver = Driver().get_instance()
        pass

    def teardown(self):
        self.driver.close()
        self.driver.quit()
