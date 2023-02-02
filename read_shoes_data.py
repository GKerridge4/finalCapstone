# ===== READ SHOES DATA FUNCTION =====
'''
This function will open the file inventory.txt and read the 
data from this file, then create a shoes object with this data 
and append this object into the shoes list. One line in this 
file represents data to create one object of shoes.
'''
# === IMPORTS ===

import Shoe_class

# === THE FUNCTION ===

shoe_list = []
details_object = []

def read_shoes_data():
    while True:
        user_file = input('''
Please enter the name of the inventory file you
would like to use (or enter 'e' to exit): ''')
        if user_file == 'e':
            exit()
        else:
            try:
                with open(user_file, 'r') as inventory:
                    for item in inventory.readlines():
                        item = item.strip()
                        item = item.split(',')
                        if item[0] == 'County':
                            details_object.append(Shoe_class.Shoe(item[0],item[1],item[2],item[3],item[4]))
                            pass 
                        else:
                            shoe_object = Shoe_class.Shoe(item[0],item[1],item[2],item[3],item[4])
                            shoe_list.append(shoe_object)
                    return shoe_list and details_object
            
            except FileNotFoundError:
                print("Sorry, that file does not exist. Please try another file.")