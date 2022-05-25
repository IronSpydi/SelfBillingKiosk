from datetime import datetime
import json
from display_rates import display
obj_d = display()
#new_data = {vehicle_number:{'date & time':str(date_time),'vehicle Park time':str(Entry_time),'booked slot':slot_booked,'Wheeler type':Wheel_check}}

class order:
    def change_qt(self,item,qt):
        with open("menu.json",'r') as f:
            data = json.load(f)
        #new_qt = data['Menu'][item][2] - qt
        data['Menu'][item][2]-=qt
        data.update(data)
        with open("menu.json",'w') as f:
            json.dump(data,f,indent=4)
        
    def take_orders(self,name):
        print("What do you wanna eate we have")
        obj_d.display_menu()
        print("I    : Idly")
        print("D    : Dosa")
        print("P    : Poori")
        print("C    : Chapathi")
        print("PR   : Parotha")
        print("Q    : Thanks for now we will call you again !")

        
        while True:
            # take input from the user         
            choice = input("Enter your choice(I/D/P/C/PR/Q): ")

            # check if choice is one of the four options
            if choice in ('I','D','P','C','PR','Q'):
                if choice == 'I':
                    qt = int(input("Enter Quantity for Idly :"))
                    self.change_qt("Idly",qt) 

                    with open('data_stor.json') as f:
                        data = json.load(f)
                    new_data = {'Idly':qt}
                    data[name].update(new_data)

                    with open('data_stor.json','w') as f:
                        json.dump(data,f,indent=2)
                elif choice == 'D':
                    qt = int(input("Enter Quantity for Dosa:"))
                    self.change_qt("Dosa",qt) 
                    with open('data_stor.json') as f:
                        data = json.load(f)
                    new_data = {'Dosa':qt}
                    data[name].update(new_data)

                    with open('data_stor.json','w') as f:
                        json.dump(data,f,indent=2)

                elif choice == 'P':
                    qt = int(input("Enter Quantity for Poori:"))
                    self.change_qt("Poori",qt) 
                    with open('data_stor.json') as f:
                        data = json.load(f)
                    new_data = {'Poori':qt}
                    data[name].update(new_data)

                    with open('data_stor.json','w') as f:
                        json.dump(data,f,indent=2)
                
                elif choice == 'C':
                    qt = int(input("Enter Quantity for Chapati:"))
                    self.change_qt("Chapathi",qt)
                    with open('data_stor.json') as f:
                        data = json.load(f)
                    new_data = {'Chapati':qt}
                    data[name].update(new_data)

                    with open('data_stor.json','w') as f:
                        json.dump(data,f,indent=2)
                elif choice == 'PR':
                    qt = int(input("Enter Quantity for Parotta:"))
                    self.change_qt("Parotta",qt)
                    with open('data_stor.json') as f:
                        data = json.load(f)
                    new_data = {'Parotta':qt}
                    data[name].update(new_data)

                    with open('data_stor.json','w') as f:
                        json.dump(data,f,indent=2)
                else:
                    if choice =='Q':
                        break
            else:
                print("invalid Input")

    def order(self):
        name = input("May i know your name please ?")
        with open('data_stor.json','r') as f:
            data = json.load(f)
        if name not in data:
            new_data = {name:{}}
            data.update(new_data) 
            with open("data_stor.json",'w') as f:
                json.dump(data,f,indent=2)
            self.take_orders(name)    
        else:
            print("please try with different name")
           
    def orderAgain(self):
        name = input("tell me your name please: ")
        with open("data_stor.json") as f:
            data=json.load(f)
        if name in data:
            self.take_orders(name)
        else:
            print("you have not ordered before please select an option order instead of order again")

#class order_again(order):
    

        
