import matplotlib.pyplot as plt
from datetime import datetime
import csv
import numpy as np
import pandas as pd

def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%d' % int(height), ha='center', va='bottom')

branch1 = pd.read_csv("Branch1.csv")
df1=pd.DataFrame(branch1)
branch2 = pd.read_csv("Branch2.csv")
df2=pd.DataFrame(branch2)
branch3 = pd.read_csv("Branch3.csv")
df3=pd.DataFrame(branch3)
branch4 = pd.read_csv("Branch4.csv")
df4=pd.DataFrame(branch4)
branch5 = pd.read_csv("Branch5.csv")
df5=pd.DataFrame(branch5)

frames=['Branch1.csv','Branch2.csv','Branch3.csv','Branch4.csv','Branch5.csv']

datelist=df1['Date']
start_date=(pd.to_datetime(df1['Date'], format='%d-%m-%Y'))
start_date_year=start_date.dt.year
print(start_date_year)
# df1.plot.bar(x='Revenue Type',y='Total Collections')
# plt.show()
def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%d' % int(height), ha='center', va='bottom')

choice1 = int(input('1.Yearly Collection Of All Branchesn\n2.Quaterly Collection(Gross)\n'
                        '3.Quaterly Collection(Branch Wise)\n4.Performance of a Branch on given Date Range\n'
                        '5.Collection of Whole Year For Selective Branch\n'
                        '6.Find Total shares of all branches with reeespect to Revenue Type(MonthWise)'))
if choice1 == 1:

    year=int(input("Enter the year"));
    
    for i in range(len(frames)):
        if(start_date_year[i]==2020):
            print("Matched")
        
            list1=df1['Total Collections'][i].sum(),df2['Total Collections'][i].sum(),df3['Total Collections'][i].sum(),df4['Total Collections'][i].sum(),df5['Total Collections'][i].sum()
            print(list1)
            x = np.arange(5)
            fig, ax = plt.subplots()
            rect1 = plt.bar(x, list1, width=0.2)
            
            plt.ylabel('Total Collections')
            plt.title('Yearly Total Collections of all Branches ')
            plt.xticks(x, ('Branch1', 'Branch2', 'Branch3', 'Branch4', 'Branch5'))
            plt.legend('Total Collections')
            
            autolabel(rect1)
            plt.show()
            

elif choice1 == 2:

    q1_b=[]
    q2_b=[]
    q3_b=[]
    q4_b=[]

    for x in range(len(frames)):
        branch = pd.read_csv(frames[x])
        df = pd.DataFrame(branch)
        q1 = df[df["Date"].between('2020-01-01', '2020-03-31')]
        q2 = df[df["Date"].between('2020-04-01', '2020-06-31')]
        q3 = df[df["Date"].between('2020-07-01', '2020-09-31')]
        q4=df[df['Date'].between('2020-10-01','2020-12-31')]
        t1 = q1['Total Collections'].sum()
        t2 = q2['Total Collections'].sum()
        t3 = q3['Total Collections'].sum()
        t4 = q4['Total Collections'].sum()
        q1_b.append(t1)
        q2_b.append(t2)
        q3_b.append(t3)
        q4_b.append(t4)
    final = [sum(q1_b), sum(q2_b), sum(q3_b), sum(q4_b)]
    i = np.arange(3)
    rect1 = plt.bar(i, final, width=0.2)
    plt.xticks(i, ['Quarter1', 'Quarter2', 'Quarter3','Quarter4'])
    autolabel(rect1)
    plt.show()

elif choice1 == 3:

    b_name =input("Enter Branch Name")
    for x in range(len(all_files)):
        if (b_name + '.csv').lower() == frames[x].lower():
            branch = pd.read_csv(all_files[x])
            df = pd.DataFrame(branch)
            q1 = df[df["Date"].between('2020-01-01', '2020-04-04')]
            q2 = df[df["Date"].between('2020-05-01', '2020-08-04')]
            q3 = df[df["Date"].between('2020-09-01', '2020-12-04')]
            q4=df
            bt1 = q1['Total_Collection'].sum()
            bt2 = q2['Total_Collection'].sum()
            bt3 = q3['Total_Collection'].sum()
    final = [bt1, bt2, bt3]
    i = np.arange(3)
    rect1 = plt.bar(i, final, width=0.2)
    plt.xticks(np.arange(3), ['Quarter1', 'Quarter2', 'Quarter3'])
    autolabel(rect1)
    plt.show()
elif choice1 == 4:
    d_from=input('From:')
    d_to=input('To')
    Cinema_Functions.perfomance(d_from, d_to)
elif choice1 == 5:
    b_name= input("Enter Branch Name")
    Cinema_Functions.collection_Whole_Year(b_name)
elif choice1 == 6:
    choice2 = int(input('1.Screen-1\n2.Screen-2\n3.Screen-3\n4.Food & Beverages\n5.Advertisment'))
    if choice2==1:
        r_name='Screen-1'
        Cinema_Functions.revenue_Type(r_name)
    elif choice2==2:
        r_name='Screen-2'
        Cinema_Functions.revenue_Type(r_name)
    elif choice2==3:
        r_name='Screen-3'
        Cinema_Functions.revenue_Type(r_name)
    elif choice2==4:
        r_name='Food & Beverages'
        Cinema_Functions.revenue_Type(r_name)
    elif choice2==5:
        r_name='Advertisment'
        Cinema_Functions.revenue_Type(r_name)
    else:
        print("Invalid Choice")
else:
    print('Invalid Choice')

