from base_elements.base_test import BaseTest
from pages.main_page import MainPage
from pages.search_page import SearchPage


class TestSearchTitle(BaseTest):

    def test_search_title(self):
        main_page = MainPage()
        main_page.open()
        main_page.search_bar.search_for("automation")
        result = SearchPage().search_results.search_in_title("automation", 1)
        assert result, "Результат пошуку не містить пошукового слова"
