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
    "tcin": 
    "upc": 
    "Sizing": 
    "Care and Cleaning": 
    "Lining Material": 
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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import AnyStr

import csv
import os

from env_reader import PAGE
from driver_options import driver

def get_links(page: AnyStr):

    driver.maximize_window()
    driver.get(page)

    # product-list-container

    li_elements = driver.find_element_by_css_selector('div[data-test="product-price"] ul li')

    for li in li_elements:
        print(li)

    pass


def startpy():

    page = "https://www.target.com/c/fall-outfits/-/N-aa4n4Z88sn6Z7hfymZvobmxZg02vbZ1idnuZ7u8lwZ51incZhf43iZjasm7Zvnk9qZlxvhqZal25lfpwxyz?type=products"

    get_links(page)
    
if __name__ == '__main__':
    startpy()