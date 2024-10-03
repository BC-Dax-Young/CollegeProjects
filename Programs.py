
#==========================={[IMPORTS]}============================

import numpy as np # imports Numpy library for numerical operations
import sys # imports system library for managing system operations
import time # imports time library for controlling time operations
import random # imports random
import bisect # imports bisect for maintaining sorted lists
import re # imports re

#======================{[SHARED SUBROUTINES]}======================

def getinput(message, inp): # custom input function with input validation and input choice
        while True: # loop until valid input is provided
            if inp=="int": # check inp for int
                try: # validates input
                    response=int(input(f"{message}")) # set response as int input value
                    break
                except: # catches exception and prints error message
                    print("Error enter integers only!") # print error message
                    continue
            elif inp=="float": # check inp for float 
                try: # validates input
                    response=float(input(f"{message}")) # set response as float input value
                    break
                except: # catches exception and prints error message
                    print("Error enter floats only!") # print error message
                    continue
            elif inp=="str": # check inp for str
                try: # validates input
                    response=str(input(f"{message}")) # set response as string input value
                    break
                except: # catches exception and prints error message
                    print("Error enter strings only!") # print error message
                    continue
        return response # returns validated response

def typeout(message, response_wanted, responder): # function to type out a message and wait for user input if response_wanted is 1
    for char in message: # loop through each character in the message
        time.sleep(0.0125) # pause for 0.0125 seconds
        sys.stdout.write(char) # print character to console
    if response_wanted==1: # check if response_wanted is 1
        return getinput(f"{responder}", "str") # get user input if response_wanted is 1


#======================{[SELECTOR PROCEDURE]}======================

def selector(): # main selector function
    global programs # global variable for storing available programs
    programs=["Dice Program", # 1
              "Temperature Converter", # 2
              "Character Print", # 3
              "Fishtank Volume", # 4
              "Carpet Cost",  # 5
              "Energy Bill",   # 6
              "Circle Properties", # 7
              "Ball Pit", # 8
              "Driving Test", # 9
              "Number Comparitor", # 10
              "Water States", # 11
              "Career Quotes", # 12
              "Currency Converter", # 13
              "Nitrate Problem", # 14
              "Exam Grade", # 15
              "Periodic Table", # 16
              "Day Format", # 17
              "Save the Change", # 18
              "Dice", # 19
              "Clamp",# 20
              "Leap Year", #21
              "Days",#23
              "Dice Game",#24
              "Division",#25
              "Dogs life",#26
              "Electric Car",#27
              "Twitter",#28
              "Initial and Surname",#29
              "Inventory ",#30
              "Flight",#31
              "Teacher Code",#32
              "Email",#33
              "Seperator",#34
              "Ascii EBCDIC",#35
              "Paper Clip Game",#36
              "Password"#37
              ]
    counter=1 # counter for printing program numbers
    print("=======================\nAvailable/Allotted Programs: \n=======================") # print header
    for i in programs: # loop through each program in the list
        print(f"{counter}: {i}") # print program number and name
        counter+=1 # increment counter
    while True: # loop until valid selection is provided
        while True: # loop until valid input is provided
            try: # validates input
                selection=str(input("Enter the list integer number to select the desired program: ")) # set selection as string input value
                break 
            except Exception as error: # catches exception and prints error message
                print(f"Program has encoutered an error: {error}")
                continue
        program(selection) # call program function with selected program number
        break            

#==================={[PROGRAM SELECTOR PROCEDURE]}===================

def program(selection): # main program function
    try:
        print(f"Program: {programs[int(selection)-1]}") # print selected program name
        eval("program"+selection)() # call selected program function
    except Exception as error: # catches exception and prints error message
        print(f"{error}") # print error message

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

def program1(): # Dice Program
    	print("ooooooooooo\no         o\no  #   #  o\no    #    o\no  #   #  o\no         o\nooooooooooo")

def program2(): # Conversion Program
    def f2c(F): # function to convert Fahrenheit to Celsius
        return (F-32)/1.8 # formula to convert Fahrenheit to Celsius
    def c2f(C): # function to convert Celsius to Fahrenheit
        return (C*1.8)+32 # formula to convert Celsius to Fahrenheit
    while True: #   loop until valid input is provided
        try: # validates input
            while True: # loop until valid input is provided
                unit=int(input("Enter the unit you want to convert to:\nC: 1\nF: 2\nEnter here: ")) # Get unit input
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
        
def program3(): # Characters printing program
    print("The digits are: 0123456789 \nThe characters are: abcdABCD@#! \nThe alphanumerics are: 0123456789 abcdABCD@#!") # print all characters and digits

def program4(): # Fishtank Volume program
    while True:
        try: # validates input
            h=int(input("Input height: ")) # Get unit input
            w=int(input("Input width: "))
            d=int(input("Input depth: "))
            break
        except: # catches exception and prints error message
            print("Error: Enter integers only!")
            continue
    print(f"The volume is {(h*w*d)/1000}") # calculate and print the volume
        
def program5(): # Carpet Cost program
    while True: # loop until valid input is provided
        try: # validates input
            h=int(input("Input height: ")) # Get height input
            w=int(input("Input width: "))
            c=int(input("Carpet price in metres squared: ")) # Get carpet price input
            break
        except: # catches exception and prints error message
            print("Error: Enter integers only!")
            continue
    print(f"The underlay price is ${(c*3)}") # calculate and print the underlay cost
    print(f"The grippers price is ${(h*2 + w*2)}") # calculate and print the grippers cost
    print(f"The total is ${(h*2 + w*2)+(c*3)}") # calculate and print the total cost
    
def program6(): # Energy Bill program
    while True: # loop until valid input is provided
        try: # validates input
            u=int(input("Input Units Used: "))
            break
        except: # catches exception and prints error message
            print("Error: Enter integers only!")
            continue
    print(f"The kWh is {(u*39.3*1.022)/3.6}") # calculate and print the kWh
    print(f"The price is ${((u*39.3*1.022)/3.6)*2.84}") # calculate and print the price
    
def program7(): # Circle Properties program
    while True:
        try:
            dia=int(input("Input diamater: ")) # get diameter input
            arc=int(input("Input arc angle: ")) # get arc angle input
            break
        except: # catches exception and prints error message
            print("Error: Enter integers only!")
            continue
    print(f"The radius is {(dia)/2}") # calculate and print the radius
    print(f"The area is {3.14*(dia/2)**2}") # calculate and print the area
    print(f"The circumfrence is ${3.14*dia}") # calculate and print the circumfrence
    print(f"The arc length is ${((3.14*dia)*arc)/360}") # calculate and print the arc length
    
def program8(): # Ball Pit program
    while True: # loop until valid input is provided
        try: # validates input
            radius=int(input("Input radius: ")) # get radius input
            h=int(input("Input height: ")) # get height input
            break
        except: # catches exception and prints error message
            print("Error: Enter integers only!")
            continue
    print(f"The volume is {(4/3)*3.14*radius**3}") # calculate and print the volume
    print(f"The volume of a ball is {(4/3)*3.14*radius**3}") # calculate and print the volume of a ball
    print(f"The required amount of balls is {((4/3)*3.14*radius**3)/(4/3)*3.14*radius**3}") # calculate and print the required amount of balls
    
        
def program9(): # Driving Test
    def PassFail(MinorFaults): # function to determine pass or fail based on minor faults
        if MinorFaults < 16:
            return "fail"
        else:
            return "pass"
    print(PassFail(16)) # call function with minor faults and print result

def program10(): # Compatispn program

    num1=getinput("Enter Number 1: ", "int")
    num2=getinput("Enter Number 2: ", "int")

    if num1<num2:
        print(num2)
    elif num1>num2:
        print(num1)
    else:
        print("They are the same")

def program11():
    temp=getinput("Temperature",0)

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
    amount=getinput("Enter amount: ", "int")
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
        doseage=getinput("Enter dosage: ", "int")
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
    grade=getinput("Enter Grade: ", "int")
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
    purchasecost=getinput("Enter Cost", "float")
    rounded=np.ceil(purchasecost)
    diff=rounded-purchasecost
    print(f"Item cost: {purchasecost},\nPaid Amount: {rounded},\n Saved to Savings: {diff}")

def program19():
    die=getinput("How many sides to your die?: ", "int")
    print(f"Your {die} sided die rolled a {random.randint(1,die)}")

def program20():
    def clamp():
        num1=getinput("Enter Number 1: ", "int")
        num2=getinput("Enter Number 2: ", "int")

        if num1<num2:
            print(num2)
        elif num1>num2:
            print(num1)
        else:
            print(num1)
    clamp()

def program21():
    year=getinput("Enter year: ", "int")
    if year % 4 == 0 or year % 400 == 0 and year %100 != 0:
        print(f"{year} is a leap year!")
    else:
       print(f"{year} is not a leap year.")

def program22():
    day=getinput("Enter Number of days: ", "int")
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

    div(getinput("Enter Number 1: ", "int"),getinput("Enter Number 2: ", "int"))

def program25():
    age=getinput("Enter age: ", "float")
    if age <= 2:
        print(f"Your dog is {age*12} years old.")
    elif age > 2:
        print(f"Your dog is {24+(age*6)-2}")

def program26():
    time=getinput("Enter number of minutes parked: ", "int")
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

def program35():
    print("======================================================")

    #
    def printstats():
        global paperclipsper
        global paperclips
        global money
        global sold
        global robots
        typeout(f"You have {paperclips} Paper Clips\n", 0, "")
        typeout(f"You have {money} Dollars\n", 0, "")
        typeout(f"You have sold {sold} Paper Clips\n", 0, "")
        typeout(f"You have {robots} Robots making Paper Clips\n", 0, "")
    #
    def makepaperclip():
        global paperclipsper
        global paperclips
        global money
        global sold
        global robots
        while True:
            robotpc()
            var=getinput(f"Press Enter to make {paperclipsper} Paper Clip or type exit to exit: ", "str")
            if "exit" not in var:

                money=money-2
                paperclips+=paperclipsper
                print(f"Made {paperclipsper} Paper Clips for $2.")
                continue
            else:
                print("======================================================")
                break
        
    #
    def buyrobot():
        global paperclipsper
        global paperclips
        global money
        global sold
        global robots
        robots+=1
        typeout("Robot Purchased\n", 0, "")
        robotpc()
        print("======================================================")
    #
    def robotpc():
        global paperclipsper
        global paperclips
        global money
        global sold
        global robots
        if robots!=0:
            paperclips+=paperclipsper
            money=money-2

    def upgrade():
        global paperclipsper
        global paperclips
        global money
        global sold
        global robots
        robotpc()
        if money >= 50:
            paperclipsper+=1
            money-=50
            print("Upgrade Purchased")
        else:
            print("Insufficient Funds")
            print("======================================================")

        

    typeout("Welcome to Paperclip game!\n", 0, "")
    time.sleep(1)
    typeout("Press enter to start!", 1, "")
    print("======================================================")
    global paperclipsper
    global paperclips
    global money
    global sold
    global robots
    paperclipsper=1
    paperclips=0
    money=500
    sold=0
    robots=0
    printstats()
    print("======================================================")
    while True:
        if paperclips!=0:
            sell=random.randint(1,paperclips)
            paperclips=paperclips-sell
            money=money+(sell*4)
            print(f"Sold {sell} Paper Clips for ${sell*4}")
            print("======================================================")
        choice=getinput("Enter your choice,\n1 for make a Paper Clip,\n2 for buy a robot,\n3 for Upgrade,\n4 for Statistics,\nChoice: ", "str")
        if "1" in choice:
            print("======================================================")
            makepaperclip()
        elif "2" in choice:
            print("======================================================")
            buyrobot()
        elif "3" in choice:
            print("======================================================")
            upgrade()
        elif "4" in choice:
            print("======================================================")
            printstats()
        else:
            print("Skipping Action")
            print("======================================================")

def program36():
    while True:
        password=getinput("Enter Password", "str")
        ints=["1","2","3","4","5","6","7","8","9","0"]
        antisymbols=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for char in password:
            if char.isupper()==True:
                capital=True
            if char in ints:
                numbers=True
            if char not in antisymbols:
                symbols=True
        if len(password)>=10:
            length=True
        if capital==True and (numbers==True or symbols==True)==True and length==True:
            print("Your crap code works")




        



#==================================================================


selector()
