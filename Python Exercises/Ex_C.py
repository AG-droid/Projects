#Importing the necessary files
from prettytable import PrettyTable

#Creating a class
class Wmn():

    #Initialising the class
    def __init__(self,num):
        self.num = num

    #Collecting the info from the user
    def info1(self):
        global tpl, a,b,c
        b = input('Name footballer {} --> '.format(self.num))
        a = int(input('How many Goals did they score --> '))
        c = input('What country did they play for --> ')


    #Sorting the collected  info into different categories
    def sort(self):

        global a0,a1,a2,a3
        global b0,b1,b2,b3
        global c0,c1,c2,c3
        global l,sum
        if self.num == 1:
            a0 = a
            b0 = b
            c0 = c

        elif self.num == 2:
            a1 = a
            b1 = b
            c1 = c
        elif self.num == 3:
            a2 = a
            b2 = b
            c2 = c
        elif self.num == 4:
            a3 = a
            b3 = b
            c3 = c

        if self.num == 4:

            sum = a0 + a1 + a2 + a3

            x.sort2()
            x.final()
            x.sort3()


    #Sorting the collected data on the basis of the highest score
    def sort2(self):
        global hghst_scr,l
        l = (a0, a1, a2, a3)
        if a0 == max(l):
            hghst_scr = b0
        elif a1 == max(l):
            hghst_scr = b1
        elif a2 == max(l):
            hghst_scr = b2
        elif a3 == max(l):
            hghst_scr = b3

    #Arranging the collected data in a tabular form
    def sort3(self):
        print('The details of the players are :')
        mytable = PrettyTable(['Player Name', 'No. of Goals Scored', 'Country'])
        mytable.add_row([b0,a0,c0])
        mytable.add_row([b1,a1,c1])
        mytable.add_row([b2,a2,c2])
        mytable.add_row([b3,a3,c3])
        print(mytable)

    #Displaying the final output
    def final(self):
        print('The highest scorer is {}'.format(hghst_scr))
        print('These players scored {} goals between them'.format(sum))




#Initialisng the loop
for i in range(1, 5):
    x = Wmn(i)
    x.info1()
    x.sort()

