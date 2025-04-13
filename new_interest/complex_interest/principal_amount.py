# Calculating the complex interest principal amount

amount = float(input("Enter the final amount: "))
rate = float(input("Enter the rate of interest per year: "))
time = float(input("Enter the time in years: "))

principal = amount / ((1 + rate / 100) ** time)

print(f"The principal amount is {principal}")