'''
Created on 

Course work: 

@author: Raja CSP Raman

Source:
    

'''

# Import necessary modules
from app import PAGE
import os
from dotenv import load_dotenv

load_dotenv()


DRIVER_PATH     = os.environ.get('DRIVER_PATH')
PAGE            = os.environ.get('PAGE')
