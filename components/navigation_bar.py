from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_elements.base_page import BasePage
import conftest


class NavigationBar(BasePage):
    navigation_bar = (By.CSS_SELECTOR, 'div[id=navcnt]')  # локатор компоненту пагінації
    navigation_page = (By.CSS_SELECTOR, 'a[aria-label*="Page"]')  # локатор компоненту сторінки пагінації

    def __init__(self):
        super(NavigationBar, self).__init__()
        # вебелемент компоненту
        component = WebDriverWait(self.driver, conftest.CONFIG["COMPONENT_WAIT_TIME"]) \
            .until(EC.visibility_of_element_located(self.navigation_bar), 'Відсутній блок пошуку')
        # кастомний вейт від компоненту
        self.wait = WebDriverWait(component, conftest.CONFIG["ELEMENT_WAIT_TIME"])

    def navigate_to_page(self, page_number):
        """
        Перехід до вказаної сторінки
        :param page_number: номер сторінки
        """
        # пошук усіх локаторів сторінок
        pages = self.wait.until(EC.presence_of_all_elements_located(self.navigation_page),
                                "Елементи пагінації відсутні")
        # клік по обраній сторінці
        pages[page_number].click()

    def search_in_pages(self, number_of_pages):
        """
        Навігація по заданій кількості сторінок
        :param number_of_pages: кількість сторінок для пошуку
        """
        for page in range(1, number_of_pages):
            self.navigate_to_page(page)
