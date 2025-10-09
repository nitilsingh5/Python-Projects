import pickle
# Business Logic Layer

id_list = []
name_list = []
age_list = []
mob_list = []

def add_Customer(id, name, age, mob):
    try:
        id_list.append(id)
        name_list.append(name)
        age_list.append(age)
        mob_list.append(mob)
    except Exception as e:
        print("Error while adding customer:", e)

def search_by_Id(id):
    try:
        index = id_list.index(id)
        return index
    except ValueError:
        print("Customer ID not found.")
        return None

def search_by_Name(name):
    try:
        index = name_list.index(name)
        return index
    except ValueError:
        print("Customer Name not found.")
        return None

def search_by_Mob(mob):
    try:
        index = mob_list.index(mob)
        return index
    except ValueError:
        print("Customer Mobile not found.")
        return None

def delete_by_Id(id):
    try:
        index = id_list.index(id)
        id_list.pop(index)
        name_list.pop(index)
        age_list.pop(index)
        mob_list.pop(index)
    except ValueError:
        print("Customer ID not found, cannot delete.")
    except Exception as e:
        print("Error while deleting customer:", e)

def delete_by_Name(name):
    try:
        index = name_list.index(name)
        id_list.pop(index)
        name_list.pop(index)
        age_list.pop(index)
        mob_list.pop(index)
    except ValueError:
        print("Customer Name not found, cannot delete.")
    except Exception as e:
        print("Error while deleting customer:", e)

def delete_by_Mob(mob):
    try:
        index = mob_list.index(mob)
        id_list.pop(index)
        name_list.pop(index)
        age_list.pop(index)
        mob_list.pop(index)
    except ValueError:
        print("Customer Mobile not found, cannot delete.")
    except Exception as e:
        print("Error while deleting customer:", e)

def modify_Customer(id, name, age, mob):
    try:
        i = id_list.index(id)
        name_list[i] = name
        age_list[i] = age
        mob_list[i] = mob
    except ValueError:
        print("Customer ID not found, cannot modify.")
    except Exception as e:
        print("Error while modifying customer:", e)

def save_to_pickle():
    try:
        data = {
            'id_list': id_list,
            'name_list': name_list,
            'age_list': age_list,
            'mob_list': mob_list
        }
        with open('customers.pkl', 'wb') as f:
            pickle.dump(data, f)
        print("Data saved successfully.")
    except Exception as e:
        print("Error saving data:", e)

def load_from_pickle():
    global id_list, name_list, age_list, mob_list
    try:
        with open('customers.pkl', 'rb') as f:
            data = pickle.load(f)
            id_list = data['id_list']
            name_list = data['name_list']
            age_list = data['age_list']
            mob_list = data['mob_list']
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No saved file found. Please save data first.")
    except Exception as e:
        print("Error loading data:", e)

# Presentation Layer
print('Welcome to Customer Management System')

def show_Customer(i):
    try:
        print('Cust ID:', id_list[i], 'Cust Name:', name_list[i], 'Cust Age:', age_list[i], 'Cust Mob:', mob_list[i])
    except IndexError:
        print("Invalid customer index.")

def get_Id():
    while True:
        id = input('Enter Customer ID: ')
        if id.isdecimal():
            if id not in id_list:
                return id
            else:
                print('Duplicate ID')
        else:
            print('Enter numbers only.')

def get_Mob():
    while True:
        mob = input('Enter Customer Mobile Number: ')
        if mob.isdecimal():
            if len(mob) == 10:
                return mob
            else:
                print('Enter exactly 10 digits for mobile number.')
        else:
            print('Enter digits only.')

while True:
    try:
        ch = input('Enter Choice : 1.add_customer 2.search_customer 3.delete_customer 4.modify_customer 5.view_all_customers 6.save 7.load 8.exit: ')
        
        if ch == '1':
            id = get_Id()
            name = input('Enter Customer Name: ')
            age = input('Enter Customer Age: ')
            mob = get_Mob()
            add_Customer(id, name, age, mob)
            print('Customer Added Successfully')
        
        elif ch == '2':
            while True:
                ch2 = input('Search: 1.by id 2.by name 3.by mob 4.back: ')
                if ch2 == '1':
                    id = input('Enter Id: ')
                    i = search_by_Id(id)
                    if i is not None:
                        show_Customer(i)
                elif ch2 == '2':
                    name = input('Enter Name: ')
                    i = search_by_Name(name)
                    if i is not None:
                        show_Customer(i)
                elif ch2 == '3':
                    mob = input('Enter Mob: ')
                    i = search_by_Mob(mob)
                    if i is not None:
                        show_Customer(i)
                elif ch2 == '4':
                    break
        
        elif ch == '3':
            while True:
                ch2 = input('Delete: 1.by id 2.by name 3.by mob 4.backH: ')
                if ch2 == '1':
                    id = input('Enter ID: ')
                    delete_by_Id(id)
                elif ch2 == '2':
                    name = input('Enter Name: ')
                    delete_by_Name(name)
                elif ch2 == '3':
                    mob = input('Enter Mob: ')
                    delete_by_Mob(mob)
                elif ch2 == '4':
                    break
        
        elif ch == '4':
            id = input('Enter ID to modify: ')
            name = input('Enter new Name: ')
            age = input('Enter new Age: ')
            mob = input('Enter new Mobile: ')
            modify_Customer(id, name, age, mob)
        
        elif ch == '5':
            if not id_list:
                print("No customers found.")
            for i in range(len(id_list)):
                show_Customer(i)
        
        elif ch == '6':
            save_to_pickle()
        
        elif ch == '7':
            load_from_pickle()
        
        elif ch == '8':
            print('Thank You for using Customer Management System')
            break
        
        else:
            print('Incorrect Choice')

    except KeyboardInterrupt:
        print("\nProgram exited by user.")
        break
    except Exception as e:
        print("Unexpected error:", e)
