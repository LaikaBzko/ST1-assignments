    ########################################################################################################################
    ########################################################################################################################
    ### Author: Laika Marshall                                                                                           ###
    ### Date Created: 16/08/2021                                                                                         ###
    ### Date Last Changed: 16/08/2021                                                                                    ###
    ### A simple program to help narrow down a restaurant to go to based on dietary restrictions                         ###
    ########################################################################################################################
    ########################################################################################################################


def main():
    while True: 
        print("\nWelcome to the interactive restaurant selection tool! Please type yes or no for each question")
        veggie = input("\nIs anyone in your party a vegetarian? ")
        if veggie == "no":
            #partyCounter = 0
            vegetarian = False
            break
        elif veggie == "yes":
            #partyCounter = 1
            vegetarian = True
            break
        else: 
            print("please input a valid selection!")
    while True: 
        vegan = input("\nIs anyone in your party a vegan? ")
        if vegan == "no":
            vegan = False
            break
        elif vegan == "yes":
            vegan = True
            #partyCounter = partyCounter + 3
            break
        else: 
            print("please input a valid selection! (yes/no)")
    while True: 
        gf = input("\nIs anyone in your party gluten free? ")
        if gf == "no":
            glutenFree = False
            break
        elif gf == "yes":
            glutenFree = True
            #partyCounter = partyCounter + 5
            break
        else: 
            print("please input a valid selection! (yes/no)")
    
    outputSelection(vegetarian, vegan, glutenFree)
    
    #################################################################### this was my first attempt, inspired by how unix handles permissions (a three digit int that is higher or lower based on read/write/execute permissions)
    # if partyCounter == 0:
    #     print("Joe's Gourmet Burgers")
    # elif partyCounter == 1:
    #     print("vegetarian YES, vegan NO, gf NO")
    # elif partyCounter == 3:
    #     print("vegetarian NO, vegan YES, gf NO")
    # elif partyCounter == 4:
    #     print("vegetarian YES, vegan YES, gf NO")
    # elif partyCounter == 5: 
    #     print("vegetarian NO, vegan NO, gf YES")
    # elif partyCounter == 6:
    #     print("vegetarian YES, vegan NO, gf YES")
    # elif partyCounter == 8:
    #     print("vegetarian NO, vegan YES, gf YES")
    # elif partyCounter == 9:
    #     print("vegetarian YES, vegan YES, gf YES")
    # else:
    #     print("something has gone wrong?")

def outputSelection(vegetarian, vegan, glutenFree):
    print("Here are your restaurant choices:")
    ########################################################################### my second attempt, not really inspired by anything
    # if (vegetarian == True) and (vegan == True) and (glutenFree == True):
    #     print(" The Chef's kitchen")
    #     print(" Corner Cafe")
    #     return
    # elif (vegetarian == True) and (vegan == False) and (glutenFree == True):
    #     print(" The Chef's kitchen")
    #     print(" Corner Cafe")
    #     print(" Main Street Pizza Company")
    #     return
    # elif (vegetarian == True) and (vegan == False) and (glutenFree == False):
    #     print(" The Chef's kitchen")
    #     print(" Corner Cafe")
    #     print(" Main Street Pizza Company")
    #     print(" Mama's Fine Italian")
    #     return
    # elif (vegetarian == False) and (vegan == False) and (glutenFree == False):
    #     print(" The Chef's kitchen")
    #     print(" Corner Cafe")
    #     print(" Main Street Pizza Company")
    #     print(" Mama's Fine Italian")
    #     print(" Joe's Gourmet Burgers")
    #     return

    ####### my third attempt, where i realised that rather than adding onto what we say, we should removve from a list. The try/except calls are so that we don't get valueErrors from trying to remove something that's already been removed
    restaurants = ["Joe's Gourmet Burgers", "Main Street Pizza Company", "Corner Cafe", "Mama's Fine Italian", "The Chef's Kitchen"]
    if vegetarian == True:
        restaurants.remove("Joe's Gourmet Burgers")
    if vegan == True:
        try:
            restaurants.remove("Joe's Gourmet Burgers")
        except ValueError:
            pass #do nothing!
        restaurants.remove("Main Street Pizza Company")
        restaurants.remove("Mama's Fine Italian")
    if glutenFree == True: 
        try:
            restaurants.remove("Joe's Gourmet Burgers")
        except ValueError:
            pass #do nothing!
        try:
            restaurants.remove("Mama's Fine Italian")
        except ValueError:
            pass #do nothing!
    for i in restaurants:
        print("     {}".format(i))
main()
