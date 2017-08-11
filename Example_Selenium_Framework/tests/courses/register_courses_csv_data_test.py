"""
Example Selenium Framework
filename: register_courses_csv_data_test.py
@author: Neil_Crerar

Demonstrates importing a CSV data file to use to drive a single test multiple
times with different data.  Sleeps added as some timing issues in I.Explorer 
and especially in Chrome where test quicker than browser.
"""

# Declare imports
import os
import unittest
import pytest
import time
from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.test_results import ResultStatus
from utilities.read_data import get_csv_data
from ddt import ddt, data, unpack 

@pytest.mark.usefixtures("one_time_setup", "setup")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):
    test_data = os.path.join("..", "register_course_data.csv")


    @pytest.fixture(autouse=True)
    def object_setup(self, one_time_setup):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = ResultStatus(self.driver)
        self.nav = NavigationPage(self.driver)


    # Method name must be specified in camel case in order to work 
    def setUp(self):
        self.nav.navigate_to_website_logo()
        time.sleep(3)     
        self.nav.navigate_to_all_courses()
        time.sleep(2)  

    
    # Enrolment failure - credit card number incorrect
    @pytest.mark.run(order=1)
    @data(*get_csv_data(test_data))
    @unpack  
    def test_enrol_failed(self, course_name, cc_num, cc_exp, cc_cvc, 
                          cc_country, country_type):
        """
        Test failure for incorrect card number when enter payment details for 
        enrolling on a course and the credit card fails validation.  Is only
        applicable to paid-for courses.
        """ 
        self.courses.enter_course_name(course_name)
        self.courses.select_course_to_enroll(course_name)
        self.courses.enroll_course(num=cc_num,
                                   exp=cc_exp,
                                   cvc=cc_cvc,
                                   country=cc_country,
                                   data_type=country_type)
        result1, result2 = self.courses.verify_card_check_failed(
            "The card number is incorrect.") 
        self.ts.mark(result1, "Card validation failure message is present")
        self.ts.mark_final("test_enroll_failed", 
                           result2, 
                           "Card validation failure message displayed")

