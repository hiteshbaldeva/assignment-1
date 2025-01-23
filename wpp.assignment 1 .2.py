import random
list_1 = []
for i in range(1,101):
    list_1.append(random.randint(0,1))
print(list_1)

count = 0
list_2=[]
for i in range(0,100):
    if list_1[i] ==0:
        count = count +1

    else:
        list_2.append(count)
        count =0
print(list_2)
print(max(list_2))
