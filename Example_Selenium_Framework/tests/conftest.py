"""
Example Selenium Framework
filename: conftest.py
@author: Neil_Crerar
"""

# Declare imports
import time
import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage
import logging
import utilities.custom_logger as cl


log = cl.custom_logger(logging.DEBUG)

@pytest.yield_fixture()
def setup():
    log.debug("Running method level setup")
    yield
    log.debug("Running method level tear down")


@pytest.yield_fixture(scope="class")
def one_time_setup(request, browser):
    log.debug("Running one time setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()
    lp = LoginPage(driver)
    # Test login details shared so sometimes gets altered by others and not
    # always react as expected
    lp.login("test@email.com", "abcabc")
    
    # Delay put in here as some oddities with IE where login works but doesn't 
    # seem to hold as get silently kicked out when select next action
    time.sleep(3) 

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    log.debug("Running one time tear down")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")

