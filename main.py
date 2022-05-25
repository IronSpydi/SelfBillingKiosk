from display_rates import display
from order import order
from generate_bill import bill_generate
print("\nSelect operation.")
print("DM   : Display Menu")
print("ODR  : Order")
print("OA   : Order Again")
print("GB   : Generate Bill")
print("Q    : Quit an application")
with open('data_stor.json','w') as file:
    file.truncate(0)
    file.write('{}')

obj_display = display()
obj_order = order()
obj_bill = bill_generate()

while True:
    # take input from the user
    choice = input("Enter choice(DM/ODR/OA/GB/Q): ")

    # check if choice is one of the four options
    if choice in ('DM', 'ODR','OA', 'GB','Q'):
        if choice == 'DM':
            obj_display.display_menu()

        elif choice == 'ODR':
            obj_order.order()
            
        elif choice == 'OA':
            obj_order.orderAgain()
        elif choice == 'GB':
            obj_bill.bill_generate()
            
        else:
            if choice =='Q':
                break
    else:
        print("invalid Input")