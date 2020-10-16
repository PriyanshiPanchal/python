list1 = [10, 4, 66, 1, 18, 6] 
evenlist = [] 
oddlist = [] 
evencount=0
oddcount=0
for i in list1: 
    if (i % 2 == 0): 
         evenlist.append(i) 
         evencount+=1
    else:
        oddlist.append(i) 
        oddcount+=1

print("Even lists:", evenlist) 
print("Odd lists:", oddlist) 
print("Number of even number in the list:",evencount)
print("Number of odd number in the list:",oddcount)