    ########################################################################################################################
    ########################################################################################################################
    ### Author: Laika Marshall                                                                                           ###
    ### Date Created: 16/08/2021                                                                                         ###
    ### Date Last Changed: 16/08/2021                                                                                    ###
    ### A simple program to create a payroll statement from given inputs                                                 ###
    ########################################################################################################################
    ########################################################################################################################


def main():
    employeeName = getName()
    hoursWorked = getHours()
    hourlyRate = getHourlyRate()
    atoRate = getATORate()
    medicareLevy = getMedicareLevi()
    grossPay = calculateGrossPay(hoursWorked, hourlyRate)
    print("\n======================================================")
    print("Employee Name: {}".format(employeeName))
    print("Hours Worked: {}".format(hoursWorked))
    print("Pay Rate: ${}".format(hourlyRate))
    print("Gross Pay: ${}".format(grossPay))
    netPay = getDeductions(grossPay, atoRate, medicareLevy)
    print("Net pay: {}".format(netPay))
    print("======================================================\n")


def getName():                                                                  
    name = input("Enter employee's Name: ")
    return name

def getHours():
    hours = float(input("Enter number of hours worked in a week: "))
    return hours
    
def getHourlyRate():
    rate = float(input("Enter hourly pay rate: "))
    return rate

def getATORate():
    ATO = float(input("Enter ATO tax withholding rate: "))
    return ATO 

def getMedicareLevi():
    levi = float(input("Enter Medicare Levi Rate: "))
    return levi

def calculateGrossPay(hours, rate):
    pay = hours * rate
    return pay

def getDeductions(pay, tax, levy):
    taxDeduction = tax * pay 
    medicare = levy * pay
    taxAmt = tax * 100
    levyAmt = levy * 100
    deductions = taxDeduction + medicare
    netPay = pay - deductions
    print("Deductions: ")
    print("     ATO Tax ({}%): ${}".format(taxAmt, taxDeduction))
    print("     Medicare Levy ({}%): ${}".format(levyAmt, medicare))
    print("     Total Deductions: ${}".format(deductions))
    return(netPay)
main()
