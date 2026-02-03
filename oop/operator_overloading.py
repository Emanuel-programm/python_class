## Alot of thing are predifened -- syntatic sugar
# a=10
# b=6

# c=a+b
# print(c)

# print(int.__add__(a,b))

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    ## operator overloading
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2

        s3=Student(m1,m2)

        return s3
    def __gt__(self,other):
        r1=self.m1+other.m1
        r2=self.m2+other.m2

        # s3=Student(r1,r2)
        # return s3
        if(r1>r2):
            return True
        else:
            return False
    
    
    

s1=Student(90,78)
s2=Student(80,90)

s3=s1+s2
print(s3.m2)

if(s1>s2):
    print('S1 wins')
else:
    print('S2 wins')