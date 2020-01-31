from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM= (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON= (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE= (By.CSS_SELECTOR, "p.price_color")
    ADDED_PRODUCT_NAME=(By.CSS_SELECTOR,"div.alert-success:nth-child(1) strong")
    ADDED_PRODUCT_PRICE=(By.CSS_SELECTOR, "div.alert-info strong")

    SUCCESS_MESSAGE=(By.CSS_SELECTOR, "div.alert-success:nth-child(1)")