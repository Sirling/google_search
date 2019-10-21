from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_elements.base_page import BasePage
from utilities import settings


class NavigationBar(BasePage):

    navigation_bar = (By.CSS_SELECTOR, 'div[id=navcnt]')
    navigation_page = (By.CSS_SELECTOR, 'a[class=fl]')

    def __init__(self):
        super(NavigationBar, self).__init__()
        component = WebDriverWait(self.driver, settings.component_wait_time) \
            .until(EC.visibility_of_element_located(self.navigation_bar), 'Відсутній блок пошуку')
        self.wait = WebDriverWait(component, settings.element_wait_time)

    def navigate_to_page(self, page_number):

        page = self.wait.until(EC.presence_of_all_elements_located(self.navigation_page),
                               "Елементи пагінації відсутні")
        page[page_number].click()

    def search_in_pages(self, number_of_pages):

        for page in range(1, number_of_pages):
            self.navigate_to_page(page)
