# ===== VALUE PER ITEM FUNCTION =====
'''
This function will calculate the total 
value for each item in the inventory.
'''
# === IMPORTS ===

from read_shoes_data import shoe_list
from tabulate import tabulate
import Shoe_class

# === THE FUNCTION ===

def value_per_item():

    shoe_value_list = []

    for item in shoe_list:
        item_data = []
        item_value = int(Shoe_class.Shoe.get_cost(item)) * int(Shoe_class.Shoe.get_quantity(item))
        item_data.append(Shoe_class.Shoe.get_product(item))
        item_data.append(item_value)
        shoe_value_list.append(item_data)

    print("\n*** HERE ARE THE TOTALS FOR EACH PRODUCT ***")
    print(tabulate(shoe_value_list, headers=["Product Name:","Total Value (£):"], tablefmt='pretty'))