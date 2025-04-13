#calculate the principle amount

interest = float(input("Enter the simple interest: "))
rate = float(input("Enter the rate of interest per year: "))
time = float(input("Enter the time in years: "))

principal = (interest * 100) / (rate * time)

print(f"The principal amount is {principal}")
