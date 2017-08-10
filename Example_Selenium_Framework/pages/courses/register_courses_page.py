"""
Example Selenium Framework
filename: register_courses_page.py
@author: Neil_Crerar

Page Object Model for Registering for a Course on the Let's Kode It practice 
website. 
"""

# Declare imports
import time
import logging
import utilities.custom_logger as cl
from base.base_page import BasePage


class RegisterCoursesPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    ###########################################################################
    #    SET PAGE VARIABLES AND ELEMENT LOCATORS                              #
    ###########################################################################
    _title = "Let's Kode It"
    _search_box = "search-courses"  # id
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"  # xpath
    _all_courses = "course-listing-title"  # class
    _enroll_button = "enroll-button-top"  # id 
    _ccard_num = "cc_field"  # id
    _ccard_exp = "cc-exp"  # id
    _ccard_cvc = "cc_cvc"  # id
    _ccard_country = ".//select[contains(@id,'country-select-inside') and (@name='country')]"  # xpath     
    _check_card = "verify_cc_btn"  # id
    _enroll_error_message = ".//div[contains(@class,'payment-errors') and contains(text(),'{0}')]"  # xpath

    
    ###########################################################################
    #    DEFINE WEBPAGE ACTIONS                                               #
    ###########################################################################
    
    # Clear' used so tests can re-set themselves if earlier one fails
    def enter_course_name(self, name):
        """
        Enters provided text into the course search field
        :param name: Text to use for the course search
        """
        self.wait_for_element_clickable(self._search_box, 
                                                  locator_type="id", 
                                                  timeout=10)
        self.clear_field(self._search_box)
        self.sendKeys(name, self._search_box)
    

    def select_course_to_enroll(self, full_course_name):
        """
        Selects an entry from course list using full course name
        :param full_course_name: Value to use to select course entry
        """
        self.wait_for_element_clickable(self._course.format(full_course_name), 
                              locator_type="xpath", 
                              timeout=10)
        
        self.element_click(self._course.format(full_course_name), 
                           locator_type="xpath")

        
    def click_enroll_button(self):
        """
        Clicks on button to trigger enrolment on displayed course
        """
        self.wait_for_element_clickable(self._enroll_button, 
                              locator_type="id", 
                              timeout=10)
        self.element_click(self._enroll_button)

        
    def enter_card_number(self, number):
        """
        Enters provided value into Credit Card Number field for card details
        :param number: Value to enter into the field
        """
        self.sendKeys(number, self._ccard_num)

        
    def enter_card_expiry(self, expiry):
        """
        Enters provided value into Credit Card Expiry field for card details
        :param expiry: Value to enter into the field
        """
        self.sendKeys(expiry, self._ccard_exp)

        
    def enter_card_cvc(self, cvc):
        """
        Enters provided value into Credit Card Security field for card details
        :param cvc: Value to enter into the field
        """
        self.sendKeys(cvc, self._ccard_cvc)
    

    def enter_country(self, country, data_type):
        """
        Select provided value from Country dropdown for credit card details
        :param country: Value to use to select from dropdown
        :param data_type: Data type for the value provided
        """
        self.select_dropdown_entry(self._ccard_country,
                                   locator_type="xpath",
                                   data=country,
                                   data_type=data_type)


    def verify_card(self):
        """
        Clicks button to trigger validation of entered credit card details
        """
        self.element_click(self._check_card)    
       
        
    ###########################################################################
    #    ACTION CHAINS/WORKFLOWS                                              #
    ###########################################################################

    def enter_credit_card_info(self, num, exp, cvc, country, data_type):
        """
        Workflow for entering credit card information to pay for a course as 
        part of the enrolment process.
        :param num: Value to use for credit card number (12 digits)
        :param exp: Value to use for credit card expiry date (6 digits MMYYYY)
        :param cvc: Value to use for credit card security number (3 digits)
        :param country: Value to use for credit card country (droplist)
        :param data_type: Data type for the credit card country
        """
        self.enter_card_number(num)
        self.enter_card_expiry(exp)
        self.enter_card_cvc(cvc)
        self.enter_country(country, data_type)
        self.log.info("Credit Card details entered.")
        
          
    
    def enroll_course(self, num="", exp="", cvc="", country="", data_type=""):
        """
        Workflow for enrolling and paying for course once it's been selected
        :param num: Value to use for credit card number (12 digits)
        :param exp: Value to use for credit card expiry date (6 digits MMYYYY)
        :param cvc: Value to use for credit card security number (3 digits)
        :param country: Value to use for credit card country (droplist)
        :param data_type: Data type for the credit card country
        """
        self.click_enroll_button()
        self.scrolling(direction="down")
        self.enter_credit_card_info(num, exp, cvc, country, data_type)
        time.sleep(2)
        self.verify_card()
        self.log.info("Course enrolment workflow completed.")


    ###########################################################################
    #    VALIDATION METHODS                                                   #
    ###########################################################################

    def verify_title(self, _title):
        """
        Verify webpage title is correctly displayed
        :param _title: Expected page title
        :returns: Boolean
        """
        return self.verify_page_title(_title)       


    def verify_failure_msg_present(self, expected_error):
        """
        Verify card validation failure message exists in the DOM.
        :param Expected_error: error message expect to be displayed
        :returns: Boolean
        """          
        return self.is_element_present(
            self._enroll_error_message.format(expected_error), 
            locator_type="xpath")


    def verify_failure_msg_displayed(self, expected_error):
        """
        Verify card validation failure message displayed on webpage.
        :param Expected_error: error message expect to be displayed
        :returns: Boolean
        """    
        fail_message = self.wait_for_element(
            self._enroll_error_message.format(expected_error), 
            locator_type="xpath",
            timeout=20)       
        result = self.is_element_displayed(element=fail_message)       
        return result

        
    def verify_card_check_failed(self, expected_error):
        """
        Verify if error message is present, displayed and correct.  Returns a 
        result for each check individually.
        :param Expected_error: error message expect to be displayed
        :returns: Boolean for each of the checks
        """      
        result1 = self.verify_failure_msg_present(expected_error)
        result2 = self.verify_failure_msg_displayed(expected_error)   
        return result1, result2
    
    