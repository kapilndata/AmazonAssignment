import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.mark.usefixtures('setup')
class BaseClass:
    driver: WebDriver
    pass

