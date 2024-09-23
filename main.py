'''This is main.py. It includes the main functions and events of the program, and imports the conversion factor functions from conversions.py. 
Again, these are separate .py files, as conversions.py will be imported in this file.'''

#Unit Converter
from decimal import *
from conversions import *

#Variables
unitType = ['Weight','Distance','Measure'] #manages which unit type should be converted
unitWeight = ['g','kgs','mgs','lbs','oz'] #stores strings relating to weight
unitDistance = ['mi','km','m','mm','yd','ft','in'] #strings related to distance
unitMeasure = ['cup','tbsp','gal','quart','tsp','L','mL'] #strings related to measure

#Functions
def askType(): #takes user input to decide which list to pull from
    global units
    end = 0
    units = input('Weight, Distance, or Measure: ')
    while end == 0: #error compensation: loops program until user enters valid unit type
        if units in unitType:
            end = 1
        elif units not in unitType:
            print('Please enter valid unit type with no extra characters')
            units = input('Weight, Distance, or Measure: ')

def askVariables(units): #sets global variables value,unitIn,unitOut,decimal based on user input for use later
    global unitIn,unitOut,decimal,value #these variables will be used for conversions after this function completes
    end = 0
    value = float(input('Value to convert: ')) #takes users input as a float, allowing the user to enter decimal numbers
    while end == 0: #error compensation
        match units: #checks which category of units the user input (Match statement only works in Python 3.10.0 and later ; Can substitute if,elif statement if necessary)
            case 'Weight':
                print('The Weight type supports g, kgs, mgs, oz, and lbs')
                unitIn = input('Convert from: ')
                unitOut = input('Convert to: ')
                if unitIn and unitOut in unitWeight:
                    end = 1
                else: #prevents program from failing due to an invalid entry
                    print('Invalid Entry')
            case 'Distance':
                print('The Distance type supports mi, km, m, mm, yd, ft, and in')
                unitIn = input('Convert from: ')
                unitOut = input('Convert to: ')
                if unitIn and unitOut in unitDistance:
                    end = 1
                else: #prevents program from failing due to an invalid entry
                    print('Invalid Entry')
            case 'Measure':
                print('The Measure type supports cup, tbsp, gal, quart, tsp, L, mL')
                unitIn = input('Convert from: ')
                unitOut = input('Convert to: ')
                if unitIn and unitOut in unitMeasure:
                    end = 1
                else: #prevents program from failing due to an invalid entry
                    print('Invalid Entry')
    decimal = int(input('Decimal places to round to: ')) #takes user input as an integer for decimal places (no need for float here)

def convert(units,value,unitIn,unitOut,decimal): #runs conversion functions from conversions.py based on user's unit type input, then returns the calculated value
    match units: #match statement only works in python 3.10.0 or later ; substitute if,elif statement if necessary
        case 'Weight':
            return convertWeight(value,unitIn,unitOut,decimal) #inputs the previously assigned value,unitIn,unitOut,decimal variables into conversions.py
        case 'Distance':
            return convertDistance(value,unitIn,unitOut,decimal) #same but for distance unit type
        case 'Measure':
            return convertMeasure(value,unitIn,unitOut,decimal) #same but for measure unit type

#Events
end = 'y'
while end == 'y': #asks user the unit type and values to convert, then returns the calculated value and loops based on user's input
    askType()
    askVariables(units)
    print(convert(units,value,unitIn,unitOut,decimal)) #prints the returned value of the convert function, which is calculated by conversions.py
    end = input('Convert more? y or n: ') 