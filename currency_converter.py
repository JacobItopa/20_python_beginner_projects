def convert_currency():
    print("This is a currency converter that converts dollars to pounds\n")

    dollars = eval(input("Amount entered would be in dollars: "))
    pounds = convert_to_pounds(dollars)
    print("That is ", pounds, " pounds")

convert_to_pounds = lambda dollars: dollars * 0.79

convert_currency()