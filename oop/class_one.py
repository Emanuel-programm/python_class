# class Computer:
    
#     ## think of constructor in other programming language like java (init__function works the same here)
#     ## At time we create a object of class init_function called itself
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram

#     def config(self):
#         print('config is',self.cpu,self.ram)

# comp1=Computer('15',16)
# comp2=Computer('Ryzen 3',8)


# class Student:
#     def __init__(self):
#         self.name='Diana'
#         self.age=22
#     def compare(self,std2):
#         if self.age==std2.age:
#             return True
#         else:
#             return False  


# std1=Student()
# std2=Student()
# std2.name='Wandola'
# std2.age=30

# print(std1.name)
# print(std2.name)

# # comapre two objects
# if std1.compare(std2):
#     print("They are equal")
# else:
#     print("They are different")



## They are two types of variables in oop --class variables and instances variables


## methods types in oop
## instance method --class method and static method

class Student:
    shool='Wandola university'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    ## instances method
    def average(self):
        return (self.m1+self.m2+self.m3)/3
    # class methods
    @classmethod
    def getSchoolName(cls):
        return cls.shool
    @staticmethod
    def info():
        print("This is a student class ")


# creating objects
std1=Student(20,39,30)
std2=Student(60,39,70)

print(std1.average())
print(std2.average())
print(Student.getSchoolName())
Student.info()

















# comp2.config()
# comp1.config()
# Computer.config(comp1)
# Computer.config(comp2)
# print(type(comp1))

# Computer.config()
# comp2.config(Computer)
# a='10'
# b=9
# ### Every thing in python is object
# print(type(a))
# print(type(b))

