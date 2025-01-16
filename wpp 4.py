# swap two variable without using third variable

a= int(input("enter first number"))
b= int(input("enter second number"))
a=a+b
b=a-b
a=a-b
print("after swap")
print(f"a = {a} and b = {b}")