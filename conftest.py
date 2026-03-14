import pytest
from utils.driver_factory import get_driver

@pytest.fixture(scope="function")
def driver(request):
    browser = getattr(request, "param", "chrome")
    driver = get_driver(browser)
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
