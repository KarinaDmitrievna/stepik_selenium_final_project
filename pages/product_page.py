from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def add_product_to_card(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BUTTON).click()
        self.solve_quiz_and_get_code()
        self.should_be_success_message()
        self.should_be_same_titles()
        self.should_be_message_with_price()
        self.should_be_same_prices()

    def should_be_success_message(self):
        element = self.is_element_present(*ProductPageLocators.ADDED_TO_CARD)
        assert element, "There is no success message"

    def should_be_same_titles(self):
        element_title = self.browser.find_element(*ProductPageLocators.ADDED_TO_CARD).text
        book_title = self.browser.find_element(*ProductPageLocators.HEAD_TITLE).text
        assert element_title == book_title, "The book titles don't match"

    def should_be_message_with_price(self):
        element = self.is_element_present(*ProductPageLocators.COUNT_CARD)
        assert element, "There is no message with card price"

    def should_be_same_prices(self):
        element_price = self.browser.find_element(*ProductPageLocators.COUNT_CARD).text
        book_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert element_price == book_price, "The book prices don't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_CARD), "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_CARD), 'Success message is presented, but should be hidden after 4 seconds'
