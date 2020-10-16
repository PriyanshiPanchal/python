import datetime
import sys
import time
from datetime import datetime
from datetime import date
Medical=[{'Name':'Ophthalmic','Batch_No':'BD001','Category':'Eye','Form_Type':'Liquid','Expiry_Date':'10/12/2019','Age_Limits':'>5 & <18',
           'Ingredients':[{'Ing_Name':'chrolide'},{'Ing_Name':'glycerin'},{'Ing_Name':'boric acid'},{'Ing_Name':'purified water'}]},
           {'Name':'Alcaftadine','Batch_No':'BD002','Category':'Eye','Form_Type':'Tabletts','Expiry_Date':'12/01/2020','Age_Limits':'<5',
           'Ingredients':[{'Ing_Name':'chrolide'},{'Ing_Name':'hydrochloric acid'},{'Ing_Name':'sodium hydroxide'},{'Ing_Name':'purified water'}]},
           {'Name':'Emadastine','Batch_No':'BD003','Category':'Eye','Form_Type':'Capsules','Expiry_Date':'31/12/2019','Age_Limits':'>18',
           'Ingredients':[{'Ing_Name':'hydrochloride'},{'Ing_Name':'hydrochloric acid'},{'Ing_Name':'disodium'},{'Ing_Name':'purified water'}]},
           {'Name':'Augmentin','Batch_No':'BD004','Category':'Ear','Form_Type':'Liquid','Expiry_Date':'30/12/2019','Age_Limits':'>18',
           'Ingredients':[{'Ing_Name':'benzocaine'},{'Ing_Name':'antipyrine'},{'Ing_Name':'disodium'},{'Ing_Name':'purified water'}]},
           {'Name':'Cortisporin','Batch_No':'BD005','Category':'Ear','Form_Type':'Tablets','Expiry_Date':'01/01/2019','Age_Limits':'>5 & <18',
           'Ingredients':[{'Ing_Name':'benzocaine'},{'Ing_Name':'antipyrine'},{'Ing_Name':'zinc acetate'},{'Ing_Name':'hydrocortisone'}]},
           {'Name':'Warfarin','Batch_No':'BD006','Category':'Nose','Form_Type':'Capsules','Expiry_Date':'02/01/2020','Age_Limits':'>18',
           'Ingredients':[{'Ing_Name':'benzocaine'},{'Ing_Name':'antipyrine'},{'Ing_Name':'zinc acetate'},{'Ing_Name':'hydrocortisone'}]},
           {'Name':'Plavix','Batch_No':'BD007','Category':'Nose','Form_Type':'Liquid','Expiry_Date':'01/01/2020','Age_Limits':'<5',
           'Ingredients':[{'Ing_Name':'benzocaine'},{'Ing_Name':'antipyrine'},{'Ing_Name':'pseudoephedrine'},{'Ing_Name':'hydrocortisone'}]},
           {'Name':'Corticosteroids','Batch_No':'BD008','Category':'Skin','Form_Type':'Tablets','Expiry_Date':'30/12/2019','Age_Limits':'>5 & <18',
           'Ingredients':[{'Ing_Name':'beta hydroxy acids'},{'Ing_Name':'antipyrine'},{'Ing_Name':'retinol'},{'Ing_Name':'hydrocortisone'}]},
           {'Name':'Anthralin','Batch_No':'BD009','Category':'Skin','Form_Type':'Capsules','Expiry_Date':'01/01/2020','Age_Limits':'>18',
           'Ingredients':[{'Ing_Name':'benzocaine'},{'Ing_Name':'kojic acid'},{'Ing_Name':'pseudoephedrine'},{'Ing_Name':'alpha-hydroxyacids'}]},
           {'Name':'Levofloxacin','Batch_No':'BD010','Category':'Pain','Form_Type':'Liquid','Expiry_Date':'30/12/2019','Age_Limits':'<5',
           'Ingredients':[{'Ing_Name':'Polyhydroxy acids'},{'Ing_Name':'kojic acid'},{'Ing_Name':'pseudoephedrine'},{'Ing_Name':'alpha-hydroxyacids'}]},
           {'Name':'Doxycycline','Batch_No':'BD011','Category':'Pain','Form_Type':'Tablets','Expiry_Date':'31/12/2019','Age_Limits':'>5 & <18',
           'Ingredients':[{'Ing_Name':'zinc acetate'},{'Ing_Name':'kojic acid'},{'Ing_Name':'pseudoephedrine'},{'Ing_Name':'alpha-hydroxyacids'}]},
           {'Name':'Amoxicillin','Batch_No':'BD012','Category':'Infections','Form_Type':'Capsules','Expiry_Date':'31/12/2019','Age_Limits':'>18',
           'Ingredients':[{'Ing_Name':'zinc acetate'},{'Ing_Name':'kojic acid'},{'Ing_Name':'pseudoephedrine'},{'Ing_Name':'alpha-hydroxyacids'}]},
           {'Name':'Acticlate','Batch_No':'BD001','Category':'Infections','Form_Type':'Liquid','Expiry_Date':'12/12/2019','Age_Limits':'>5 & <18',
           'Ingredients':[{'Ing_Name':'zinc acetate'},{'Ing_Name':'kojic acid'},{'Ing_Name':'pseudoephedrine'},{'Ing_Name':'alpha-hydroxyacids'}]},
           {'Name':'Acticlate','Batch_No':'BD001','Category':'Infections','Form_Type':'Liquid','Expiry_Date':'01/06/1998','Age_Limits':'>5 & <18',
           'Ingredients':[{'Ing_Name':'zinc acetate'},{'Ing_Name':'kojic acid'},{'Ing_Name':'pseudoephedrine'},{'Ing_Name':'alpha-hydroxyacids'}]},
           {'Name':'Acticlate','Batch_No':'BD001','Category':'Infections','Form_Type':'Liquid','Expiry_Date':'12/06/2000','Age_Limits':'>5 & <18',
           'Ingredients':[{'Ing_Name':'zinc acetate'},{'Ing_Name':'kojic acid'},{'Ing_Name':'pseudoephedrine'},{'Ing_Name':'alpha-hydroxyacids'}]}]

main={
    "1": "Find the records by category",
    "2": "Find the records by form type",
    "3": "Find the records for current month expiration",
    "4": "Find the records for batch no.",
    "5": "Enter new record",
    "6": "Batch + Category",
    "7": "Batch + Forms",
    "8": "Batch + Expirations(Months)",
    "9": "Filter the records by age limits",
    "10": "Age Limits + Category + Batch Number",
    "11":"Age Limits + Category + Form-Type",
    "12": "Filter the records by ingredients",
    "13":"Search the medicines name"
}

for i in main:
    print(i+" "+main[i])

main_input=input("Choose  from the list:")

if main_input=="1":
        Category = {
            "1":"Eye",
            "2":"Ear",
            "3":"Nose",
            "4":"Skin",
            "5":"Pain",
            "6":"Infections"
        }

        for i in Category:
            print(i + " " + Category[i])

        user_choice = input("Choose the category from the list above:")

        if user_choice == "1":
            for i in range(len(Medical)):
                if Medical[i]['Category']=="Eye":
                    print(Medical[i])

        elif user_choice == "2":
            for i in range(len(Medical)):
                if Medical[i]['Category']=="Ear":
                    print(Medical[i])

        elif user_choice == "3":
            for i in range(len(Medical)):
                if Medical[i]['Category']=="Nose":
                    print(Medical[i])

        elif user_choice == "4":
            for i in range(len(Medical)):
                if Medical[i]['Category']=="Skin":
                    print(Medical[i])

        elif user_choice == "5":
            for i in range(len(Medical)):
                if Medical[i]['Category']=="Pain":
                    print(Medical[i])

        elif user_choice == "6":
            for i in range(len(Medical)):
                if Medical[i]['Category']=="Infections":
                    print(Medical[i])

elif main_input=="2":
    
    Form_Type={
        "1":"Liquid",
        "2":"Tablets",
        "3":"Capsules"
    }
    for i in Form_Type:
            print(i + " " + Form_Type[i])

    user_choice = input("Choose the form-type from the list above:")

    if user_choice == "1":
        for i in range(len(Medical)):
            if Medical[i]['Form_Type']=="Liquid":
                print(Medical[i])

    if user_choice == "2":    
        for i in range(len(Medical)):
            if Medical[i]['Form_Type']=="Tablets":
                print(Medical[i])

    if user_choice == "3":    
        for i in range(len(Medical)):
            if Medical[i]['Form_Type']=="Capsules":
                print(Medical[i])

elif main_input=="3":
    cur_mon=[]
    today = datetime.today()
    print(today)
    for i in range(len(Medical)):
        med_list = (Medical[i]['Expiry_Date'])
        li=datetime.strptime(med_list, '%d/%m/%Y')
        if(li.month==today.month):
             cur_mon.append(Medical[i])
    print(cur_mon,sep='\n')

elif main_input=="4":
    batch=input("Enter the batch number:")
    for i in range(len(Medical)):
        if Medical[i]['Batch_No']== batch:
            print(Medical[i])

elif main_input=="5":
    print("Enter the details:")
    name=input("Enter nmedicine name:")
    batch=input("Enter batch number")
    category=input("Enter category")
    form=input("Enter form type:")
    expirydate=input("Enter expiry date:")
    age=input("Enter age limits:")
    ing1=input("Enter ingredients1:")
    ing2=input("Enter ingredients2:")
    ing3=input("Enter ingredients3:")
    ing4=input("Enter ingredients3:")
    print("List after adding new employee to existing list")
    Medical.insert(2, {"Name":name,"Batch_No":batch,"Category":category,"Form_Type":form,"Expiry_Date":expirydate,"Age_Limits":age,"Ingredients":[{"Ing_Name":ing1,"Ing_Name":ing2,"Ing_Name":ing3,"Ing_Name":ing4}]})
    print(*Medical,sep='\n')

elif main_input=="6":
    batch=input("Enter the batch number:")
    category=input("Enter the category:")
    for i in range(len(Medical)):
        if Medical[i]['Batch_No']==batch and Medical[i]['Category']==category:
            print(Medical[i])
        

elif main_input=="7":
    batch=input("Enter the batch number:")
    form=input("Enter the form type")
    for i in range(len(Medical)):
        if Medical[i]['Batch_No']==batch and Medical[i]['Form_Type']==form:
            print(Medical[i])

elif main_input=="8":
    cur_list=[]
    med_list=[]
    batch=input("Enter the batch number:")
    for i in range(len(Medical)):
        if(Medical[i]['Batch_No']==batch):
            cur_list.append(Medical[i])

    n = len(cur_list)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            exp_year = cur_list[min_idx].get('Expiry_Date').split('/')[2]
            exp_year1 = cur_list[j].get('Expiry_Date').split('/')[2]
            if exp_year > exp_year1:
                min_idx=j
        cur_list[i],cur_list[min_idx]=cur_list[min_idx],cur_list[i]
    # print(cur_list)    

    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            exp_month= cur_list[min_idx].get('Expiry_Date').split('/')[1]
            exp_month1= cur_list[j].get('Expiry_Date').split('/')[1]
            exp_year = cur_list[min_idx].get('Expiry_Date').split('/')[2]
            exp_year1 = cur_list[j].get('Expiry_Date').split('/')[2]
            if exp_year == exp_year1:
                if exp_month > exp_month1:
                    min_idx=j
        cur_list[i],cur_list[min_idx]=cur_list[min_idx],cur_list[i]
    # print(cur_list)    

    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            exp_days=cur_list[min_idx].get('Expiry_Date').split('/')[0]
            exp_days1=cur_list[j].get('Expiry_Date').split('/')[0]
            exp_month= cur_list[min_idx].get('Expiry_Date').split('/')[1]
            exp_month1= cur_list[j].get('Expiry_Date').split('/')[1]
            exp_year = cur_list[min_idx].get('Expiry_Date').split('/')[2]
            exp_year1 = cur_list[j].get('Expiry_Date').split('/')[2]
            if exp_year == exp_year1:
                if exp_month == exp_month1:
                    if exp_days > exp_days1:
                        min_idx=j
        cur_list[i],cur_list[min_idx]=cur_list[min_idx],cur_list[i]
    print(cur_list)    

elif main_input=="9":
    cur_list=[]
    n=len(Medical)
    for i in range(n):
        min_idx=i      
        for j in range(i+1,n):
            res=Medical[min_idx]['Age_Limits']
            res2=Medical[j]['Age_Limits']

            if((res=='>18' and res2=='>5 & <18') or (res=='>18' and res2=="<5")):
                min_idx=j
            
                Medical[i],Medical[min_idx]=Medical[min_idx],Medical[i]

            elif((res=='>5 & <18' and res2=='<5') or (res=='>18' and res2=='<5')):
                min_idx=j
             
                Medical[i],Medical[min_idx]=Medical[min_idx],Medical[i]

    print(Medical)

    for i in range(n):
        res=Medical[i]['Age_Limits']
        print(res)

elif main_input=="10":
    agelimit=input("Enter Age Limits")
    batch=input("Enter the batch number:")
    category=input("Enter the category:")
    for i in range(len(Medical)):
        if Medical[i]['Batch_No']==batch and Medical[i]['Category']==category and Medical[i]['Age_Limits']==agelimit:
            print(Medical[i])
        
            

elif main_input=='11':
    agelimit=input("Enter Age Limits")
    formtype=input("Enter Form Type")
    category=input("Enter the category:")
    for i in range(len(Medical)):
        if Medical[i]['Form_Type']==formtype and Medical[i]['Category']==category and Medical[i]['Age_Limits']==agelimit:
            print(Medical[i])
        
elif main_input=='12':
    ing=input("Enter the ingredients name:")
    n=len(Medical)
    for i in range(n):
        for j in range(4):
            med=(Medical[i]['Ingredients'][j]['Ing_Name'])
            if(med==ing):
                print(Medical[i])

elif main_input=='13':

    substring=input("Enter the string to be searched:")

    for i in range(len(Medical)):
        if substring in Medical[i]['Name']:
            res=print(Medical[i])
           

        



