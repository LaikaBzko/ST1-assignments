    ########################################################################################################################
    ########################################################################################################################
    ### Author: Laika Marshall                                                                                           ###
    ### Date Created: 16/08/2021                                                                                         ###
    ### Date Last Changed: 25/08/2021                                                                                    ###
    ### A simple program to track a population from given inputs                                                         ###
    ########################################################################################################################
    ########################################################################################################################



def main():
    print("====================================================")
    print("welcome to the simple population tracker tool!")
    startOrganisms = float(input("Please input the starting number of organisms: "))
    popIncrease = float(input("please input the daily population increase percentage (as decimal): "))
    simLength = int(input("please input the number of days to simulate: "))
    print("\n====================")    
    print("test parameters: ")
    print("starting organisms: {} organisms".format(startOrganisms))
    print("rate of multiplication: {}% per day".format(popIncrease))
    print("days the experiment will run: {} days".format(simLength))
    print("the simulation will now begin on return key press")
    input("====================")
    calculate(startOrganisms, popIncrease, simLength)


def calculate(organisms, multiplication, days):
    for i in range(days):
        if i > 0:
            organisms = organisms * (1 + (multiplication / 100)) 
        # print("increase: {}".format(increase))                here for testing purposes!
        print("\nday: {}".format(i+1))
        print("organisms: {}".format(round(organisms, 7)))
        i + 1


main()
