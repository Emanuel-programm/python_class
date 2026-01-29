# def add_sub(a,b):
#     y=a+b
#     x=a-b
#     return y,b

# result_1,result_2=add_sub(6,3)
# print(result_1,result_2)

# def person(name,age): #formal Arguments/parameteres
#     print(name)
#     print(age)
# #passing keywords
# person(name="Mary",age=20)  #Actual parameters --keyword argumets
# person('Diana',28)


# pass a n expected number of arguments
# def sum(*b):
#     c=0
#     for i in b:
#         c=c+i
#     print(c)
# sum(20,40,90)


# passing n number of keywords
# def person(name,**data):
    
#     print(name)
#     for i,j in data.items():
#         print(i,j)

# person('Emanuel',age=23,city='mbeya',mob=8393939)


# Global and local variable
a=10

def something():
    global a
    a=7
    print(a)

something()

print(a)

