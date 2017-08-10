"""
Example Selenium Framework
filename: login_page.py
@author: Neil_Crerar

Page Object Model for logging into the Let's Kode It practice website. 
"""

# Declare imports
import logging
import utilities.custom_logger as cl
from base.base_page import BasePage
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
    
    
    ###########################################################################
    #    SET PAGE VARIABLES AND ELEMENT LOCATORS                              #
    ###########################################################################
    _title = "Let's Kode It"
    _login_link = "Login"  # linktext
    _email_field = "user_email"  # id
    _password_field = "user_password"  # id
    _login_button = "commit"  # name


    ###########################################################################
    #    DEFINE WEBPAGE ACTIONS                                               #
    ###########################################################################

    # Actions for elements
    def click_login_link(self):
        """
        Clicks navigation bar button to login to the website
        """
        self.element_click(self._login_link, locator_type="linktext")

    def enter_email(self, email):
        """
        Enters provided value into email field for logging into website
        :param email: Value to enter into the field
        """
        self.sendKeys(email, self._email_field, locator_type="id")
        
    def enter_password(self, password):
        """
        Enters provided value into password field for logging into website
        :param password: Value to enter into the field
        """
        self.sendKeys(password, self._password_field, locator_type="id")

    def click_login_button(self):
        """
        Clicks button to login to website using provided credentials
        """
        self.element_click(self._login_button, locator_type="name")
        
    def clear_email(self, email):
        """
        Clears contents of the email field when trying to login to website
        """
        self.clear_field(self._email_field, locator_type="id")
        
    def logout(self):
        """
        CLicks on the navigation bar option to logout of the website
        """
        self.nav.navigate_to_user_logout()
                           

    ###########################################################################
    #    ACTION CHAINS/WORKFLOWS                                              #
    ###########################################################################

    # Define login sequence
    def login(self, email, password):
        """
        Workflow for logging into the website via navigation bar option
        :param email: Value to use as the login email
        :param password: Value to use as the login password
        """
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        self.log.info("Login workflow completed.")


    ###########################################################################
    #    VALIDATION METHODS                                                   #
    ###########################################################################
        
    # Check get user icon when login is successful
    def verify_login_success(self):        
        """
        Verify that the 'user' icon displayed for a successful login
        """
        result = self.is_element_present(
            ".//div[@id='navbar']/div/div/div/ul/li[4]/a/img",
            locator_type ="xpath")
        return result

       
    # Check get correct failure message for a login failure
    def verify_login_failed(self):
        """
        Verify error message displayed for failed login
        """
        result = self.is_element_present(
            "//div[contains(text(),'Invalid email or password')]",
            locator_type="xpath")
        return result

    
    # Check retrieved page title matches expected value
    def verify_title(self, _title):
        """
        Verify webpage title is correctly displayed
        :param _title: Expected page title
        :returns: Boolean
        """
        return self.verify_page_title(self._title)        
    
