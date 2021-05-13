# Author - Anmol Goyal
# MiniProject - Jurrasic Park Game


import random
import time
import os
from prettytable import PrettyTable 

class Dino():
    def __init__(self):
        pass

    def var(self):
        dinos = {}
        
        for i in range(1, 3):
            name = input('Please name Dinosaur No. {} --> '.format(i))
            calm = random.randint(1, 5)
            hunger = random.randint(1, 10)
            fin = [name, calm, hunger]
            dinos[i] = fin

        table = PrettyTable(['No.', 'Name', 'Calmness', 'Hunger'])
        dino1 = dinos[1]
        dino2 = dinos[2]
        table.add_row([1, dino1[0], dino1[1], dino1[2]])
        table.add_row([2, dino2[0], dino2[1], dino2[2]])
        print(table)
        print('INFO - PLS ONLY TYPE IN THE SERIAL NO. OF YOUR SELECTED DINO')
        ask = (input("""Which dinosaur do you want to choose?
        (1/2) """))

        if ask == '1' or ask == dino1[0]:
            final = dino1
        elif ask == '2' or ask == dino2[0]:
            final = dino2
        elif ask == '':
            print('No problem, we will choose the your Dino for you :)')
            final = dinos[random.randint(1, i)]

        a = final[0]
        b = final[1]
        c = final[2]

        def info1():
            print('{} HAS BEEN CHOSEN FOR THIS ROUND.'.format(a.upper()))
            print('The {} are a vicious yet an intelligent species.'.format(a))

        def feed():
            l = input("""Would you like to feed your Dinosaur?  
            
            (y/n) """)

            if l in ('YES', 'yes', 'y'):
                k = input("""What would you like to feed him from the following options :-
                A. Ham
                B. Carrot
                C. Chicken
                D. Human
                Type  your desired food here -->  """)

                if k == 'Ham' or 'ham' or 'A' or 'a':
                    e = c - 4
                elif k == 'Carrot' or 'carrot' or 'B' or 'b':
                    e = c - 2
                elif k == 'Chicken' or 'chicken' or 'C' or 'c':
                    e = c - 3
                elif k == 'Human' or 'human' or 'D' or 'd':
                    e = c - 5
                else:
                    e = c
            else:
                e = c

            f = input("""Would you like to sooth you Dinosaur? 
            
            (y/n) """)

            if f == 'Yes' or f == 'yes' or f == 'y':
                h = input("""Where would you like to sooth him?
                A. Neck
                B. Stomach
                C. Head
                D. Back
                Type your selected option here --> """)

                if h == 'Neck'or h == 'neck' or h == 'A'or h == 'a':
                    m = b + 1
                elif h == 'Stomach' or h == 'stomach' or h == 'B'or h == 'b':
                    m = b + 2
                elif h == 'Head' or h == 'head' or h == 'C'or h == 'c':
                    m = b + 5
                elif h == 'Back' or h == 'back' or h == 'D' or h == 'd':
                    m = b + 3
                else:
                    m = b
            else:
                m = b

            def hunger():
                d = e - m
                if final == dinos[1]:
                    dino2 = dinos[2]

                elif final == dinos[2]:
                    dino2 = dinos[1]
                name2 = dino2[0]

                if d >= 5:
                    print("{} LOOKS VERY HUNGRY, HE WILL EAT {} !".format(a, name2))
                    time.sleep(1)

                    riddle = input("""YOU HAVE TO SOLVE THE FOLLOWING RIDDLE TO SAVE {}'S LIFE
                    
                    What's as big as a dinosaur but weighs nothing?
                    (Hint : IT ONLY APPEARS UNDER A LIGHT) 
                    Ans --> """.format(name2)).lower()
                    if riddle == "dinosaur's shadow" or riddle == 'shadow' or riddle == "dinosaur'sshadow":
                        print("CONGRATS YOU SAVED {}'S LIFE!".format(name2))
                    else:
                        print('{} WAS EATEN BY {} ;-;'.format(name2, a))

                def level():
                    if d < 3:
                        print('The {} looks Calm.... Come closer'.format(a))
                        print('Congrats, YOU SURVIVED!')
                    elif d >= 3 and d < 5:
                        print('The {} looks Aroused... Be careful.'.format(a))
                        print('Congrats, YOU SURVIVED!')
                    elif d >= 5 and d < 8:
                        print('The {} looks Dangerous.. Maintain Distance'.format(a))
                        print('YOU SURVIVED! but you lost your arm !')
                    elif d > 8:
                        print('The {} looks Killer.. RUN!!'.format(a))
                        print('YOU DIED! better luck next time')

                level()
            hunger()

        def caller():
            info1()
            feed()

        caller()


if __name__ == '__main__':

    for i in range(1, 100):
        print('WELCOME TO ROUND {} !'.format(i))

        x = Dino()
        x.var()
        q = input("""Do you want to play another match? 
        
        (y/n) """)
        if q == 'yes' or q == 'Yes' or q == 'y':
            pass
        else:
            break
