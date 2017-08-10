"""
Example Selenium Framework
filename: navigation_page.py
@author: Neil_Crerar

Page Object Model for navigating around the Let's Kode It practice website. 
"""

# Declare imports
import utilities.custom_logger as cl
import logging
from base.base_page import BasePage

class NavigationPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ###########################################################################
    #    SET PAGE VARIABLES AND ELEMENT LOCATORS                              #
    ###########################################################################

    _website_logo = "//a[@class='navbar-brand header-logo']/img"  # xpath
    _my_courses = "All Courses"  # linktext
    _all_courses = "My Courses"  # linktext
    _practice = "Practice"  # linktext
    _user_settings = "//div[@id='navbar']//li[@class='dropdown']"  # xpath    
    _user_profile = "//div[@id='navbar']//a[@href='/current_user/profile']"  # xpath
    _user_subs = "//div[@id='navbar']//a[@href='/current_user/subscriptions']"  # xpath
    _user_ccard = "//div[@id='navbar']//a[@href='/current_user/credit_card]"  # xpath
    _user_logout = "//div[@id='navbar']//a[@href='/sign_out']"  # xpath
    

    ###########################################################################
    #    DEFINE WEBPAGE ACTIONS                                               #
    ###########################################################################

    def navigate_to_website_logo(self):
        """
        Clicks on the website logo image in the header navigation bar to 
        go to the default home page for the website
        """        
        self.scrolling("up")
        self.log.info("Navigating to navigation bar :: website logo link")
        self.element_click(locator=self._website_logo, locator_type="xpath")


    def navigate_to_my_courses(self):
        """
        Clicks on the 'my courses' link in the header navigation bar
        """        
        self.log.info("Navigating to navigation bar :: my courses link")
        self.wait_for_element_clickable(self._my_courses,
                                        locator_type="linktext",
                                        timeout=10)
        self.element_click(locator=self._my_courses, locator_type="linktext")

    def navigate_to_all_courses(self):
        """
        Clicks on the 'all courses' link in the header navigation bar
        """        
        self.log.info("Navigating to navigation bar :: all courses link")
        self.wait_for_element_clickable(self._all_courses,
                                        locator_type="linktext",
                                        timeout=10)
        self.element_click(locator=self._all_courses, locator_type="linktext")


    def navigate_to_practice(self):
        """
        Clicks on the 'practice' link in the header navigation bar
        """        
        self.log.info("Navigating to navigation bar :: practice link")
        self.wait_for_element_clickable(self._practice,
                                        locator_type="linktext",
                                        timeout=10)
        self.element_click(locator=self._practice, locator_type="linktext")


    def navigate_to_user_settings(self):
        """
        Clicks on the 'user settings' link in the header navigation bar
        """                
        self.log.info("Navigating to navigation bar :: user settings menu")
        user_settings = self.wait_for_element_clickable(self._user_settings,
                                                        locator_type="xpath",
                                                        timeout=3)
        self.element_click(element=user_settings)
        

    def navigate_to_user_profile(self):
        """
        Clicks on the entry for 'edit profile' in the user settings drop-down 
        menu
        """        
        self.log.info("Navigating to user settings :: profile link")
        self.navigate_to_user_settings()
        profile = self.wait_for_element_clickable(locator=self._user_profile, 
                                                       locator_type="xpath", 
                                                       timeout=3)
        self.element_click(element=profile)


    def navigate_to_user_subscriptions(self):
        """
        Clicks on the entry for 'manage subscriptions' in the user settings 
        drop-down menu
        """
        self.navigate_to_user_settings()
        self.log.info("Navigating to user settings :: subscriptions link")
        subscriptions = self.wait_for_element_clickable(locator=self._user_subs, 
                                                        locator_type="xpath", 
                                                        timeout=3)
        self.element_click(element=subscriptions)


    def navigate_to_user_credit_card(self):
        """
        Clicks on the entry for 'add/change credit card' in the user settings 
        drop-down menu
        """
        self.navigate_to_user_settings()
        self.log.info("Navigating to user settings :: saved card details link")
        credit_card = self.wait_for_element_clickable(locator=self._user_ccard, 
                                                      locator_type="xpath", 
                                                      timeout=3)  
        self.element_click(element=credit_card)


    def navigate_to_user_logout(self):
        """
        Clicks on the entry for 'logout' in the user settings drop-down menu
        """
        self.navigate_to_user_settings()
        self.log.info("Navigating to user settings :: logout link")
        logout = self.wait_for_element_clickable(locator=self._user_logout, 
                                                 locator_type="xpath", 
                                                 timeout=3)
        self.element_click(element=logout)

