
#==========================={[IMPORTS]}============================

from socket import EAI_BADFLAGS
import numpy as np
import sys
import time
import random
import bisect 
import re

#======================{[SHARED SUBROUTINES]}======================

def getint(numnum):
        while True:
            try:
                getint=int(input(f"Enter Number {numnum}: "))
                break
            except:
                print("Error enter integers only!")
                continue
        return getint

def getfloat(numnum):
        while True:
            try:
                getfloat=int(input(f"Enter Number {numnum}: "))
                break
            except:
                print("Error enter integers only!")
                continue
        return getfloat

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
              "Day Format",
              "Save the Change",
              "Dice",
              "Clamp",
              "Leap Year",
              "Days",
              "Dice Game",
              "Division",
              "Dogs life",
              "Electric Car",
              "Twitter",
              "Initial and Surname",
              "Inventory ",
              "Flight",
              "Teacher Code",
              "Email",
              "Seperator",
              "Ascii EBCDIC"
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
    def PassFail(MinorFaults):
        if MinorFaults < 16:
            return "fail"
        else:
            return "pass"
    print(PassFail(16))

def program10():

    num1=getint(1)
    num2=getint(2)

    if num1<num2:
        print(num2)
    elif num1>num2:
        print(num1)
    else:
        print("They are the same")

def program11():
    temp=getint()

    if temp>100:
        print("Gas")
    elif temp<100 and temp>0:
        print("Liquid")
    else:
        print("Solid")

def program12():
    job=input("Job: ").lower()
    if job=="engineer":
        print("The engineer has been, and is, a maker of history.")
    elif job=="developer":
        print("Logical thinking, passion and perseverance is the paint on your palette.")
    elif job=="analyst":
        print("Seeing what other people can`t see gives you great vision.")
    else:
        print("I'm sorry. We could not find a quote for your job.")

def program13():

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

def program14():
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

def program15():
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

def program16():
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

def program17():
    day=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    shortday=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    char=["M", "Tu", "W", "Th", "F", "Sa", "Su"]
    value=input("Enter day:").title()
    if value in day:
        daypos=day.index(value)
        print(shortday[daypos])
        print(char[daypos])
    elif value in shortday:
        daypos=day.index(value)
        print(day[daypos])
        print(char[daypos])
    elif value in char:
        daypos=day.index(value)
        print(day[daypos])
        print(shortday[daypos])

def program18():
    purchasecost=getfloat("")
    rounded=np.ceil(purchasecost)
    diff=rounded-purchasecost
    print(f"Item cost: {purchasecost},\nPaid Amount: {rounded},\n Saved to Savings: {diff}")

def program19():
    die=getint("of faces")
    print(f"Your {die} sided die rolled a {random.randint(1,die)}")

def program20():
    def clamp():
        num1=getint(1)
        num2=getint(2)

        if num1<num2:
            print(num2)
        elif num1>num2:
            print(num1)
        else:
            print(num1)
    clamp()

def program21():
    year=getint("")
    if year % 4 == 0 or year % 400 == 0 and year %100 != 0:
        print(f"{year} is a leap year!")
    else:
       print(f"{year} is not a leap year.")

def program22():
    day=getint("")
    print(day//24)

def program23():
    input("Roll dice one?")
    dice1=random.randint(1,6)
    print(dice1)
    input("Roll dice two?")
    dice2=random.randint(1,6)
    print(dice2)
    input("Roll dice three?")
    dice3=random.randint(1,6)
    print(dice3)
    def scoredice(d1,d2,d3):
        if d1==d2==d3:
            score=d1+d2+d3
        elif d1==d2:
            score=d1+d2
            score-=d3
        elif d3==d2:
            score=d2+d3
            score-=d1
        elif d1==d3:
            score=d1+d3
            score-=d2
        else:
            score=0
        return score
    print(scoredice(dice1,dice2,dice3))

def program24():

    def div(val1,val2):
        if val1 == 0 or val2 == 0:
            return False
        elif val1 % val2 == 0:
            return True
        else:
            return False

    div(getint(""),getint(""))

def program25():
    age=getint("")
    if age <= 2:
        print(f"Your dog is {age*12} years old.")
    elif age > 2:
        print(f"Your dog is {24+(age*6)-2}")

def program26():
    time=getint("of minutes to charge")
    points=1.5*time
    price=1+(float(0.2)*time)
    print(f"You owe ${price} and earned {points} points")

def program27():
    while True:
        tweet=input("Tweet: ")
        if len(tweet) > 20:
            print("Tweet Exceeds maximum character limit!")
        else:
            print(tweet)

def program28():
    forename=input("Enter Forename: ")
    surname=input("Enter Surname: ")
    print(forename[0].upper(),surname.upper())

def program29():
    def exists(inv, check):
        if any(x in inv for x in check)==True:
            print(True)
        else:
            print(False)
    plrinv=["Sword" "Shield", "Potion", "Amulet"]
    invcheck= ["Shield", "Potion", "Charm" ,"Bow"]
    exists(plrinv,invcheck)

def program30():
    city1=input()
    city2=input()
    flight=city1[0:4].upper()+"-"+city2[0:4].upper()
    print(flight)

def program31():
    dax=["Dax","Aleckzander","Young"]
    ebony=["Ebony-Jayne","Sapphire","Davies-Waterhouse"]
    filip=["Filip"," ","Trzcinski"]
    if " " in filip:
        pos=filip.index(" ")
        filiptrz=filip[2]
        filip.insert(pos,"Z")
        filip.insert(pos+1,filiptrz)
    def abbreviate(list):
        value=list[0][0]+list[1][0]+list[2][0]
        print(value)

    abbreviate(dax)
    abbreviate(ebony)
    abbreviate(filip)

def program32():
    email=input("Enter email: ")
    if "@" in email and "." in email:
        print("Email Valid")
    else:
        print("Email Invalid")

def program33():
    name=input("Enter name:").title()
    split=name.split()
    for i in split:
        print(i.title())
            
def program34():
    dictionary={
        "A":"Ascii: 65\n EBCDIC:193",
        "B":"Ascii: 66\n EBCDIC:194",
        "C":"Ascii: 67\n EBCDIC:195",
        "D":"Ascii: 68\n EBCDIC:196",
        "E":"Ascii: 69\n EBCDIC:197",
        "F":"Ascii: 70\n EBCDIC:198",
        "G":"Ascii: 71\n EBCDIC:199",
        "H":"Ascii: 72\n EBCDIC:200",
        "I":"Ascii: 73\n EBCDIC:201",
        "J":"Ascii: 74\n EBCDIC:209",
        "K":"Ascii: 75\n EBCDIC:210",
        "L":"Ascii: 76\n EBCDIC:211",
        "M":"Ascii: 77\n EBCDIC:212",
        "N":"Ascii: 78\n EBCDIC:213",
        "O":"Ascii: 79\n EBCDIC:214",
        "P":"Ascii: 80\n EBCDIC:215",
        "Q":"Ascii: 81\n EBCDIC:216",
        "R":"Ascii: 82\n EBCDIC:217",
        "S":"Ascii: 83\n EBCDIC:226",
        "T":"Ascii: 84\n EBCDIC:227",
        "U":"Ascii: 85\n EBCDIC:228",
        "V":"Ascii: 86\n EBCDIC:229",
        "W":"Ascii: 87\n EBCDIC:230",
        "X":"Ascii: 88\n EBCDIC:231",
        "Y":"Ascii: 89\n EBCDIC:232",
        "Z":"Ascii: 90\n EBCDIC:233",
        " ":"Ascii: 32\n EBCDIC:64"
        }

    lookup=input("Enter Letter to lookup: ").upper()
    print(dictionary[lookup])

#==================================================================


selector()
