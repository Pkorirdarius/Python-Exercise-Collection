

# <p>Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in. Add an attribute, privileges, that stores a list of
# strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.</p>


# create a class known as user
class User :
    def __init__(self,first_name,last_name,age,contact_info,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.contact_info = contact_info
        self.gender = gender
        self.bonus_point = 1 
        self.login_attempts = 0
        # create a method that dives a description of the user
    def describe_user(self):
        print(f"Users first_name is: {self.first_name} and sir name is : {self.last_name}")
        print(f"user is : {self.age} years old and of gender : {self.gender}")
        print(f"User can be contacted via : {self.contact_info}")
        # method to greet the user
    def greet_user(self):
        print(f"Hello {self.first_name}, we are pleased to have you {self.last_name}\n")
        # method that shows the users bonus points
    def bonus(self):
        print(f"{self.first_name} has the following bonus points : {self.bonus_point}")
        # method that dynamically updates the users bonus points
    def update_bonus_point(self,points):
        self.bonus_point += points
        print(f"{self.first_name} has the following updated points : {self.bonus_point}")
        # method that increments the login attempts as per login
    def  increment_login_attempts(self):
        self.login_attempts += 1
        print(f"You have attempted to log in :{self.login_attempts} times")
        # method that resets the login attempts
    def  reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Please log into your account , you have logged in :{self.login_attempts} times")


class Admin(User):
    """
    Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 
    Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.
    """
    def __init__(self,first_name,last_name,age,contact_info,gender,admin_privileges):
        super().__init__(first_name,last_name,age,contact_info,gender)
        self.admin_privileges = admin_privileges
        
    


user_one = Admin('Darius','Pilakan',21,'0745303445',"male",["can add post","can delete post", "can ban user"])


user_one.show_privileges()


user_one.describe_user()


# <p>Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Admin. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges</p>


class Previleges(Admin):
    """
    create a 
    """
    def __init__(self,first_name,last_name,age,contact_info,gender,admin_privileges):
        super().__init__(first_name,last_name,age,contact_info,gender,admin_privileges)
    
    def show_privileges(self):
        print(f"The administrator  has the following privileges : ")
        for privilege in self.admin_privileges:
            print(f" :{privilege}")


admin_one = Previleges('Darius','Pilakan',21,'0745303445',"male",["can add post","can delete post", "can ban user"])


admin_one.show_privileges()




