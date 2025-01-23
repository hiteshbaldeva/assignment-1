length = float(input("enter the length in feet"))
i =int(input("if you want to convert feet in  inches, yards, miles, millimeters, centimeters,meters, or kilometers press the number 1,2,3,4,5,6,7 respectively "))
list = [12,1/3,1/5280,304.8,30.48,0.3048,0.0003048]
print(length*list[i-1])
