#!/usr/bin/python
# -*- coding: utf-8- -*-

import flask
import os
import requests
import json
from random import randrange
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        url = "https://api.cdiscount.com/OpenApi/json/Search"
        params = {
            "ApiKey": "38e82e08-ec23-4b46-ac36-3e3f903a264d",
            "SearchRequest": {
                "Keyword": "tv",
                "Pagination": {
                    "ItemsPerPage": 5,
                    "PageNumber": 5
                },
                "Filters": {
                    "Price": {
                        "Min": 0,
                        "Max": 0
                    },
                    "Navigation": "",
                    "IncludeMarketPlace": "false",
                    "Condition": None
                }
            }
        }

        response = requests.post(url, data=json.dumps(params))
        pr = json.loads(response.text)
        objet = pr['Products'][randrange(0, len(pr['Products']))]
        image = objet['MainImageUrl']
        price = round(float(objet['BestOffer']['SalePrice']), 2)
        name = objet['Name']
        print(image, price, name)

    if request.method == 'POST':
        price = price
        name = name
        image = image
        essaye = request.form['prix']
        print(essaye)
        if essaye < price:
            data
            resultat = "C'est plus ! essaye encore"
        elif essaye > price:
            resultat = "C'est moins ! essaye encore"
        elif essaye == price:
            resultat = "Bravo"
        return render_template('home.html', resultat=resultat, price=price, name=name, image=image, lastTry=essaye)
    else:
        return render_template('home.html', resultat="", price=price, name=name, image=image, lastTry="")

if __name__ == '__main__':
    app.run(debug= True)




