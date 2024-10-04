
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
              "Days",#22
              "Dice Game",#23
              "Division",#24
              "Dogs life",#25
              "Electric Car",#26
              "Twitter",#27
              "Initial and Surname",#28
              "Inventory ",#29
              "Flight",#30
              "Teacher Code",#31
              "Email",#32
              "Seperator",#33
              "Ascii EBCDIC",#34
              "Paper Clip Game",#35
              "Time Tables",#36
              "Factorial",#37
              "Green Bottles",#38
              "ASCII Art",#39
              "Fizz Buzz",#40
              "Scrabble",#41
              "Passcode",#42
              "Cassini Problem",#43
              "Prime test",#44
              "Compount Interest",#45
              "Car Depreaciation",#46
              "Discount Counter",#47
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

def program10():
    # Number Comparator program
    
    # Get two integer inputs from the user
    num1 = getinput("Enter Number 1: ", "int")
    num2 = getinput("Enter Number 2: ", "int")

    # Compare the two numbers and print the result
    if num1 < num2:
        print(num2)  # If num1 is smaller, print num2
    elif num1 > num2:
        print(num1)  # If num1 is larger, print num1
    else:
        print("They are the same")  # If both numbers are equal, print this message

def program11():
    # Water States program

    # Get temperature input from the user
    temp = getinput("Temperature", 0)  # custom function for input validation

    # Determine the state of water based on temperature
    if temp > 100:
        print("Gas")  # Water is in gaseous state (steam) above 100°C
    elif temp < 100 and temp > 0:
        print("Liquid")  # Water is liquid between 0°C and 100°C
    else:
        print("Solid")  # Water is solid (ice) at or below 0°C

def program12():
    # Career Quotes program

    # Get the job input from the user and convert it to lowercase
    job = input("Job: ").lower()

    # Check the job input and print the corresponding quote
    if job == "engineer":
        print("The engineer has been, and is, a maker of history.")
    elif job == "developer":
        print("Logical thinking, passion and perseverance is the paint on your palette.")
    elif job == "analyst":
        print("Seeing what other people can't see gives you great vision.")
    else:
        # If the job doesn't match any predefined options, print a default message
        print("I'm sorry. We could not find a quote for your job.")

def program13():
    # Currency Converter program

    # Get the target currency from user input and convert to lowercase
    currency = input("Enter Currency, GBP to USD, Euro, Yuan or Yen: ").lower()

    # Get the amount to convert from user input (as an integer)
    amount = getinput("Enter amount: ", "int")

    # Convert GBP to the specified currency
    if currency == "usd":
        print(f"{amount} GBP = {amount*1.35} USD")
    elif currency == "euro":
        print(f"{amount} GBP = {amount*1.20} Euro")
    elif currency == "yuan":
        print(f"{amount} GBP = {amount*9.37} Yuan")
    elif currency == "yen":  # Fixed: changed "euro" to "yen"
        print(f"{amount} GBP = {amount*193.26} Yen")
    else:
        print("Invalid Currency")

def program14():
    def dose():
        # Get the dosage input from the user and convert it to an integer
        doseage = getinput("Enter dosage: ", "int")
        
        # Determine the value based on the dosage
        if doseage > 10:
            val = 3
        else:
            if doseage > 2.5:
                val = 2
            else:
                if doseage > 1:
                    val = 1
                else:
                    val = 0.5
        
        # Print the result
        print(f"For {doseage} nitrate dose {val} ml")
        
    dose()

def program15():
    def determine_grade(scores, breakpoints=[1, 2, 4, 13, 22, 31, 41, 54, 67, 80], grades='U123456789'):
        while True:
            try:
                # Find the position to insert the score in the breakpoints list
                i = bisect.bisect(breakpoints, scores)
                
                # Return the corresponding grade and the points needed to reach the next breakpoint
                return grades[i], breakpoints[int(grades[i])] - scores
                break
            except:
                # Continue the loop if an exception occurs
                continue
    
    # Get the grade input from the user and convert it to an integer
    grade = getinput("Enter Grade: ", "int")
    
    # Determine the grade and the points needed
    dtrgrade, needed = determine_grade(grade)
    
    # Print the result
    print(f"You got a grade {dtrgrade}, you need {needed} more points.")


def program16():
    # Define the elements with their properties
    Hydrogen = ["Hydrogen", "H", 1, 1.0078]
    Lithium = ["Lithium", "Li", 3, 6.9410]
    Beryllium = ["Beryllium", "Be", 4, 9.0122]
    
    # Get the element input from the user
    element = input("Enter the element: ")
    
    # Check if the input element is in the Hydrogen list
    if element in Hydrogen:
        print("Hydrogen Info:")
        for i in Hydrogen:
            print(i)
    # Check if the input element is in the Lithium list
    elif element in Lithium:
        print("Lithium Info:")
        for i in Lithium:
            print(i)
    # Check if the input element is in the Beryllium list
    elif element in Beryllium:
        print("Beryllium Info:")
        for i in Beryllium:
            print(i)

def program17():
    # Define lists for full day names, short day names, and character representations
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    shortday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    char = ["M", "Tu", "W", "Th", "F", "Sa", "Su"]
    
    # Get the day input from the user and capitalize the first letter
    value = input("Enter day:").title()
    
    # Check if the input value is in the full day names list
    if value in day:
        daypos = day.index(value)
        print(shortday[daypos])
        print(char[daypos])
    # Check if the input value is in the short day names list
    elif value in shortday:
        daypos = shortday.index(value)
        print(day[daypos])
        print(char[daypos])
    # Check if the input value is in the character representations list
    elif value in char:
        daypos = char.index(value)
        print(day[daypos])
        print(shortday[daypos])


def program18():
    # Get the purchase cost input from the user and convert it to a float
    purchasecost = getinput("Enter Cost", "float")
    
    # Round up the purchase cost to the nearest whole number
    rounded = np.ceil(purchasecost)
    
    # Calculate the difference between the rounded amount and the actual purchase cost
    diff = rounded - purchasecost
    
    # Print the item cost, the rounded amount paid, and the amount saved to savings
    print(f"Item cost: {purchasecost},\nPaid Amount: {rounded},\nSaved to Savings: {diff}")


def program19():
    # Get the number of sides for the die from the user and convert it to an integer
    die = getinput("How many sides to your die?: ", "int")
    
    # Roll the die and print the result
    print(f"Your {die}-sided die rolled a {random.randint(1, die)}")


def program20():
    def clamp():
        # Get the first number input from the user and convert it to an integer
        num1 = getinput("Enter Number 1: ", "int")
        
        # Get the second number input from the user and convert it to an integer
        num2 = getinput("Enter Number 2: ", "int")

        # Compare the two numbers and print the larger one
        if num1 < num2:
            print(num2)
        elif num1 > num2:
            print(num1)
        else:
            # If the numbers are equal, print either one
            print(num1)
    
    clamp()


def program21():
    # Get the year input from the user and convert it to an integer
    year = getinput("Enter year: ", "int")
    
    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year.")


def program22():
    # Get the number of hours input from the user and convert it to an integer
    hours = getinput("Enter Number of hours: ", "int")
    
    # Calculate the number of full days
    print(hours // 24)

def program23():
    # Prompt the user to roll the first dice and generate a random number between 1 and 6
    input("Roll dice one?")
    dice1 = random.randint(1, 6)
    print(dice1)
    
    # Prompt the user to roll the second dice and generate a random number between 1 and 6
    input("Roll dice two?")
    dice2 = random.randint(1, 6)
    print(dice2)
    
    # Prompt the user to roll the third dice and generate a random number between 1 and 6
    input("Roll dice three?")
    dice3 = random.randint(1, 6)
    print(dice3)
    
    def scoredice(d1, d2, d3):
        # Check if all three dice have the same value
        if d1 == d2 == d3:
            score = d1 + d2 + d3
        # Check if the first and second dice have the same value
        elif d1 == d2:
            score = d1 + d2
            score -= d3
        # Check if the second and third dice have the same value
        elif d3 == d2:
            score = d2 + d3
            score -= d1
        # Check if the first and third dice have the same value
        elif d1 == d3:
            score = d1 + d3
            score -= d2
        # If no dice have the same value, the score is 0
        else:
            score = 0
        return score
    
    # Calculate and print the score based on the dice values
    print(scoredice(dice1, dice2, dice3))


def program24():

    def div(val1, val2):
        # Check if either value is zero
        if val1 == 0 or val2 == 0:
            return False
        # Check if val1 is divisible by val2
        elif val1 % val2 == 0:
            return True
        else:
            return False

    # Get two integer inputs from the user and check divisibility
    div(getinput("Enter Number 1: ", "int"), getinput("Enter Number 2: ", "int"))


def program25():
    # Get the dog's age input from the user and convert it to a float
    age = getinput("Enter age: ", "float")
    
    # Calculate the dog's age in human years for the first two years
    if age <= 2:
        print(f"Your dog is {age * 12} years old.")
    # Calculate the dog's age in human years for ages greater than two years
    elif age > 2:
        print(f"Your dog is {24 + (age - 2) * 6} years old.")


def program26():
    # Get the number of minutes parked from the user and convert it to an integer
    time = getinput("Enter number of minutes parked: ", "int")
    
    # Calculate the points earned based on the time parked
    points = 1.5 * time
    
    # Calculate the price to be paid based on the time parked
    price = 1 + (0.2 * time)
    
    # Print the amount owed and the points earned
    print(f"You owe ${price} and earned {points} points")


def program27():
    while True:
        # Prompt the user to enter a tweet
        tweet = input("Tweet: ")
        
        # Check if the tweet exceeds the maximum character limit
        if len(tweet) > 20:
            print("Tweet Exceeds maximum character limit!")
        else:
            # Print the tweet if it is within the limit
            print(tweet)


def program28():
    # Get the forename input from the user
    forename = input("Enter Forename: ")
    
    # Get the surname input from the user
    surname = input("Enter Surname: ")
    
    # Print the initial of the forename in uppercase and the surname in uppercase
    print(forename[0].upper(), surname.upper())


def program29():
    def exists(inv, check):
        # Check if any item in the check list exists in the inventory list
        if any(x in inv for x in check) == True:
            print(True)
        else:
            print(False)
    
    # Define the player's inventory list
    plrinv = ["Sword", "Shield", "Potion", "Amulet"]
    
    # Define the list of items to check
    invcheck = ["Shield", "Potion", "Charm", "Bow"]
    
    # Check if any items in invcheck exist in plrinv
    exists(plrinv, invcheck)


def program30():
    # Get the first city input from the user
    city1 = getinput("Enter First City: ", "str")
    
    # Get the second city input from the user
    city2 = getinput("Enter Second City: ", "str")
    
    # Create the flight code by taking the first four letters of each city, converting to uppercase, and joining with a hyphen
    flight = city1[0:4].upper() + "-" + city2[0:4].upper()
    
    # Print the flight code
    print(flight)


def program31():
    # Define lists for names
    dax = ["Dax", "Aleckzander", "Young"]
    ebony = ["Ebony-Jayne", "Sapphire", "Davies-Waterhouse"]
    filip = ["Filip", " ", "Trzcinski"]
    
    # Check if there is a space in the 'filip' list and insert 'Z' in the appropriate position
    if " " in filip:
        pos = filip.index(" ")
        filiptrz = filip
        filip.insert(pos, "Z")
        filip.insert(pos + 1, filiptrz)
    
    def abbreviate(name_list):
        # Create an abbreviation by taking the first letter of each name part
        abbreviation = name_list + name_list + name_list
        print(abbreviation)
    
    # Abbreviate and print the names
    abbreviate(dax)
    abbreviate(ebony)
    abbreviate(filip)



def program32():
    # Prompt the user to enter an email address
    email = input("Enter email: ")
    
    # Check if the email contains both "@" and "."
    if "@" in email and "." in email:
        # If both are present, print that the email is valid
        print("Email Valid")
    else:
        # If either is missing, print that the email is invalid
        print("Email Invalid")

def program33():
    # Prompt the user to enter a name and convert it to title case
    name = input("Enter name:").title()
    
    # Split the name into individual words
    split = name.split()
    
    # Iterate through each word in the split name
    for i in split:
        # Print each word in title case
        print(i.title())

            
def program34():
    # Define a dictionary with ASCII and EBCDIC values for each letter and space
    dictionary = {
        "A": "Ascii: 65\n EBCDIC:193",
        "B": "Ascii: 66\n EBCDIC:194",
        "C": "Ascii: 67\n EBCDIC:195",
        "D": "Ascii: 68\n EBCDIC:196",
        "E": "Ascii: 69\n EBCDIC:197",
        "F": "Ascii: 70\n EBCDIC:198",
        "G": "Ascii: 71\n EBCDIC:199",
        "H": "Ascii: 72\n EBCDIC:200",
        "I": "Ascii: 73\n EBCDIC:201",
        "J": "Ascii: 74\n EBCDIC:209",
        "K": "Ascii: 75\n EBCDIC:210",
        "L": "Ascii: 76\n EBCDIC:211",
        "M": "Ascii: 77\n EBCDIC:212",
        "N": "Ascii: 78\n EBCDIC:213",
        "O": "Ascii: 79\n EBCDIC:214",
        "P": "Ascii: 80\n EBCDIC:215",
        "Q": "Ascii: 81\n EBCDIC:216",
        "R": "Ascii: 82\n EBCDIC:217",
        "S": "Ascii: 83\n EBCDIC:226",
        "T": "Ascii: 84\n EBCDIC:227",
        "U": "Ascii: 85\n EBCDIC:228",
        "V": "Ascii: 86\n EBCDIC:229",
        "W": "Ascii: 87\n EBCDIC:230",
        "X": "Ascii: 88\n EBCDIC:231",
        "Y": "Ascii: 89\n EBCDIC:232",
        "Z": "Ascii: 90\n EBCDIC:233",
        " ": "Ascii: 32\n EBCDIC:64"
    }

    # Prompt the user to enter a letter to look up
    lookup = input("Enter Letter to lookup: ").upper()
    
    # Print the ASCII and EBCDIC values for the entered letter
    print(dictionary[lookup])


def program35():
    # Print a separator line
    print("======================================================")

    # Function to print the current statistics
    def printstats():
        global paperclipsper
        global paperclips
        global money
        global sold
        global robots
        # Print the number of paper clips
        typeout(f"You have {paperclips} Paper Clips\n", 0, "")
        # Print the amount of money
        typeout(f"You have {money} Dollars\n", 0, "")
        # Print the number of paper clips sold
        typeout(f"You have sold {sold} Paper Clips\n", 0, "")
        # Print the number of robots making paper clips
        typeout(f"You have {robots} Robots making Paper Clips\n", 0, "")

    # Function to make paper clips
    def makepaperclip():
        global paperclipsper
        global paperclips
        global money
        global sold
        global robots
        while True:
            # Call the robotpc function
            robotpc()
            # Prompt the user to make paper clips or exit
            var = getinput(f"Press Enter to make {paperclipsper} Paper Clip or type exit to exit: ", "str")
            if "exit" not in var:
                # Deduct $2 from money and add paper clips
                money = money - 2
                paperclips += paperclipsper
                print(f"Made {paperclipsper} Paper Clips for $2.")
                continue
            else:
                # Print a separator line and exit the loop
                print("======================================================")
                break
        
    # Function to buy a robot
    def buyrobot():
        global paperclipsper
        global paperclips
        global money
        global sold
        global robots
        # Increase the number of robots by 1
        robots += 1
        typeout("Robot Purchased\n", 0, "")
        # Call the robotpc function to update paper clips and money
        robotpc()
        print("======================================================")
    
    # Function to handle robot paper clip production
    def robotpc():
        global paperclipsper
        global paperclips
        global money
        global sold
        global robots
        if robots != 0:
            # Increase paper clips and decrease money for each robot
            paperclips += paperclipsper
            money -= 2

    # Function to upgrade paper clip production
    def upgrade():
        global paperclipsper
        global paperclips
        global money
        global sold
        global robots
        # Call the robotpc function to update paper clips and money
        robotpc()
        if money >= 50:
            # Increase paper clips per production and decrease money
            paperclipsper += 1
            money -= 50
            print("Upgrade Purchased")
        else:
            print("Insufficient Funds")
            print("======================================================")

    # Welcome message and game initialization
    typeout("Welcome to Paperclip game!\n", 0, "")
    time.sleep(1)
    typeout("Press enter to start!", 1, "")
    print("======================================================")
    
    # Initialize global variables
    global paperclipsper
    global paperclips
    global money
    global sold
    global robots
    paperclipsper = 1
    paperclips = 0
    money = 500
    sold = 0
    robots = 0
    
    # Print initial statistics
    printstats()
    print("======================================================")
    
    while True:
        if paperclips != 0:
            # Randomly sell some paper clips and update money
            sell = random.randint(1, paperclips)
            paperclips -= sell
            money += sell * 4
            print(f"Sold {sell} Paper Clips for ${sell * 4}")
            print("======================================================")
        
        # Prompt the user for their choice of action
        choice = getinput("Enter your choice,\n1 for make a Paper Clip,\n2 for buy a robot,\n3 for Upgrade,\n4 for Statistics,\nChoice: ", "str")
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
    def TimesTable(x):
        for counter in range(1, 13):
            print(f"{counter} x {x} = {counter * x}")
    TimesTable(getinput("Enter Number: ", "int"))

def program37():
    num = getinput("Enter Number: ", "int")
    numbers = ""
    
    # Build the multiplication string
    while num != 0:
        
        if numbers == "":
            stringnum = str(num)
            num -= 1
            numbers = stringnum

        else:

            stringnum = str(num)
            num -= 1
            numbers = numbers + "*" + stringnum

    
    # Evaluate the multiplication string safely
    evaluated = eval(numbers)
    print(f"{numbers} = {evaluated}")


def program38():
    def lyrics(number, bottle):
        print(f"{number} green {bottle} hanging on the wall,\n{number} green {bottle} hanging on the wall,\nAnd if one green bottle should accidentally fall\nThere'll be {number-1} green {bottle} hanging on the wall.")
    number=10
    bottle="bottles"
    while number!=1:
        lyrics(number, bottle)
        number-=1
    lyrics(1, "bottle")

def program39():
    name=getinput("Enter name: ", "str")
    nameart=""
    for x in name:
        nameart=nameart+"|"+x.upper()
    print("+-+-+-+-+-+-+-+-+-+-+-+-+")
    print(nameart+"|")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+")

def program40():
    def fizz_buzz(n):
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

    fizz_buzz(getinput("Enter Number: ", "int"))

def program41():
    one=["E","A","I","O","N","R","T","L","S","U"]
    two=["D","G"]
    three=["B","C","M","P"]
    four=["F","H","V","W","Y"]
    five="K"
    eight=["J","X"]
    ten=["Q","Z"]
    scrabble=getinput("Enter Word: ", "str")
    score=0
    for char in scrabble:
        if char in one:
            score+=1
        elif char in two:
            score+=2
        elif char in three:
            score+=3
        elif char in four:
            score+=4
        elif char in five:
            score+=5
        elif char in eight:
            score+=8
        elif char in ten:
            score+=10
    print(f"You got {score}!")


def program42():
    passcode=""
    password=getinput("Enter passcode: ", "str")
    vowels=["A","E","I","O","U","a","e","i","o","u"]
    for char in password:
        if char in vowels:
            num=random.randint(0,9)
            passcode=passcode+str(num)
    print(f"Your passcode is: {passcode}")
    
def program43():
    binary=getinput("Enter binary: ", "str")
    counter=0
    for x in binary:
        if x == "1":
            counter+=1
    if counter % 2 == 0:
        print("Even")
    else:
        print("Odd")

def program44():
    def is_prime(num):
        # Initialize a flag variable
        flag = True

        # Numbers less than 2 are not prime
        if num < 2:
            flag = False
        else:
            # Check for factors from 2 to num-1
            for i in range(2, num):
                if num % i == 0:
                    flag = False
                    break

        # Return the result based on the flag variable
        return flag

    # Example usage
    number = getinput("Enter Number: ", "int")
    if is_prime(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

def program45():
    balance=getinput("Enter Balance: ", "int")
    interest=0.04
    desiredbal=getinput("Enter Desired Balance: ", "int")
    while not balance>=desiredbal:
        print(f"Your balance is {balance}.")
        balance=balance*(1+interest)
        input("Press Enter to skip a year")

def program46():
    balance=getinput("Enter Value: ", "int")
    desiredbal=getinput("Enter Resale Value: ", "int")
    print(f"Your car Value is {balance}.")
    balance=balance-(0.3*balance)
    input("Press Enter to skip a year")
    while balance>desiredbal:
        print(f"Your car Value is {balance}.")
        balance=balance-(0.2*balance)
        input("Press Enter to skip a year")

def program47():
    balance=10
    desiredbal=getinput("Enter Final Discount: ", "int")
    print(f"Your current Discount is 0%.")
    balance=balance-(0.5*balance)
    input("Press Enter to skip a week")
    while balance>desiredbal:
        print(f"Your Discount Value is {balance}.")
        balance=balance-(0.5*balance)
        input("Press Enter to skip a year")

def program48():

    


        



#==================================================================


selector()
