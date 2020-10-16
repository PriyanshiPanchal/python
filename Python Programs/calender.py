import datetime 

# start_date = datetime.strptime(input('Enter Start date in the format y/m/d'), '%Y/%m/%d')
# end_date = datetime.strptime(input('Enter End date in the format y/m/d'), '%Y/%m/%d')
 
# date1=print(start_date)
# date2=print(end_date)
# date_time_1=dt.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
# date_time_2=dt.datetime.strptime(date2,'%Y-%m-%d %H:%M:%S')
# datetimeFormat = '%Y-%m-%d %H:%M:%S'
# # date1 = '2016-04-16 00:00:00'
# # date2 = '2016-03-10 00:00:00'
# diff = datetime.datetime.strptime(date_time_1, datetimeFormat)\
#     - datetime.datetime.strptime(date_time_2, datetimeFormat)
 
# print("Days:", diff.days)
 
# d1=start_date.date()
# d2=end_date.date()

# replace=d1.replace('-',',')
today = datetime.date.today()
print(today)
in_year = int(input("enter year :"))
in_mon = int(input("enter mon :"))
in_date = int(input("enter date :"))

birthdate = datetime.date(in_year,in_mon,in_date)
# print(birthdate)
diff = (today - birthdate).days
print("difference between dates are :",diff,"days")



