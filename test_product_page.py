#!/usr/bin/python

import pytest
from pages.product_page import ProductPage

#@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", 
#                                         "5", "6", 
#                                         pytest.param("7", marks=pytest.mark.xfail),"8", "9"])
#def test_guest_can_add_product_to_basket(browser, promo_offer):
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#    print(link)
#    page = ProductPage(browser, link)
#    page.open()
#    page.should_be_product_page()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        from pages.utils import generate_random_email, generate_random_password
        from pages.login_page import LoginPage
        email = generate_random_email()
        password = generate_random_password()
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link, 5)
        page.open()
        page.register_new_user(email, password)


    def test_user_cant_see_success_message(self, browser):
        """
        1. Открываем страницу товара
        2. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        """
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.guest_cant_see_success_message()


    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    1. Открываем страницу товара 
    2. Добавляем товар в корзину 
    3. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    print(link)
    page = ProductPage(browser, link)
    page.open()
    page.cant_see_success_message_after_adding_product()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    1. Открываем страницу товара.
    2. Добавляем товар в корзину
    3. Проверяем, что нет сообщения об успехе с помощью is_disappeared
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    print(link)
    page = ProductPage(browser, link)
    page.open()
    page.message_disappeared_after_adding_product()


def test_guest_cant_see_success_message(browser):
    """
    1. Открываем страницу товара
    2. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    print(link)
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_and_should_be_empty()
