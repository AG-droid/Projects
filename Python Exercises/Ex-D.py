#Getting the user input
num_sttions = int(input('How many stations do you want to Know about --> '))

#Storing the info regarding the stations
stp_free = ['Oxford Circus','Stepney Green','Westminster Abbey', 'Piccadily Circus',
            'oxford circus','stepney green','westminster abbey', 'piccadily circus']

stp = ['Kensington','Northern', 'Bakerloo', 'Central',
       'kensington','northern', 'bakerloo', 'central']

dist = {
        'Oxford Circus': 200,
        'Stepney Green': 300,
        'Westminster Abbey': 400,
        'Piccadily Circus': 500,
        'Kensington': 600,
        'Northern': 700,
        'Bakerloo': 800,
        'Central': 900,
        }

#Defining the class Station
class Stations:
    #Initialising the class
    def __init__(self,name):
        self.name = name
    #Filtering the stations according to their features and giving the output
    def info1(self):
        if self.name in stp_free:
            print('{} is a step free station'.format(self.name))
        elif self.name in stp:
            print('{} is not a step free station'.format(self.name))
        elif self.name == '':
            print('Pls enter the name of a station')
        else:
            print('{} is not in london'.format(self.name))
    #Giving the distance from the stations
    def info2(self):
        if self.name in dist :
            print('This station is {} metres away'.format(dist[stion]))
        else:
            print('ERROR : The information of the following station is not available at the moment')



#Initialising the for loop
for i in range(num_sttions):
    global stion
    stion = input('Which station do you want to know about --> ')
    x = Stations(stion)
    x.info1()
    x.info2()

