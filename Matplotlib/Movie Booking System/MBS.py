from datetime import datetime
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

df = pd.read_csv("BookingData.csv")
df.head()


Sum_Total= df['Total Booking'].sum()
# print(sum_total)

BMS_Total=df['BMS Book'].sum()
# print(BMS_Total)

PayTM_Total=df['PayTM Book'].sum()
# print(PayTM_Total)

Amazon_Total=df['Amazon Pay Book'].sum()
# print(Amazon_Total)

Other_Total=df['Other Book'].sum()
# print(Other_Total)

Sum_Total_Cancel= df['Total Cancel'].sum()
BMS_Total_Cancel=df['BMS Cancel'].sum()
PayTM_Total_Cancel=df['PayTM Cancel'].sum()
Amazon_Total_Cancel=df['Amazon Pay Cancel'].sum()
Other_Total_Cancel=df['Other Cancel'].sum()

fig = plt.figure(figsize=(40,40), dpi=100)
ax1 = plt.subplot2grid((4,2),(0,0))
y = 'Total','BMS','PayTM','Amazon Pay','Other'
x = [Sum_Total, BMS_Total, PayTM_Total, Amazon_Total, Other_Total]  
plt.pie(x, labels=y, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Movie Ticket Booking', bbox={'facecolor':'0.8', 'pad':5})

ax1 = plt.subplot2grid((4,2),(0,1))
y = 'Total','BMS','PayTM','Amazon Pay','Other'
x = [Sum_Total_Cancel, BMS_Total_Cancel, PayTM_Total_Cancel, Amazon_Total_Cancel, Other_Total_Cancel]  
plt.pie(x, labels=y, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Movie Ticket Cancelation', bbox={'facecolor':'0.8', 'pad':5})
plt.show()