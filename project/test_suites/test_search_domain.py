from project.base_elements.base_test import BaseTest
from project.pages.main_page import MainPage
from project.pages.search_page import SearchPage


class TestSearchDomain(BaseTest):

    def test_find_domain(self):
        MainPage().search_bar.fill_search_field(search_word="automation")
        SearchPage().search_in_pages()