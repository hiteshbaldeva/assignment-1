n= int(input("enter the number of students :"))
print("student's name size must be less than 15")
list =[]
for i in range(0,n):
    s = input(f"enter the name of student{i+1} :")
    list.append(s)

names=[]

for name in list:
    names.append(name[::-1])

print(names)