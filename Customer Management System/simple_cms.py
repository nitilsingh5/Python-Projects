# Busisness Logic Layer

id_list=[]
name_list=[]
age_list=[]
mob_list=[]

def add_Customer(id,name,age,mob):
    id_list.append(id)
    name_list.append(name)
    age_list.append(age)
    mob_list.append(mob)
    return

def search_Customer(id):
    index=id_list.index(id)
    return index


# Presentation Layer
print('Welcome to Customer Management System')

def show_Customer(i):
    print('Cust ID:',id_list[i],'Cust Name:',name_list[i],'Cust Age:',age_list[i],'Cust Mob:',mob_list[i])



while(1):
    ch=input('Enter Choice : 1.add_customer 2.search_customer 3.delete_customer 4.modify_customer 5.view_all_customers 6.exit: ')
    if ch=='1':
        id=input('Enter Customer ID: ')
        name=input('Enter Customer Name: ')
        age=input('Enter Customer Age: ')
        mob=input('Enter Customer Mobile Number: ')
        add_Customer(id,name,age,mob)
        print('Customer Added Successfully')
    
    elif ch=='2':
        id=input('Enter Id to Search Customer: ')
        i=search_Customer(id)
        show_Customer(i)
