#################################
#Name: Jaleel Savoy
#Collaborators: NA
#Time: 
#Program: Housing Hunting part 2
#################################
def houseHunter2():
    annual_salary = float(input("Enter your annual salary (as float): "))
    
    portion_saved = float(input("Enter portion of salary saved (as float): "))
    
    total_cost = float(input("Enter the total cost of your dream home (as float): "))
    
    semi_annual_raise = float(input("Enter semi-annual raise percent (as float): " ))
    
    portion_down_payment = total_cost * 0.25
    
    r = 0.04
    
    current_savings = 0
    
    monthly_salary = annual_salary/12.0
    
    monthly_salary_saved = monthly_salary * portion_saved
    
    months = 1
    
    while (current_savings < portion_down_payment):
        current_savings += monthly_salary_saved
        investments = ((annual_salary * r )/12.0)
        current_savings += investments
        while ((months >= 6) and ((months % 6) ==0)):
            annual_salary += (semi_annual_raise * annual_salary)
            break
        months += 1
    
    print("Number of months: ", months)
    
houseHunter2()