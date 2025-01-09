
# # Python introduction

# ## Python Syntax

# print statement
print("Hello world!")


# In[ ]:


# printing multiple print statements
print ("School : GO MY CODE")
print ("Course : Data science")
print ("python")


# In[ ]:


# printing on a new line using \n
print ("Hello \ndata science")


# In[ ]:


# print numeric value
print ( 6 )
print ( 5.6)
print( "pi" )
print (3.142)


# In[ ]:


print(8 + 5) 
2 + 4


# In[ ]:


input("What is your name?")


# In[ ]:


input("What is your name? ")
input("What is your age? ")


# In[ ]:


print (input("What is your name? "))
print(input("What is your age? "))


# # Greeting Program

# ## Objective: Create a friendly program that greets the user by name.
# 
# **Instructions:**
# 
# * Ask for Name: Use input to ask the user for their name.
# * Personalized Greeting: Print a welcoming message that includes their name.
# * Additional Engagement: Ask them how they are feeling today and print a message based on their answer.

# In[ ]:


# taking the input (names ) of users
name = input("Enter your name? ")
# Displaying the name and a welcome message
print("Welcome " + name )
# Additional engement by asking how they feel and how was their day
status = input("How are you feeling today? ")
if (status == "fine"):
    print("great.")
else:
    print("Not everyday is awesome.")


# # Simple Recipe
# 
# ## Objective: Encourage creativity by suggesting a recipe based on user inputs.
# 
# **Instructions:**
# 
# * Ingredient Input: Ask the user for two ingredients they have at home.
# * Recipe Suggestion: Print a creative dish idea using those ingredients.
# * Further Exploration: Encourage them to think of how they would prepare it.

# In[4]:


# Input 2 ingredients at home
print ("State 2 ingredients for a recommended recipe")
recipe1 = input("What is the first ingredient? ")
recipe2 = input("What is the second ingredient? ")
# Print a creative dish idea based on the two ingedients
if (recipe1 == recipe2):
    print("We will grill " + recipe1 + "Or we'll stew " + recipe2)
else :
    print ("The ingredients can be used to make fish curry " + recipe1 + " we dice it up and " + recipe2 + " season on the fish" )
# encourage them to think of how it can be prepared
print("How best can it be prepared?")


# In[ ]:




