from base_elements.base_page import BasePage
from components.search_bar import SearchBar


class MainPage(BasePage):

    @property
    def search_bar(self):
        return SearchBar()
