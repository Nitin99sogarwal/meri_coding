month =int(input("enter your month = "))
card = str(input("enter card type = "))
if month <=12 and card == "visa" or card == "mastercard" :
    print("your card is valid")
else:
    print("your card is not valid")