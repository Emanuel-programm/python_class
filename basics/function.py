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
# a=10
# print(id(a))

# def something():

    # global a
    # a=7
    # x=globals()['a']
    # print(id(x))
#     globals()['a']=25
#     a=7
#     print('inside fun',a)

# something()

# print('outside fun',a)

#passing list to the function

# def count(list):
#     even=0
#     odd=0
#     for i in list:
#         if i%2==0:
#             even+=even
#         else:
#             odd+=odd
#     return even,odd

# list=[1,2,3,4,5,6,7,8,9]

# even,odd=count(list)
# print('Even: {} and odd: {}'.format(even,odd))


# Fibonacci series
# def fib(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)
# x=int(input("Enter range of the series "))
# fib(x)



## Factorial 
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i

#     return f




# x=int(input("Enter the number you want to compute factorial "))
# result=fact(x)
# print(result)



## Recursion
## nothing but a function calling itself
# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# def great():
#     print("Hello")
#     great()
# great()

## factorial using recursion
# def fact(b):
#     if(b==0):
#         return 1
#     return b*fact(b-1)    
# x=5
# result=fact(x)
# print(result)

# Lambda function --anonymous function --function without a name
# f=lambda a:a*a
# print(f(4))

## lambda function inside others 
# def is_even(n):
#     if(n%2==0):
#         return n


# num=[1,2,3,4,5,67,8,9]

# even=list(filter(lambda n: n%2==0,num))

# doubles=list(map(lambda n: n*n,even))

# print(doubles)
# from functools import reduce

# sum=reduce(lambda a,b:a+b,doubles)
# print(sum)

##################################################################################################
#decorators

# def div(a,b):
#     # if(a<b):
#     #     a,b=b,a
#     print(a/b)

#     # decorators
# def smartFunct(funct):
#     def inner(a,b):
#         if(a<b):
#             a,b=b,a
#         return funct(a,b)
#     return inner

# div1=smartFunct(div)
# div1(2,4)


