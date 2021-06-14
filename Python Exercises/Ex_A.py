#Creating necessary variables
a = {}
c = input('Which country is the team representing --> ')


class swim:
    def __init__(self):
        pass
    #Collecting info from the user

    def info(self):
        b = int(input('What is the disability category of Swimmer {} --> '.format(i)))
        a[i] = b
    #Sorting and creating an output of the collected information

    def sort(self):
        d = sum(a.values())
        if d > 34 :
            l = 'illegal'
        else:
            l = 'legal'

        print('The {} team has {} points so it is {}'.format(c,d,l))


class finalise(swim):
    def __init__(self):
        pass
    #Creating a function to run the other functions in sequence

    def run(self):
        x = swim()
        x.info()

        if i == 4:
            x.sort()

#Creating a loop

for i in range (1,5):

    #Initialising the final function

    y = finalise()
    y.run()