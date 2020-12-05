#By: Universal Impact
#https://github.com/universalimpact

#Importing flask and newsapi
from flask import Flask,render_template,request
import requests

app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html', news={})
     
@app.route('/info/',methods=['POST']) 
def displayinfo():
    stock = request.form['stock']
    # print(stock)
    arr = stock.split(" ")
    stockdict = {}
    for x in arr:
        response = requests.get('https://api.polygon.io/v1/meta/symbols/'+x+'/company?apiKey=ChwNR2KpdodhMd4R3TYgI256brfKZ7_7')
        stockdict[x] = response.json()
    # print(stockdict)
    #Send the articles to the html file to display in a user-friendly format
    return render_template('index.html',news=stockdict)