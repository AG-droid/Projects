#Creating the variables
d = 0
c = 0
a = {}

#Creating a class named bus
class bus:
    def __init__(self):
        pass

    #Collecting the info from the user and sorting them on the basis of their type

    def info(self):
        global i
        i = (input('How many passengers were on the bus --> '))

        #Nesting some more functions to let go off the usage of global variables

        #Sorting out the collected data

        def sort(i):

            #Collecting the data in the form of dictionaries

            def dic(z):
                value = z
                a[c] = value


            if i == 'x' or i == 'X':
                i = i
            else:
                z = int(i)
                dic(z)


        sort(i)











#Creating a while loop
while d < 10:
    c += 1
    x = bus()
    x.info()

    #Adding a Condition to finalise and end the loop

    if i == 'X' or i == 'x':
        c -= 1
        sum = sum(a.values())
        print('There were a total {} passengers on {} buses'.format(sum,c))

        break





