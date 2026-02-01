# Single level inheritance
class A:
    def __init__(self):
        print("A init")
    def feauture1(self):
        print("Feauture 1 is working")
    def feature2(self):
        print("Feauture 2 is working")
class B(A):
    def __init__(self):
        super.__init__
        print("B init")
    def feauture3(self):
        print("Feauture 3 is working")
    def feature4(self):
        print("Feauture 4 is working")

a=A()
b=B()

## method resolution order(MRO) from always got to left first
# multlevel Inheritance
# class C:
#     def feauture4(self):
#         print("Feauture 5 is working")

# multiple inheritance
## Assume class B does not inherit from A
## class C(A,B):
##      print("multiple inheritance in action")


# a=A()
# a.feauture1()
# a.feature2()
# b=B()
# b.feauture1()
# b.feature2()
# b.feauture3()
# b.feature4()
