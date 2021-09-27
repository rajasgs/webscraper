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
from typing import AnyStr
import time
from target_info_collector import TargetInfoCollector
import json
import csv
import os

# from env_reader import PAGE
from driver_options import driver

def get_links(page: AnyStr):

    driver.maximize_window()
    driver.get(page)

    # product-list-container

    wait = WebDriverWait(driver, 40)
    # element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))

    driver.execute_script("window.scrollTo(0,1200);")

    time.sleep(10)

    elems = driver.find_elements_by_css_selector('div[data-test="product-grid"]')

    # print(elem.get_attribute('innerHTML'))

    # print(li_elements)

    available_links = []

    for li in elems:
        # print(li.get_attribute('innerHTML'))

        anchors = driver.find_elements_by_css_selector('a')

        for a in anchors:
            link = a.get_attribute("href")

            if(not link):
                continue

            if(link.startswith( "https://www.target.com/p/" )):
                print(link)

                link = link.split('?')[0]

                available_links.append(link)

    # driver.quit()

    return available_links


def startpy():

    page = "https://www.target.com/c/fall-outfits/-/N-aa4n4Z88sn6Z7hfymZvobmxZg02vbZ1idnuZ7u8lwZ51incZhf43iZjasm7Zvnk9qZlxvhqZal25lfpwxyz?type=products"

    links = get_links(page)

    t_info_collctor = TargetInfoCollector()

    for link in links:

        data            = t_info_collctor.get_single_page(driver, link)
        print(json.dumps(data, indent = 4))

        print('-' * 100)

    # driver.quit()
    
if __name__ == '__main__':
    startpy()