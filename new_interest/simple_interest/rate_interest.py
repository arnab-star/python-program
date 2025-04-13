#rate for the interest

interest = float(input("Enter the interest: "))
principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time in years: "))

rate = (interest * 100) / (principal * time)

print(f"The rate of interest is {rate}% per year")