#  reverse of a given number

number = int(input("enter your number"))
 # print(number[::-1])                     in one line over but change number into string
reverse = 0
while number>0:
    temp = number%10
    reverse = reverse * 10 + temp
    number = number//10

print(f"reverse of a given number is {reverse}")