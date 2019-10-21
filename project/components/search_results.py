from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from project.base_elements.base_page import BasePage
from utilities import settings


class SearchResults(BasePage):

    search_list = (By.CSS_SELECTOR, 'div[id=res]')
    search_titles = (By.CSS_SELECTOR, 'h3[class=LC20lb]')
    search_domains = (By.CSS_SELECTOR, 'div[class=r] a')

    def __init__(self):
        super(SearchResults, self).__init__()
        component = WebDriverWait(self.driver, settings.component_wait_time) \
            .until(EC.visibility_of_element_located(self.search_list), 'Відсутній блок пошуку')
        self.wait = WebDriverWait(component, settings.element_wait_time)

    def domain_extractor(self):
        domains = None
        links = self.wait.until(EC.presence_of_all_elements_located(self.search_domains), 'Відсутні елементи з доменами')
        for link in links:
            domains.append(link)
        return domains
