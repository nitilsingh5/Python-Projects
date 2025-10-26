# Customer Management System
import pickle
import json
# Buisness Logic Layer
class Customer:
    cus_list=[]

    def __init__(self):
        self.id=''
        self.name=''
        self.age=''
        self.mob=''

    def addCustomer(self):
        Customer.cus_list.append(self)
        return

    def searchCustomer(self):
        for cus in Customer.cus_list:
            if cus.id==self.id:
                return cus
    
    def deleteCustomer(self):
        for cus in Customer.cus_list:
            if cus.id==self.id:
                Customer.cus_list.remove(cus)
    
    def modifyCustomer(self):
        for cus in Customer.cus_list:
            if cus.id==self.id:
                cus.name=self.name
                cus.age=self.age
                cus.mob=self.mob
    
    @staticmethod
    def save_to_pickle():
        f=open(r'C:\Users\nitil\OneDrive\Desktop\Study\Python\Project\Python Projects\Customer Management System\cus_list.txt','wb')
        pickle.dump(Customer.cus_list,f)
    
    @staticmethod
    def load_from_pickle():
        f=open(r'C:\Users\nitil\OneDrive\Desktop\Study\Python\Project\Python Projects\Customer Management System\cus_list.txt','rb')
        Customer.cus_list=pickle.load(f)
    
    @staticmethod
    def obj_to_dict(cus):
        return cus.__dict__
    @staticmethod
    def save_to_json():
        f=open(r'C:\Users\nitil\OneDrive\Desktop\Study\Python\Project\Python Projects\Customer Management System\cus_list.txt','w')
        json.dump(Customer.cus_list,f,default=Customer.obj_to_dict)
    
    @staticmethod
    def dict_to_obj(d):
        cus=Customer()
        cus.id=d['id']
        cus.name=d['name']
        cus.age=d['age']
        cus.mob=d['mob']
        return cus
    @staticmethod
    def load_from_json():
        f=open(r'C:\Users\nitil\OneDrive\Desktop\Study\Python\Project\Python Projects\Customer Management System\cus_list.txt','r')
        Customer.cus_list=json.load(f,object_hook=Customer.dict_to_obj)
    
    @staticmethod
    def sort_criteria(cus):
        return cus.id

    @staticmethod
    def sort_by_id():
        Customer.cus_list.sort(key=Customer.sort_criteria)

# Presentation Layer
if __name__=="__main__":
    print('Welcome To Customer Management System')
    def show_Customer(cus):
        print('Cust ID:',cus.id,'Cust Name:',cus.name,'Cust Age:',cus.age,'Cust Mob:',cus.mob)

    while(1):
        ch=input('Enter Choice: 1.Add Customer, 2.Search Customer, 3.Delete Customer, 4.Modify Customer, 5.View All Customer, 6.save_to_pickle, 7.load_from_pickle, 8.save_to_json, 9.load_from_json, 10.sort, 11.exit: ')
        if ch=='1':
            cus=Customer()
            cus.id=input('Enter Customer ID: ')
            cus.name=input('Enter Customer Name: ')
            cus.age=input('Enter Customer Age: ')
            cus.mob=input('Enter Customer Mob: ')
            cus.addCustomer()
            print('Customer added Suceessfully')

        elif ch=='2':
            cus=Customer()
            cus.id=input('Enter Customer ID to Search: ')
            i=cus.searchCustomer()
            show_Customer(i)

        elif ch=='3':
            cus=Customer()
            cus.id=input('Enter Customer ID to Delete: ')
            cus.deleteCustomer()
            print('Customer Deleted Successfully')
        
        elif ch=='4':
            cus=Customer()
            cus.id=input('Enter Customer ID to Modify: ')
            cus.name=input('Enter Customer Name: ')
            cus.age=input('Enter Customer Age: ')
            cus.mob=input('Enter Customer Mob: ')
            cus.modifyCustomer()
            print('Customer Modified')
        
        elif ch=='5':
            for cus in Customer.cus_list:
                show_Customer(cus)
        
        elif ch=='6':
            Customer.save_to_pickle()
            print('Saved to Pickle')
        
        elif ch=='7':
            Customer.load_from_pickle()
            print('loaded from pickle')
        
        elif ch=='8':
            Customer.save_to_json()
            print('Saved to Json')
        
        elif ch=='9':
            Customer.load_from_json()
            print('loaded from Json')
        
        elif ch=='10':
            Customer.sort_by_id()
            print('sorted')
        
        elif ch=='11':
            print('Thank You for using Customer Management System')
            break
        
        else:
            print('Incorrect Choice Please Enter Correct Choice')