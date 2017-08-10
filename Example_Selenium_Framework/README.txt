------------------------------------------------------------------------------
    EXAMPLE SELENIUM FRAMEWORK
------------------------------------------------------------------------------

This is a Selenium test automation framework written with the Python 
programming language.  It demonstrates an implementation of the Page Object 
Model approach.  It was produced as an output from an online training course in
Selenium with Python available on Udemy:
https://www.udemy.com/selenium-webdriver-with-python3/learn/v4/overview

THe framework currently utilises the 'practise' webpages provided by the course
instructor at: https://letskodeit.teachable.com/

The current version of the framework is closely aligned with the course but has
been modified by myself and will continue to be updated and transition away 
from the training course version as it is improved and enhanced as my learning 
and understanding in Selenium and Python continues.


------------------------------------------------------------------------------
    SOFTWARE VERSIONS
------------------------------------------------------------------------------

The framework has been created using the following software versions and 
modules:
  - Python 3.6.0
  - Selenium 3.4.1
  - pytest
  - pytest-html
  - ddt


------------------------------------------------------------------------------
    FRAMEWORK STRUCTURE
------------------------------------------------------------------------------

The framework consists of the following structure:

Project
  |
  |--> base
  |
  |--> configfiles
  |
  |--> logs
  |
  |--> pages 
  |      |
  |      |--> sub-directory per test area
  |             |
  |             |--> page files
  |
  |--> screenshots
  |
  |--> tests
  |      |
  |      |--> sub-directory per test area
  |      |      |
  |      |      |--> test files     
  |      |
  |      conftest.py
  |      test suite definition files
  |
  |--> utilities
  |
  README.txt
  TO_DO.txt
  
------------------------------------------------------------------------------
------------------------------------------------------------------------------
 
 