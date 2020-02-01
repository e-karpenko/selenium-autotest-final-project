from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_HEADER_LINK= (By.CSS_SELECTOR, "div.basket-mini a")
    USER_ICON=(By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    MESSAGE_OF_EMPTY_BASKET= (By.CSS_SELECTOR, "#content_inner>p")
    PRODUCT_IN_BASKET= (By.CSS_SELECTOR, "div.basket-items")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM= (By.CSS_SELECTOR, "#login_form")
    INPUT_LOGIN_EMAIL=(By.CSS_SELECTOR, "#id_login-username")
    INPUT_LOGIN_PASS=(By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN=(By.NAME, "login_submit")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")
    INPUT_REGISTER_EMAIL=(By.CSS_SELECTOR, "#id_registration-email")
    INPUT_REGISTER_PASS=(By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_REGISTER_CONFIRM_PASS=(By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON= (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE= (By.CSS_SELECTOR, "p.price_color")
    ADDED_PRODUCT_NAME=(By.CSS_SELECTOR,"div.alert-success:nth-child(1) strong")
    ADDED_PRODUCT_PRICE=(By.CSS_SELECTOR, "div.alert-info strong")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, "div.alert-success:nth-child(1)")