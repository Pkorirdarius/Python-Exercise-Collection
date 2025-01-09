#!/usr/bin/env python
# coding: utf-8

# # classes
# 

# In[7]:


# defining a class
class Cars:
    # Initializing a variable
    def __init__(self,name,manufacturer,model):
        # 
        self.name = name
        self.manufacturer = manufacturer
        self.model = model

    
    def car_info(self):
        print(f"car name {self.name} ,car manufacturer {self.manufacturer} and the model is {self.model}")


# In[8]:


my_car = Cars('BMW','Volkswagen','M5')


# In[10]:


my_car.car_info()


# In[6]:


def car_build(name,manufacturer,model):
        car_make = {
            "name":name,
            "maufacturer": manufacturer,
            "model":model
        }
        return car_make


# In[ ]:




