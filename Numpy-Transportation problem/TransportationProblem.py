import numpy as np
import sys
from datetime import datetime
from matplotlib import pyplot as plt 

vehicle = np.dtype([('Bus_ID','S20'),('Vehicle_no','S20'), ('RC_Expiration', 'datetime64[D]'), ('Year_Of_Purchase', 'i4'),('Passing','S20'),('Insurance_Due_Date','datetime64[D]'),('KM','i4'),('Fuel_Type','S20'),('Seating_Capacity','i1'),('Facilation_Type','S20'),('Driver_ID','S20')]) 
vehicle_record = np.array([('2001','MH 02 BT 2876', '2020-01-26', 2019, 'Maharastra','2022-02-20',25000,'Diesel',32,'AC','1001'),
('2002','GJ 01 HA 2576', '2022-02-26', 2015, 'Gujarat','2023-12-03',25068,'Petrol',56,'Non-AC','1021'),
('2003','AP 31 CG 0876', '2020-01-30', 2017, 'Andhra Pradesh','2020-01-25',125000,'CNG',32,'AC','1022'),
('2004','BR 01 AQ 3878', '2023-12-30', 2016, 'Bihar','2020-01-28',160460,'Diesel',56,'Non-AC','1034'),
('2005','MP 23 LA 2356', '2021-03-12', 2013, 'Madhya Pradesh','2021-11-04',265000,'Petrol',32,'AC','1035'),
('2006','PB 03 AD 8746', '2022-03-23', 2019, 'Punjab','2023-10-23',125987,'CNG',56,'Non-AC','1036'),
('2007','TN 07 AP 7647', '2023-09-17', 2013, 'Tamil Nadu','2021-12-30',5000,'Diesel',32,'AC','1037'),
('2008','WB 04 YU 4576', '2021-06-27', 2015, 'West Bengal','2023-08-25',525000,'Petrol',56,'Non-AC','1038'),
('2009','CH 45 GH 4566', '2022-04-28', 2013, 'Chandigarh','2021-04-25',125000,'CNG',32,'AC','1027'),
('2010','DL 31 KI 9876', '2023-06-16', 2012, 'Delhi','2020-01-20',225000,'Diesel',56,'Non-AC','1023')], dtype = vehicle) 
# print (vehicle_record)

driver=np.dtype([('Bus_ID','S20'),('Driver_ID','S20'),('name','S20'),('experience','i1'),('age','i1'),('salary','i4')])
driver_record=np.array([('2001','1038','Kaushal','2','25','25000'),    
                        ('2002','1021','Vijay','1','30','15000'),
                        ('2003','1022','Jayesh','3','32','10000'),
                        ('2004','1034','Rahul','1','32','25000'),
                        ('2005','1035','Jay','2','28','23000'),
                        ('2006','1036','Parth','5','29','22000'),
                        ('2007','1037','Vipul','8','26','15000'),
                        ('2008','1001','Yash','6','35','17000'),
                        ('2009','1027','Himanshu','7','34','20000'),
                        ('2010','1023','Harsh','8','27','24000')],dtype=driver)
# print(driver_record)


# for x in np.nditer(driver_record):
#     print(x)

main={
    "1": "Find the Vehicle By:",
    "2": "Find the vehicle by Fuel Type:",
    "3": "Find the vehicle by Facilitation",
    "4": "Vehicle Usage Chart(By KM Run)",
    "5": "Find vehicle by bus type ",
    "6": "Find Vehicle Driver detail For Particular Bus (Input Bus ID)",
    "7": "Find Vehicle Bus detail For Particular Driver (Input Driver ID)",
    "8": "Find Vehicle run by Experienced Drivers & Fresh Drivers",
    "9": "Find Vehicles nearly expiring Insurance",
    "10":"Find Vehicles nearly expiring RS Registration"
}


for i in main:
    print(i+" "+main[i])

main_input=input("Choose from the list:")

if main_input=="1":
        Category = {
            "1":"New",
            "2":"Running",
            "3":"Out Of Range",
        }

        for i in Category:
            print(i+" "+Category[i])

        main_input=input("Choose category from the list:")
        
        if main_input=="1":
            for i in range(len(vehicle_record)):
                if(vehicle_record[i]['KM']<25000):
                    print("Vehicle is New")
                    print(vehicle_record[i])
        elif main_input=="2":
            for i in range(len(vehicle_record)):
                if(vehicle_record[i]['KM']>25000 and vehicle_record[i]['KM']<=120000):
                    print("Vehicle is Running")
                    print(vehicle_record[i])
        elif main_input=="3":
            for i in range(len(vehicle_record)):
                if(vehicle_record[i]['KM']>120000):
                    print("Vehicle is Out Of Range")
                    print(vehicle_record[i])

elif main_input=="2":
    
    
    # print(fuel_arr[0])
    # print(fuel_arr)
    FuelType = {
            "1":"Diesel",
            "2":"Petrol",
            "3":"CNG",
        }
    
    for i in FuelType:
        print(i+" "+FuelType[i])

    fuel_input=input("Choose fuel type from the list:")
        
    fuel_arr = np.asarray(['Diesel','Petrol','CNG'],dtype='S20') 

    if fuel_input=="1":
        for i in range(len(vehicle_record)):
            # print(vehicle_record[i]['Fuel_Type'])
            if(vehicle_record[i]['Fuel_Type']==fuel_arr[0]):
                print(vehicle_record[i])
                
    elif fuel_input=="2":
        for i in range(len(vehicle_record)):
            if(vehicle_record[i]['Fuel_Type']==fuel_arr[1]):
                print(vehicle_record[i])
    elif fuel_input=="3":
        for i in range(len(vehicle_record)):
            if(vehicle_record[i]['Fuel_Type']==fuel_arr[2]):
                print(vehicle_record[i])
    
elif main_input=="3":
    Facilation = {
            "1":"AC",
            "2":"Non-AC",
    }

    for i in Facilation:
        print(i+" "+Facilation[i])

    fac_input=input("Choose facilation type from the list:")
        
    factype = np.asarray(['AC','Non-AC'],dtype='S10') 
    if fac_input=="1":
        for i in range(len(vehicle_record)):
            if(vehicle_record[i]['Facilation_Type']==factype[0]):
                print(vehicle_record[i])
    elif fac_input=="2":
        for i in range(len(vehicle_record)):
            if(vehicle_record[i]['Facilation_Type']==factype[1]):
                print(vehicle_record[i])
elif main_input=="4":
    x=[]
    for i in range(len(vehicle_record)):
        x.append(vehicle_record[i]['Vehicle_no'])

    y=[]
    for i in range(len(vehicle_record)):
        y.append(vehicle_record[i]['KM'])

    plt.title("Vehicle Usage Chart")
    plt.xlabel("Vehicle ID") 
    plt.ylabel("Distance covered by vehicle(KM)") 
    plt.bar(x,y)
    plt.tick_params(axis ='x', rotation = 90)
    plt.show()

elif main_input=="5":
    Bus_Type = {
            "1":"Mini-Bus",
            "2":"Regular",
    }

    for i in Bus_Type:
        print(i+" "+Bus_Type[i])

    bus_input=input("Choose bus type from the list:")
        
    if bus_input=="1":
        for i in range(len(vehicle_record)):
            if(vehicle_record[i]['Seating_Capacity']==32):
                print(vehicle_record[i])
    elif bus_input=="2":
        for i in range(len(vehicle_record)):
            if(vehicle_record[i]['Seating_Capacity']==56):
                print(vehicle_record[i])
elif main_input=="6":
    bus_id=input("Enter the Bus ID, to get the vehicle driver details:")

    bus_id = np.asarray(bus_id,dtype='S20') 

    for i in range(len(vehicle_record)):
        for j in range(len(driver_record)):
            if(vehicle_record[i]['Bus_ID']==bus_id and vehicle_record[j]['Bus_ID']==bus_id):
                print(vehicle_record[i])
                print(driver_record[j])
    

elif main_input=="7":
    driver=input("Enter the Driver ID, to get the vehicle bus details:")

    driver_id = np.asarray(driver,dtype='S20') 

    for i in range(len(vehicle_record)):
        for j in range(len(driver_record)):
            if(vehicle_record[i]['Driver_ID']==driver_id and driver_record[j]['Driver_ID']==driver_id):
                print(vehicle_record[i])
                print(driver_record[j])

elif main_input=="8":
    Driver_Experience = {
            "1":"Fresh",
            "2":"Experienced",
    }

    for i in Driver_Experience:
        print(i+" "+Driver_Experience[i])

    exp_input=input("Choose driver experienced type from the list:")
        
    if exp_input=="1":
        for i in range(len(vehicle_record)):
            if(driver_record[i]['experience']<5):
                print(driver_record[i])
                if(driver_record[i]['Bus_ID']==vehicle_record[i]['Bus_ID']):
                    print(vehicle_record[i])
    elif exp_input=="2":
        for i in range(len(vehicle_record)):
            if(driver_record[i]['experience']>=5):
                print(driver_record[i])
                if(driver_record[i]['Bus_ID']==vehicle_record[i]['Bus_ID']):
                    print(vehicle_record[i])
elif main_input=="9":
    today = datetime.today()
    today_date=today.date()
    print(today_date)
    for i in range(len(vehicle_record)):
        if(today_date.month==vehicle_record[i]['Insurance_Due_Date'].astype(object).month):
            print(vehicle_record[i])
elif main_input=="10":
    today = datetime.today()
    today_date=today.date()
    print(today_date)
    for i in range(len(vehicle_record)):
        if(today_date.month==vehicle_record[i]['RC_Expiration'].astype(object).month):
            print(vehicle_record[i])