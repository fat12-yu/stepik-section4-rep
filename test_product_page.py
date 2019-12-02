#!/usr/bin/python

import pytest
from pages.product_page import ProductPage

@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", 
                                         "5", "6", 
                                         pytest.param("7", marks=pytest.mark.xfail),"8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    print(link)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
