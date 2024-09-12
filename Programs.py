
#======================{[SELECTOR PROCEDURE]}======================

def selector():
    programs=["Dice Program", "Temperature Converter"]
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
        
    
    

#==================================================================



selector()
