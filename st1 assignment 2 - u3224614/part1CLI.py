    ########################################################################################################################
    ########################################################################################################################
    ### Author: Laika Marshall                                                                                           ###
    ### Date Created: 25/10/2021                                                                                         ###
    ### Date Last Changed: 25/10/2021                                                                                    ###
    ### notes: project 1. CLI version. CLI is so much better than GUI and I'll die on this hill if I have to             ###
    ########################################################################################################################
    ########################################################################################################################
import os

def newLogEntry():
    while True:                                                                                 # we need a loop for input validation! I mean not really but this is the approach I took /shrug
        try:
            print("\n =================")
            print("Adding a new runtime length to log...   ")
            secondsInput = int(input("Please input length of video (in seconds): "))            # more input validation stuff!
            secondsOutput = str(secondsInput)
            with open("timeLog.txt", "a") as tLog, open("timeLog.txt", "r") as tRead:           # I don't know if we learnt 'with' commands, but I did it anyway
                tLog.write(secondsOutput + "\n")
                lineCount = 0
                tLog.close()
                tRead
                for line in tRead:
                    lineCount = lineCount + 1
                print("Added entry of {} seconds to line {} of log".format(secondsOutput, lineCount))
                tRead.close()
            input("================= \n")
            break
        except ValueError:                                                                      # there's that funky input validation
            input("Please input a numerical parameter!")
            continue


def displayLog():
    print("\n =================")
    if os.path.exists("timelog.txt"):                                                           # because if I don't do this and the file gets deleted, it'll throw an error
        with open("timeLog.txt", "r") as tRead:                                                 # 'with' statements are really cool and I like them :3
            lineCount = 0
            secondsTotal = 0
            for line in tRead:
                print("clip {}, duration (seconds): {} ".format(lineCount + 1, line))
                lineCount = lineCount + 1
                currentLine = int(line)
                secondsTotal = secondsTotal + currentLine
            print("total lines: {}".format(lineCount))
            print("total seconds of runtime: {}".format(secondsTotal))                          # this worked on the first try and honestly I was pretty impressed
            input("================= \n")
    else:
        print("no existing runtime log file!")                                                  # much better this than the program erroring and peacing out
        input("================= \n")

def deleteLog():                                                                                # wasn't needed but I thought it would be a cool addition. Giving me extra marks for this would be super cool (hint hint)
    if os.path.exists("timeLog.txt"):
        os.remove("timeLog.txt")
        print("done!")
    else:
        print("runtime Log does not exist!")
    input("================= \n")

def menu():
    while True:
        print("\n Welcome to the simple runtime tracking program! What would you like to do? \n    1. record a new runtime \n    2. Display runtimes \n    3. exit the program \n    4. reset program")
        choice = input("> ")
        if choice == "1":
            newLogEntry()
            continue
        if choice == "2": 
            displayLog()
            continue
        if choice == "3":
            input("goodbye!")
            quit()
        if choice == "4":
            deleteLog()
            continue
        else:
            print("please input a valid selection")
            input("================= \n ")


def main():                         # why did I write individual functions and put them in a menu method and then put that in main? because I felt like it tbqh x3
    menu()

main()

# ████████╗██████╗░░█████╗░███╗░░██╗░██████╗  ██████╗░██╗░██████╗░██╗░░██╗████████╗░██████╗
# ╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██╔════╝  ██╔══██╗██║██╔════╝░██║░░██║╚══██╔══╝██╔════╝
# ░░░██║░░░██████╔╝███████║██╔██╗██║╚█████╗░  ██████╔╝██║██║░░██╗░███████║░░░██║░░░╚█████╗░
# ░░░██║░░░██╔══██╗██╔══██║██║╚████║░╚═══██╗  ██╔══██╗██║██║░░╚██╗██╔══██║░░░██║░░░░╚═══██╗
# ░░░██║░░░██║░░██║██║░░██║██║░╚███║██████╔╝  ██║░░██║██║╚██████╔╝██║░░██║░░░██║░░░██████╔╝
# ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░  ╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░