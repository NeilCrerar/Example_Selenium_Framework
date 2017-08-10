"""
Example Selenium Framework
filename: read_data
@author: Neil_Crerar

Utility method to read data from CSV file into a list
"""

# Declare imports
import csv
import utilities.custom_logger as cl
import logging

def get_csv_data(file_name):
    """
    Read in data from CSV file. Excludes first line as expecting file headers
    :param file_name: Name of CSV file to read from
    :returns: List of line content from the file 
    """
    
    log = cl.custom_logger(logging.DEBUG)  
    # List to store rows and row counter
    rows = []
    counter = 0
    # Open the CSV file
    data_file = open(file_name, "r")
    log.info("Opening CSV file to read: " + file_name)
    # Create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    # Skip the headers
    next(reader)
    # Add rows from reader to list
    for row in reader:
        rows.append(row)
        counter +=1
    log.debug("Total of " + str(counter) + " rows read from file.")
    return rows