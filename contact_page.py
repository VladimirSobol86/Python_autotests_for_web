from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocatorsContact:
    x_btn_contact = (By.XPATH,'//*[@id="app"]/main/nav/ul/li[2]/a')
    x_label_contact_us = (By.XPATH,'//*[@id="app"]/main/div/div/h1')
    x_name = (By.XPATH,'//*[@id="contact"]/div[1]/label/input')
    x_email = (By.XPATH,'//*[@id="contact"]/div[2]/label/input')
    x_content = (By.XPATH,'//*[@id="contact"]/div[3]/label/span/textarea')
    x_btn_send = (By.XPATH,'//*[@id="contact"]/div[4]/button/span')
    
class OperationsHelperContact(BasePage):
    def click_contact_button(self):
        logging.info("Click contact button")
        self.find_element(TestSearchLocatorsContact.x_btn_contact).click()

    def get_contact_text(self):
        contact_text = self.find_element(TestSearchLocatorsContact.x_label_contact_us, time=3)
        text = contact_text.text
        logging.info(f"We find text {text} in error field {TestSearchLocatorsContact.x_label_contact_us}")
        return text
    
    def enter_name(self, word):
        logging.info(f"Send {word} to element {TestSearchLocatorsContact.x_name[1]}")
        login_field = self.find_element(TestSearchLocatorsContact.x_name)
        login_field.clear()
        login_field.send_keys(word)
        
    def enter_email(self, email):
        logging.info(f"Send {email} to element {TestSearchLocatorsContact.x_email[1]}")
        login_field = self.find_element(TestSearchLocatorsContact.x_email)
        login_field.clear()
        login_field.send_keys(email)
        
    def enter_content(self, text):
        logging.info(f"Send {text} to element {TestSearchLocatorsContact.x_content[1]}")
        login_field = self.find_element(TestSearchLocatorsContact.x_content)
        login_field.clear()
        login_field.send_keys(text)
        
    def click_send_button(self):
        logging.info("Click send button")
        self.find_element(TestSearchLocatorsContact.x_btn_send).click()
        
    def alert_label(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f"Message in alert after clicking Send button: {text}")
        return text