from Page.input_page import InputPage
from Page.setting_page import SearchPage


class Page:


    @classmethod
    def get_search_page(cls):
        return SearchPage()

    @classmethod
    def get_input_page(cls):
        return InputPage()