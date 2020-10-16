import Cinema_Functions
restart = ['Yes', 'YES', 'Y', 'yes']
while restart not in ['NO', 'No', 'no', 'N', 'nO', 'n']:
    choice1 = int(input('1.Yearly Collection Of All Branchesn\n2.Quaterly Collection(Gross)\n'
                        '3.Quaterly Collection(Branch Wise)\n4.Performance of a Branch on given Date Range\n'
                        '5.Collection of Whole Year For Selective Branch\n'
                        '6.Find Total shares of all branches with reeespect to Revenue Type(MonthWise)'))
    if choice1 == 1:
        Cinema_Functions.yearly_Colection()
    elif choice1 == 2:
        Cinema_Functions.quaterly_Collection()
    elif choice1 == 3:
        b_name =input("Enter Branch Name")
        Cinema_Functions.quaterly_Collectio(b_name)
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
    restart=input("Do you want to continue?")
