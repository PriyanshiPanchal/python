import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 1*height,
                '%d' % int(height),
                ha='center', va='bottom')
re=pd.read_csv("Revenue Model.csv")
re1=pd.DataFrame(re)
branch_1 = pd.read_csv("Branch1.csv")
df_1 = pd.DataFrame(branch_1)
branch_2 = pd.read_csv("Branch2.csv")
df_2 = pd.DataFrame(branch_2)
branch_3 = pd.read_csv("Branch3.csv")
df_3 = pd.DataFrame(branch_3)
branch_4 = pd.read_csv("Branch4.csv")
df_4 = pd.DataFrame(branch_4)
branch_5 = pd.read_csv("Branch5.csv")
df_5 = pd.DataFrame(branch_5)
all_files=['Branch1.csv','Branch2.csv','Branch3.csv','Branch4.csv','Branch5.csv']
def yearly_Colection():
    list1 = [df_1['Total_Collection'].sum(), df_2['Total_Collection'].sum(), df_3['Total_Collection'].sum(),
             df_4['Total_Collection'].sum(), df_5['Total_Collection'].sum()]
    x = np.arange(5)
    rect1 = plt.bar(x, list1, width=0.2)
    autolabel(rect1)
    plt.show()
q1_b=[]
q2_b=[]
q3_b=[]
def quaterly_Collection():
    for x in range(len(all_files)):
        branch = pd.read_csv(all_files[x])
        df = pd.DataFrame(branch)
        q1 = df[df["Date"].between('2020-01-01', '2020-04-04')]
        q2 = df[df["Date"].between('2020-05-01', '2020-08-04')]
        q3 = df[df["Date"].between('2020-09-01', '2020-12-04')]
        t1 = q1['Total_Collection'].sum()
        t2 = q2['Total_Collection'].sum()
        t3 = q3['Total_Collection'].sum()
        q1_b.append(t1)
        q2_b.append(t2)
        q3_b.append(t3)
    final = [sum(q1_b), sum(q2_b), sum(q3_b)]
    i = np.arange(3)
    rect1 = plt.bar(i, final, width=0.2)
    plt.xticks(np.arange(3), ['Quarter1', 'Quarter2', 'Quarter3'])
    autolabel(rect1)
    plt.show()
def quaterly_Collectio(b_name):
    for x in range(len(all_files)):
        if (b_name + '.csv').lower() == all_files[x].lower():
            branch = pd.read_csv(all_files[x])
            df = pd.DataFrame(branch)
            q1 = df[df["Date"].between('2020-01-01', '2020-04-04')]
            q2 = df[df["Date"].between('2020-05-01', '2020-08-04')]
            q3 = df[df["Date"].between('2020-09-01', '2020-12-04')]
            bt1 = q1['Total_Collection'].sum()
            bt2 = q2['Total_Collection'].sum()
            bt3 = q3['Total_Collection'].sum()
    final = [bt1, bt2, bt3]
    i = np.arange(3)
    rect1 = plt.bar(i, final, width=0.2)
    plt.xticks(np.arange(3), ['Quarter1', 'Quarter2', 'Quarter3'])
    autolabel(rect1)
    plt.show()
def perfomance(d_from, d_to):
    final = []
    for x in range(len(all_files)):
        branch = pd.read_csv(all_files[x])
        df = pd.DataFrame(branch)
        q1 = df[df["Date"].between(d_from, d_to)]
        t1 = q1['Total_Collection'].sum()
        final.append(t1)
    i = np.arange(5)
    rect1 = plt.bar(i, final, width=0.2)
    plt.xticks(np.arange(5), ['Branch1', 'Branch2', 'Branch3', 'Branch4', 'Branch5'])
    autolabel(rect1)
    plt.show()
def collection_Whole_Year(b_name):
    re = pd.read_csv("Revenue Model.csv")
    re1 = pd.DataFrame(re)
    b_name = input("Enter Branch Name")
    final = []
    branch = pd.read_csv(all_files[0])
    df = pd.DataFrame(branch)
    for x in range(len(all_files)):
        if (b_name + '.csv').lower() == all_files[x].lower():
            branch = pd.read_csv(all_files[x])
            df = pd.DataFrame(branch)
            s1 = df[df['Revenue_Type'] == re1['Revenue_Type'][0]]['Total_Collection'].sum()
            s2 = df[df['Revenue_Type'] == re1['Revenue_Type'][1]]['Total_Collection'].sum()
            s3 = df[df['Revenue_Type'] == re1['Revenue_Type'][2]]['Total_Collection'].sum()
            food = df[df['Revenue_Type'] == re1['Revenue_Type'][3]]['Total_Collection'].sum()
            ad = df[df['Revenue_Type'] == re1['Revenue_Type'][4]]['Total_Collection'].sum()
            final = [s1, s2, s3, food, ad]
    name = list(re1['Revenue_Type'])
    i = np.arange(5)
    rect1 = plt.bar(i, final, width=0.2)
    plt.xticks(np.arange(5), name)
    autolabel(rect1)
    plt.show()
def revenue_Type(r_name):
    final=[]
    for x in range(len(all_files)):
        df=pd.read_csv(all_files[x])
        df['Date']=pd.to_datetime(df['Date'],dayfirst=True)
        grp=df.groupby(df['Revenue_Type'])
        a=grp.get_group(r_name)
        df1=(a.groupby(pd.Grouper(key='Date',freq='1M')))['Total_Collection'].sum()
        final=df1.tolist()
    name=list(re1['Month'])
    i=np.arange(12)
    rect1=plt.bar(i,final,width=0.2)
    plt.xticks(np.arange(12),name)
    autolabel(rect1)
    plt.show()