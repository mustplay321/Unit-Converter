'''This is Conversions.py. Conversions are pulled from this file in main.py, and it is kept as a separate file to be imported in main.py'''

from decimal import *

#functions
def convertWeight(value,unitIn,unitOut,decimal): #converts weight values ; each dictionary uses 1/(a value) to make conversion more accurate
    weight = {'g':0.001,'mgs':0.000001,'kgs':1,'lbs':1/2.20462262185,'oz':1/35.27396} #dictionary containing conversion factors with kilograms as the base
    return round(Decimal((value*weight[unitIn]/weight[unitOut])),decimal) #uses the decimal library to create more accurate conversions, rounds result based on user input for decimal

def convertDistance(value,unitIn,unitOut,decimal): #converts distance values based on user input in main.py
    distance = {'mi':1/0.6213712,'km':1,'m':0.001,'mm':0.000001,'yd':1/1093.613,'ft':1/3280.84,'in':39370.08} #dictionary containing conversion factors with kilometers as the base
    return round(Decimal((value*distance[unitIn]/distance[unitOut])),decimal)

def convertMeasure(value,unitIn,unitOut,decimal): #converts measure values based on user input in main.py
    measure = {'cup':1/4.226753,'tbsp':1/67.62804,'gal':1/0.264172,'quart':1/1.056688,'tsp':1/202.8841,'L':1,'mL':0.001} #dictionary containing conversion factors with liters as the base
    return round(Decimal((value*measure[unitIn]/measure[unitOut])),decimal)