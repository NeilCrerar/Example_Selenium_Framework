"""
Example Selenium Framework
filename: custom_logger
@author: Neil_Crerar

Demonstrates a generic logging method that can be used from within other
classes or methods to log messages to file.

NOTE: I've put this in the 'utilities' directory with the other generic 
functions created during the course rather than leaving it in the chapter 
directory as shown in the lecture.

TODO: See if can extend this to read the logger configuration from file.
"""

# Declare imports
import inspect
import logging
import logging.config
import os


def custom_logger(log_level=logging.DEBUG):
    """
    Creates a log file using the calling method/call name for the file name
    :param log_level: Logging level to be applied with default of debug
    :returns: logger object
    """
    
    # Set log file directory location
    #log_location = os.path.join("..", "..", "logs")
    # if running test suite use......
    log_location = "C:\\Users\\user\\workspace00\\Example_Selenium_Framework\\logs\\"
    # Gets the name of the class/method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    # By default, log all messages unless superseded
    logger.setLevel(logging.DEBUG)
    # Define file handler
    file_handler = logging.FileHandler(os.path.join(log_location, 
                                                    "test_framework.log"), 
                                       mode='a')
        # Set logging level to level passed in
    file_handler.setLevel(log_level)
    # Set message logging format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

