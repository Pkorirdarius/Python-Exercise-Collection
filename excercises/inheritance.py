#!/usr/bin/env python
# coding: utf-8

# # inheritance

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


# create an instance
resturant_one = Resturant('Kempinski Villa Rosa','spanish omlette')


# In[3]:


class Supplier(Resturant) :
    """
    A class that restocks food ingredients in resturants 
    """
    # defining a function that allows inheritance of fromparent class
    def __init__(self,restaurant_name,dish,supplier_name,supplier_main_product,contact_no):
        super().__init__(restaurant_name,dish)
        self.supplier_name = supplier_name
        self.supplier_main_product = supplier_main_product
        self.contact_no = contact_no
        
        # define a function that describes the omain commondity of the suppliers and to which resturant
    def supplies_descriptions(self):
        print(f"Restock for : {self.restaurant_name} provided by : {self.supplier_name}")
        print(f"Main products to restock is: {self.supplier_main_product}")
        print(f"For more inquires reach out to us via: {self.contact_no}")
        
    def describe_restaurant(self):
        print(f"The most popular Resturants in the area is : {self.restaurant_name}")


# In[4]:


# create
supplier_one = Supplier('Kempinski Villa Rosa','spanish omlette','Pilakan Enterprise','ChickenEggs','0720065343')


# In[5]:


supplier_one.supplies_descriptions()


# In[6]:


supplier_one.set_number_served(2)


# In[7]:


supplier_one.increment_number_served(4)


# In[8]:


supplier_one.describe_restaurant()


# In[9]:


resturant_one.describe_restaurant()


# <p>Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote in
# Either version of the class
# will work; just pick the one you like better. Add an attribute called flavors that
# stores a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.</p>

# In[28]:


class IceCreamStand(Resturant):
    """
    Class Icecream stand inherits from Resturant 
    """
    def __init__(self,restaurant_name,dish,flavors):
        super().__init__(restaurant_name,dish)
        self.flavors = flavors

    def different_flavors(self):
        print(f"The following flavors are offered at {self.restaurant_name} ice cream stand : ")
        for flavor in self.flavors:
            print(f" :{flavor}")


# In[29]:


scoop_one = IceCreamStand('Juniors ','Icecream',['Vanilla','stawberry','chocolate'])


# In[30]:


scoop_one.different_flavors()


# In[ ]:




