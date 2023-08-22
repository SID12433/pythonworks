lst=[10,20,30,40]

l=int(input("enter the location: "))
try:
    print(lst[l])
except Exception as e:
    print(e.args)
finally:
    print("db commit")
    print("file read")
