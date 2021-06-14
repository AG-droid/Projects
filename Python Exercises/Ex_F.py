
#Declaring variables to get the input from the user
a = int(input('Pls enter your age --> '))
b = int(input('Pls enter your heart rate --> '))
c = int(input('How far can you stretch (In centimetres)--> '))

#Creating a function to calculate the user's age
def calculator():
    #Declaring the variable d as a global variable
    global d
    #Calculating the age on the basis of the user's heart rate
    if b < 62 :
       d =  a - 5
    elif b >= 62 and b <= 64 :
       d = a - 1
    elif b >= 65 and b <=70 :
       d =  a + 1
    elif b >= 71 :
       d =  a + 2

    #Calculating the age on the basis of the user's flexibility
    if c < 20 :
        d += 4
    elif c >= 20 and c <= 32 :
        d += 1
    elif c >= 33 and c <= 37 :
        d+= 0
    elif c > 37 :
        d -= 3

#Initialising the function
calculator()

#Presenting the output to the user
print('Your body age is {}'.format(d))
