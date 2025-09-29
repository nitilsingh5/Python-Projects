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

def search_by_Id(id):
    index=id_list.index(id)
    return index

def search_by_Name(name):
    index=name_list.index(name)
    return index

def search_by_Mob(mob):
    index=mob_list.index(mob)
    return index

def delete_by_Id(id):
    index=id_list.index(id)
    id_list.pop(index)
    name_list.pop(index)
    age_list.pop(index)
    mob_list.pop(index)
    return

def delete_by_Name(name):
    index=name_list.index(name)
    id_list.pop(index)
    name_list.pop(index)
    age_list.pop(index)
    mob_list.pop(index)
    return

def delete_by_Mob(mob):
    index=mob_list.index(mob)
    id_list.pop(index)
    name_list.pop(index)
    age_list.pop(index)
    mob_list.pop(index)
    return

def modify_Customer(id,name,age,mob):
    i=id_list.index(id)
    name_list[i]=name
    age_list[i]=age
    mob_list[i]=mob
    return

# Presentation Layer
print('Welcome to Customer Management System')

def show_Customer(i):
    print('Cust ID:',id_list[i],'Cust Name:',name_list[i],'Cust Age:',age_list[i],'Cust Mob:',mob_list[i])

def get_Id():
    while(1):
        id=input('Enter Customer ID: ')
        if id.isdecimal():
            if id not in id_list:
                return id
            else:
                print('Duplicate ID')
        else:
            print('Enter in number only')

def get_Mob():
    while(1):
        mob=input('Enter Customer Mobile Number: ')
        if mob.isdecimal():
            if len(mob)==10:
                return mob
            else:
                print('Enter only 10 digits Mobile Number')
        else:
            print('Enter Only in Digits')




while(1):
    ch=input('Enter Choice : 1.add_customer 2.search_customer 3.delete_customer 4.modify_customer 5.view_all_customers 6.exit: ')
    if ch=='1':
        # id=input('Enter Customer ID: ')
        id=get_Id()
        name=input('Enter Customer Name: ')
        age=input('Enter Customer Age: ')
        # mob=input('Enter Customer Mobile Number: ')
        mob=get_Mob()
        add_Customer(id,name,age,mob)
        print('Customer Added Successfully')
    
    elif ch=='2':
        while(1):
            ch=input('Enter Choice to Search: 1.by id 2.by name 3.by mob 4.back to main: ')
            if ch=='1':
                id=input('Enter Id to Search Customer: ')
                i=search_by_Id(id)
                show_Customer(i)
            elif ch=='2':
                name=input('Enter Customer Name to Search Customer: ')
                i=search_by_Name(name)
                show_Customer(i)
            elif ch=='3':
                mob=input('Enter Customer Mob to Search Customer: ')
                i=search_by_Mob(mob)
                show_Customer(i)
            elif ch=='4':
                print('Back to Main')
                break
    
    elif ch=='3':
        while(1):
            ch=input('Enter Choice to Delete: 1.by id 2.by name 3.by mob 4.back to main: ')
            if ch=='1':
                id=input('Enter ID to Delete Customer: ')
                delete_by_Id(id)
                print('Customer Deleted Successfully')
            elif ch=='2':
                name=input('Enter Customer Name to Search Customer: ')
                delete_by_Name(name)
                print('Customer Deleted Successfully')
            elif ch=='3':
                mob=input('Enter Customer Mob to Search Customer: ')
                delete_by_Mob(mob)
                print('Customer Deleted Successfully')
            elif ch=='4':
                print('Back to Main')
                break
        

    elif ch=='4':
        id=input('Enter Customer ID to Update: ')
        name=input('Enter Customer Name to Update: ')
        age=input('Enter Customer Age to Update: ')
        mob=input('Enter Customer Mobile Number to Update: ')
        modify_Customer(id,name,age,mob)
        print('Customer Modified Successfully')
    
    elif ch=='5':
        for i in range(len(id_list)):
            show_Customer(i)
    
    elif ch=='6':
        print('Thank You for using Customer Management System')
        break
    
    else:
        print('Incorrect Choice')


