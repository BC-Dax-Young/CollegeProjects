
#======================{[SELECTOR PROCEDURE]}======================

def selector():
    programs=["Program1"]
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
    else:
        print("Error! Selection is not within bounds!")

#============================={[PROGRAMS]}==========================

def program1():
    print("AAAAAA")

#==================================================================



selector()