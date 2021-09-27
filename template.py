'''
Created on 

Course work: 

@author: Raja CSP Raman

Source:
    

'''

# Import necessary modules
import re
import locale

def price_convert(_price):
    return float(re.sub(r'[^0-9.]', '', _price))

def startpy():

    pass
    
if __name__ == '__main__':
    startpy()