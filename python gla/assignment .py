p = float(input("Enter the principal loan amount (in dollars): "))
a = float(input("Enter the annual interest rate (in percentage): "))
t= int(input("Enter the loan term (in years): "))
r = (a / 12) / 100
n = t * 12
m = p * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
print(m)

