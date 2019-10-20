# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:46:38 2019

@author: Hamza
"""

# we import the class that we need scraping our blog

import requests
from bs4 import BeautifulSoup
from csv import writer


berk = requests.get('https://umassdining.com/locations-menus/berkshire/menu')
hamp = requests.get('https://umassdining.com/locations-menus/hampshire/menu')
frank = requests.get('https://umassdining.com/locations-menus/franklin/menu')
woo = requests.get('https://umassdining.com/locations-menus/worcester/menu')

#initialize Beautifulsoup to parse information from the DC websites

berksoup = BeautifulSoup(berk.text, 'html.parser')
hampsoup = BeautifulSoup(hamp.text, 'html.parser')
franksoup = BeautifulSoup(frank.text, 'html.parser')
woosoup = BeautifulSoup(woo.text, 'html.parser')

# lightbox-nutrition is the class name for all the food items on the DC website

berkfood = berksoup.findAll(class_='lightbox-nutrition')
hampfood = hampsoup.findAll(class_='lightbox-nutrition')
frankfood = franksoup.findAll(class_='lightbox-nutrition')
woofood = woosoup.findAll(class_='lightbox-nutrition')


#write to a csv file that can later be analyzed

with open('foodList.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    
    headers = ['Dining Common', 'Food', 'Calories', 'Ingredients']
    
    csv_writer.writerow(headers)
    
    for food in berkfood:
        name = food.contents[0].contents
        cal = food.contents[0].get('data-calories')
        ingredients = food.contents[0].get('data-ingredient-list')
        csv_writer.writerow(['Berkshire DC', name, cal, ingredients])
        
    for food in hampfood:
        name = food.contents[0].contents
        cal = food.contents[0].get('data-calories')
        ingredients = food.contents[0].get('data-ingredient-list')
        csv_writer.writerow(['Hampshire DC', name, cal, ingredients])
        
    for food in frankfood:
        name = food.contents[0].contents
        cal = food.contents[0].get('data-calories')
        ingredients = food.contents[0].get('data-ingredient-list')
        csv_writer.writerow(['Franklin DC', name, cal, ingredients])
        
    for food in woofood:
        name = food.contents[0].contents
        cal = food.contents[0].get('data-calories')
        ingredients = food.contents[0].get('data-ingredient-list')
        csv_writer.writerow(['Worcester DC', name, cal, ingredients])
        