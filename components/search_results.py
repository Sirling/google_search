from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_elements.base_page import BasePage
import conftest


class SearchResults(BasePage):

    search_list = (By.CSS_SELECTOR, 'div[id=res]')
    search_title = (By.CSS_SELECTOR, 'h3[class=LC20lb]')
    search_domain = (By.CSS_SELECTOR, 'cite[class*="iUh30"]')

    def __init__(self):
        super(SearchResults, self).__init__()
        component = WebDriverWait(self.driver, conftest.CONFIG["COMPONENT_WAIT_TIME"]) \
            .until(EC.visibility_of_element_located(self.search_list), 'Відсутній блок пошуку')
        self.wait = WebDriverWait(component, conftest.CONFIG["ELEMENT_WAIT_TIME"])

    def domains(self):
        """
        Пошук усіх доменів у рещультатах пошуку
        :return: список усіх доменів
        """
        # створення порожнього списку доменів
        domains = []
        # список усіх вебелементів з доменами
        links = self.wait.until(EC.presence_of_all_elements_located(self.search_domain),
                                'Відсутні елементи з доменами')
        for link in links:
            # запис кожного домена з вебелемента у список
            domains.append(link.text)
        return domains

    def search_in_title(self, word, results_range):
        """
        Пошук результату у тайтлі на сторінці результатів
        :param word: строка для пошуку
        :param results_range: кількість результатів для пошуку (максимум - 9)
        :return: True -  якщо є співпадіння, в іншому випадку - False
        """
        # пошук усіх тайтлів у результатах пошуку
        titles = self.wait.until(EC.presence_of_all_elements_located(self.search_title),
                                 'Відсутні елементи з тайтлами')
        for item in range(0, results_range):
            # пошук заданої строки у кожному тайтлі
            if word in titles[item].text.lower():
                return True
            else:
                return False
