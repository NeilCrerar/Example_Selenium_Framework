"""
Example Selenium Framework
filename: base\webdriverfactory.py
@author: Neil_Crerar

WebDriver Factory class implementation.  Creates a webdriver instance based on 
browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

# Declare imports
import os
from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        """
        Initialises the WebDriverFactory class
        :param browser: browser application name (text)
        """
        self.browser = browser.lower()

        
    def get_webdriver_instance(self):
        """
        Get WebDriver instance based on the browser configuration.  Will return
        Firefox if none specified.
        :returns: Configured WebDriver instance
        """
        base_url = "https://letskodeit.teachable.com/"
        
        if self.browser == "firefox":
            driver = webdriver.Firefox()        
        elif self.browser == "iexplorer":
            # Set location and environment for IE
            driver_location = "C:\\Users\\user\\Selenium_Drivers\\IEDriverServer\\IEDriverServer.exe"
            os.environ["webdriver.ie.driver"] = driver_location
            driver = webdriver.Ie(driver_location)  
        elif self.browser == "chrome":
            # Set location and environment from Chrome
            driver_location = "C:\\Users\\user\\Selenium_Drivers\\chromedriver\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = driver_location
            driver = webdriver.Chrome(driver_location)       
            driver.set_window_size(1024, 768)       
        else:
            # If no browser specified, default to Firefox
            driver = webdriver.Firefox()
        
        # Setting driver defaults
        driver.implicitly_wait(10)
        
        """
        Issue with FF means the maximise not working at the moment.  Needs
        next release version 55. If loop below is a temporary workaround - has 
        to do browsers this way around to handle no or an unrecognised browser 
        being used which then defaults to firefox
        """
        if self.browser == "chrome" or self.browser == "iexplorer":
            driver.maximize_window()       
        else:
            driver.set_window_size(1024, 768)
        driver.get(base_url)
        
        return driver
    