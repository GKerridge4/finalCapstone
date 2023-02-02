# ***===== INVENTORY CHECKER =====***
'''
This python file contains the imports and code 
to run the inventory menu options for a user.
All imported files are within this same folder.
'''
# ===== IMPORTS =====

import read_shoes_data
import capture_shoe
import view_all
import re_stock
import search_shoe
import value_per_item
import highest_qty

# ===== MAIN MENU =====

def main_menu():

    # read_shoes_data must be initiated to create the 
    # shoe_list, which every other section runs off.
    read_shoes_data.read_shoes_data()
    
    # A variable containing the menu so 
    # it is easily accessable for editing:
    menu = f'''
=== Welcome to your Inventory Checker ===

Please select one of the following options:

va - View All Shoe Data 
a - Add Shoe To Inventory
r - Restock Lowest Stock
f - Find Shoe with Code Number
t - Total Value For Each Item
h - Highest Quantity Stock 
e - Exit 
'''

    # A while loop that takes the users menu selection 
    # and triggers the corrosponding module.
    while True:
        print(menu)
        menu_choice = input("Please enter the menu option here: ").lower()

        if menu_choice == 'va':
            print(view_all.view_all())
        
        elif menu_choice == 'a':
            capture_shoe.capture_shoes()

        elif menu_choice == 'r':
            re_stock.re_stock()

        elif menu_choice == 'f':
            search_shoe.seach_shoe()

        elif menu_choice == 't':
            value_per_item.value_per_item()

        elif menu_choice == 'h':
            highest_qty.highest_qty()

        elif menu_choice == 'e':
            exit()
        
        else:
            menu_choice = print("That is not a menu item.")

# Triggers the main_menu function:
main_menu()