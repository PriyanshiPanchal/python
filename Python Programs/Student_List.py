print("Using Sort Functions")
Students=['Priyanshi','Prachi','Yash','Rahul','Jay','Kavya','Anjali']
print(sorted(Students))

print("Without using sort functions")

def sortString(Students):
    for i in range(len(Students)-1):
        for j in range(i+1,len(Students)):
            if Students[i]>Students[j]:
                temp=Students[i]
                Students[i]=Students[j]
                Students[j]=temp
    print("sorted list:{}".format(Students))

Students=['Priyanshi','Prachi','Yash','Rahul','Jay','Kavya','Anjali']
sortString(Students)

# Students=['Priyanshi','Prachi','Yash','Rahul','Jay','Kavya','Anjali']
# # using list comprehension 
# listToStr = ' '.join(map(str, Students)) 
  
# print(listToStr)

# out = ''
# for n in listToStr:
#     if n not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#         out = out + n
#     else:
#         k = ord(n)
#         l = k + 32
#         out = out + chr(l)
# print(out)    

# def Convert(string): 
#     li = list(string.split(" ")) 
#     return li 

# print(Convert(out)) 

substring=input("Enter the string to be searched:")
#substring=substring.lower()
  
for i in Students:
    if substring in i:
        res=print(Students.index(i),i)
        # res=print(i)
        # abc=print(Students.index(i))