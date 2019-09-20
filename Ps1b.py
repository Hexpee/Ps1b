#A program that calculate month it take a user to buy house.there should be increase in Salary if the user works more than some certain month
annual_salary = float(input("Enter your annual salary: "))
#portion saved in percentage
portion_saved = float(input("Enter the percent of your salary to save, in decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
#new Variable for the Question 1b for semi annual raise incrsement....
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))
#to get the portion down payment 
portion_down_payment = total_cost * 0.25
#initializing the current saving getting a return value from monthly salary X by portion saved plus value of current+
current_savings = 0
r = 0.04
months = 0
monthly_salary=annual_salary/12
while current_savings < portion_down_payment:
    current_savings += (monthly_salary)*portion_saved + current_savings*(r/12)
    months += 1
    if months%6 == 0:
        annual_salary += annual_salary * semi_annual_raise
print("Number of months to saved: ", months)
