# ===== HIGHEST QUANTITY CODE =====
'''
This function finds the shoes with the highest 
quantity and tells the user it is for sale.
'''
# === IMPORTS ===

from read_shoes_data import shoe_list
import Shoe_class

# === THE FUNCTION ===

def highest_qty():
    quantity_list = []
    for item in shoe_list:
        quantity_list.append(int(Shoe_class.Shoe.get_quantity(item)))
    largest_num = max(quantity_list)
    for shoe in shoe_list:
        if int(Shoe_class.Shoe.get_quantity(shoe)) == largest_num:
            most_stocked_item = shoe

    print(f'''
The item with the most stock is:
{most_stocked_item}.

This item is 
*** FOR SALE *** ''')