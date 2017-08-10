"""
Example Selenium Framework
filename: base\selenium_driver.py
@author: Neil_Crerar

Custom WebDriver wrapper providing access to common framework functions
Access should be inherited by all pages via the base_page
"""

# Declare imports
import os
import time
import logging
import utilities.custom_logger as cl
from traceback import print_stack
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class SeleniumDriver():
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        """
        Initialises the SeleniumDriver class
        :param driver: WebDriver to be used by the class
        """        
        self.driver = driver


    ###########################################################################
    #    GET/FIND ELEMENTS                                                    #
    ###########################################################################

    def get_by_type(self, locator_type):
        """
        Translates the locator type from passed in string
        :param locator_type: Type of locator being passed (id, xpath, etc.)
        :returns: Python code to be used for locator_type 
        """
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            self.log.error("Locator type: " + locator_type + 
                          " is not correct/supported")
        return False


    def get_element(self, locator, locator_type="id"):
        """
        Finds elements based on passed in parameters
        :param locator: Unique identifier for the element to be found
        :param locator_type: Type of locator being passed (default "id")
        :returns: Located element
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.debug("Got element by locator: " + locator + 
                          " :: locator_type: " + locator_type)
        except:
            self.log.error("Element not found: " + locator + 
                           " :: locator_type: " + locator_type)
            print_stack()
        return element


    def get_element_list(self, locator, locator_type="id"):
        """
        Get list of elements from a webpage
        :param locator: Unique identifier for the element to be found
        :param locator_type: Type of locator being passed (default "id")
        :returns: Located elements list
        """
        element = None
        try:
            locator_type = locator_type.lower()
            byType = self.get_by_type(locator_type)
            element = self.driver.find_elements(byType, locator)
            self.log.debug("Element list found with locator: " + locator +
                          " :: locator_type: " + locator_type)
        except:
            self.log.error("Element list not found!  Locator: " + locator +
                          " :: locator_type: " + locator_type)
            print_stack()
        return element


    def is_element_present(self, locator="", locator_type="id", element=None):
        """
        Check whether an individual element can be found
        Either provide element or a combination of locator and locator_type
        :param locator: Unique identifier for the element to be found
        :param locator_type: Type of locator being passed (default "id")
        :param element: Element to perform the action against
        :returns: Boolean
        """
        try:
            # if locator passed in, go find the associated element
            if locator: 
                element = self.driver.find_element(locator_type, locator)
            if element is not None:
                self.log.debug("Element is present.  Locator: " + locator + 
                               " :: locator_type: " + locator_type)
                return True
            else:
                self.log.error("Element  not present!  Locator: " + locator + 
                               " :: locator_type: " + locator_type)
                return False
        except:
            self.log.error("Element not present!  Locator: " + locator + 
                               " :: locator_type: " + locator_type)
            print_stack()
            return False
      
        
    def elements_are_present_check(self, locator, locator_type):
        """
        Check whether a list of elements can be found
        :param locator: Unique identifier for the element to be found
        :param locator_type: Type of locator being passed (default "id")
        :returns: Boolean
        """        
        try:
            element_list = self.driver.find_elements(locator_type, locator)
            if len(element_list) > 0:
                self.log.debug("Element presence check passed.  Locator: " + 
                              locator + " :: locator_type: " + locator_type)
                return True
            else:
                self.log.error("Element presence check failed!  Locator: " + 
                              locator + " :: locator_type: " + locator_type)
                return False
        except:
            self.log.error("Element presence check failed!  Locator: " + 
                           locator + " :: locator_type: " + locator_type)
            print_stack()
            return False


    def is_element_displayed(self, locator="", locator_type="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locator_type
        :param locator: Unique identifier for the element to be found
        :param locator_type: Type of locator being passed (default "id")
        :param element: Element to perform the action against
        :returns: Boolean
        """
        is_displayed = False
        try:
            # if locator passed in, go find the associated element
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.debug("Element displayed.  Locator: " + locator +
                              " :: locator_type: " + locator_type)
            else:
                self.log.error("Element not displayed!  Locator: " + locator +
                              " :: locator_type: " + locator_type)
            return is_displayed
        except:
            self.log.error("Element not displayed!  Locator: " + locator +
                              " :: locator_type: " + locator_type)
            print_stack()
            return False
        
        
    def wait_for_element(self, locator, locator_type="id",
                               timeout=10, poll_frequency=0.5):
        """
        Wait for an element to become visible
        :param locator: Unique identifier for the element to be found
        :param locator_type: Type of locator being passed (default "id")
        :param timeout: Period to wait for the element
        :param poll_frequency: Period to check if element visible
        :returns: Located element
        """
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.debug("Waiting max " + str(timeout) + 
                          " seconds for element to be visible. Locator:" + 
                          locator + " :: locator type: " + by_type)
            wait = WebDriverWait(self.driver, 
                                 timeout=timeout, 
                                 poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            self.log.debug("Element visible.  Locator: " + 
                          locator + " :: locator_type: " + by_type)
        except:
            self.log.error("Element not visible!  Locator: " + 
                          locator + " :: locator_type: " + by_type)
            print_stack()
        return element


    def wait_for_element_clickable(self, locator, locator_type="id",
                               timeout=10, poll_frequency=0.5):
        """
        Wait for an element to become clickable
        :param locator: Unique identifier for the element to be found
        :param locator_type: Type of locator being passed (default "id")
        :param timeout: Period to wait for the element
        :param poll_frequency: Period to check if element visible
        :returns: Located element
        """
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.debug("Waiting max " + str(timeout) + 
                          " seconds for element to be clickable.  Locator:" + 
                          locator + " :: locator type: " + by_type)
            wait = WebDriverWait(self.driver, 
                                 timeout=timeout, 
                                 poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.debug("Element clickable.  Locator: " + 
                          locator + " :: locator_type: " + by_type)
        except:
            self.log.error("Element not clickable!  Locator: " + 
                          locator + " :: locator_type: " + by_type)
            print_stack()
        return element


    def select_dropdown_entry(self, locator, locator_type="id", element=None,
                              data="", data_type=""):
        """
        Select an entry from the dropdown element specifying how to select and
        data to use.  Also either provide element or a combination of locator 
        and locator_type.
        :param locator: Unique identifier for the element to be found
        :param locator_type: Type of locator being passed (default "id")
        :param element: Element to perform the action against
        :param data: Data to use to identify the dropdown entry
        :param data_type: Data type of the dropdown entry (value, index, text)
        """
        try:
            # if locator passed in, go find the associated element
            if locator:
                element = self.get_element(locator, locator_type)
            sel = Select(element)

            if data_type == "value":
                sel.select_by_value(data)     
                self.log.debug("Selected drop-down data: " + data + 
                              " :: locator:" + locator)   
            elif data_type == "index":
                sel.select_by_index(data)          
            elif data_type == "text":
                sel.select_by_visible_text(data)
            else:
                self.log.error("Could not select data: " + data + 
                               " :: locator: " + locator)
        except:
            self.log.error("Could not select drop-down data: " + data + 
                           " :: locator: " + locator + " :: as type: " + 
                           data_type)
            print_stack()
            
            
    ###########################################################################
    #    ELEMENT ACTIONS                                                      #
    ###########################################################################  
    
    def element_click(self, locator="", locator_type="id", element=None):
        """
        Execute click action against specified element
        Either provide element or a combination of locator and locator_type
        :param locator: Unique identifier for the element to be found
        :param locator_type: Type of locator being passed (default "id")
        :param element: Element to perform the action against
        """
        try:
            # if locator passed in, go find the associated element
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.debug("Clicked on element.  Locator: " + locator + 
                          " :: locator_type: " + locator_type)
        except:
            self.log.error("Cannot click on element.  Locator: " + 
                          locator + " :: locator_type: " + locator_type)
            print_stack()


    def sendKeys(self, data, locator="", locator_type="id", element=None):
        """
        Submit data entry against specified element.  
        Either provide element or a combination of locator and locator_type
        Name format used to prevent clash with built-in method "send_keys()".  
        Artificial delay added to data entry as a workaround for some issues 
        with Firefox and data overwriting itself. 
        :param data: Data to be sent to the element
        :param locator: Unique identifier for the element to be found
        :param locator_type: Type of locator being passed (default "id")
        :param element: Element to perform the action against
        """
        try:
            # if locator passed in, go find the associated element
            if locator:
                element = self.get_element(locator, locator_type)
            for character in data:
                element.send_keys(character)
                #time.sleep(0.1)
            self.log.debug("Sent data on element.  Locator: " + locator + 
                          " :: locator_type: " + locator_type + " :: data:" +
                          data)
        except:
            self.log.error("Cannot send data on element!  Locator: " + 
                          locator + " :: locator_type: " + locator_type + 
                          " :: data:" + data)
            print_stack()

            
    def clear_field(self, locator, locator_type="id", element=None):
        """
        Remove any pre-existing entry for specified element
        :param locator: Unique identifier for the element to be found
        :param locator_type: Type of locator being passed (default "id")
        """
        try:
            # if locator passed in, go find the associated element
            if locator:
                element = self.get_element(locator, locator_type)
            element.clear()
            self.log.debug("Cleared element.  Locator: " + locator + 
                          " :: locator_type: " + locator_type)
        except:
            self.log.error("Cannot clear element.  Locator: " + locator + 
                          " :: locator_type: " + locator_type)
            print_stack()


    def get_text(self, locator="", locator_type="id", element=None, info=""):
        """
        Get the 'Text' displayed for an element
        Either provide element or a combination of locator and locator_type
        :param locator: Unique identifier for the element to be found
        :param locator_type: Type of locator being passed (default "id")
        :param element: Element to perform the action against
        :param info: Message to be included in the logs        
        """
        try:
            # if locator passed in, go find the associated element
            if locator:
                element = self.get_element(locator, locator_type)
            text = element.text
            self.log.debug("Found element size: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.debug("Getting text on element: " + info)
                self.log.debug("The text is: " + text)
                text = text.strip()
        except:
            self.log.error("Failed to get text on element: " + info)
            print_stack()
            text = None
        return text
        
        
    def get_title(self):
        """
        Get the title for current or specified webpage
        :returns: Title retrieved for the webpage
        """
        return self.driver.title 
               
    
    ###########################################################################
    #    OTHER ACTIONS                                                        #
    ###########################################################################
    
    def take_screenshot(self, result_message):
        """
        Takes screenshot of the current open web page
        :param result_message: Message from the test to create filename 
        """
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, 
                                             screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)         
            self.log.info("Screenshot saved to directory: " + destination_file)            
        except:
            self.log.error("Exception occurred when taking screenshot")
            print_stack()
            
            
    def scrolling(self, direction="up"):
        """
        Scroll the display in the browser window
        :param direction: Direction in which to scroll the webpage 
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")
            self.log.info("Scrolled up on the page")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")
            self.log.info("Scrolled down on the page")
