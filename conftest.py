from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None)


@pytest.fixture(scope="function")
@pytest.mark.parametrize('language', ['ru', 'en-gb', 'fr', 'es'])
def browser(request):
    user_language = request.config.getoption("language")
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()




