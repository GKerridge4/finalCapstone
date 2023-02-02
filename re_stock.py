# ===== RE-STOCK FUNCTION =====
'''
This function will find the shoe object with the lowest quantity
and will ask the user how much they would like to re-stock.
'''
# === IMPORTS ===

from read_shoes_data import shoe_list
from read_shoes_data import details_object
import Shoe_class

# === THE FUNCTION ===

def re_stock():
    quantity_list = []

    for item in shoe_list:
        quantity_list.append(int(Shoe_class.Shoe.get_quantity(item)))
    smallest_num = min(quantity_list)
    for item in shoe_list:
        if int(Shoe_class.Shoe.get_quantity(item)) == smallest_num:
            lowest_stocked_item = item
    
    user_choice = input(f'''
The item with the lowest stock is:
{lowest_stocked_item}
Would you like it restocked?
'Yes' or 'No': ''').lower()

    while True:
        if user_choice == 'yes':
            increase_quantity = int(input("How many would you like to add? "))
            lowest_stocked_item.quantity = smallest_num + increase_quantity
            print("This is the item now:")
            print(lowest_stocked_item, '\n')
            print(f'''
Would you like to confirm: '{Shoe_class.Shoe.get_quantity(lowest_stocked_item)}'
as the new product quantity for: '{Shoe_class.Shoe.get_product(lowest_stocked_item)}'.''')
            user_conformation = input("'Yes' or 'No': ").lower()
            
            while True:
                if user_conformation == 'yes':
                    for item in shoe_list:
                        if Shoe_class.Shoe.get_product(item)\
                            == Shoe_class.Shoe.get_product(lowest_stocked_item):
                            shoe_list.remove(item)
                            shoe_list.append(lowest_stocked_item)
                            for details in details_object:
                                shoe_list.insert(0, details)
                    
                    with open('inventory.txt', 'w') as inventory:
                        for shoe in shoe_list:
                            inventory.write(f"{repr(shoe)}\n")
                    
                    print("The inventory has been updated.")
                    break

                elif user_conformation == 'no':
                    print("No changes have been made to the inventory.")
                    break

                else:
                    user_conformation = input("Please enter 'Yes' or 'No': ").lower()

            break

        
        elif user_choice == 'no':
            break
        
        else:
            user_choice = input("Please enter 'Yes' or 'No': ")