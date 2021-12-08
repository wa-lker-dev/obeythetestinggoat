from selenium import webdriver
from pytest import fixture

@fixture
def browser():
    browser = webdriver.Firefox()
    browser.get('http://localhost:8000')

    yield browser

    browser.close()


def test_browser(browser: webdriver.Firefox):
    assert 'Django' in browser.title
