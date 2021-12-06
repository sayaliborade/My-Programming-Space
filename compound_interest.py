#A = P(1+R/100)^t
#Compound Interest = A - P

p = int(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time: "))

a = p * ((1 + r/100)**t)
ci = a - p

print("Compound interest is {0}".format(ci))