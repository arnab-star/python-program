# Calculating the complex interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest per year: "))
time = float(input("Enter the time in years: "))

amount = principal * (1 + rate / 100) ** time
ci = amount - principal

print(f"The compound interest is {ci}")
