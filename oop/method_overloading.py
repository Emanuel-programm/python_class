### Method overloading is not directly supported in python
# class Student:

#     def sum(self,a=None,b=None,c=None):
#         s=0
#         if a!=None and b!=None and c!=None:
#             return a+b+c
#         elif a!=None and b!=None:
#             return a+b
#         else:
#             return a

    

# std=Student()

# print(std.sum(8,7,7))
# print(std.sum(8,7))




class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

b1=B()
print(b1.show())