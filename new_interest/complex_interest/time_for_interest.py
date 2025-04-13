#  Calculating the complex interest time

principal = float(input("Enter the principal amount: "))
amount = float(input("Enter the final amount: "))
rate = float(input("Enter the rate of interest per year: "))

time = (amount / principal) /(1 + rate / 100)

print(f"The time required is {time} years")
