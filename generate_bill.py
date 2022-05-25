import json


class bill_generate:
    
    def bill_generate(self):
        name = input("Enter naame:")
        with open("data_stor.json") as f:
            data = json.load(f)
        if name in data:
            print(data[name])
            bill=list()
            for x in data[name]:
                print(x)
                with open("menu.json") as fn:
                    data_menu = json.load(fn)
                amount = float(data_menu['Menu'][x][0])*float(data[name][x]) + float(data[name][x])*float(data_menu['Menu'][x][0])*float(data_menu['Menu'][x][1]/100)
                print(amount)
                bill.append(amount)
            total=sum(bill)
            print(f"{name} your bill is Rs {total} with GST.\nThanks for visiting.")
        else:
            print("You have not ordered yet ! \nplease make order first and then select this option\nThank you :)")