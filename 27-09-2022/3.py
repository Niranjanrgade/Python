# Person class and child Student class
# Create a class Person with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student which inherits from the Person class and which also has a section attribute.
# Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# Create a student object via an instantiation on the Student class and then test the displayStudent method

# Base/ super/ parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name of the person is {self.name}")
        print(f"Age of the person is {self.age}")


# Derived/ sub/ child class
class Student(Person):
    def __init__(self, name, age, section):
        Person.__init__(self, name, age)
        self.section = section

    def display_student(self):
        Person.display(self)
        print(f"Section of the student is {self.section}")


# Derived/ sub/ child class instance
student = Student('Jim', 'Ten', 'A')

# Method call of Base /super /parent class method using Derived/ sub/ child class instance
student.display_student()
