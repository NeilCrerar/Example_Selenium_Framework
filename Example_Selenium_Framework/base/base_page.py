"""
Example Selenium Framework
filename: base\base_page.py
@author: Neil_Crerar

Implements methods common to pages throughout the framework.  This class needs 
to be inherited by all the page classes.  It should not be used by creating 
object instances.

Example:
    Class LoginPage(BasePage)
"""

# Declare imports
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Initialises the BasePage class
        :param driver: The webdriver instance being used
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()


    def verify_page_title(self, expected_title):
        """
        Verify the retrieved title of a webpage against a given value
        :param expected_title: Title on the page that needs to be verified
        :returns: boolean
        """
        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, expected_title)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

