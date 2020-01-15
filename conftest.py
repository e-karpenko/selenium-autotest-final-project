import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

#данные о переменных browser_name и language из командной строки. по умолчанию запускается браузер chrome на англ языке 
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", help ="Choose browser language: ru, en, fr...")

@pytest.fixture(scope="function")
def browser(request):

#значения переменных получены из командной строки
    browser_name=request.config.getoption("browser_name")
    user_lng=request.config.getoption("language")  
  
#запуск локализации в зависимости от выбора браузера   
    if browser_name=="chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_lng})
        browser = webdriver.Chrome(options=options)
    elif browser_name=="firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_lng)
        browser = webdriver.Firefox(firefox_profile=fp)          
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")  
    yield browser
    browser.quit()