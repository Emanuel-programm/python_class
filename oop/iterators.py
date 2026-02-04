# num=[1,2,3,4,5]

# # for i in num:
# #     print(i)

# it=iter(num)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# print(next(it)) 

class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration


values=TopTen()
print(next(values))
for i in values:
    print(i)