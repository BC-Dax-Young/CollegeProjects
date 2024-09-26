
#==========================={[IMPORTS]}============================

from math import hypot
import sys
import time
import random
import bisect 

#======================{[SELECTOR PROCEDURE]}======================

def selector():
    global programs
    programs=["Dice Program", 
              "Temperature Converter", 
              "Character Print", 
              "Fishtank Volume", 
              "Carpet Cost", 
              "Energy Bill", 
              "Circle Properties", 
              "Ball Pit",
              "Gambling Game",
              "Driving Test",
              "Number Comparitor",
              "Water States",
              "Career Quotes",
              "Currency Converter",
              "Nitrate Problem",
              "Exam Grade",
              "Periodic Table",
              "Day Format"
              ]
    counter=1
    print("=======================\nAvailable/Allotted Programs: \n=======================")
    for i in programs:
        print(f"{counter}: {i}")
        counter+=1
    while True:
        while True:
            try: 
                selection=str(input("Enter the list integer number to select the desired program: "))
                break
            except Exception as error:
                print(f"Program has encoutered an error: {error}")
                continue
        program(selection)
        break            

#==================={[PROGRAM SELECTOR PROCEDURE]}===================

def program(selection):
    try:
        print(f"Program: {programs[int(selection)-1]}")
        eval("program"+selection)()
    except Exception as error:
        print(f"{error}")

    '''
    if selection==1:
        program1()
    elif selection==2:
        program2()
    elif selection==3:
        program()
    elif selection==4:
        program4()
    elif selection==5:
        program5()
    elif selection==6:
        program6()
    elif selection==7:
        program7()
    elif selection==8:
        program8()
    else:
        print("Error! Selection is not within bounds!")
    '''
#============================={[PROGRAMS]}==========================

def program1():
    	print("ooooooooooo\no         o\no  #   #  o\no    #    o\no  #   #  o\no         o\nooooooooooo")

def program2():
    def f2c(F):
        return (F-32)/1.8
    def c2f(C):
        return (C*1.8)+32
    while True:
        try:
            while True:
                unit=int(input("Enter the unit you want to convert to:\nC: 1\nF: 2\nEnter here: "))
                if unit==1:
                    break
                elif unit==2:
                    break
                else:
                    continue
            convert=int(input("Enter integer input: "))
            break
        except Exception as error:
            print(f"Error!: {error}")
            continue
    if unit==1:
        print(c2f(convert))
    elif unit==2:
        print(f2c(convert))
        
def program3():
    print("The digits are: 0123456789 \nThe characters are: abcdABCD@#! \nThe alphanumerics are: 0123456789 abcdABCD@#!")

def program4():
    while True:
        try:
            h=int(input("Input height: "))
            w=int(input("Input width: "))
            d=int(input("Input depth: "))
            break
        except:
            print("Error: Enter integers only!")
            continue
    print(f"The volume is {(h*w*d)/1000}")
        
def program5():
    while True:
        try:
            h=int(input("Input height: "))
            w=int(input("Input width: "))
            c=int(input("Carped price in metres squared: "))
            break
        except:
            print("Error: Enter integers only!")
            continue
    print(f"The underlay price is ${(c*3)}")
    print(f"The grippers price is ${(h*2 + w*2)}")
    print(f"The total is ${(h*2 + w*2)+(c*3)}")
    
def program6():
    while True:
        try:
            u=int(input("Input Units Used: "))
            break
        except:
            print("Error: Enter integers only!")
            continue
    print(f"The kWh is {(u*39.3*1.022)/3.6}")
    print(f"The price is ${((u*39.3*1.022)/3.6)*2.84}")
    
def program7():
    while True:
        try:
            dia=int(input("Input diamater: "))
            arc=int(input("Input arc angle: "))
            break
        except:
            print("Error: Enter integers only!")
            continue
    print(f"The radius is {(dia)/2}")
    print(f"The area is {3.14*(dia/2)**2}")
    print(f"The circumfrence is ${3.14*dia}")
    print(f"The arc length is ${((3.14*dia)*arc)/360}")
    
def program8():
    while True:
        try:
            radius=int(input("Input radius: "))
            h=int(input("Input height: "))
            break
        except:
            print("Error: Enter integers only!")
            continue
    print(f"The volume is {(4/3)*3.14*radius**3}")
    print(f"The volume of a ball is {(4/3)*3.14*radius**3}")
    print(f"The required amount of balls is {((4/3)*3.14*radius**3)/(4/3)*3.14*radius**3}")
    
def program9():
    
    def chat(message, response, responder):
        for char in message:
            time.sleep(0.025)
            sys.stdout.write(char)
        if response == 1:
            res=input(f"{responder}: ")
            return res
        
        
    def cardgen(user):
        card=random.randint(1,13)
        cardtype=random.randint(1,4)
        if cardtype==1:
            cardtype="Hearts"
        elif cardtype==2:
            cardtype="Spades"
        elif cardtype==3:
            cardtype="Clubs"
        elif cardtype==4:
            cardtype="Diamonds"
        if card==1:
            card="Ace"
            rt=(f"{user} got dealt {card} of {cardtype}")
            print(rt)
            return(rt, card, cardtype)
        elif card < 11 and card != 1:
            rt=(f"{user} got dealt {card} of {cardtype}")
            print(rt)
            return(rt)
        elif card == 11:
            ct="Jack"
            rt=(f"{user} got dealt {ct} of {cardtype}")
            print(rt)
            return(rt, card, cardtype)
        elif card == 12:
            ct="Queen"
            rt=(f"{user} got dealt {ct} of {cardtype}")
            print(rt)
            return(rt, card, cardtype)
        elif card == 13:
            ct="King"
            rt=(f"{user} got dealt {ct} of {cardtype}")
            print(rt)
            return(rt, card, cardtype)
            
    

    def main():
        global games
        games = ["slot machines", "blackjack", "roulette"]
        while True:
            try:
                age=int(chat("Bouncer: Hey! How old are you?\n", 1, "You"))
                break
            except:
                chat("Bouncer: Your age can't have letters in it bud\n", 0, "You")
                continue
        if age < 18:
            chat("Bouncer: You aren't old enough to go in here!\n", 0, "You")
        else:
            chat("Bouncer: Welcome!\n", 0, "You: ")
        while True:
            gamechoice=chat(f"Narrator: You enter the casino; you see a large assortment of varying gambiling games, Roulette, Black-Jack, Slot Machines; you walk over to the: ", 1, "")
            counter=0
            if "black" in gamechoice:
                numeric_types = [int, float, complex]
                usercards=[]
                enemycards=[]
                
                while counter!=2:
                    cardadd=cardgen("You")
                    usercards.append(cardadd)
                    counter+=1
                counter=0
                while counter!=2:
                    cardadd=cardgen("Dealer")
                    enemycards.append(cardadd)
                    counter+=1
                char="abcdefghijklmnopqrstuvwxyz"
                for idx, ele in enumerate(usercards):
                    usercards[idx] = ele.replace(char, '')
        
def program10():
    def PassFail(MinorFaults):
        if MinorFaults < 16:
            return "fail"
        else:
            return "pass"
    print(PassFail(16))

def program11():
    def getint(numnum):
        while True:
            try:
                getint=int(input(f"Enter Number {numnum}: "))
                break
            except:
                print("Error enter integers only!")
                continue
        return getint

    num1=getint(1)
    num2=getint(2)

    if num1<num2:
        print(num2)
    elif num1>num2:
        print(num1)
    else:
        print("They are the same")

def program12():
    def getint():
        while True:
            try:
                getint=int(input(f"Enter Temperature: "))
                break
            except:
                print("Error enter integers only!")
                continue
        return getint

    temp=getint()

    if temp>100:
        print("Gas")
    elif temp<100 and temp>0:
        print("Liquid")
    else:
        print("Solid")

def program13():
    job=input("Job: ").lower()
    if job=="engineer":
        print("The engineer has been, and is, a maker of history.")
    elif job=="developer":
        print("Logical thinking, passion and perseverance is the paint on your palette.")
    elif job=="analyst":
        print("Seeing what other people can`t see gives you great vision.")
    else:
        print("I'm sorry. We could not find a quote for your job.")

def program14():
    def getint(numnum):
        while True:
            try:
                getint=int(input(f"Enter Number {numnum}: "))
                break
            except:
                print("Error enter integers only!")
                continue
        return getint

    currency=input("Enter Currency, GBP to USD, Euro, Yuan or Yen: ").lower()
    amount=getint("")
    if currency=="usd":
        print(f"{amount} GBP = {amount*1.35} USD")
    elif currency=="euro":
        print(f"{amount} GBP = {amount*1.20} Euro")
    elif currency=="yuan":
        print(f"{amount} GBP = {amount*9.37} Yuan")
    elif currency=="euro":
        print(f"{amount} GBP = {amount*193.26} Yen")
    else:
        print("Invalid Currency")

def program15():
    def getint(numnum):
        while True:
            try:
                getint=int(input(f"Enter Number {numnum}: "))
                break
            except:
                print("Error enter integers only!")
                continue
        return getint
    def dose():
        doseage=getint("")
        if doseage>10:
            val= 3
        else:
            if doseage>2.5:
                val= 2
            else:
                if doseage>1:
                    val= 1
                else:
                    val= 0.5
        print(f"For {doseage} nitrate dose {val} ml")
        
    dose()

def program16():
    def getint(numnum):
        while True:
            try:
                getint=int(input(f"Enter Number {numnum}: "))
                break
            except:
                print("Error enter integers only!")
                continue
        return getint
    def determine_grade(scores, breakpoints=[1,2,4,13,22,31,41,54,67,80], grades='U123456789'):
        while True:
            try:
                i = bisect.bisect(breakpoints, scores)
                return grades[i], breakpoints[int(grades[i])]-scores
                break
            except:
                continue
    grade=getint("")
    dtrgrade, needed =determine_grade(grade)
    print(f"You got a grade {dtrgrade}, you need {needed} more points.")

def program17():
    Hydrogen=["Hydrogen", "H", 1, 1.0078]
    Lithium=["Lithium", "Li", 3, 6.9410]
    Beryllium=["Berylium", "Be", 4, 1.0078]
    element=input("Enter the element: ")
    if element in Hydrogen:
        print("Hydrogren Info:")
        for i in Hydrogen:
            print(i)
    elif element in Lithium:
        print("Hydrogren Info:")
        for i in Lithium:
            print(i)
    elif element in Beryllium:
        print("Beryllium Info:")
        for i in Beryllium:
            print(i)

def program18():
    day=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    shortday=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    char=["M", "Tu", "W", "Th", "F", "Sa", "Su"]
    value=input("Enter day:").title()
    if value in day:
        daypos=day.index(value)
        print(day[daypos])
        print(shortday[daypos])
        print(char[daypos])
    elif value in shortday:
        daypos=day.index(value)
        print(day[daypos])
        print(shortday[daypos])
        print(char[daypos])
    elif value in char:
        daypos=day.index(value)
        print(day[daypos])
        print(shortday[daypos])
        print(char[daypos])



#==================================================================



selector()
