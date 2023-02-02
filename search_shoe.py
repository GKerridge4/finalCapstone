# ===== SEARCH SHOE FUNCTION =====
'''
This function will search for a shoe from the list
using the shoe code and return this object so that it will be printed.
'''
# === IMPORTS ===

from read_shoes_data import shoe_list
from read_shoes_data import details_object
import Shoe_class

# === THE FUNCTION ===

def seach_shoe():
    matching_shoe_code = []

    user_code_choice = input("Would you like to see the list of shoe codes?\
        \nEnters 'Yes' or 'No': ")
    while True:
        if user_code_choice == 'yes':
            for details in details_object:    
                shoe_list.insert(0, details)
            for shoe in shoe_list:
                print(f"{Shoe_class.Shoe.get_product(shoe)}: {Shoe_class.Shoe.get_code(shoe)}")
            break

        elif user_code_choice == 'no':
            break

        else:
            user_code_choice = input("Please enter 'Yes' or 'No': ")

    user_code_choice = input("Please enter the shoe code you are searching for (or enter '0' to exit): ").upper()

    for item in shoe_list:
        if Shoe_class.Shoe.get_code(item) == user_code_choice:
            matching_shoe_code.append(item)
            break
    
    if len(matching_shoe_code) == 1:
        for shoe in matching_shoe_code:
            print("\nHere is your shoe:")
            print(shoe)
            matching_shoe_code.clear()

    elif len(matching_shoe_code) > 1:
        print('''
There seems to be more than one shoe with that code.
You should change the codes of these shoes.

Here are the shoes:''')
        for shoe in matching_shoe_code:
            print(shoe)
            matching_shoe_code.clear()
    
    elif len(matching_shoe_code) <= 0:
        print(f"\nThere are no shoes with the code: {user_code_choice}")