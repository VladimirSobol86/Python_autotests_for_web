from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocatorsLogin:
#locators
    x_login = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    x_password = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    css_btn_login = (By.CSS_SELECTOR, "button")
    x_err_label = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    # x_btn_home = (By.XPATH, '//*[@id="app"]/main/nav/a/span')
    # x_btn_create = (By.XPATH, '//*[@id="create-btn"]')
    # x_post_title = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    # x_btn_save = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button/span')
    # x_title_after_creation = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')

class OperationsHelperLogin(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocatorsLogin.x_login[1]}")
        login_field = self.find_element(TestSearchLocatorsLogin.x_login)
        login_field.clear()
        login_field.send_keys(word)
        
    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocatorsLogin.x_password[1]}")
        login_field = self.find_element(TestSearchLocatorsLogin.x_password)
        login_field.clear()
        login_field.send_keys(word)    
        
    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocatorsLogin.css_btn_login).click()
        
    def get_error_text(self):
        error_field = self.find_element(TestSearchLocatorsLogin.x_err_label, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocatorsLogin.x_err_label}")
        return text