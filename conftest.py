import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import urls


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--browser")


@pytest.fixture(scope='class')
def setup(request):

    print("setting up")
    driver = webdriver.Chrome(service=Service())
    driver.get(urls.PRODUCTION_URL)
    request.cls.driver = driver
    yield
    print("tearing down")
    driver.quit()


