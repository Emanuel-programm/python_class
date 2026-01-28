from array import *

# arr=array('i',[1,2,3,4,5])

# newArr=array(arr.typecode,(a*a for a in arr))
# arr.reverse()
# print(newArr)

#captruring the inputs from the users and pass it to array
arr=array('i',[])
n=int(input("Enter the size of the array "))

for i in range(n):
    x=int(input("Enter next element "))
    arr.append(x)



val=int(input("Enter the value you want to search "))
c=0

for a in arr:
    if(a==val):
        print(c)
        break
    c+=1


print(arr.index(val))




