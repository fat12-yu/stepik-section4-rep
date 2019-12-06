#!/usr/bin/python

from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not found"


    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.should_be_register_form()
        email_field = self.browser.find_element(*LoginPageLocators.REG_FORM_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REG_FORM_PASS1)
        password_field.send_keys(password)
        password_field = self.browser.find_element(*LoginPageLocators.REG_FORM_PASS2)
        password_field.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_FORM_BUTTON)
        reg_button.click()


    def register_user(self):
        email = 'engfneg@aol.com'
        password = 'lfgdcakmf'
        self.go_to_login_page()
        self.should_be_login_form()
        email_field = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_PASSWORD)
        password_field.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_BUTTON)
        button.click()
        self.should_be_authorized_user()
