def loan_interest_calculator():
    print("This is a monthly interest rate calculator")
    
    principal = float(input("Please input the principal amount: "))
    apr = float(input("Please input annual interest rate: "))
    year = int(input("Please input the number of years: "))

    monthly_interest_rate = apr / 1200
    number_of_months = year * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-number_of_months))

    print("The monthly payment for this loan is: %.2f" % monthly_payment)


loan_interest_calculator()