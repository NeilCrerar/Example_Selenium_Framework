"""
Example Selenium Framework
filename: test_results.py
@author: Neil_Crerar

CheckPoint class implementation.  Maintains a list of verification results and 
provides functionality to assert a final result based on whether the list 
contains any failures.

Example:
    self.check_point.mark_final("test name", result, "message")
"""

# Declare imports
import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver


class ResultStatus(SeleniumDriver):
    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        super(ResultStatus, self).__init__(driver)
        self.result_list = []


    def set_result(self, result, result_message):
        """
        Append result of a test to a list and log an appropriate message
        :param result: Result of the verification check
        :param result_message: Description of the verification performed
        """
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info("Test verification successful :: " + 
                                  result_message)
                else:
                    self.result_list.append("FAIL")
                    self.log.error("!! Test verification failed :: " + 
                                   result_message)
                    self.take_screenshot(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.error("!! Test verification failed :: " + 
                               result_message)
                self.take_screenshot(result_message)
        except:
            self.result_list.append("FAIL")
            self.log.error("!! Test verification failed")
            self.take_screenshot(result_message)


    def mark(self, result, result_message):
        """
        Called from verification point in a test case to add result to tracking 
        list for that test.
        :param result: Result of the verification check
        :param result_message: Description of the verification performed
        """        
        self.set_result(result, result_message)


    def mark_final(self, test_name, result, result_message):
        """
        Called for final verification point in a test.  Takes the last result 
        and generates final result based on whether the list contains any 
        failures.  Needs to be called at least once per test as the final test 
        status.
        :param test_name: Name of the test being executed
        :param result: Result of the verification check
        :param result_message: Description of the verification performed
        """
        self.set_result(result, result_message)

        if "FAIL" in self.result_list:
            self.log.error("##### TEST FAILED :: " + test_name + " #####")
            self.result_list.clear()
            assert True == False
        else:
            self.log.info("##### TEST SUCCESSFUL :: " + test_name + "#####")
            self.result_list.clear()
            assert True == True        

