#Importing the modules
import math
#Declaring Variable for getting the information from the user
a = float(input('Amount of loan at the start of the year --> '))
b = float(input('Amount paid off this year --> '))
#Calculating the amount
c = (a - b) + (a * 7/100)

# rounding down our value
d = math.floor(c*10)/10

#Displaying the output
print('The new amount owed is ${}'.format(d))


