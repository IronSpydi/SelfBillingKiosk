import json
from tabulate import tabulate

class display:

    def display_menu(self):
            with open("menu.json") as f:
                obj = json.load(f)
            
            l = [[obj['Menu'][x] for x in obj['Menu']]]
            table = tabulate(l,headers=[y for y in obj['Menu']],tablefmt='orgtbl')
            print(table)

d1 = display()
