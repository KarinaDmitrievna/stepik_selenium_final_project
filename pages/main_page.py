from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def should_be_empty_card(self):
    #     assert not self.is_not_element_present(*MainPageLocators.PRODUCTS_IN_CARD), 'There is any products in card'
    #
    # def should_be_text_empty_present(self):
    #     assert self.is_element_present(*MainPageLocators.CARD_EMPTY_FIELD), "The text 'Empty card' is not present"


