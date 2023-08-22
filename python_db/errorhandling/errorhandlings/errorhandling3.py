age=int(input("Enter the age: "))

if age<18:
    raise Exception("invalid age error")
else:
    print("valid")