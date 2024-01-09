a = float(input("enter first no. = "))
b = float(input("enter second no. = "))
if a>0 and b>0:
    print("valid")
elif a<=b:
    print("invalid")
if a>b:
    print(a," is greater ", b,"is smallest" )
elif a<b:
    print(b," is greater ", a,"is smallest")

