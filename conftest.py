import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # Задаем опции браузера и языка
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: firefox or chrome")
    parser.addoption('--language', action='store', default='en', help="Say language name to select")

@pytest.fixture(scope="function")
def browser(request):
    choosen_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    # Инициализация выбранного браузера
    if browser_name == "chrome":
        opts = Options()
        opts.add_experimental_option('prefs', {'intl.accept_languages': choosen_language})
        browser = webdriver.Chrome(options=opts)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", choosen_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise ValueError(f"Указанный браузер не поддерживается системой: {browser_name}")

    yield browser
    browser.quit()