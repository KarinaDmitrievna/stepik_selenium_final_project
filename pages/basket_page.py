from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_card(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_CARD), 'There is any products in card'

    def should_be_text_empty_present(self):
        assert self.is_element_present(*BasketPageLocators.CARD_EMPTY_FIELD), "The text 'Empty card' is not present"