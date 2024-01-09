# _init_ method is a special mehod used to initialize the object when it's created
#self is a reference to the current instance of a class
# class dog:
#     def __init__(self,name):
#         self.name = name
# dog1 = dog("buddy")
# print(dog1.name)
# classes in python are like blueprint for creating objects
# class car:
#     def __init__(self,make ,model):
#         self.make = make
#         self.model = model
# car1 = car("nitin","nhr")
# print(car1.make,car1.model)

#encapsulation is a concept that restricts access to certain

# class bankaccount:
#     def __init__(self,account_number,balance):
#         self.account_number = account_number
#         self.balance = balance
#     def get_balance(self):
#         return self._balance
# account = bankaccount("12345",1000)
# print(account.account_number)
# print(account.balance)

#inheritance allows you to create new classes that inherit properties and method from existing classes
# class animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         pass
# class dog(animal):
#     def speak(self):
#         return "woof"
# class cat(animal):
#     def speak(self):
#         return "meow"
# dog1 = dog("buddy")
# cat1 = cat("hahah")
# print(dog1.name,dog1.speak())
# print(cat1.name,cat1.speak())