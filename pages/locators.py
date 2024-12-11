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

class  BasePageLocators:
    LOGIN_LINK = ("css selector", "#login_link")
    LOGIN_LINK_INVALID = ("css selector", "#login_link_inc")
    CARD_LINK = ('xpath', '//a[@class="btn btn-default"]')


class BasketPageLocators:
    CARD_EMPTY_FIELD = ('xpath', '//p')
    PRODUCTS_IN_CARD = ('xpath', '//h2[text()="Товары в корзине"]')