from selenium import webdriver
import pytest

@pytest.fixture
def browser():
    browser = webdriver.Firefox()
    browser.get('http://localhost:8000')

    yield browser

    browser.close()


def test_edith_persona(browser: webdriver.Firefox):
    # She notices the page title and header mention to-do lists
    assert 'To-Do' in browser.title, "Browser title was " + browser.title

    # She is invited to enter a to-do item straight away

    # She types "Buy peacock feathers" into a text box (Edith's hobby
    # is tying fly-fishing lures)

    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list

    # There is still a text box inviting her to add another item. She
    # enters "Use peacock feathers to make a fly" (Edith is very methodical)

    # The page updates again, and now shows both items on her list

    # Edith wonders whether the site will remember her list. Then she sees
    # that the site has generated a unique URL for her -- there is some
    # explanatory text to that effect.

    # She visits that URL - her to-do list is still there.

    # Satisfied, she goes back to sleep
    pytest.fail('Finish the test!')

if __name__ == '__main__':  
    pytest.main()