#!/usr/bin/env python
# coding: utf-8

# <p>Restaurant: Make a class called Restaurant. The _init_() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.</p>

# In[1]:


# Create a class that houses resturant functions
class Resturant :
    def __init__(self,restaurant_name,dish):
        self.restaurant_name = restaurant_name
        self.dish = dish
        self.number_served = 0
        # 
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.dish}")
        # 
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
        # 
    def set_number_served(self,dishes_served):
        self.number_served = dishes_served
        print(f"Number of customers served are : {self.number_served}")
        # 
    def  increment_number_served(self,customer_served):
        self.number_served += customer_served
        print(f"Number of customers served in a day : {self.number_served}")


# In[2]:


# Creating an instance
resturant_1 = Resturant('Kempinski','omena')
resturant_2 = Resturant('Arabian Place','platter')
resturant_3 = Resturant('Java House','vanilla latte')

resturant_1.describe_restaurant()
resturant_1.open_restaurant()   
resturant_2.describe_restaurant()
resturant_2.open_restaurant()  
resturant_3.describe_restaurant()
resturant_3.open_restaurant()  


# In[4]:


resturant_1.set_number_served(5)


# In[5]:


resturant_1.increment_number_served(3)


# In[ ]:




