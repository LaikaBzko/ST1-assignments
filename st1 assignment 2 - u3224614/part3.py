    ########################################################################################################################
    ########################################################################################################################
    ### Author: Laika Marshall                                                                                           ###
    ### Date Created: 27/10/2021                                                                                         ###
    ### Date Last Changed: 27/10/2021                                                                                    ###
    ### Notes: Part 3, CLI version. Dear Diary, should I get a real diary instead of entering logs in programming        ###
    ### assignments?                                                                                                     ###
    ########################################################################################################################
    ########################################################################################################################
import pickle                                       # need this for saving / loading
import os                                           # need this for checking existence of file

employeeRecords = {}                                # this is here as a duplicate because my IDE hates me :(

class Employee():
    def __init__(self, idNum, name, department, jobTitle):
        self.idNum=int(idNum)
        self.name=name
        self.department=department
        self.jobTitle=jobTitle

    def employeeInfo(self):                         # this only actually gets used by the subclasses x3
        print("\n===============")
        print("Employee name: {}".format(self.name))
        print("Employee ID: {}".format(self.idNum))
        print("Emplyoee Department: {}".format(self.department))
        print("Employee Job Title: {}\n".format(self.jobTitle))

    def saveInDict(self):
        employeeRecords[self.idNum] = [self.name, self.department, self.jobTitle]
    
    def setidNum(self, newID):
        self.idNum = newID
    
    def setName(self, newName):
        self.name = newName
    
    def setDept(self, newDept):
        self.department = newDept

    def setJobTitle(self, newTitle):
        self.jobTitle = newTitle

class ShiftEmployee(Employee):
    def __init__(self, idNum, name, department, jobTitle, shiftNo, payRate):
        super().__init__(idNum, name, department, jobTitle)
        self.shiftNo = int(shiftNo)
        self.payRate = float(payRate)
    def get_special_attrs(self):
        return(self.shiftNo, self.payRate)
    def set_shift(self, newShiftNo):
        self.shiftNo = newShiftNo
    def set_payRate(self, newPayRate):
        self.payRate = newPayRate
    def sEmployeeInfo(self):
        self.employeeInfo()
        print("Shift Employee specific Information:")
        print("Employee Shift Number: {}".format(self.get_special_attrs()[0]))
        print("Employee Pay Rate: {}".format(self.get_special_attrs()[1]))

class Contractor(Employee):
    def __init__(self, idNum, name, department, jobTitle, contractEnd, ABN, contractSalary):
        super().__init__(idNum, name, department, jobTitle)
        self.contractEnd = int(contractEnd)     #I like to imagine that if further developed, one would use a UNIX timestamp. 
        self.ABN = int(ABN)
        self.contractSalary = int(contractSalary) #salaries aren't floats right? Like, they'd be round numbers because common sense? At least that's what you'd think...
    def ContractorInfo(self):
        self.employeeInfo()
        print("Contractor specific Information:")
        print("Contract End Date: {}".format(self.contractEnd))
        print("Contractor ABN: {}".format(self.ABN))
        print("Contractor fixed Salary: {}".format(self.contractSalary))

# the following work with the dict rather than the object itself because dicts are more flexible
def updateEmployee(employee, field, newInfo):
    oldInfo = employeeRecords[employee]                   # save this for later
    print("===============")
    print("Old attributes:")
    print("Name: {}".format(oldInfo[0]))
    print("Department: {}".format(oldInfo[1]))
    print("Job Title: {}".format(oldInfo[2]))
    print("===============\n")
    temp = Employee(employee, oldInfo[0], oldInfo[1], oldInfo[2])
    setattr(temp, field, newInfo)           # changes the asked for attribute
    temp.saveInDict()
    newInfo = employeeRecords[employee]
    print("Done!")
    searchEmployee(employee)

def searchEmployee(employee):
    try:
        employeeInfo = employeeRecords[employee]
        print("\n===============")
        print("Information for employee ID {}:".format(employee))
        print("Name: {}".format(employeeInfo[0]))
        print("Department: {}".format(employeeInfo[1]))
        print("Job Title: {}".format(employeeInfo[2]))
        print("===============\n")
    except KeyError:
        print("There is no employee with ID {}!".format(employee))
    except: 
        print("Something went wrong. Please try again!")

def createNewEmployee():#need to go back through and support creation of new subclasses?
    print("Creating new employee... ")
    try:
        newEmpID = int(input("Please enter new employee ID number: "))
    except ValueError:
        print("Please input a numerical employee ID!")
    else:
        newEmpName = input("Please enter new employees name: ")
        newEmpDep = input("Please enter new employees department: ")
        newEmpJob = input("Please enter new employees job title: ")
        print("\n===============")
        print("New Employee ID set to {}".format(newEmpID))
        print("New employees name: {}".format(newEmpName))
        print("New employee will be assigned to department {}".format(newEmpDep))
        print("New employees job title will be: {}".format(newEmpJob))
        print("===============\n")
        while True:
            choice = input("Confirm these choices? y/n: ")
            if choice == "y":
                print("writing to records...")
                newEmployee = Employee(newEmpID, newEmpName, newEmpDep, newEmpJob)
                newEmployee.saveInDict()
                print("Done! New employee record as follows:")
                searchEmployee(newEmpID)
                break
            elif choice == "n": 
                print("aborting!")
                break
            else:
                print("invalid choice. \n")
                continue

def deleteEmployee():
    try:
        employeeToDel = int(input("Please input the ID of the employee to remove: "))
        temp = employeeRecords[employeeToDel]
    except KeyError:
        print("No such employee exists!")
    except ValueError:
        print("Please input a numerical employee ID!")
    else:
        searchEmployee(employeeToDel)
        while True:
            choice = input("Please confirm you would like to delete this employee! y/n: ")
            if choice == "y":
                print("deleting employee...")
                employeeRecords.pop(employeeToDel)
                print("Done!")
                break
            elif choice == "n": 
                print("aborting!")
                break
            else:
                print("invalid choice. \n")
                continue

def listAllEmployees():
    for key, value in employeeRecords.items():
        print(key, ':', value)
# well except this one but w/e
def quitProgram():
    with open('employeeRecords.pickle', 'wb') as handle:
        pickle.dump(employeeRecords, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print("Goodbye!")
    quit()

###########
# UX stuff
###########

def main():
    global employeeRecords
    if not os.path.exists("employeeRecords.pickle"):                                #handle file loading
        with open('employeeRecords.pickle', 'wb') as handle:
            pickle.dump(employeeRecords, handle, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        with open('employeeRecords.pickle', 'rb') as handle:
            employeeRecords = pickle.load(handle)
    employee1 =  Employee(47899, "Susanna Myer", "Accounting", "Vice President")        #init question 1/2 stuff
    employee2 = Employee(39119, "Mark Joseph", "Info Tech", "Programmer")
    employee3 = Employee(81774, "Joyce Roberts", "Manufacturing", "Engineer")
    employee1.saveInDict()  # we need employee.saveindict - automagic for new employee creation function, but these need to be here for part 1
    employee2.saveInDict()                                    
    employee3.saveInDict()
    while True:             # the first of many menus
        print("\n=============================================================================")
        print("Please select an option: \n 1. Part 1 \n 2. Part 2 \n 3. Part 3 \n 4. Quit")
        userChoice = input(" > ")
        if userChoice == "1":
            part1()
        elif userChoice == "2":
            part2()
        elif userChoice == "3":
            part3()
        elif userChoice == "4":
            quitProgram()
        else:
            print("Please make a valid choice!")
            input("(Press any key to continue)")

def part1():    # :)
    while True:
        print("\n=============================================================================")
        print("Welcome to the simple employee management tool! please select a menu option: ")
        print(" 1. list all employees \n 2. Look an employee up \n 3. Add new employee \n 4. Update an employees information \n 5. Delete an employee \n 6. Quit the program \n 7. Back to main menu")
        menuChoice = input("  > ")
        if menuChoice == "1":
            listAllEmployees()
            input("(Press any key to continue)")
            continue
        elif menuChoice == "2":
            try:
                userInput = int(input("Please enter employee number to search: "))
                searchEmployee(userInput)
            except ValueError:
                print("Please enter a valid employee number!")
            finally:
                input("(Press any key to continue)")
                continue
        elif menuChoice == "3": 
            createNewEmployee()
            input("(Press any key to continue)")
            continue
        elif menuChoice == "4":
            updateMenu()
            input("(Press any key to continue)")
            continue
        elif menuChoice == "5":
            deleteEmployee()
            input("(Press any key to continue)")
            continue
        elif menuChoice == "6":
            quitProgram()
        elif menuChoice == "7":
            return
        else: 
            print("Please select a valid option!")
            input("(Press any key to continue)")
            continue

def updateMenu():   # submenu for part 1
    print("Accessing Employee record update subsystem...")
    while True:
        employeeChoice = input("Please enter an employee's ID to update the records of, or \"q\" to quit: ")
        if employeeChoice == "q":
            break
        try:
            employeeChoice = int(employeeChoice)
            temp = employeeRecords[employeeChoice]
            print("accessing employee records...")
            searchEmployee(employeeChoice)
            while True:
                print("Please choose a field to update:")
                fieldChoice = input(" 1. Name \n 2. Department \n 3. Job Title \n   > ")
                if fieldChoice == "1":
                    updateInput = input("Please input the updated name: ")
                    updateEmployee(employeeChoice, "name", updateInput)
                    return
                elif fieldChoice == "2":
                    updateInput = input("Please input updated department: ")
                    updateEmployee(employeeChoice, "department", input)
                    return
                elif fieldChoice == "3": 
                    updateInput = input("Please enter updated job title: ")
                    updateEmployee(employeeChoice, "jobTitle", updateInput)
                    input("(Press any key to continue)")
                    return
                else: 
                    print("\nPlease make a valid selection! ")
                    continue
        except KeyError:
            print("No such employee exists with the ID of {}!".format(employeeChoice))
        except ValueError:
            print("Please input a numerical employee ID!")

def part2():        # I was actually impressed at how I got the two choices to work on one function, not gonna lie
    while True:
        print("\n=============================================================================")
        print("Welcome to the simple employee management tool! please select a menu option: ")
        print(" 1. Wheatly \n 2. GLADoS \n 3. Quit the program \n 4. Return to main menu")
        menuChoice = input("  > ")
        if menuChoice == "1":
            menu("Wheatly")
            input("(Press any key to continue)")
            continue
        elif menuChoice == "2":
            menu("glados")
            input("(Press any key to continue)")
            continue
        elif menuChoice == "3":
            quitProgram()
        elif menuChoice == "4": 
            return
        else:
            print("Please make a valid decision!")
            continue

def menu(employee): 
    sEmployee1 = ShiftEmployee(9999, "Wheatly", "Dept. of bad ideas", "Moron", "1", "0.001")
    sEmployee2 = ShiftEmployee(2, "Caroline", "Administration", "Caroline", 12, "9999")
    if employee == "Wheatly":
        working = sEmployee1
    elif employee == "glados":
        working = sEmployee2
    while True: 
        print("Currently accessing menu for {}".format(employee))
        print("Please select a menu option: \n 1. List shift employee information \n 2. edit shift employee shift \n 3. edit shift employee payrate \n 4. Return")
        menuChoice = input(" > ")
        if menuChoice == "1":
            working.sEmployeeInfo()
            input("(Press any key to continue)")
            continue
        if menuChoice == "2":
            while True:
                newShift = input("Please input what you would like the new value to be (1 for day, 2 for night): ")
                if newShift == "1" or newShift == "2":
                    working.set_shift(newShift)
                    input("(Press any key to continue)")
                    break
                else:
                    print("Please input a valid choice.")
                    input("(Press any key to continue)")
                    continue

        if menuChoice == "3":
            while True:
                try:
                    newPay = float(input("Please input what you would like the pay rate to be: "))
                    working.set_payRate(newPay)
                    input("(Press any key to continue)")
                    break
                except ValueError:
                    print("Please input a valid choice.")
                    input("(Press any key to continue)")
                    continue
        if menuChoice == "4":
            return

def part3():        #feel free to google these references if you don't know them
    contractor1 = Contractor(23, "Gordon Freeman", "Anomalous Materials Researcher", "Theoretical Physicist/Saviour of humanity", 0000, 1289367, 54000)
    contractor2 = Contractor(0, "the G man", "???", "???", 0, 0, 0)
    print("\n=============================================================================")
    print("Contractor information as follows:")
    contractor1.ContractorInfo()
    contractor2.ContractorInfo()
    input("(Press any key to continue)")
    return

main()
