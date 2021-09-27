'''
Created on 

Course work: 

@author: Raja CSP Raman

Source:
    
'''

# Import necessary modules
from selenium import webdriver
from env_reader import DRIVER_PATH

option = webdriver.ChromeOptions()

option.headless = True
option.add_argument('window-size=1400,600')
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

driver  = webdriver.Chrome(DRIVER_PATH, options= option)