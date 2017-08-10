"""""
Example Selenium Framework
filename: util.py
@author: Neil_Crerar

Util class implementation
All most commonly used utilities should be implemented in this class
Example: name = self.util.get_unique_name()
"""


# Declare imports
import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging

class Util(object):
    log = cl.custom_logger(logging.INFO)


    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        :param sec:
        :param info:
        """
        if info is not None:
            self.log.info("Wait :: " + str(sec) + " seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()


    def get_alpha_numeric(self, length, char_type="letters"):
        """
        Get random string of characters
        Provide lower/upper/digits for different types
        :param length: Length of string, number of characters string should have
        :param char_type: Type of characters string should have. Default is letters
        :returns: a generated character string of the requested character type(s)
        """
        alpha_num = ""
        if char_type == "lower":
            case = string.ascii_lowercase
        elif char_type == "upper":
            case = string.ascii_uppercase
        elif char_type == "digits":
            case = string.digits
        elif char_type == "mix":
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))


    def get_unique_name(self, char_count=10):
        """
        Get a unique name of a specified number of characters
        :param char_count: number of characters required for the name 
        :returns: a generated character string of the specified length
        """
        return self.get_alpha_numeric(char_count, "lower")


    def get_unique_name_list(self, list_size=5, item_length=None):
        """
        Get a list of valid names
        :param list_size: Number of names. Default is 5 names in a list
        :param item_length: It should be a list containing number of items equal
                to the list_size.  This determines the length of the each item 
                in the list. E.g. [1, 2, 3, 4, 5]
        :returns: a generated list of character strings of the specified lengths
        """
        name_list = []
        for i in range(0, list_size):
            name_list.append(self.get_unique_name(item_length[i]))
        return name_list


    def verify_text_contains(self, actual_text, expected_text):
        """
        Verify actual text contains expected text string
        :param expected_list: Expected Text
        :param actual_list: Actual Text
        """
        self.log.debug("Actual Text From Application Web UI :: " + actual_text)
        self.log.debug("Expected Text From Application Web UI :: " + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info("Text contains verification successful")
            return True
        else:
            self.log.error("!! Text contains verification failed")
            return False


    def verify_text_match(self, actual_text, expected_text):
        """
        Verify text match
        :param expected_list: Expected Text
        :param actual_list: Actual Text
        """
        self.log.debug("Actual Text From Application Web UI :: " + actual_text)
        self.log.debug("Expected Text From Application Web UI :: " + expected_text)
        if actual_text.lower() == expected_text.lower():
            self.log.info("Text match verification successful")
            return True
        else:
            self.log.error("!! Text match verification failed")
            return False


    def verify_list_contains(self, expected_list, actual_list):
        """
        Verify actual list contains elements of expected list
        :param expected_list: Expected List
        :param actual_list: Actual List
        """
        length = len(expected_list)
        for i in range(0, length):
            if expected_list[i] not in actual_list:
                self.log.info("!! List contains items verification failed")
                return False
        else:
            self.log.error("List contains items verification successful")
            return True
        
        
        
    def verify_list_match(self, expected_list, actual_list):
        """
        Verify two list matches
        :param expected_list: Expected List
        :param actual_list: Actual List
        """
        if set(expected_list) == set(actual_list):
            self.log.info("List equivalence verification successful")
            return True
        else:
            self.log.error("!! List equivalence verification failed")
            return False   
    
