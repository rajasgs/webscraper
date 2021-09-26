'''
Created on 

Course work: 

@author: Raja CSP Raman

Source:
    
'''

# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

PATH    = "/Users/str-kwml0011/.chromedriver/chromedriver"
driver  = webdriver.Chrome(PATH)


def get_info():

    driver.get("https://www.asc-csa.gc.ca/eng/astronauts/space-medicine/projects.asp")

    # gets first element from the given tag
    heading = driver.find_element_by_class_name("panel-title")
    print(heading.text)

    driver.quit()


def startpy():

    get_info()
    
if __name__ == '__main__':
    startpy()