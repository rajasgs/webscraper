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

Pending:
    "Insole Material": 
    "Features": 
    "Upper Shoe Material": 
    "Sole Material": 
    "Heel": 
    "Shoe Width": 
    "Footwear outsole details":

Testing URLs:
    https://www.target.com/p/women-s-neida-eva-two-band-slide-sandals-shade-shore/-/A-80776263

'''

# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import requests
# from bs4 import BeautifulSoup
from env_reader import DRIVER_PATH, PAGE
import os
from typing import AnyStr
import json
# from selenium.webdriver.chrome.options import Options
option = webdriver.ChromeOptions()

option.headless = True
option.add_argument('window-size=1400,600')
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)


def get_currency(driver):

    return "USD"

def get_title(driver):

    # Get element with tag name 'h1'
    element = driver.find_element(By.TAG_NAME, 'h1')

    # Get all the elements available with tag name 'span'
    spans = element.find_elements(By.TAG_NAME, 'span')
    for span in spans:
        return span.text

def get_size(driver):

    size_divs = driver.find_elements_by_css_selector('div[data-test=VariationSelector]')
    size_div = size_divs[1]

    divs = size_div.find_elements_by_css_selector('div')[1].find_elements_by_css_selector('div')
    
    for div in divs:
        # button = div.find_element(By.TAG_NAME, 'button')
        # print(button.text)
        print(div.text)

    # print(description)

    return None

def get_price(driver):

    price_element = driver.find_element_by_css_selector('div[data-test="product-price"]')
    price = price_element.text
    # print(price)

    return price

def get_description(driver):

    description_elements = driver.find_elements_by_css_selector('div#product-details-tabs div.h-margin-v-default')
    description = description_elements[1].text
    # print(description)

    return description

def get_specs(driver):

    # Get the button and click to show more
    button = driver.find_element_by_css_selector('div#tabContent-tab-Details div button')
    button.click()

    specs = driver.find_element_by_css_selector('div#specAndDescript div:nth-child(1) div')
    specs =  specs.text.split('\n')
    specs = [spec for spec in specs if spec != 'Specifications']

    final_dict = {}

    for spec in specs:
        current_list    = spec.split(':')
        key             = current_list[0]
        value           = current_list[1]

        final_dict[key] = value

    return final_dict


def get_single_page(page: AnyStr):

    driver  = webdriver.Chrome(DRIVER_PATH, options= option)

    driver.maximize_window()
    driver.get(page)

    data                = get_specs(driver)
    data['price']       = get_price(driver)
    data['description'] = get_description(driver)
    data['currency']    = get_currency(driver)
    data['title']       = get_title(driver)

    # print(data)

    print(json.dumps(data, indent = 4))

    driver.quit()

    return data

def startpy():

    page            = os.environ.get('PAGE')
    get_single_page(page)
    
if __name__ == '__main__':
    startpy()