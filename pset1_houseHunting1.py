#################################
#Name: Jaleel Savoy
#Collaborators: NA
#Time: 15min
#Program: Housing Hunting
#################################
def houseHunter1():
    annual_salary = float(input("Enter your annual salary: "))
    
    portion_saved = float(input("Enter portion of salary saved: "))
    
    total_cost = float(input("Enter the total cost of your dream home: "))

    portion_down_payment = total_cost * 0.25

    r = 0.04

    current_savings = 0

    monthly_salary = annual_salary/12.0

    monthly_salary_saved = monthly_salary * portion_saved

    months = 0

    while (current_savings <= portion_down_payment):
        investments = current_savings * (r/12.0)
        current_savings += monthly_salary_saved
        current_savings += investments
        months += 1
    print("It will take ", months, "months to save for the down payment!")
        
houseHunter1()