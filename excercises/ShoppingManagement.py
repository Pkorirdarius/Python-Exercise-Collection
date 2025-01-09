#!/usr/bin/env python
# coding: utf-8

# # program for users to manage their shopping list

# **Statement:**
# 
# * Create a list to store the shopping items
# * Use a while loop to create a menu of options for the user to add, remove, or  view items from the list
# * Use a for loop to iterate through the list of items and display them to the user
# * Use the range() function to limit the number of items that can be added to the list
# * Use the list, tuple, set, and dictionary data structures to store and manipulate the shopping items
# **Instructions:**
# 
# <p>Create a list named 'shopping_list' to store the items.
# Use a while loop to create a menu of options for the user to add, remove, or view items from the list.
# Use the input() function to prompt the user to make a selection from the menu.
# Use an if-elif-else block to determine the user's selection and perform the corresponding action.
# If the user selects 'add', use the input() function to prompt the user to enter an item to add to the list. Use the range() function to limit the number of items that can be added to the list.
# If the user selects 'remove', use the input() function to prompt the user to enter an item to remove from the list.
# If the user selects 'view', use a for loop to iterate through the list of items and display them to the user.
# Use the list, tuple, set, and dictionary data structures to store and manipulate the shopping items.</p>

# In[1]:


# initialize a list
shopping_list = []
# initializing the upperlimit of values to add to the list
max_items = 5
# use a while loop to iterate through the options
while True:
    options = input("Choose what option you want to implemant to your shopping list : \n1.Add to list \n2.Remove item from list \n3.View item in list \n4.Exit \n")
    if options == '1':
        if len(shopping_list) < max_items:
            items = input("Enter the item you want to add to the list :").split(", ")
            # add item to the shopping_list and dictionary
            shopping_list.extend(items[:max_items - len(shopping_list)])
            print(f"'{items}' has been added to the list.")
        else:
            print("The shopping list is full. Please remove an item before adding another.")
    elif options == '2':
        # selecting the item to be removed from the list
        removing_item = input("Enter the item you want to remove from the list : ").split(", ")
        # for loop to iterate through the list checking for the item to be removed
        for item in removing_item:
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{removing_item} has been removed from the list")
            else:
                print(f"{removing_item} not found in the list")
    elif options == '3' :
        if shopping_list:
            print("\nCurrent shopping list:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("The shopping list is empty.")
    elif options == '4' :
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


# In[ ]:




