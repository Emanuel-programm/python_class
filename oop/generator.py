def TopTen():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1


val=TopTen()
for i in val:
    print(i)