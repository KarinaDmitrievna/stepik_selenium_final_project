class MainPageLocators:
    LOGIN_LINK = ("css selector", "#login_link")

class LoginPageLocators:
    LOGIN_FORM = ('xpath', '//form[@id="login_form"]')
    REGISTER_FORM = ('xpath', '//form[@id="register_form"]')

class ProductPageLocators:
    ADD_TO_CARD_BUTTON = ('xpath', '(//button[@type="submit"])[2]')
    ADDED_TO_CARD = ('xpath', '(//strong)[4]')
    COUNT_CARD = ('xpath', '(//strong)[6]')
    HEAD_TITLE = ('xpath', '//h1')
    PRICE = ('xpath', '//p[@class="price_color"]')


