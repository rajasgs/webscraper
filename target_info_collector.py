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
from driver_options import driver, option
import re
import selenium
# from selenium.webdriver.chrome.options import Options


class TargetInfoCollector():

    def __init__(self, **kwargs):
        pass

    def get_title(self, driver):

        # Get element with tag name 'h1'
        element = driver.find_element(By.TAG_NAME, 'h1')

        # Get all the elements available with tag name 'span'
        spans = element.find_elements(By.TAG_NAME, 'span')
        for span in spans:
            return span.text

    def get_size(self, driver):

        size_divs = driver.find_elements_by_css_selector('div[data-test=VariationSelector]')
        size_div = size_divs[1]

        divs = size_div.find_elements_by_css_selector('div')[1].find_elements_by_css_selector('div')
        
        for div in divs:
            # button = div.find_element(By.TAG_NAME, 'button')
            # print(button.text)
            print(div.text)

        # print(description)

        return None

    def get_price(self, driver):

        price_element = driver.find_element_by_css_selector('div[data-test="product-price"]')
        price = price_element.text
        # print(price)

        return price

    # This can be improved by using REGEX
    def get_price_number_and_currency(self, price):

        if('$' in price):
            currency    = "USD"
            price_val = float(re.sub(r'[^0-9.]', '', price))

        return price_val, currency

    def get_description(self, driver):

        description_elements = driver.find_elements_by_css_selector('div#product-details-tabs div.h-margin-v-default')
        description = description_elements[1].text
        # print(description)

        return description

    def get_specs(self, driver):

        try:
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

            spec_dict = {
                "specs" : final_dict
            }
        except selenium.common.exceptions.NoSuchElementException as er:
            print(er)
            return {"specs" : "None"}

        return spec_dict


    def get_single_page(self, driver, page: AnyStr):

        # driver  = webdriver.Chrome(DRIVER_PATH, options= option)

        print(f'Finding page : {page}')

        driver.maximize_window()
        driver.get(page)

        data                = self.get_specs(driver)
        data['price']       = self.get_price(driver)
        data['description'] = self.get_description(driver)
        # data['currency']    = self.get_currency(driver, data['price'])
        
        data['title']       = self.get_title(driver)

        data['price'], data['currency']  = self.get_price_number_and_currency(data['price'])

        # print(data)

        # print(json.dumps(data, indent = 4))

        # driver.quit()

        return data

def startpy():

    page            = os.environ.get('PAGE')

    target_info_collctor = TargetInfoCollector()

    data            = target_info_collctor.get_single_page(driver, page)
    print(json.dumps(data, indent = 4))

    # driver.quit()


    
if __name__ == '__main__':
    startpy()