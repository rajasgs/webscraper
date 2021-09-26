'''
Created on 

Course work: 

@author: Raja CSP Raman

Source:
    
Things to get:
    "url": "https://www.target.com/p/toddler-girls-shanel-fisherman-sandals-cat-jack/-/A-81204099?preselect=80859208",
    "tcin": "80859208",
    "upc": "0829576374731",
    "price": 16.99,
    "currency": "USD",
    "title": "Toddler Girls' Shanel Fisherman Sandals - Cat & Jack™",
    "description": "She'll be ready for fun in the sun whenever she sports the Shanel Fisherman Sandals from Cat & Jack™. These strappy sandals feature an open design to keep her feet cool and comfy on warm, sunny days, and they're easy to dress up or down thanks to the classic straps of the fisherman-style design. A back sling strap helps provide a firm fit that stays put on her feet as she moves, while the buckle accent conceals a hook-and-loop fastener that makes for adjustable wear as well as making on and off easy.",
    "Sizing": "Toddler",
    "Care and Cleaning": "Care Instructions Not Provided",
    "Lining Material": "Man Made Materials",
    "Insole Material": "Man Made Materials",
    "Features": "Quarter Strap, Hook and Loop Closure, Open Toe",
    "Upper Shoe Material": "100% Plastic",
    "Sole Material": "100% TPR (Thermoplastic Rubber)",
    "Heel": "Approximately 0.5 Inches No Heel",
    "Shoe Width": "Medium",
    "Footwear outsole details": "Non Marking Outsole"

'''

# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

PATH    = "/Users/str-kwml0011/.chromedriver/chromedriver"
driver  = webdriver.Chrome(PATH)

PAGE = "https://www.target.com/p/women-s-neida-eva-two-band-slide-sandals-shade-shore/-/A-80776263"

def get_currency(price):

    return None

def get_title(driver):

    # Get element with tag name 'h1'
    element = driver.find_element(By.TAG_NAME, 'h1')

    # Get all the elements available with tag name 'span'
    spans = element.find_elements(By.TAG_NAME, 'span')
    for span in spans:
        return span.text


def get_info():

    driver.get(PAGE)

    title = get_title(driver)
    print(title)

    # driver.find_element_by_xpath('//input[@node-type="searchInput"]')
    price_element = driver.find_element_by_css_selector('div[data-test="product-price"]')
    price = price_element.text
    print(price)

    driver.quit()


def startpy():

    get_info()
    
if __name__ == '__main__':
    startpy()