from datetime import datetime
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%d' % int(height), ha='center', va='bottom')

df = pd.read_csv("BookingData.csv")

df.head()
datelist=df['Date']
# print(datelist)

start_date=(pd.to_datetime(df['Date'], format='%d/%m/%Y'))
# print(start_date)
start_date_month=start_date.dt.month
# print(start_date_month)

user_month=input("Enter the months:")

if user_month=="January":
    month= int(1);
elif user_month=="February":
    month= int(2);
elif user_month=="March":
    month= int(3);
elif user_month=="April":
    month= int(4);
elif user_month=="May":
    month= int(5);
elif user_month=="June":
    month= int(6);
elif user_month=="July":
    month= int(7);
elif user_month=="August":
    month= int(8);
elif user_month=="September":
    month= int(9);
elif user_month=="October":
    month= int(10);
elif user_month=="November":
    month= int(11);
elif user_month=="December":
    month= int(12);

Tot_Book=[]
Tot_Cancel=[]

# Total=0
# for j in range(len(start_date)):
#     Total += (df['Total Booking'][j])
# print(Total)
 
Total=0
BMS=0
PayTM=0
AmazonPay=0
Other=0
for i in range(len(start_date)):
    if(start_date_month[i]==month):
        Total += (df['Total Booking'][i])
        BMS+=(df['BMS Book'][i])
        PayTM+=(df['PayTM Book'][i])
        AmazonPay+=df['Amazon Pay Book'][i]
        Other+=df['Other Book'][i]

Tot_Book.append(Total)
Tot_Book.append(BMS)
Tot_Book.append(PayTM)
Tot_Book.append(AmazonPay)
Tot_Book.append(Other)
# print(Tot_Book)

for i in range(len(start_date)):
    if(start_date_month[i]==month):
        Total += (df['Total Cancel'][i])
        BMS+=(df['BMS Cancel'][i])
        PayTM+=(df['PayTM Cancel'][i])
        AmazonPay+=df['Amazon Pay Cancel'][i]
        Other+=df['Other Cancel'][i]

Tot_Cancel.append(Total)
Tot_Cancel.append(BMS)
Tot_Cancel.append(PayTM)
Tot_Cancel.append(AmazonPay)
Tot_Cancel.append(Other)
# print(Tot_Cancel)

        # print(start_date[i].date())
        # print(df['Date'][i],df['Total Booking'][i],df['Total Cancel'][i],df['BMS Book'][i],df['BMS Cancel'][i],df['PayTM Book'][i],df['Amazon Pay Book'][i],df['Amazon Pay Cancel'][i],df['Other Book'][i],df['Other Cancel'][i])
        
        # Tot_Book.append(df['Date'][i])
        # print(Tot_Book)
        
            # Total_Booking=df['Total Booking'].sum()
        # print(Total_Booking)
        # Tot_Book.append(Total_Booking)
        # Total_Cancel=df['Total Cancel'].sum()
        # Tot_Cancel.append(Total_Cancel)
        # BMS_Book=df['BMS Book'].sum()
        # Tot_Book.append(BMS_Book)
        # BMS_Cancel=df['BMS Cancel'].sum()
        # Tot_Cancel.append(BMS_Cancel)
        # PayTM_Book=df['PayTM Book'].sum()
        # Tot_Book.append(PayTM_Book)
        # PayTM_Cancel=df['PayTM Cancel'].sum()
        # Tot_Cancel.append(PayTM_Cancel)
        # AmazonPay_Book=df['Amazon Pay Book'].sum()
        # Tot_Book.append(AmazonPay_Book)
        # AmazonPay_Cancel=df['Amazon Pay Cancel'].sum()
        # Tot_Cancel.append(AmazonPay_Cancel)
        # Other_Book=df['Other Book'].sum()
        # Tot_Book.append(Other_Book)
        # Other_Cancel=df['Other Cancel'].sum()
        # Tot_Cancel.append(Other_Cancel)

        # print(Tot_Book)
        # print(Tot_Cancel)

# N = 5
# ind = np.arange(N) 
# width = 0.35; 
# fig, ax = plt.subplots()

# rects1 = ax.bar(ind, Tot_Book, width, bottom=Tot_Cancel)
# rects2 = ax.bar(ind, Tot_Cancel, width)

# plt.ylabel('Number of tickets')
# plt.title('Total Booking and Cancelation of Movie Booking System')
# plt.xticks(ind, ('Total', 'BMS', 'PayTM', 'AmazonPay', 'Other'))
# plt.legend((rects1[0], rects2[0]), ('Booking', 'Cancelation'))

# autolabel(rects1)
# autolabel(rects2)

# plt.show()


N = 5

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, Tot_Book, width, color='r')

rects2 = ax.bar(ind + width, Tot_Cancel, width, color='y')

# add some text for labels, title and axes ticks
ax.set_ylabel('Number of tickets')
ax.set_title('Total Booking and Cancelation of Movie Booking System')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('Total', 'BMS', 'PayTM', 'AmazonPay', 'Other'))

ax.legend((rects1[0], rects2[0]), ('Booking', 'Cancelation'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()



