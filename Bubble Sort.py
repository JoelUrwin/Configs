def return_variables():
    #Used for passing variables into the Functions, since I had issues getting them in there.
    array = [9,5,4,15,3,8,11,2]
    maxrange = len(array)
    indexpiece_1 = 0
    indexpiece_2 = 1
    passes = 1
    total_comparisons = 1
    return array,maxrange,indexpiece_1,indexpiece_2,passes,total_comparisons



def menu():
    #Main Menu Function - Derived from my Angle Converter Program
    print("JoelTEK Bubble-Sort-Inator")
    print("Choose the Following Action:")
    print("A – Bubble Sort the Array in Ascending Order")
    print("B – Bubble Sort the Array in Descending Order")
    print("X – Exit Program")
    menuChoice = str(input("[A,B,X] : ")) # Asks for menu choice, casted as string since there aren't any numeric options.
    while menuChoice not in ["A","B","X"]: 
        print("Choice Invalid, Please try again.")
        menuChoice = str(input("[A,B,X] : "))
    return menuChoice


def ascending():
    array,maxrange,indexpiece_1,indexpiece_2,passes,total_comparisons = return_variables()
    while True:
        try:
        
            if indexpiece_2 == 9:
                #Resets the index after a pass
                indexpiece_1 = 0
                indexpiece_2 = 1
                passes += 1
                
            if array[indexpiece_1] > array[indexpiece_2]:
                #Compares two values within the list using the index
                temp = array[indexpiece_1]
                array[indexpiece_1] = array[indexpiece_2]
                array[indexpiece_2] = temp
                #Index is incremented by one per loop (this is not the same as a pass)
                indexpiece_1 += 1
                indexpiece_2 += 1
                total_comparisons += 1

                print(f"{array} |  Compared {array[indexpiece_1 - 1]} and {array[indexpiece_2 - 1]} (Indexes {indexpiece_1 - 1} and {indexpiece_2 - 1}) | Pass {passes}")
            
            else:
                #Comparing Numbers that do not need to be moved
                print(f"{array} |  Compared {array[indexpiece_1]} and {array[indexpiece_2]} (Indexes {indexpiece_1} and {indexpiece_2}) | Pass {passes}")
                #This still increments the index and reloops
                indexpiece_1 += 1
                indexpiece_2 += 1
                total_comparisons += 1
                #Total Comparisons isn't necessary but i added it.

        except IndexError:
            #IndexError is used to find out when the array is completely sorted.
            maxpassrange = maxrange - 1
            if passes == maxpassrange:
                print("")
                print(f"Sorted in {passes} Passes with {total_comparisons} Comparisons.")
                print("")
                break
            else:
                #If it's not complete, the index is reset and pass is incremented by one.
                indexpiece_1 = 0
                indexpiece_2 = 1
                passes += 1

def descending():
    array,maxrange,indexpiece_1,indexpiece_2,passes,total_comparisons = return_variables()
    while True:
        try:
            

            if indexpiece_2 == 9:
                #Resets the index after a pass
                indexpiece_1 = 0
                indexpiece_2 = 1
                passes += 1
                

            if array[indexpiece_2] > array[indexpiece_1]:
                #Compares two values within the list using the index
                temp = array[indexpiece_2]
                array[indexpiece_2] = array[indexpiece_1]
                array[indexpiece_1] = temp
                #Index is incremented by one per loop (this is not the same as a pass)
                indexpiece_1 += 1
                indexpiece_2 += 1
                total_comparisons += 1
                #Total Comparisons isn't necessary but i added it.

                print(f"{array} |  Compared {array[indexpiece_1 - 1]} and {array[indexpiece_2 - 1]} (Indexes {indexpiece_1 - 1} and {indexpiece_2 - 1}) | Pass {passes}")
            
            else:
                #Comparing Numbers that do not need to be moved
                print(f"{array} |  Compared {array[indexpiece_1]} and {array[indexpiece_2]} (Indexes {indexpiece_1} and {indexpiece_2}) | Pass {passes}")
                indexpiece_1 += 1
                indexpiece_2 += 1
                total_comparisons += 1

        except IndexError:
            #IndexError is used to find out when the array is completely sorted.
            maxpassrange = maxrange - 1
            if passes == maxpassrange:
                print("")
                print(f"Sorted in {passes} Passes with {total_comparisons} Comparisons.")
                print("")
                break
            else:
                #If it's not complete, the index is reset and pass is incremented by one.
                indexpiece_1 = 0
                indexpiece_2 = 1
                passes += 1


#Since the AngleConverter Program's Menu was to my liking, i've put it in here for the Menu System.
carryOn = True
while carryOn:
    selection = menu()
    if selection == "A":
        ascending() 
    elif selection == "B":
        descending()
    elif selection == "X":
        carryOn = False  
        print("Exiting.")
        break # Breaks the while loop



#Original Code (without modularisation or menus)
#while True:
#    try:
#        if indexpiece_2 == 9:
#            indexpiece_1 = 0
#            indexpiece_2 = 1
#            passes += 1
#            
#
#        if array[indexpiece_1] > array[indexpiece_2]:
#            temp = array[indexpiece_1]
#            array[indexpiece_1] = array[indexpiece_2]
#            array[indexpiece_2] = temp
#            indexpiece_1 += 1
#            indexpiece_2 += 1
#            total_comparisons += 1
#
#            print(f"{array} |  Compared {array[indexpiece_1 - 1]} and {array[indexpiece_2 - 1]} (Indexes {indexpiece_1 - 1} and {indexpiece_2 - 1}) | Pass {passes}")
#        
#        else:
#            print(f"{array} |  Compared {array[indexpiece_1]} and {array[indexpiece_2]} (Indexes {indexpiece_1} and {indexpiece_2}) | Pass {passes}")
#            indexpiece_1 += 1
#            indexpiece_2 += 1
#            total_comparisons += 1
#
#    except IndexError:
#        maxpassrange = maxrange - 1
#        if passes == maxpassrange:
#            print("")
#            print(f"Sorted in {passes} Passes with {total_comparisons} Comparisons.")
#            print("")
#            break
#        else:
#            indexpiece_1 = 0
#            indexpiece_2 = 1
#            passes += 1

