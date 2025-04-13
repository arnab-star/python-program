# Calculating the complex interest rate per year

principal = float(input("Enter the principal amount: "))
amount = float(input("Enter the final amount: "))
time = float(input("Enter the time in years: "))

rate = ((amount / principal) ** (1 / time) - 1) * 100

print(f"The rate of interest is {rate}% per year")
