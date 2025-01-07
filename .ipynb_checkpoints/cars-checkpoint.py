""" 8-14. Cars: Write a function that stores information about a car in a diction- ary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the func- tion with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True)
"""

# define a function that stores inforamation about a car in a dictionary
# **kwargs to allow for an arbitrary number of keyword arguments, which it then stores in the dictionary.
# the function takes in two paramenters a manufacturer and model name
def car_build(manufacturer,model_name, **kwargs):
    car_info ={
        'manufacturer': manufacturer,
        'model': model_name
    }
    # adds the extra parameters to the dictionary
    car_info.update(kwargs)
    return car_info
