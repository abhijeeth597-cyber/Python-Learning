#Topic 1: Objects & Classes
#This is a simple example of creating classes and objects in Python. We define two classes, `Student` and `Car`, and then create instances (objects) of each class. Finally, we print the objects to see their memory addresses.
class Student:
    pass
student1=Student()
print(student1)
class Car:
    pass
car1=Car()
print(car1)
#Topic 2: Attributes(Properties of an object )
#currently:
class Student:
    pass
#A student object exists,but it doesn't have any attributes to describe it. We can add attributes to the Student class to give it more meaning. For example, we can add a name and age attribute to the Student class.
class Student:
    pass
student1=Student()
student1.name="Abhijeeth"
student1.age=20
print(student1.name)
print(student1.age)
class Car:
    pass
    car1 = Car()
    car1.brand= "BMW"
    car1.color= "Black"
    print(car1.brand)
    print(car1.color)
   # 3. Constructor(__init__ method )
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Abhijeeth", 20)
print(student1.name)
print(student1.age)
#Topic 4: Methods (Functions inside a class)
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def start_engine(self):
        print(f"The {self.color} {self.brand} engine has started.")

car1 = Car("BMW","Black")
car1.start_engine()