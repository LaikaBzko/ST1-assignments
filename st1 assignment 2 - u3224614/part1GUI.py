    ########################################################################################################################
    ########################################################################################################################
    ### Author: Laika Marshall                                                                                           ###
    ### Date Created: 25/10/2021                                                                                         ###
    ### Date Last Changed: 25/10/2021                                                                                    ###
    ### notes: project 1. Trans rights. GUI version. GUI is overrated, but that may just be the linux user in me.        ###
    ### this is gonna be structured a little different. It just helps, at least for me. 
    ########################################################################################################################
    ########################################################################################################################
import os
from tkinter import *
import webbrowser

root = Tk()
root.geometry("575x450")

###############
# frames
###############

topFrame = Frame(root)
midFrame = Frame(root)
botFrame = Frame(root)
listFrame = Frame(root)

topFrame.grid_rowconfigure(0, weight=1)
topFrame.grid_columnconfigure(0, weight=1)
topFrame.grid_columnconfigure(3, weight=1)

topFrame.grid(row=0, column=0, padx = 10, pady=10)
midFrame.grid(row=2,column=1,padx=10,pady=10)
listFrame.grid(row=2, column=0, padx = 10, pady = 10)
botFrame.grid(row=3,column=1,padx=15,pady=10)
###############
# functions
###############
def secret():
    webbrowser.open("https://youtu.be/dQw4w9WgXcQ", new=1, autoraise=True)

def populateBoxoid(): 
    boxoid.delete(0, END)
    with open("timeLog.txt", "r") as tRead:
        lineCount = 0
        for line in tRead:
            itemInput = "clip number {}".format(lineCount + 1)
            boxoid.insert(END, itemInput)
            lineCount = lineCount + 1

def getTotalPlayTime():
    if os.path.exists("timelog.txt"):                                                          
        with open("timeLog.txt", "r") as tRead:                                                
            secondsTotal = 0
            for line in tRead:
                currentLine = int(line)
                secondsTotal = secondsTotal + currentLine
            return(secondsTotal)
    else:
        pass

def getCurrentPlayTime(track):
    if os.path.exists("timelog.txt"):                                                          
        with open("timeLog.txt", "r") as tRead:                                                
            content = tRead.readlines()
            currentLine = int(content[track - 1])
            return(currentLine)
    else:
        pass

def updateInfo(e):                                                                    # this is hacky but hell, it works
    currentSelectionTempA = boxoid.curselection()
    currentSelectionTempB = int(currentSelectionTempA[0])
    currentSelection = currentSelectionTempB + 1
    currentTrackLabel.configure(text = "Track No. {}".format(currentSelection))
    newTrackLabel.configure(text = "Track No. {}".format(boxoid.size() + 1))
    totalTracksLabel.configure(text = "{} tracks".format(boxoid.size()))
    totalPlayTimeLabel.configure(text = "{} seconds".format(getTotalPlayTime()))
    currentTrackLengthLabel.configure(text="{} seconds".format(getCurrentPlayTime(currentSelection)))
    populateBoxoid()

def trackAdd():
    try:
        inputData = int((newTrackEntry.get()))
        outputData = str(inputData)
        with open("timeLog.txt", "a") as tLog, open("timeLog.txt", "r") as tRead:           # I don't know if we learnt 'with' commands, but I did it anyway
            tLog.write(outputData + "\n")
            tLog.close()
            populateBoxoid()
    except:
        pass

def quitProgram():
    root.destroy()

###############
# GUI elements
###############
boxoid = Listbox(listFrame, height = 16, width = 32, bd = 3, exportselection=False)
populateBoxoid()
boxoid.grid(row = 0, column = 0)
boxoid.bind('<<ListboxSelect>>', updateInfo)

newTrack = Label(midFrame, text="New Track Length")
newTrackEntry = Entry(midFrame, width = 21)

newTrackNo = Label(midFrame, text="New Track Number")
newTrackLabel = Label(midFrame, width = 18, relief = "groove")

currentTrackLength = Label(midFrame, text="Current Track Length")
currentTrackLengthLabel = Label(midFrame, width= 18, relief = "groove")

currentTrack = Label(midFrame, text="Current Track")
currentTrackLabel = Label(midFrame, width = 18, relief = "groove")

totalPlayTime = Label(midFrame, text="Total Playtime")
totalPlayTimeLabel = Label(midFrame, width = 18, relief = "groove")

totalTracks = Label(midFrame, text="Total Tracks")
totalTracksLabel = Label(midFrame, width = 18, relief = "groove")



newTrack.grid(row = 1, column = 0, pady=(15,3))
newTrackEntry.grid(row = 2, column = 0, padx = 10, pady=(2,10))
newTrackNo.grid(row = 1, column = 1, pady=(15,3))
newTrackLabel.grid(row = 2, column = 1, padx = 10, pady=(2,10))
currentTrackLength.grid(row = 3, column = 0, pady=(15,3))
currentTrackLengthLabel.grid(row = 4, column = 0, padx = 10, pady=(2,10))
currentTrack.grid(row = 3, column = 1, pady=(15,3))
currentTrackLabel.grid(row = 4, column = 1, pady=(2,10))
totalPlayTime.grid(row = 5, column = 0, padx = 10, pady=(15,3))
totalPlayTimeLabel.grid(row = 6, column = 0, padx = 10, pady=(2,10))
totalTracks.grid(row=5, column = 1, padx = 5, pady=(15,3))
totalTracksLabel.grid(row=6, column = 1, padx = 10, pady=(2,10))


boxUpdateButton = Button (botFrame, text = "Update", command = populateBoxoid, relief = "groove", bd = 2, padx = 15, pady=5)
addNewButton = Button (botFrame, text = "Add Track", command = trackAdd,  relief = "groove", bd = 2, padx = 15, pady=5 )
quitButton = Button (botFrame, text = "Quit", command = quitProgram,  relief = "groove", bd = 2, padx = 15, pady=5 )
boxUpdateButton.grid(row = 0, column=0, padx = 5, pady = 15)
addNewButton.grid(row = 0, column=1, padx = 5, pady = 15)
quitButton.grid(row = 0, column=2, padx = 5, pady = 15)

###############
# housekeeping
###############
mainMenu = Menu(root)
mainMenu.add_command(label = "secret :3", command = secret)
root.config(menu = mainMenu)

root.mainloop()



# ████████╗██████╗░░█████╗░███╗░░██╗░██████╗  ██████╗░██╗░██████╗░██╗░░██╗████████╗░██████╗
# ╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██╔════╝  ██╔══██╗██║██╔════╝░██║░░██║╚══██╔══╝██╔════╝
# ░░░██║░░░██████╔╝███████║██╔██╗██║╚█████╗░  ██████╔╝██║██║░░██╗░███████║░░░██║░░░╚█████╗░
# ░░░██║░░░██╔══██╗██╔══██║██║╚████║░╚═══██╗  ██╔══██╗██║██║░░╚██╗██╔══██║░░░██║░░░░╚═══██╗
# ░░░██║░░░██║░░██║██║░░██║██║░╚███║██████╔╝  ██║░░██║██║╚██████╔╝██║░░██║░░░██║░░░██████╔╝
# ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░  ╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░
