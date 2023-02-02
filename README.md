# finalCapstone

## Description:
This project is a Capstone project completed for my HyperionDev bootcamp.
In this project I am created code for a shoe shops inventory.
The user has a range of different options within the menu to select pre-written functions.
I will break down what each function does with it's corresponding .py file.

### Table of Contents:
 - #### [inventory.txt](#inventory.txt)
 - #### [inventory.py](#inventory.py)
 - #### [read_shoes_data.py](#read_shoes_data.py)
 - #### [capture_shoe.py](#capture_shoe.py)
 - #### [view_all.py](#view_all.py)
 - #### [re_stock.py](#re_stock.py)
 - #### [search_shoe.py](#search_shoe.py)
 - #### [value_per_item.py](#value_per_item.py)
 - #### [highest_qty.py](#highest_qty.py)
 
<a name="inventory.txt"></a>
## inventory.txt
This is a txt file that holds the contents of the inventory.
Every line in this file represents a different product(shoe),
with the following information in order:
###### County
Where the shoe is manfactured.
###### Code
The seriel no. of the shoe type.
###### Product
The name of the shoe type.
###### Cost
How much the shoe is worth per item.
###### Quantity
How many items of this shoe type is in stock.

<a name="inventory.py"></a>
## inventory.py
This file contains the main menu code and is what initiates the rest of the code.
Here are all of the files imported into inventory.py:
```
import read_shoes_data
import capture_shoe
import view_all
import re_stock
import search_shoe
import value_per_item
import highest_qty
```

<a name="read_shoes_data.py"></a>
## read_shoes_data.py
This function will open the file inventory.txt and read the 
data from this file, then create a shoes object with this data 
and append this object into the shoes list. One line in this 
file represents data to create one object of shoes.

<a name="capture_shoe.py"></a>
## capture_shoe.py
This function asks the user for shoe details which 
gets turned into a 'Shoe' object and added to 
the 'shoe_list' and 'inventory.txt' file.

<a name="view_all.py"></a>
## view_all.py
This function will iterate over the shoes list and
print the details of the shoes into a table using 
the tabulate module.

<a name="re_stock.py"></a>
## re_stock.py
This function will find the shoe object with the lowest quantity
and will ask the user how much they would like to re-stock.

<a name="search_shoe.py"></a>
## search_shoe.py
This function will search for a shoe from the list using the 
shoe code and return this object so that it will be printed.

<a name="value_per_item.py"></a>
## value_per_item.py
This function will calculate the total 
value for each item in the inventory.

<a name="highest_qty.py"></a>
## highest_qty.py
This function finds the shoes with the highest 
quantity and tells the user it is for sale.

