"""
Example Selenium Framework
filename: register_courses_multiple_data_test.py
@author: Neil_Crerar

Demonstrates using hard-coded data sets to drive a single test multiple times 
using the different data sets
"""

# Declare imports
import unittest
import pytest
import time
from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.test_results import ResultStatus
from ddt import ddt, data, unpack 


@pytest.mark.usefixtures("one_time_setup", "setup")
@ddt
class RegisterCoursesMultiDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = ResultStatus(self.driver)
        self.nav = NavigationPage(self.driver)


    # Method name must be specified in camel case in order to work 
    def setUp(self):
        self.nav.navigate_to_website_logo()
        time.sleep(2)     
        self.nav.navigate_to_all_courses()
        time.sleep(2)        

    
    # Enrolment failure - credit card number incorrect
    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "6414524464145244", "122017", "123", "GB", "value"), 
          ("Learn Python 3 from scratch", "2014574120145741", "012019", "230", "US", "value"))
    @unpack  
    def test_enrol_failed(self, course_name, num, exp, cvc, country, 
                          country_type):
        """
        Test failure for incorrect card number when enter payment details for 
        enrolling on a course and the credit card fails validation
        """
        self.courses.enter_course_name(course_name)
        self.courses.select_course_to_enroll(course_name)
        self.courses.enroll_course(num=num,
                                   exp=exp,
                                   cvc=cvc,
                                   country=country,
                                   data_type=country_type)

        result1, result2 = self.courses.verify_card_check_failed(
            "The card number is incorrect.")
        self.ts.mark(result1, "Card failure message is present")
        self.ts.mark_final("test_enroll_failed", 
                           result2, 
                           "Card failure message displayed")

