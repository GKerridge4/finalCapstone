# ===== VIEW ALL FUNCTION =====
'''
This function will iterate over the shoes list and
print the details of the shoes.
'''
# === IMPORTS ===

from tabulate import tabulate

# === THE FUNCTION ===

def view_all():
    display_shoes_list = []
    with open('inventory.txt', 'r') as inventory:
        for item in inventory.readlines():
            item = item.strip()
            item = item.split(',')
            display_shoes_list.append(item)
    
    return tabulate(display_shoes_list, headers="firstrow", tablefmt="pretty")