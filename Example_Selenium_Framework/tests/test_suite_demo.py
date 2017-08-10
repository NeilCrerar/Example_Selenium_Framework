"""
Example Selenium Framework
filename: test_suite_demop.py
@author: Neil_Crerar
"""

# Declare imports
import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_multiple_data_test import RegisterCoursesMultiDataTests
from tests.courses.register_courses_csv_data_test import RegisterCoursesCSVDataTests

##############################################################################
#    GET TESTS TO BE ICLUDED                                                 #
##############################################################################

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesMultiDataTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)


##############################################################################
#    TEST SUITE DEFINITION                                                   #
##############################################################################

smoke_test = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smoke_test)

