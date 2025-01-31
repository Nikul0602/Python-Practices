#### OOPS CONCEPTS AND METHODS
### CLASS

# class Person:
#     name = "Nikul"
#     occupation = "Python Programmer"
#     Salary = 25000
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
#
# a = Person()
# b = Person()
#
# a.name = "Jay"
# a.occupation = "Cyber Security"
# a.Salary = 28000

# a.info()
# b.info()
# print(Person.name, a.name)

## CONSTRUCTOR
# class Person:
#     # def __init__(self):              #Default Constructor
#     #     print("hello")
#
#     def __init__(self, name, occ):              #Perametarized Constructor
#         self.name = name
#         self.occ  = occ
#
#
#     def info(self):
#         print(f"{self.name} is a {self.occ}.")
#
# a = Person("Nikul", "Programmer")
# b = Person("Amisha", "HR")
# # c = Person()
#
# a.info()
# b.info()


## DECORATORS

# def greet(fx):
#     def ma(*args, **kwargs):
#         print("Good Morning")
#         fx(*args, **kwargs)
#         print("Thanks for Using this Function.")
#     return ma
# #
# @greet
# def hello():
#     print("Nikul")
#
# # @greet
# def add(a, b):
#     print(f"The Sum of {a} + {b} is: ",a + b)
#
# greet(add)(6, 9)
# hello()
# greet(add(5))
# hello()


## GETTERS AND SETTERS

# class Myclass:
#     def __init__(self, n):
#         self._number = n
#
#     def show(self):
#         print(f"Number is {self._number}")
#
#     @property                   #GETTER
#     def arith_n (self):
#         return 6 * self._number - 2
#
#     @ arith_n.setter                   # GETTER
#     def arith_n(self, new_number):
#         self._number = new_number/2
#         # return 6 * self._number
#
#
# obj = Myclass(5)
# obj.arith_n = 25
# print(obj.arith_n)
# obj.show()


## INHERITANCE

# class Emp:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
    # def showdetails(self):
    #     print(f"The name of Employee {self.id} is : {self.name}")
#
#
# class Programmer(Emp):
#     def showlanguage(self):
#         print("The default language is Python")
#
#
# class Language(Programmer):
#
#     def lang(self):
#         print(f"{self.name} has mastery in Java Language.")
#
#
# e = Emp("Rohan", 51)
# e.showdetails()
#
# e = Programmer("Nikul", 41)
# e.showdetails()
#
# e = Language("Pritesh", 46)
# e.showdetails()
# e.lang()


## Access Modifiers
## PRIVATE, PUBLIC AND PROTECTED VARIABLES

## PRIVATE MODIFIER
# There is no such thing like private variables in python when we declare variable "__name" like this, python will
# simply use Name Mangling to make it difficult to access directly. but we can access it with method like this
# "_classname__variablename" here "_employee__name".

# class Employee:
#     def __init__(self):
#         self.__name = "Nikul"    ## It will use Name mangling     ## will store value of variable as private and
#         can't be accessed directly

    # def __init__(self):
    #     self._name = "Nikul"          ## will store value of variable as public and can be accessed directly

# a = Employee()

# print(a._name)      ## this can be accessed by directly
# print(a.__name)  ## Can't be Accessed Directly like this.

#Name Mangling method
# print(a._Employee__name)            ## can be Accessed Indirectly by using this method
# print(a.__dir__())


## STATIC METHOD

# class Math:
#     def __init__(self, num):
#         self.num = num
#
#     def add2num(self, n):
#         self.num = self.num + n
#
#     @staticmethod
#     def add(a, b):
#         return a + b


# result = Math.add(5, 15)
# print(result)
#
# a = Math(8)
# print(a.num)
# a.add2num(6)
# print(a.num)

# print(Math.add(5, 6))
# a = Math
# print(a.add(5, 6))


## INSTANCE VARIABLES VS CLASS VARIABLES
# class Emp:
#     comp_name = "Zynova"          ## Class Variable
#     noofEmp = 0
#     def __init__(self, name):
#         self.name = name          ## Instance Variable
#         self.raise_amt = 0.25
#         Emp.noofEmp += 1
#
#     def showdetails(self):
#         print(f"The name of Employee is {self.name} and will get raise of {self.raise_amt} amount in "
#               f"{self.noofEmp} sized {self.comp_name} "
#               f"Company.")
#
# # Emp.showdetails(emp)
# emp = Emp("Nikul")
# emp.comp_name = "Zynova Germany"            #Instance Variable
# # Emp.comp_name = "Picare Solutions"            # Class Variable
# emp.showdetails()
# emp1 = Emp("Jay")
# emp1.raise_amt = 0.3
# emp1.showdetails()
# print(Emp.comp_name)

## CLASS METHODS

# class Employee:
#     company = "Amazon"
#     def show(self):
#         print(f"The name is {self.name} and comapny is {self.company}")
#
#     @classmethod                ## will change the name of company in the class.
#     def changecompany(cls, newcomp):
#         cls.company = newcomp
#         # print(f"The company name is {cls.company}")
#
# emp = Employee()
# emp.name = "Nikul"
# emp.show()
# print(Employee.company)
# emp.changecompany("Google")
# emp.show()
# print(Employee.company)


## CLASS METHOD AS ALTERNATE CONSTRUCTORS

# class Employee:
#     def __init__(self, name, salary):
#         self.n = name
#         self.s = salary
#
#     @classmethod
#     def fromstr(cls, string):
#         return cls(string.split("-")[0],string.split("-")[1])             ##FIRST METHOD FOR USE CLASSMETHOD AS
#         # ALTERNATE CONSTRUCTOR
#
#     # @classmethod
#     # def fromstr(cls, string):
#     #     name, salary = string.split("-")
#     #     return cls(name, salary)             ##SECOND METHODFOR USE CLASSMETHOD AS ALTERNATE CONSTRUCTOR
#
# emp = Employee("Nikul", 20000)
# print(emp.n)
# print(emp.s)
#
# string = "Jay-15000"
# emp1 = Employee(string.split("-")[0], string.split("-")[1])
# print(emp1.n)
# print(emp1.s)
#
#
# ## ClassMethod as Alternative Constructor
# string = "Pritesh-25000"
# emp2 = Employee.fromstr(string)
# print(emp2.n)
# print(emp2.s)
#
# emp3 = Employee.fromstr("Aniket-\n18000")
# print(emp3.n, emp3.s)


## Different methods in python
# dir() method
# it shows all the available methods for variable

# a = (1,2,3)
# b = [1,2,3]
# c = {1, 2, 3}
#
#
# print(dir(a))
# print(dir(b))
# print(dir(c))
#
# print(a.__add__)


#__dict__ attribute
## it will convert the string into the Dictionary

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# person = Person("Nikul", 21)
# print(person.__dict__)
#
# print(help(Person))


## SUPER KEYWORD

# class Parent:
#     def parent(self):
#         print("This is Parent Class")
#
# class Child(Parent):
#     def parent(self):
#         print("Nikul")
#         super().parent()
#     def child(self):
#         print("This is Child Class")
#         super().parent()
#
#
# child_obj = Child()
# child_obj.child()
# child_obj.parent()


# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
# class Programmer(Employee):
#     def __init__(self, name, id, language):
#         self.lang = language
#         super().__init__(name, id)
#
#     def showdetals(self):
#         print(f"The name of Employee id {self.id} is {self.name} and has mastery in {self.lang} Programming Language")
#
# emp  = Employee("Nikul", 5)
# emp1 = Programmer("Jay", 6, "Python")
#
# emp1.showdetals()


## MAGIC/DUNDER METHOD

# class Emp:
#     def __init__(self, name):
#         self.name = name
#
#     def __len__(self):
#         i = 0
#         for i in self.name:
#             i = i + 1
#         return i
#
#     def __str__(self):
#         return f"The name of the Employee is {self.name} str"
#
#     def __repr__(self):
#         return f"The name of the Employee is ('{self.name}') repr"
#
#     def __call__(self):
#         print(f"Hello! Good Evening {self.name}")
# e = Emp("Jaykishanraj")
# # print(e.name)
# # print(len(e))
#
# print(str(e))
# print(repr(e))
# e()


## METHOD OVERRIDING

# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.x * self.y

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         super().__init__(radius, radius)

#     def area(self):
#         return 3.14 * super().area()

# rec = Circle(5)
# print(rec.area())
# a = Shape(8, 5)
# print(a.area())


## OPERATOR OVERLOADING

# class Vector:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __str__(self):
#         return f"{self.a}a + {self.b}b + {self.c}c"
#
#     def __add__(self, x):
#         return Vector(self.a + x.a, self.b + x.b, self.c + x.c)
#
#
# v1 = Vector(2, 3, -1)
# print(v1)
#
# v2 = Vector(8, 6, 9)
# print(v2)
#
# print(v1 + v2)
# print(type(v1 + v2))


## SINGLE INHERITANCE

# class Emp:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def showdetails(self):
#         print(f"The name of Employee {self.id} is : {self.name}")
# #
# #     def showlanguage(self):
# #         print("The default language is Java")
# #
# class Programmer(Emp):
#     def showlanguage(self):
#         print("The default language is Python")
#
# a = Programmer("Nikul", 50)
# a.showdetails()
# a.showlanguage()
#
# b = Emp("Nikul", 50)
# b.showdetails()
# b.showlanguage()


# class Animal:
#     def __init__(self,name, species):
#         self.name = name
#         self.species = species
#
#
#     def sound(self):
#         print("Sound made by Animal")
#
# class Cat(Animal):
#     def __init__(self, name, breed, action):
#         Animal.__init__(self, name, species = "Cat")
#         self.breed = breed
#         self.action = action
#
#     def sound(self):
#         print("Copycat")
#
#
#     def actions(self):
#         print("cat usually performs actions like")
#
# c = Cat("Cat", "Brown", "Jumping")
# c.sound()
# c.actions()
# a = Animal("Cat", "Brown")
# a.sound()


## MULTIPLE INHERITANCE

# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print(f"The name is {self.name}")
#
# class Dancer:
#     def __init__(self, dance):
#         self.dance = dance
#
#     def show(self):
#         print(f"The Dance is {self.dance}")
#
# class DancerEmployee(Dancer, Employee ):
#     def __init__(self, name, dance):
#         Employee.__init__(self, name)
#         Dancer.__init__(self, dance)
#
# a = DancerEmployee("Amisha", "Katahak")
# print(a.name)
# print(a.dance)
# a.show()
# print(DancerEmployee.mro())
# DancerEmployee.mro()


## MULTILEVEL INHERITANCE

# class Emp:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def show_details(self):
#         print(f"The Name of Employee is : {self.name}")
#         print(f"The ID of Employee is : {self.id}")
#
#
# class Programmer(Emp):
#     def __init__(self,  name, whattype):
#         Emp.__init__(self, name, id = "50")
#         self.type = whattype
#
#     def show_details(self):
#         Emp.show_details(self)
#         print(f"Type of Programmer is : {self.type}")
#
# class Language(Programmer):
#     def __init__(self, name, whichlang):
#         Programmer.__init__(self, name, whattype = "fullstack")
#         self.lang = whichlang
#
#     def show_details(self):
#         Programmer.show_details(self)
#         print(f"Language is : {self.lang}")
#
#
# e = Language("Pritesh", "Java-Script")
# e.show_details()
# # e.show_language()
# print(Language.mro())


## HYBRID AND HIERARCHICAL INHERITANCE

#HYBRID INHERITANCE

# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def show(self):
#         print(f"The Name of Employee is: {self.name}")
#         print(f"The ID of Employee {self.name} is: {self.id}")
#
# class Department(Employee):
#     def __init__(self, name, dept):
#         Employee.__init__(self, name, id = 21)
#         self.dept = dept
#
#     def show(self):
#         print(f"The department of Employee {self.name} is: {self.dept}")
#
# class Programmer(Employee):
#     def __init__(self, name, lang):
#         Employee.__init__(self, name, id=22)
#         self.lang = lang
#
#     def show(self):
#         print(f"The Employee {self.name} has Mastery in language {self.lang}")
#
# class Type(Department, Programmer):
#     def __init__(self, name, whattype):
#         Employee.__init__(self, name, id = 23)
#         self.type = whattype
#
#     def show(self):
#         print(f"The Employee {self.name} is a {self.type}")
#
#
# a = Type("Pritesh", "Back-End Developer")
# a.show()


## HIERARCHICAL INHERITANCE