'''
Created on 

Course work: 

@author: Raja CSP Raman

Source:
    
'''

# Import necessary modules
from flask import Flask, render_template

app = Flask(__name__)

'''
    http://localhost:5000
'''
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)