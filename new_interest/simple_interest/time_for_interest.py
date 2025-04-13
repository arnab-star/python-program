#calculate the time for the interest

interest = float(input("Enter the simple interest : "))
principal = float(input("Enter the principal amount : "))
rate = float(input("Enter the rate of interest per year : "))

time = (interest * 100) / (principal * rate)

print(f"The time required to earn the interest is {time} years")
