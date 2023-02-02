# ===== CAPTURE SHOE FUNCTION =====
'''
This function asks the user for shoe details which 
gets turned into a 'Shoe' object and added to 
the 'shoe_list' and 'inventory.txt' file.
'''
# === IMPORTS ===

from read_shoes_data import shoe_list
from read_shoes_data import details_object
import Shoe_class

# === THE FUNCTION ===

def capture_shoes():
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = input("Cost: ")
    quantity = input("Quantity: ")

    shoe_list.append(Shoe_class.Shoe(country,code,product,cost,quantity))
    
    print(shoe_list[-1])

    user_choice = input("Are these the details you want to add?\
        \n'Yes' or 'No': ").lower()
    while True:
        if user_choice == 'yes':
            with open('inventory.txt', 'w') as inventory:
                for details in details_object:
                    inventory.write(f"{repr(details)}\n")
                for shoe in shoe_list:
                    inventory.write(f"{repr(shoe)}\n")
            
            print("The inventory has been updated.")
            break
        
        elif user_choice == 'no':
            shoe_list.remove([-1])
            print("Details discarded. You will return to the menu.")
            break

        else:
            user_choice = input("Please enter 'Yes' or 'No': ")