# a function is a block of code that performs a specific task
#type of function is 2
# 1 = built in function  .2 = user defined function
# 1 = built function

# a= 2
# b=3
# c=max((a,b))    #find greater value automatic
# print(c)

# a=5
# b=7
# c=sum((a,b))    # sum of no.
# print(c)

# user defined function
# a=4
# def nitin ():
#     b=a*a
#     print(b)

# nitin()



# def printline():
#     print("-------------------------------")
# def nhr (tot):
#     per = tot/500*100
#     return per
# phy =86
# che=57
# math= 80
# hindi=88
# english=78
# tot=sum((phy,che,math,hindi,english))
# result=nhr (tot)
# printline()
# print("your total no. is ",tot)
# printline()
# print("your percentage is =",round(result,2))  # round = round figure krna 
# printline()


                        #lambda function
# sqr = lambda a : a*a
# print(sqr(3)) 
# tot = lambda a,b:a+b
# print(tot(2,4))

# x=2
# y=3
# print(pow(x,y))


                                                    # squares = ["red","yellow"]
                                                    # for i,square in enumerate(squares):
                                                    #     print(i,square)
                                                        # print(i)


# def nowork():
#     pass
#     return None
# print(nowork())

# def  nitin(a):
#     for i,j in enumerate(a):
#         print(i,j)
# a=[52,6,2,6,266,7]
# nitin(a)

# def nitin(a):
#     a=a+"in"
#     print(a)
# a="nit"
# y=nitin(a)

# def nitin():
#     date =1405
#     print(date)
#     # return date
# nitin()
# def nitin(y):
#     rating = 9
#     print(rating)
#     return(rating+y)

# print(nitin(1))

# c1 = Circle(10,'red')
# class Circle(object):
#     def _init_(self,radius,color):
#         self.radius=radius;
#         self.color=color;


# class car:
#     max_speed = 120
#     def _init_(self,make,mode1,color,speed=0):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.speed = speed

#     def accelerate(self,acceleration):
#         if self.speed + acceleration <= car.max_speed:
#             self.speed += acceleration
#         else:
#             self.speed = car.max_speed
#     def get_speed(self):
#         return self.speed

# car1 = car("toyota","camry","blue")
# car2= car("honda","civic","red")

# car1.accelerate(30)
# car2.accelerate(20)

# print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h")
# print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h")


# def myfunction(food):
#     for x in food:
#         print(x)
# fruits = ["apple","banana","coconut"]
# myfunction(fruits)


# def nitin(b):
    # c = b*5
    # print(c)
    # return b*5
# print(nitin(5))
# nitin(5)

# def add(a,b):
#     c = a+b
#     print(c)
# def sub(a,b):
#     c = a-b
#     print(c)
# def mul(a,b):
#     c = a*b
#     print(c)
# def div(a,b):
#     if b == 0:
#         print("cannot divide")
#     else:
#          c = a/b
#          print(c)
# add(5,9)
# div(10,0)



# while True:
#     choice = int(input("enter choice : "))

#     if choice == 1:

#         def year(year):
#             if year%4 ==0 and year % 100!=0:
#                 print(f"{year} is the leap year ")
#             else :
#                 print(f"{year} is not leap year")
#         year(2024)
#     elif choice==2:
#         def factorail(a):
            
#             b = 1
#             c=1
#             while a>b: 
#                 c = a*c
#                 a -= 1
#             print(c)
#         factorail(5)
#     elif choice == 3:
#         def primenumber(n):
#             count =0
#             for num in range(1,n+1):
#                 if n % num ==0:
#                     count += 1
#             if count == 2:
#                 print(f"{n} is prime number")
#             else :
#                 print(f"{n} is not prime number")
#         primenumber(17)
#     elif choice == 4:
        
#         num = int(input("enter number : "))
#         a = num
        
#         def palindrome(num):
#             reverse_number= 0
#             while num>0:
#                 reminder = num%10
#                 reverse_number=( reverse_number*10)+reminder
#                 num = num//10
#             if reverse_number ==  a:
#                 print(f"{a} is  palindrome number")
#             else:
#                 print(f"{a} is not palindrome number")
#         palindrome(num)
#     else:
#         break

#immutable
# def nitin(x):
#     x += 19
#     print("inside the function : " , x)
# num = 5
# nitin(num)
# print("outside the function : ", num)


# def nitin(x):
#     x += "world"
#     print("inside the function : " , x)
# num = "hello "
# nitin(num)
# print("outside the function : ", num)

# def modify(t):
#     t += (4,5)
#     print("inside the function",t)
# coordinates = (1,2,3)
# modify(coordinates)
# print("outside the function",coordinates) 

# #mutable
# def list(lst):
#     lst.append(4)
#     lst[0]=99
#     print("inside the function",lst)
# number = [1,2,3]
# list(number)
# print("outside the function",number)

# def dict(d):
#     d['new_key'] = 'new_value'
#     print("inside the function",d)
# my_dict = {'key1':'value1','key2':'value2'}
# dict(my_dict)
# print("outside the function",my_dict)


# def dict(d):
#     d.add(4)
#     print("inside the function",d)
# my_dict = {'key1':'value1','key2':'value2'}
# my_set = {1,2,3}
# dict(my_set)
# print("outside the function",my_set)

# def list(lst):
#     a = 1
#     b = 0
#     for x in lst:
#         a = x**2
#         b = b+a
#     print(b)
# lst = [2,3,4]
# list(lst)

def dict(mydict):
    for x in range(1,2):
        key = input("enter key : ")
        value = int(input("enter value : "))
    mydict[key]=value
    print(mydict)
mydict = {'a':1,'b':2}
dict(mydict)