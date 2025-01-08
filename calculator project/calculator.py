
# # a calculator program
# performing basic calculations and intermediate like log,exponential and square root


# import relevant library for complex mathematical calculations
import math
# define the Calculator class
class Calculator:
    def __init__(self):
    # create a dictionary
        self.operations = {
        '+': self.add,
        '-': self.subtract,
        '*': self.multiply,
        '/': self.divide,
    }
    # four  mathematical functions:'add', 'subtract', 'multiply', and 'divide'
    def add(self,x, y):
        return x + y
    
    def subtract(self,x, y):
        return x - y
    
    def multiply(self,x, y):
        return x * y
    
    def divide(self,x, y):
        if y != 0:
            return x / y
        else:
            return "not divisible by zero"
    # method that adds new calculations
    def add_operation(self,symbol,function):
        self.operations[symbol] = function
        
    # initializing main function calculator
    def calculate(self, num1, operation, num2):
        # condition that chakes for invalid mathematical sign
        if operation not in self.operations:
            return (f"Invalid operation '{operation}'. Please choose a valid operation.")
            # checks if both numbers entered are actual numbers int/float and for square root if it's unary
        if not isinstance(num1, (int, float)):
            return "The first input must be a number."
            # If the operation is unary like 'sqrt' does not use num2 ,num2 has been made optional
        if operation == 'sqrt':
            return self.operations[operation](num1)
            # if the operation uses num2 
        if not isinstance(num2, (int, float)):
            return("The second input must be a number.")
        return self.operations[operation](num1, num2)

 # Advanced mathematical functions
def exponentiate(x, y):
    return x ** y

def square_root(x, _=None):  # Single argument, ignore the second one
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(x)

def logarithm(x, base=10):
    if x <= 0:
        raise ValueError("Logarithm is undefined for non-positive numbers.")
    return math.log(x, base)
   # Main program 
if __name__ == "__main__":
    calc = Calculator()
    # Add advanced mathemathematical operations
    calc.add_operation('^', exponentiate)
    calc.add_operation('sqrt', square_root)
    calc.add_operation('log', logarithm)

    print("Welcome to Calculator 2.0")
    print("Available operations:")
    print(", ".join(calc.operations.keys()))

    while True:
        try:
            # User input for numbers and operation
            num1 = float(input("\nEnter the first number: "))
            operation = input("Enter the operation: ")
            
            # If the operation is unary (e.g: square root), only one number is needed
            if operation == 'sqrt':
                result = calc.calculate(num1, operation, None)
            else:
                num2 = float(input("Enter the second number: "))
                result = calc.calculate(num1, operation, num2)

            print(f"Result: {result}")

            # Ask if the user wants to continue
            cont = input("Would you like to perform another calculation? (yes/no): ").lower()
            if cont != 'yes':
                print("Thank you for using Calculator 2.0. Goodbye!")
                break
        # error handling operation 
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
# will further be expanded for complex fuctinality like quadratic function