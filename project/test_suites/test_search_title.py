from project.base_elements.base_test import BaseTest
from project.pages.main_page import MainPage
from project.pages.search_page import SearchPage


class TestSearchTitle(BaseTest):

    def test_search_title(self):
        MainPage().search_bar.search_for("automation")
        result = SearchPage().search_results.search_in_title("automation")
        assert result, "Результат пошуку не містить пошукового слова"
