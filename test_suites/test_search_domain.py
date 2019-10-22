from base_elements.base_test import BaseTest
from pages.main_page import MainPage
from pages.search_page import SearchPage


class TestSearchDomain(BaseTest):

    def test_find_domain(self):
        """
        Пошук домена серед результатів пошукового результату
        """
        main_page = MainPage()
        main_page.open()
        main_page.search_bar.search_for(search_word="automation")
        result = SearchPage().search_domain_in_pages('testautomationday.com', 5)
        assert result, "Результат пошуку не містить пошукового слова"
