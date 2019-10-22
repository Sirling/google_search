from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_elements.base_page import BasePage
import conftest


class SearchBar(BasePage):

    search_block = (By.CSS_SELECTOR, 'div[id=searchform]')      # локатор блоку пошуку
    search_input = (By.CSS_SELECTOR, 'input[class*=gLFyf]')     # локатор поля пошуку
    search_button = (By.CSS_SELECTOR, 'input[name=btnK]')       # локатор кнопки пошуку

    def __init__(self):
        super(SearchBar, self).__init__()
        component = WebDriverWait(self.driver, conftest.CONFIG["COMPONENT_WAIT_TIME"]) \
            .until(EC.visibility_of_element_located(self.search_block), 'Відсутній блок пошуку')
        self.wait = WebDriverWait(component, conftest.CONFIG["ELEMENT_WAIT_TIME"])

    def search_for(self, search_word):
        """
        Пошук по заданій строці
        :param search_word: Строка для пошуку
        """
        # пошук елементу та введення строки у поле пошуку
        self.wait.until(EC.visibility_of_element_located(self.search_input), 'Відсутнє поле пошуку')\
            .send_keys(search_word)
        # пошук елементу кнопки "Пошук" та клік по ній
        self.wait.until(EC.visibility_of_element_located(self.search_button), 'Відсутня кнопка пошуку')\
            .click()
