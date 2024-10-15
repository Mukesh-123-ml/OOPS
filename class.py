from os import name
""" 
A class is a collection of attributes and methods
A class is a collection of object.
A class is user defined datatype.

Constructor : special method /dunder method /Automatically initialise when an object is instantiate from the class
initialising objects with attribute.

special attribute (__dict__). with this special attribute we can see an object contect.

***without constructor - we can not create an object***
when an object is created then Heap memory will be allocated to the object. Now the hexadecimal memory address will be allocatd to e1 object


***Built in class functions***

getattr(object_name,attribute_name)
setattr(object_name,attribute_name,new_value)
delattr(object_name,attribute_name)
hasattr(object_name,attribute_name)

***Built in class attribute***
__dict__
__name___
__doc__ : class doc string
__module__ : Module name in which class is defined.
__bases__ : list of base class

del std1.name
"""

class employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_info(self):
        print(f"Hello! my name is {self.name} and I'm {self.age} yrs old and I'm earning a good amount of {self.salary}")

e1 = employee("Mukesh",27,81000)

e1.get_info()
print(e1.name)
