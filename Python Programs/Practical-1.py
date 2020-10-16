Employee=[{"name":"abc","sID":1,"email":"abc@mail.com","mobile":"9232328725"},
          {"name":"xyz","sID":2,"email":"xyz@mail.com","mobile":"9825562882"}]
print(*Employee,sep='\n')

#Search by employee name
n=input("Enter the name of employee from the existing employee list:")
for i in range(len(Employee)):
    if Employee[i]['name']==n:
        print(Employee[i])

#Adding new employee
print("Enter the details of employee")
value1=input("Enter name:")
value2=input("Enter sID")
value3=input("Enter email")
value4=input("Enter mobile number:")
print("List after adding new employee to existing list")
Employee.insert(2, {"name":value1,"sID":value2,"email":value3,"mobile":value4})
print(*Employee,sep='\n')

#Removing existing employee
name=input("Enter the name to be deleted from the list:")
for i in range(len(Employee)): 
    if Employee[i]['name'] == name: 
        del Employee[i] 
        break
print ("List after deletion of dictionary : " )
print(*Employee,sep='\n')

#Edit the existing employee detail
user=input("Enter the name in the list where you want to update:")
update=input("Enter the value to be updated")

for i in range(len(Employee)):
    if Employee[i]['name']=="xyz":
        Employee[i]['name']="def"
        break
    # elif Employee[i]['sID']==user:
    #     Employee[i]['sID']=update
    # elif Employee[i]['email']==user:
    #     Employee[i]['email']==update
    # elif Employee[i]['mobile']==user:
    #     Employee[i]['mobile']=update
    # break

print ("List after updation of dictionary : ")
print(*Employee,sep='\n')
