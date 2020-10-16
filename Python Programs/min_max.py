import random
import string
list=[]

for i in range(4):
    list.append(random.randint(1,100))

print(list)

for i in list:
    min1=min(list[0],list[1])
    min2=min(list[2],list[3])
    min3=min(min1,min2)
    print("Minimum number:",min3)
    break;    

for i in list:
    min1=max(list[0],list[1])
    min2=max(list[2],list[3])
    min3=max(min1,min2)
    print("Maximum number:",min3)
    break;    

