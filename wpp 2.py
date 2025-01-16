 # factorial of a number

number = int(input("enter your number :"))
factorial = 1
while number>0:
    factorial = factorial*number
    number = number-1
print(f"factorial is {factorial}")