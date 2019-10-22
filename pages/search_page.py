from components.navigation_bar import NavigationBar
from components.search_results import SearchResults


class SearchPage:

    @property
    def search_results(self):
        return SearchResults()

    @property
    def navigation_bar(self):
        return NavigationBar()

    def search_domain_in_pages(self, domain_name, number_of_pages):
        page = 1
        while page != number_of_pages:
            self.navigation_bar.navigate_to_page(page)
            page += 1
            domains = self.search_results.domains()
            for domain in domains:
                if domain_name in domain:
                    return True
