    ########################################################################################################################
    ########################################################################################################################
    ### Author: Laika Marshall                                                                                           ###
    ### Date Created: 26/10/2021                                                                                         ###
    ### Date Last Changed: 27/10/2021                                                                                    ###
    ### notes: project 2. That was an all nighter and I hate myself now. Still hate working with KTinker more though     ###
    ########################################################################################################################
    ########################################################################################################################
from statistics import mean

def parseInput():
    with open ("steps.txt") as file:
        rawData = file.read().split('\n')
        global lines
        lines = list(map(int, rawData))

def quarter1():
    January = lines[0:31]
    Febuary = lines[31:59]
    March = lines[59:90]
    print("January: {}".format(mean(January)))
    print("Febuary: {}".format(mean(Febuary)))
    print("March: {}".format(mean(March)))

def quarter2():
    April = lines[90:120]
    May = lines[120:151]
    June = lines[151:181]
    print("April: {}".format(mean(April)))
    print("May: {}".format(mean(May)))
    print("June: {}".format(mean(June)))

def quarter3():
    July = lines[181:212]
    August = lines[212:243]
    September = lines[243:273]
    print("July: {}".format(mean(July)))
    print("August: {}".format(mean(August)))
    print("September: {}".format(mean(September)))

def quarter4():
    October = lines[273:304]
    November = lines[304:334]
    December = lines[334:365]
    print("October: {}".format(mean(October)))
    print("November: {}".format(mean(November)))
    print("December: {}".format(mean(December)))

def year():
    quarter1()
    quarter2()
    quarter3()
    quarter4()
    print("yearly average: {}".format(mean(lines)))

def main():
    print("====================================")
    try:
        parseInput()
        year()
    except FileNotFoundError:
        print("Error! No existing source file. Please ensure the file is in the same directory \nas this program and is titled steps.txt")
    print("====================================")
main()
