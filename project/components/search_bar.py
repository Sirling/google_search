from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from project.base_elements.base_page import BasePage
from utilities import settings


class SearchBar(BasePage):

    search_block = (By.CSS_SELECTOR, 'div[id=searchform]')
    search_input = (By.CSS_SELECTOR, 'input[class*=gLFyf]')
    search_button = (By.CSS_SELECTOR, 'input[name=btnK]')

    def __init__(self):
        super(SearchBar, self).__init__()
        component = WebDriverWait(self.driver, settings.component_wait_time) \
            .until(EC.visibility_of_element_located(self.search_block), 'Відсутній блок пошуку')
        self.wait = WebDriverWait(component, settings.element_wait_time)

    def fill_search_field(self):
        pass
