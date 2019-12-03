#!/usr/bin/python

from selenium.webdriver.common.by import By
from .base_page import BasePage


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
