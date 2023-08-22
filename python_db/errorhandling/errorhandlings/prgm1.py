num=input("enter the number: ")

if type(num)==int:
    print(num**3)
else:
    raise Exception("operand must be an integer") 