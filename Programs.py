
#======================{[SELECTOR PROCEDURE]}======================

def selector():
    programs=["Dice Program", "Temperature Converter", "Character Print", "Fishtank Volume", "Carpet Cost", "Energy Bill", "Circle Properties", "Ball Pit" ]
    counter=1
    print("Available/Allotted Programs: ")
    for i in programs:
        print(f"{counter}: {i}")
        counter+=1
    while True:
        while True:
            try: 
                selection=int(input("Enter the list integer number to select the desired program: "))
                break
            except Exception as error:
                print(f"Program has encoutered an error: {error}")
                continue
        program(selection)
        break            

#==================={[PROGRAM SELECTOR PROCEDURE]}===================

def program(selection):
    if selection==1:
        program1()
    elif selection==2:
        program2()
    elif selection==3:
        program3()
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
    
#==================================================================



selector()
