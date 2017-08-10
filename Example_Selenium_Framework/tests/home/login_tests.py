"""
Example Selenium Framework
filename: login_tests.py
@author: Neil_Crerar
"""

# Declare imports
import unittest
import pytest
from pages.home.login_page import LoginPage
from utilities.test_results import ResultStatus 

@pytest.mark.usefixtures("one_time_setup", "setup")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.lp = LoginPage(self.driver)
        self.ts = ResultStatus(self.driver)
    
    
    # Log on successfully with valid credentials (test user account)
    @pytest.mark.run(order=2)
    def test_valid_login(self):
        
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verify_title()
        self.ts.mark(result1, "Webpage title check")
        result2 = self.lp.verify_login_success()
        self.ts.mark_final("test_valid_login", 
                           result2, 
                           "Login success icon check")        
    
    
    # Log on failure for empty password handled correctly
    @pytest.mark.run(order=1)        
    def test_invalid_login(self):
        self.lp.logout()
        self.lp.login("test@email.com", "")
        result = self.lp.verify_login_failed()
        self.ts.mark_final("test_invalid_login", 
                           result, 
                           "Login failure message displayed")
    
    
    