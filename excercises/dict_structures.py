
# ## Dictionary{}

# * {key:vaue} pair


# sample dictionary
my_dict = {'name': 'Darius', 'Course': 'Data science'}

# check the type of object
type(my_dict)

# # properties

# * indexing
# Accessing item in a dictionary using the key
my_dict['name']

# Indexing using the .get method
my_dict.get('Course')

# # mutable
# modify the dict
my_dict['school'] = 'Gomycode'

# Display the items in the dictionary
my_dict


# * **key unqueness**

# Before adding a duplicated key
my_dict['location'] = 'Nairobi'
print(my_dict)
# Key must be unique
my_dict['location'] = 'Westlands'
print("After adding a diff value to the same key")
(my_dict)

# Accessing keys
my_dict.keys()
# Accessing values
my_dict.values()
# Accessing all of them
my_dict.items()


# # Problem statement
# <p>You are given a nested dictionary that contains information about students and their grades in different subjects. Your task is to write an algorithm that performs the following tasks:</p>
# 
# **instructions**
# * Find the average grade for each student.
# * Determine the highest grade in each subject.
# * List all students who have a grade above a specified threshold in a given subject.

# sample student grades
students = {
    "Alice": {"Math": 85, "Science": 92, "English": 88, "Social studies": 66},
    "Hilda": {"Math": 90, "Science": 85, "English": 95, "Social studies": 65},
    "Masibo": {"Math": 78, "Science": 80, "English": 82, "Social studies" : 72},
    "Darius": {"Math": 88, "Science": 90, "English": 84, "Social studies": 80}
}
# find the average grade for each student
averages = {student: sum(grades.values()) / len(grades) for student, grades in students.items()}
# Display the average of each student
print(averages)
# Determine the highest grade in each subject
subjects = students["Alice"].keys()
highest_grades = {subject: max(students[student][subject] for student in students) for subject in subjects}
# Display highest grades in each subject
print(highest_grades)
#List all students who have a grade above a specified threshold in a given subject
threshold = 85
subject = "Math"
students_above_threshold = [student for student in students if students[student][subject] > threshold]
print(f"Students above threshold are:{students_above_threshold}")


# # Question 2
# <p>Create a dictionary called "employee" that contains the keys "name", "age", "position" and "salary", with their corresponding values "John", 25, "Developer" and 3000 respectively.</p>
# 
# * Print the employee's name
# * Change the employee's position to "Manager"
# * Add a new key "email" with the value "john@example.com" to the employee dictionary


employee = {
    "name": "John",
    "age": 25,
    "position": "Developer",
    "Salary": 3000
}
# Display the name value from the dictionary
print(employee.get("name"))
# change position to manager
employee["position"] = "Manager"
# Add new key to email
employee["email"] = "john@example.com"
print(employee)




