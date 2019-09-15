#A program that calculate month it take a user to buy house.there should be increase in Salary if the user works more than some certain month
annualSalary = float(input("Enter your annual salary: "))
#portion saved
portionSaved = float(input("Enter the percent of your salary to save, in decimal: "))
totalCost = float(input("Enter the cost of your dream home: "))
#new Variable for the Question 1b for semi annual raise incrsement....
semiAnnualRaise = float(input("Enter the semi­annual raise, as a decimal: "))
#to get the portion down payment 
portionDownPayment = totalCost * 0.25
#initializing the current saving getting a return value from monthly salary X by portion saved plus value of current+
currentSavings = 0
r = 0.04
months = 0
monthlySalary=annualSalary/12
while currentSavings < portionDownPayment:
    currentSavings += (monthlySalary)*portionSaved + currentSavings*(r/12)
    months += 1
    if months%6 == 0:
        annualSalary += annualSalary * semiAnnualRaise
print("Number of months to saved: ", months)
