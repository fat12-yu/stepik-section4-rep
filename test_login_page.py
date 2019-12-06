#!/usr/bin/python

from pages.login_page import LoginPage

def test_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

def test_user_login(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.register_user()

def test_user_reg(browser):
    from pages.utils import generate_random_email, generate_random_password
    email = generate_random_email()
    password = generate_random_password()
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link, 5)
    page.open()
    page.register_new_user(email, password)

