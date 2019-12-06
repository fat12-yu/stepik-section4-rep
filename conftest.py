#!/usr/bin/python


try:
    from conftest_dev import *
except ImportError:
    from selenium import webdriver
    import pytest


    def pytest_addoption(parser):
        parser.addoption('--language', action='store', default='en',
                         help="Choose language")

    @pytest.fixture(scope="function")
    def browser(request):
        language = request.config.getoption('language')
        print(f'\n######################## lang: {language}')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages':language})
        print("\nstart browser for test..")
        browser = webdriver.Chrome(options=options)
        yield browser
        print("\nquit browser..")
        browser.quit()
