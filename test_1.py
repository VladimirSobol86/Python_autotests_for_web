from login_page import OperationsHelperLogin
from contact_page import OperationsHelperContact
import time
import logging
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

# site = Site(testdata["address"])
#Lection3 test
# def test_with_invalid_values(browser, err_label_text):
#     logging.info("Test with invalid values starting")
#     testpage_login = OperationsHelperLogin(browser)
#     testpage_login.go_to_site()
#     testpage_login.enter_login("invalid login")
#     testpage_login.enter_pass("invalid pass")
#     testpage_login.click_login_button()
#     assert testpage_login.get_error_text() == err_label_text

def test_contact_page(browser, contact_text):
    logging.info("Test Contact page starting")   
    testpage_login = OperationsHelperLogin(browser)
    testpage_login.go_to_site()
    testpage_login.enter_login(testdata["login"])
    testpage_login.enter_pass(testdata["password"])
    testpage_login.click_login_button()
    time.sleep(2)
    testpage_contact = OperationsHelperContact(browser)
    testpage_contact.click_contact_button()
    time.sleep(2)
    assert testpage_contact.get_contact_text() == contact_text
    testpage_contact.enter_name(testdata["name"])
    testpage_contact.enter_email(testdata["email"])
    testpage_contact.enter_content(testdata["content"])
    time.sleep(2)
    testpage_contact.click_send_button()
    time.sleep(2)
    assert testpage_contact.alert_label() == testdata["alert"]
#Lesson2    
# def test_with_correct_values(site, path_login, path_password, 
#                              button_selector, btn_home_selector, 
#                              btn_home_text, btn_create_blog, path_title, 
#                              btn_save_blog, title_after_creation, title_text):
#     input1 = site.find_element("xpath", path_login)
#     input1.send_keys(testdata["login"])
    
#     input2 = site.find_element("xpath", path_password)
#     input2.send_keys(testdata["password"])
    
#     btn = site.find_element("css", button_selector)
#     btn.click()
    
#     btn_home = site.find_element("xpath", btn_home_selector)
#     assert btn_home.text == btn_home_text
# #HW code is below______________________________________    
#     btn_create = site.find_element("xpath", btn_create_blog)
#     btn_create.click()
#     time.sleep(2)
    
#     title = site.find_element("xpath", path_title)
#     title.send_keys(title_text)
#     time.sleep(2)
    
#     btn_save = site.find_element("xpath", btn_save_blog)
#     btn_save.click()
#     time.sleep(2)
        
#     title_path = site.find_element("xpath", title_after_creation)
#     assert title_path.text == title_text
#     time.sleep(2)
    
    