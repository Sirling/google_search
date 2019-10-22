from components.navigation_bar import NavigationBar
from components.search_results import SearchResults


class SearchPage:

    # lazy ініціалізація компоненту
    @property
    def search_results(self):
        return SearchResults()

    # lazy ініціалізація компоненту
    @property
    def navigation_bar(self):
        return NavigationBar()

    def search_domain_in_pages(self, domain_name, number_of_pages):
        """
        Пошук заданої строки у полі домена
        :param domain_name: строка домену
        :param number_of_pages: кількість сторінок для пошуку
        :return: True якщо э співпадіння, в іншому випадку - False
        """
        # пошук на першій сторінці результатів
        domains = self.search_results.domains()
        for domain in domains:
            if domain_name in domain:
                return True
        # цикл на пошук
        for page in range(number_of_pages):
            # перехід на сторінку
            self.navigation_bar.navigate_to_page(page)
            # пошук усіх доменів з результатів пошуку
            domains = self.search_results.domains()
            # пошук заданої строки у кожному домені
            for domain in domains:
                if domain_name in domain:
                    return True
        return False
