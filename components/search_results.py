from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_elements.base_page import BasePage
from conftest import CONFIG


class SearchResults(BasePage):

    search_list = (By.CSS_SELECTOR, 'div[id=res]')
    search_title = (By.CSS_SELECTOR, 'h3[class=LC20lb]')
    search_domain = (By.CSS_SELECTOR, 'div[class=r] a')

    def __init__(self):
        super(SearchResults, self).__init__()
        component = WebDriverWait(self.driver, CONFIG["COMPONENT_WAIT_TIME"]) \
            .until(EC.visibility_of_element_located(self.search_list), 'Відсутній блок пошуку')
        self.wait = WebDriverWait(component, CONFIG["ELEMENT_WAIT_TIME"])

    def domains(self):
        domains = None
        links = self.wait.until(EC.presence_of_all_elements_located(self.search_domain),
                                'Відсутні елементи з доменами')
        for link in links:
            domains.append(link)
        return domains

    def search_in_title(self, word, results_range):
        titles = self.wait.until(EC.presence_of_all_elements_located(self.search_title),
                                 'Відсутні елементи з тайтлами')
        for item in range(1, results_range):
            if word in titles[item]:
                return True
            else:
                return False
