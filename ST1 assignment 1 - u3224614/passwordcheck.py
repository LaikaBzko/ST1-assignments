    ########################################################################################################################
    ########################################################################################################################
    ### Author: Laika Marshall                                                                                           ###
    ### Date Created: 07/09/2021                                                                                         ###
    ### Date Last Changed: 07/09/2021                                                                                    ###
    ### A not so simple program created to check password integrity,                                                     ###
    ### (and for me to teach myself about classes and methods in python)                                                 ###
    ########################################################################################################################
    ########################################################################################################################

from string import punctuation
#define the class for passwords
class passwordChecker:
    def __init__(self, charMin, symbolsMin, specialChars, passwrdToChk):
        self.charMin=int(charMin)
        self.symbolsMin=int(symbolsMin)
        self.specialChars=bool(specialChars)
        self.passwrdToChk=passwrdToChk
#checks the length of the password
    def charCheck(self):
        if len(self.passwrdToChk) < self.charMin:
            return False
        elif len(self.passwrdToChk) >= self.charMin:
            return True
#checks if numbers (0-9) and punctuation (!,@,#,$ etc..) are present, and how many are present
    def symbolsCheck(self):
        punctuationCounter = 0
        numCounter = 0
        nums = ("1","2","3","4","5","6","7","8","9","0")
        symbols = set(punctuation)
        for i in self.passwrdToChk:
            if i in symbols:
                punctuationCounter += 1
            if i in nums: 
                numCounter += 1
        symbolsTotal = numCounter + punctuationCounter
        if symbolsTotal >= self.symbolsMin:
            return True
        else:
            return False
#checks if special characters are allowed or not, and if they aren't, checks if the password is alpha-numeric only (doesn't include punctuation!)
    def specialCharsCheck(self):
        if self.specialChars == False:
            return self.passwrdToChk.isalnum()
        else:
            return True
#reminds you of the requirements for a password
    def requirements(self): 
        print("###################################")
        print("requirements for password as follow: ")
        print("special characters allowed?: {}".format(self.specialChars))
        print("required number of numerical symbols: {}".format(self.symbolsMin))
        print("required number of characters: {}".format(self.charMin))
        print("your password is: {}".format(self.passwrdToChk))
        print("###################################")
# runs the checks and balances
    def assignmentPasswordCheck(self):
        if self.charCheck() == True and self.symbolsCheck() == True and self.specialCharsCheck() == True:
            print("This password fulfills all necessary requirements!")
        elif self.charCheck() == False:
            print("This password does not have enough characters!")
        elif self.symbolsCheck() == False: 
            print("This password does not contain the required amount of symbols!")
        elif self.specialCharsCheck() == False: 
            print("This password contains forbidden special characters!")
        else:
            print("something went very wrong here")

#Requirements are assigned here!

def getInputs():
    global passwordInput
    global charMinInput
    global symbolsMinInput
    passwordInput = input("please input a password: ")
    charMinInput = int(input("please input minimum number of characters: "))
    symbolsMinInput = int(input("please input minimum number of symbols: "))

    while True:
        specialCharsInput = input("Allow special symbols? (y/n): ")
        global specialCharsChoice
        if specialCharsInput == "n":
            specialCharsChoice = False
            break
        elif specialCharsInput == "y":
            specialCharsChoice = True
        else: 
            print("Please input a valid selection!")


def main():
    global passwordInput
    global charMinInput
    global symbolsMinInput
    global specialCharsChoice
    getInputs()
    assignReqs = passwordChecker(charMinInput, symbolsMinInput, specialCharsChoice, passwordInput)
    assignReqs.requirements()
    assignReqs.assignmentPasswordCheck()

main()