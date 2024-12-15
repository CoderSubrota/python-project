import random 

class UserInfo:
    def __init__(self,id,name,email,age,city,gender):
        self.id=id
        self.name=name
        self.email=email
        self.age=age
        self.city=city
        self.gender=gender

class Customer(UserInfo):
     def __init__(self, id, name, email, age, city,gender):
         super().__init__(id,name, email, age, city, gender)
         
     def __repr__(self):
                 return f" ID:{self.id} \n Name:{self.name} \n Email:{self.email} \n Age:{self.age} \n City:{self.city} \n Gender:{self.gender}"

         
class Admin(UserInfo):
    def __init__(self, id, name, email, age, city, gender,salary,address,designation):
        super().__init__(id, name, email, age, city, gender)
        self.salary=salary
        self.address=address
        self.designation=designation

    def __repr__(self):
                   return f" ID:{self.id} \n Name:{self.name} \n Email:{self.email} \n Age:{self.age} \n City:{self.city} \n Gender:{self.gender} \n Salary:{self.salary} \n Address:{self.address} \n Designation:{self.designation}"

class Employee(Admin):
     def __init__(self, id, name, email, age, city, gender, salary, address, designation):
         super().__init__(id, name, email, age, city, gender, salary, address, designation)
     
     def __repr__(self):
               return f" ID:{self.id} \n Name:{self.name} \n Email:{self.email} \n Age:{self.age} \n City:{self.city} \n Gender:{self.gender} \n Salary:{self.salary} \n Address:{self.address} \n Designation:{self.designation}"


class Manage_Admin:
    admin_list=[]
    
    @classmethod
    def add_admin(self, add_new_admin):
        self.admin_list.append(add_new_admin)
        print("\n --------- Admin account created successfully --------- \n")
        
    @classmethod
    def show_admin(self):
        print("\n ----- Admin List ----- \n")
        for admin in self.admin_list:
            print(admin)
            print("*"*50)      
        
class Manage_Customer:
      customer_list=[]
      
      @classmethod
      def add_customer(self,add_new_customer):
          self.customer_list.append(add_new_customer)
          print("\n-------- Customer Added Successfully -------\n")
          
      @classmethod
      def show_customer(self):
          print("\n-------- Customer List -------\n")
          for customer in self.customer_list:
              print(customer)
              print("*"*50)
              
      @classmethod
      def delete_customer(self,id):
        message=""
        if self.customer_list: 
            for customer in self.customer_list:
                if  int(customer.id) == id:
                  result = list(filter(lambda item: item.id != id,self.customer_list))
                  self.customer_list=result 
                  message="\n-------- Customer deleted -------\n"
                  break
                else:
                    message= f"\n Customer not available by {id} id"
                    break
        else:
             message="\n-------- Customer not found -------\n"
             
        print(message)

class Manage_Employee:
      employee_list=[]
      
      @classmethod
      def add_employee(self,add_new_employee):
          self.employee_list.append(add_new_employee)
          print("\n-------- Employee Added Successfully -------\n")
          
      @classmethod
      def show_employee(self):
          print("\n-------- Employee List -------\n")
          for employee in self.employee_list:
              print(employee)
              print("*"*50)
          
      @classmethod
      def delete_employee(self,id):
        message=""
        if self.employee_list:
          for employee in self.employee_list:
              if int(employee.id) == id :
                  result = list(filter(lambda item: item.id != id, self.employee_list))
                  self.employee_list=result
                  message="\n-------- Employee deleted -------\n"
                  break
              else:
                  message="Employee not available by this : ", id
                  break
        else:
            message="\n-------- Employee not found -------\n"
            
        print(message)
        
class Add_Item:
    def __init__(self,id, item_name,item_price, item_quantity):
        self.id=id
        self.item_name=item_name
        self.item_price=item_price 
        self.item_quantity=item_quantity
        
    def __repr__(self):
        return f" ID: {self.id}\n Name:{self.item_name}\n Price:{self.item_price}\n Quantity:{self.item_quantity}"

class Item_Management:
      item_list=[]
      
      @classmethod
      def add_item(self,add_new_item):
          self.item_list.append(add_new_item)
          print("\n-------- Item Added Successfully -------\n")
          
      @classmethod
      def show_item(self):
          print("\n-------- Item List -------\n")
          for item in self.item_list:
              print(item)
              print("*"*50)
             
      @classmethod
      def delete_item(self,id):
        message=""
        if self.item_list:
            for item in self.item_list:
              if int(item.id) == id :
                  result = list(filter(lambda item: item.id != id, self.item_list))
                  self.item_list=result
                  # [1,2,3,[1,3]] Not Ok  => OK [1,2,3] => [1,3]
                  message="\n-------- Item deleted -------\n"
                  break
              else:
                 
                 message="\n >>>>>>> Item not available"
                 break
        else:
             message="\n-------- Item not found -------\n"
             
        print(message)

class Item_Order:
    def __init__(self,id,item_name,item_quantity):
        
        self.id=id
        self.item_name=item_name
        self.item_quantity=item_quantity

    def __repr__(self):
        return f" ID:{self.id} \n Item Name:{self.item_name} \n Item Quantity:{self.item_quantity}"
    
class Order_Management:
     order_list=[]
     sum_of_total_products=0
     
     @classmethod 
     def total_price(self,quantity,price):
          get_price = quantity*price
          self.sum_of_total_products+=get_price
      
     @classmethod
     def add_order(self,add_new_order):
             message=""
             for item in Item_Management.item_list:
                 if item.item_name.lower()==add_new_order.item_name.lower():
                     print(item.item_quantity,add_new_order.item_quantity)
                     if item.item_quantity >=  add_new_order.item_quantity:
                        self.order_list.append(add_new_order)
                        item.item_quantity =  item.item_quantity - add_new_order.item_quantity
                        message="\n --------- Congratulation your order has been placed !! --------- \n"
                        self.total_price(item.item_quantity,int( item.item_price))
                        break
                     else:
                       message="\n >>> Sorry!! quantity is not sufficient"
                       break
                 else:
                    message="\n --------- Your order item is not available --------- \n"
             print(message)

     @classmethod
     def show_order(self):
         print("\n ---------- Order List --------- \n")
         print(f"ID  Item Name  Item Price")
         for order in self.order_list:
             print(order)
             print("*"*50)
               
         print(f"\n >>>>> You have to pay just: ${self.sum_of_total_products} <<<<<")

class Pay_Bill:
    @classmethod
    def pay_bill(self,amount):
        
        if Order_Management.order_list:
            if int(Order_Management.sum_of_total_products) == int(amount):
             print(f"\n---------- Thanks sir, your bill paid successfully ${amount} !! ----------\n")
             Order_Management.order_list=[]
            else:
                print(f"\n Please pay us ${Order_Management.sum_of_total_products} amount sir !!")
        else:
            print("\n <<<< There is no order till now !! >>>> \n")


class Customer_Access:
    
    @classmethod
    def customer_menu(self):
        while True:
            print("\n------- Welcome Dear Customer ------- \n")
            print("------- 1.Order an Item -------")
            print("------- 2.Pay bill -------")
            print("------- 3.Show Order -------")  
            print("------- 4.Exit -------")  
            
            choice = input(">> Enter your option: ")
            choice_int = int(choice)
            
            if choice_int==1:
                id = random.randint(20,500)
                item_name = input(">> Enter your item name: ") 
                item_quantity = input(">> Enter your item quantity: ") 
                item_quantity_int=int(item_quantity)
                
                new_order = Item_Order(id=id, item_name=item_name, item_quantity=item_quantity_int)
                Order_Management.add_order(new_order)
                
            elif choice_int==2:
                amount = input(">> Enter your amount: ") 
                Pay_Bill.pay_bill(amount)
                
            elif choice_int==3:
                Order_Management.show_order()
            
            elif choice_int == 4:
                print("\n --------- You are exit from order menu --------- \n")
                break
            else:
                print("\n ========== Please enter valid input between 1 to 4. ==========")
                
class Admin_Access:
         @classmethod
         def admin_menu(self):
             while True:
                 print("\n ********** Welcome Dear Admin **********\n")
                 print("--------- 1.Show Customer Data -----------") 
                 print("--------- 2.Delete Customer Data -----------") 
                 print("--------- 3.Add Employee -----------") 
                 print("--------- 4.Show Employee Data -----------") 
                 print("--------- 5.Delete Employee -----------") 
                 print("--------- 6.Add new Item -----------") 
                 print("--------- 7.Show Items -----------") 
                 print("--------- 8.Delete Items -----------") 
                 print("--------- 9.Show Admin Data -----------")     
                 print("--------- 10.Exit -----------")    
                 
                 choice = input(">> Enter your option: ")
                 choice_int = int(choice)
                 
                 if choice_int==1:
                     Manage_Customer.show_customer()
                 elif choice_int==2:
                     id = input(">> Enter customer id: ") 
                     id_int = int(id) 
                     Manage_Customer.delete_customer(id=id_int)
                     
                 elif choice_int==3:
                    id = random.randint(100,2000) 
                    name = input(">> Enter employee name: ")
                    email = input(">> Enter employee email: ")
                    age = input(">> Enter employee age: ")
                    city = input(">> Enter employee city: ")
                    gender = input(">> Enter employee gender: ")
                    salary= input(">> Enter employee salary: ")
                    address = input(">> Enter employee address: ")
                    designation=input(">> Enter employee designation: ")
                    
                    new_employee = Employee(id=id,name=name,email=email,age=age,city=city,gender=gender,salary=salary,address=address,designation=designation)
                    Manage_Employee.add_employee(new_employee)
                 
                 elif choice_int==4: 
                    Manage_Employee.show_employee()
                    
                 elif choice_int==5:
                   id  = input(">> Enter employee id: ")
                   id_int = int(id)
                   Manage_Employee.delete_employee(id=id_int)
                   
                 elif choice_int==6:
                     id = random.randint(20,380) 
                     item_name = input(">> Enter your item name: ") 
                     item_price = input(">> Enter your item price: ") 
                     item_quantity = input(">> Enter your item quantity: ") 
                     item_quantity_int=int(item_quantity)
                     new_item = Add_Item(id=id, item_name=item_name, item_price=item_price, item_quantity=item_quantity_int)
                     Item_Management.add_item(new_item)
                
                 elif choice_int==7:  
                     Item_Management.show_item() 
                     
                 elif choice_int==8:
                   id  = input(">> Enter employee id: ")
                   id_int = int(id)
                   Item_Management.delete_item(id=id_int)
                   
                 elif choice_int==9: 
                     Manage_Admin.show_admin()
                     
    
                 elif choice_int==10:
                     print("\n >>------->> Your Exited <<---------<<")
                     break
                 
                 else:
                     print("\n ------- Please choice your option between 1 to 10 -------")
                    
    
while True:
    print("\n ********* Welcome dear user ********* \n")
    print("1. Create account for customer")
    print("2. Create account for admin")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    choice_int = int(choice)
    
    if choice_int==1:
        
        id = random.randint(100,2000) 
        name = input(">> Enter your name: ")
        email = input(">> Enter your email: ")
        age = input(">> Enter your age: ")
        city = input(">> Enter your city: ")
        gender = input(">> Enter your gender: ")
        
        new_customer = Customer(id=id, name=name,email=email,age=age,city=city,gender=gender)
        Manage_Customer.add_customer(new_customer)
        
        Customer_Access.customer_menu()
        
    elif choice_int==2:
        
        id = random.randint(100,2000) 
        name = input(">> Enter your name: ")
        email = input(">> Enter your email: ")
        age = input(">> Enter your age: ")
        city = input(">> Enter your city: ")
        gender = input(">> Enter your gender: ")
        salary= input(">> Enter your salary: ")
        address = input(">> Enter your address: ")
        designation=input(">> Enter your designation: ")
        
        new_admin = Admin(id=id, name=name,email=email,age=age,city=city,gender=gender,salary=salary,address=address,designation=designation)
        Manage_Admin.add_admin(new_admin)
        
        Admin_Access.admin_menu()
        
    elif choice_int == 3:
        print("\n ---- You are exited from restaurant menu ----- \n")   
        break
          
    else:
        print("\n ---- Invalid input enter your valid option between 1 to 3 ----- \n")   
        
    