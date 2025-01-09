
# # pizza ordering system
# 

# **instructions**
# ``` Small Pizza: $15 ``` 
# 
# ``` Medium Pizza: $20 ``` 
# 
# ``` Large Pizza: $25 ``` 
# 
# <p>If they want to add pepperoni :</p>
# 
# ``` Pepperoni for Small Pizza: +$2 ``` 
# 
# ``` Pepperoni for Medium or Large Pizza: +$3 ```
# 
# <p>If they want cheese :</p>
# 
#  ``` Extra cheese for any size pizza: + $1 ```

# welcoming message to the user
print("Welcome to Python Pizza Deliveries")
total_cost = 0

# Cost for each pizza
small_pizza = 15
medium_pizza = 20
large_pizza = 25

# Cost of pepperoni on pizza
small_pepperoni = 2
medium_large_pepperoni = 3

# Cost of extra cheese
extra_cheese_cost = 1

# Prompt the user to select the size of pizza 
while True:
    # Takes input from the user use list to check for the options selected
    size = input("What pizza size do you want? \n Large = L, Medium = M, Small = S \n").upper()
    if size in ['L', 'M', 'S']:
        break
        # display invalid option 
    print("Invalid option. Please enter 'L' for Large, 'M' for Medium, or 'S' for Small.")

# Ask the user if they want pepperoni or not 
while True:
    add_pepperoni = input("Do you want pepperoni? (Yes = Y, No = N): ").upper()
    # list containing valid options
    if add_pepperoni in ['Y', 'N']:
        break
        # display invalid option ask the user to re enter value via loop
    print("Invalid option. Please enter 'Y' for Yes or 'N' for No.")

# Ask the user if they want extra cheese with validation
while True:
    extra_cheese = input("Do you want extra cheese on it? (Yes = Y, No = N): ").upper()
    # list containing valid options
    if extra_cheese in ['Y', 'N']:
        break
        # display invalid option ask the user to re enter value via loop
    print("Invalid option. Please enter 'Y' for Yes or 'N' for No.")

# Calculate the total cost based on the selections
if size == 'L':
    total_cost = large_pizza
    if add_pepperoni == 'Y':
        total_cost += medium_large_pepperoni
    if extra_cheese == 'Y':
        total_cost += extra_cheese_cost
elif size == 'M':
    total_cost = medium_pizza
    if add_pepperoni == 'Y':
        total_cost += medium_large_pepperoni
    if extra_cheese == 'Y':
        total_cost += extra_cheese_cost
elif size == 'S':
    total_cost = small_pizza
    if add_pepperoni == 'Y':
        total_cost += small_pepperoni
    if extra_cheese == 'Y':
        total_cost += extra_cheese_cost

print(f"Your final bill is: ${total_cost}")

