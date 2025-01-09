
# # classes


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

def car_build(name,manufacturer,model):
        car_make = {
            "name": name,
            "manufacturer": manufacturer,
            "model": model
        }
        return car_make
# calling the classes

my_car = Cars('BMW','Volkswagen','M5')
my_car.car_info()



