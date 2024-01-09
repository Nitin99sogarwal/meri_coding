name = str(input("enter your name = "))
password = int(input("enter your password = "))
if len(name)>=5 and len(password)>=8:
    print("login successful")
else:
    print("login unsuccessful")