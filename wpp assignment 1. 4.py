# Take numbers from 1 to 10000. Create equivalence classes for modulo 5 on this set of 
# numbers. Check the validity of your equivalence classes. [Hint: the union of all equivalence 
# classes should be the original set/list.]
original_set= set()
set_0 =set()
set_1 =set()
set_2 =set()
set_3 =set()
set_4 =set()
for i in range(1,10001):
     original_set.add(i)
for i in range(1,10001):
    if i%5==0:
        set_0.add(i)
    elif i%5==1:
        set_1.add(i)
    elif i%5==2:
        set_2.add(i)
    elif i%5==3:
        set_3.add(i)
    elif i%5==4:
        set_4.add(i)
    else:
        continue

union_set = set_0 | set_1 | set_2 | set_3 | set_4
print(union_set)

if original_set.difference(union_set)==set():
    print("hence proved , equivalence class")
else:
    print("not equivalence class")
