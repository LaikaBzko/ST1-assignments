    ########################################################################################################################
    ########################################################################################################################
    ### Author: Laika Marshall                                                                                           ###
    ### Date Created: 27/10/2021                                                                                         ###
    ### Date Last Changed: 27/10/2021                                                                                    ###
    ### notes: part 2, GUI version. I just woke up from a 4 hour 'powernap' at 12:30am, RIP my sleep schedule.           ###
    ########################################################################################################################
    ########################################################################################################################
from statistics import mean
from tkinter import *

root = Tk()
root.geometry("600x450")

###############
# frames
###############

topFrame = Frame(root)
midFrame = Frame(root)
botFrame = Frame(root)
finalFrame = Frame(root)

topFrame.grid(row = 0, column = 0, padx = 10, pady = 10)
midFrame.grid(row = 1, column = 0, padx = 10, pady = 10)
botFrame.grid(row = 2, column = 0, padx = 10, pady = 10)
finalFrame.grid(row = 3, column = 0, padx = 10, pady = 10)
###############
# functions
###############

def parseInput():
    with open ("steps.txt") as file:
        rawData = file.read().split('\n')
        global lines
        lines = list(map(int, rawData))

def topRow():
    global lines
    January = lines[0:31]
    Febuary = lines[31:59]
    March = lines[59:90]
    April = lines[90:120]
    JanMean = mean(January)
    FebMean = mean(Febuary)
    MarMean = mean(March)
    AprilMean = mean(April)
    janBox.configure(text=JanMean)
    febBox.configure(text=FebMean)
    marchBox.configure(text=MarMean)
    aprilBox.configure(text=AprilMean)

def midRow():
    global lines
    May = lines[120:151]
    June = lines[151:181]
    July = lines[181:212]
    August = lines[212:243]
    MayMean = mean(May)
    JuneMean = mean(June)
    JulyMean = mean(July)
    AugMean = mean(August)
    mayBox.configure(text=MayMean)
    juneBox.configure(text=JuneMean)
    julyBox.configure(text=JulyMean)
    augustBox.configure(text=AugMean)

def botRow():
    global lines
    September = lines[243:273]
    October = lines[273:304]
    November = lines[304:334]
    December = lines[334:365]
    SepMean = mean(September)
    OctMean = mean(October)
    NovMean = mean(November)
    DecMean = mean(December)
    sepBox.configure(text=SepMean)
    octBox.configure(text=OctMean)
    novBox.configure(text=NovMean)
    decBox.configure(text=DecMean)

def populate():
    global lines
    parseInput()
    topRow()
    midRow()
    botRow()
    totalBox.configure(text=mean(lines))

###############
# GUI elements
###############

janLabel = Label(topFrame, width = 18, text="January")
febLabel = Label(topFrame, width = 18, text="Febuary")
marchLabel = Label(topFrame, width = 18, text="March")
aprilLabel = Label(topFrame, width = 18, text="April")
janBox = Label(topFrame, width = 18, relief="groove")
febBox = Label(topFrame, width = 18, relief="groove")
marchBox = Label(topFrame, width = 18, relief="groove")
aprilBox = Label(topFrame, width = 18, relief="groove")

janLabel.grid(row=0, column=0,pady=10,padx=7)
febLabel.grid(row=0, column=1,pady=10,padx=7)
marchLabel.grid(row=0, column=2,pady=10,padx=7)
aprilLabel.grid(row=0,column=3,pady=10,padx=7)
janBox.grid(row=1, column=0)
febBox.grid(row=1, column=1)
marchBox.grid(row=1, column=2)
aprilBox.grid(row=1,column=3)

mayLabel = Label(midFrame, width = 18, text="May")
juneLabel = Label(midFrame, width = 18, text="June")
julyLabel = Label(midFrame, width = 18, text = "July")
augustLabel = Label(midFrame, width = 18, text = "August")
mayBox = Label(midFrame, width = 18, relief="groove" )
juneBox = Label(midFrame, width = 18, relief="groove")
julyBox = Label(midFrame, width = 18, relief="groove")
augustBox = Label(midFrame, width = 18, relief="groove")

mayLabel.grid(row=0, column=0, pady=10,padx=7)
juneLabel.grid(row=0, column=1,pady=10,padx=7)
julyLabel.grid(row=0, column=2,pady=10,padx=7)
augustLabel.grid(row=0,column=3,pady=10,padx=7)
mayBox.grid(row=1, column=0)
juneBox.grid(row=1, column=1)
julyBox.grid(row=1, column=2)
augustBox.grid(row=1, column=3)

sepLabel = Label(botFrame, width = 18, text="September")
octLabel = Label(botFrame, width = 18, text="October")
novLabel = Label(botFrame, width = 18, text="November")
decLabel = Label(botFrame, width = 18, text="December")
sepBox = Label(botFrame, width = 18, relief="groove")
octBox = Label(botFrame, width = 18, relief="groove")
novBox = Label(botFrame, width = 18, relief="groove")
decBox = Label(botFrame, width = 18, relief="groove")

sepLabel.grid(row=0, column=0, pady=10,padx=7)
octLabel.grid(row=0, column=1,pady=10,padx=7)
novLabel.grid(row=0, column=2,pady=10,padx=7)
decLabel.grid(row=0,column=3,pady=10,padx=7)
sepBox.grid(row=1,column=0)
octBox.grid(row=1,column=1)
novBox.grid(row=1,column=2)
decBox.grid(row=1,column=3)

totalLabel = Label(finalFrame, width = 36, text="Total")
totalBox = Label(finalFrame, width = 36, relief="groove")
totalLabel.grid(row=0,column=1,padx=10,pady=10)
totalBox.grid(row=1,column=1)

###############
# housekeeping
###############
root.after(250, populate)
root.mainloop()
