from pages.base_page import Page
from pages.cart_page import CartPage
from pages.circle_page import CirclePage
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)

        self.cart_page = CartPage(driver)
        self.circle_page = CirclePage(driver)
        self.help_page = HelpPage
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
