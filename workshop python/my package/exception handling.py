# while true:
#     try:
#     x=int(input("please enter your number:"))
#     break
    # try:this block is used to enclose the code that may raise and exception.
    # except:this block catches and handles exceptions that occur in the try block.

# def error_handling():
#     try:
#         print(1/0)
#     except:
#             print("something bad happend")
# error_handling()

# a="hi"
# if not type(a) is int:
#   raise TypeError("only integers are allowed")


import random
def guess_number():
    target=random.randint(1,100)
    while True:
        try:
            user_guess=int(input("Guess the number: "))
            if user_guess<1 or user_guess>100:
                raise ValueError("number out of range(1-100)")
        except ValueError as e:
            print(f"error: {e}. please enter a valid number between 1 and 100.")
        else:
            if user_guess==target:
                print("congratulation! you guessed the correct number.")
                break
            elif user_guess<target:
                print("try a higher number.")
            else:
                print("try a lower number.")
if _name=="main_":
    guess_number()