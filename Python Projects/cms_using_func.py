# Customer Management System

# Buisness Logic Layer
id_list=[]
name_list=[]
age_list=[]
mob_list=[]

def addCustomer(id,name,age,mob):
    id_list.append(id)
    name_list.append(name)
    age_list.append(age)
    mob_list.append(mob)

def searchCustomer(id):
    index=id_list.index(id)
    return index

def deleteCustomer(id):
    i=id_list.index(id)
    id_list.pop(i)
    name_list.pop(i)
    age_list.pop(i)
    mob_list.pop(i)

def modifyCustomer(id,name,age,mob):
    i=id_list.index(id)
    name_list[i]=name
    age_list[i]=age
    mob_list[i]=mob




# Presentation Layer
print('Welcome to Customer Management System')

def showCustomer(i):
    print('Cust Id:',id_list[i],'Cust Name:',name_list[i],'Cust Age:',age_list[i],'Cust Mob:',mob_list[i])

while(2):
    print('1 for Add Customer, 2 for Search Customer, 3 for Delete Cuetomer, 4 for Modify Customer, 5 for View All Customer and 6 for Exit: ')
    choice=input('Enter choice 1 from 6: ')
    
    if choice=='1':         # Add Customer
        id=input('Enter Customer ID: ')
        name=input('Enter Customer Name: ')
        age=input('Enter Customer Age: ')
        mob=input('Enter Customer Mob: ')
        addCustomer(id,name,age,mob)
        print('Customer Added')

    elif choice=='2':       # Search Customer
        id=input('Enter Customer ID to Search: ')
        i=searchCustomer(id)
        showCustomer(i)    

    elif choice=='3':       # Delete Customer
        id=input('Enter Customer ID to Delete: ')
        deleteCustomer(id)
        print('Customer Deleted')

    elif choice=='4':       # Modify Customer
        id=input('Enter Customer ID to Modify: ')
        name=input('Enter Customer Name to Modify: ')
        age=input('Enter Customer Age to modify: ')
        mob=input('Enter Customer Mob to modify: ')
        modifyCustomer(id,name,age,mob)
        print('Customer Modified')

    elif choice=='5':       # Veiw All Customer
        for i in range(len(id_list)):
            showCustomer(i)
    
    elif choice=='6':       # Exit from Customer Management System
        print('Thanks For using Customer Management System')
        break

    else:                   # Incorrect Choice
        print('Incorrect Choice')