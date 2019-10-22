from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_elements.base_page import BasePage
import conftest


class SearchBar(BasePage):

    search_block = (By.CSS_SELECTOR, 'div[id=searchform]')
    search_input = (By.CSS_SELECTOR, 'input[class*=gLFyf]')
    search_button = (By.CSS_SELECTOR, 'input[name=btnK]')

    def __init__(self):
        super(SearchBar, self).__init__()
        component = WebDriverWait(self.driver, conftest.CONFIG["COMPONENT_WAIT_TIME"]) \
            .until(EC.visibility_of_element_located(self.search_block), 'Відсутній блок пошуку')
        self.wait = WebDriverWait(component, conftest.CONFIG["ELEMENT_WAIT_TIME"])

    def search_for(self, search_word):
        self.wait.until(EC.visibility_of_element_located(self.search_input), 'Відсутнє поле пошуку')\
            .send_keys(search_word)
        self.wait.until(EC.visibility_of_element_located(self.search_button), 'Відсутня кнопка пошуку')\
            .click()
