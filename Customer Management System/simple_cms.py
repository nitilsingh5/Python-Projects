# Busisness Logic Layer

id_list=[]
name_list=[]
age_list=[]
mob_list=[]




# Presentation Layer
print('Welcome to Customer Management System')



while(1):
    ch=input('Enter Choice : 1.add_customer 2.search_customer 3.delete_customer 4.modify_customer 5.view_all_customers 6.exit: ')
    if ch=='1':
        id=input('Enter Customer ID: ')
        name=input('Enter Customer Name: ')
        age=input('Enter Customer Age: ')
        mob=input('Enter Customer Mobile Number: ')
        