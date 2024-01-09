# a= int(input("enter a number = "))
# b= int(input("enter b number = "))
# c= int(input("enter c number = "))
# nitin = [a,b,c]
# print(nitin)

# def line():
#     print("---------------------------")
# def nitin (total):#total is variable
#     per = total /500*100
#     return per
# a = int(input("enter hindi number = "))
# b = int(input("enter english number = "))
# c = int(input("enter maths number = "))
# d = int(input("enter physics number = "))
# e = int(input("enter chemistry number = "))
# total = sum((a,b,c,d,e))
# x=  nitin(total)
# line()
# print(round(x,2))

# line()


# a=2
# def sqr():
#     b= a*a
#     return b
# x=sqr()
# print(x)

# while True:
#     a = int(input("enter any number = "))
#     if a<100:
#         print(a)
#     else:
#         break
# a=0
# while True:
#     if a<10:
#         a += 1
#         print(a)

# i= 1
# while i<6:
#     j=1
#     while j<=i:
#         print(j,end='  ')
#         j +=1
#     print()    
#     i +=1    

# i=1
# while i<=5:
#     j=5
#     while i<=j:
#         print(j ,end=" ")
#         j -= 1
   
#     print()
#     i +=1    

# i=1
# while i<5:
#     j = 1
#     while j<=i:
#         print(i,end='' )
#         j+=1
#     print()    
#     i+=1

# x=0
# for i in range (1,11):
#     x=i+x
# print(x)

# x = [12,75,150,180,145,525,50]
# for y in x:
#     if y<150 and y%5==0:
#        print(y)
   
# list1 = [12,89,9,9,5,9,55]
# x= reversed(list1)
# for y in x:
#     print(y, end=' ')

# for x in range(-10,0):
#     print(x)

# for x in range(1,51):
#     if x>0:
#         for i in range (2,x):
#             if (x%i)==0:
#                 break
#         else :
#             print(x,end=' ')


# n= int(input("enter any number = "))

# count = 0
# i = 1
# while i<=n:
#     if n%i==0:
#            count=count+1
#     i=i+1  
# if count==2:
#     print(n, "is prime number") 
# else:
#     print("not prime number")       

# num= 7895
# reverse_number= 0
# while num>0:
#     reminder = num%10
#     reverse_number=( reverse_number*10)+reminder
#     num = num//10
# print(reverse_number)

# i = "*"
# for x in range(5,0,-1):
#     b = x*i
#     print(b,end=" ")
#     print()

# a = int(input("enter any number = "))
# x=1
# y=0
# z=0
# while z<=a:
#     print(z)
#     y=x
#     x=z
#     z=x+y

# num = int(input("enter a number"))
# sum = 0
# for x in range (1,num+1):
   
#     sum= sum+x
# print(sum)

# start = int(input("enter start number = "))
# end = int(input("enter end number = "))
# even = 0
# odd = 0
# for x in range (start,end+1):
#     if x%2==0:
#         even = even + x
#     else :
#         odd = odd + x
# print(f" even number total is {even} and odd number total is {odd}")       
  

# start = int(input("enter start number = "))
# end = int(input("enter end number = "))
# for x in range (start,end+1):
#     if x%2==0:
#         print( x, end=" ") 
# for y in range (start,end+1):
#     if y%2!=0:
#         print(  y,end=" ") 

# x = int(input("enter number = "))
# i = 1
# count = 0
# while x>=i:
#     if x%i==0:
#         count = count+1
#     i =i+1
# if count==2:
#     print("prime number")
# else:
#     print("not prime number")
        
# start = int(input("enter first number = "))
# end = int(input("enter second number = "))
# for x in range (start+1,end+1):
#     for y in range (2,x+1):
#         if x%y==0:
#             break
#     if x==y:
#         print(x)    


# string1 = input("enter word = ")
# if (string1==string1[::-1]):
#     print("it is pallidrome word")
# else:
#     print("it is not a palidrome word")

# a = int(input("enter number = "))
# b = "*"
# for x in range(a+1,1,-1):
#     c = x*b
#     print(c)

# number = int(input("enter number = "))
# x= len(str(number))
# reminder = 0
# while number>0:
#     b = number%10
#     reminder = b**x+reminder
#     number = number//10
# print(reminder)
# if (reminder==number):
#     print("it is armstrong")
# else:
#     print("it is not armstrong")

# num= 7895
# reverse_number= 0
# while num>0:
#     reminder = num%10
#     reverse_number=( reverse_number*10)+reminder
#     num = num//10
# print(reverse_number)

# number = int(input("enter number: "))
# a = 0
# while number>0:
#     reminder = number%10
#     a = (a*10)+reminder
#     number=number//10




# num1 = int(input("enter first number = "))
# num2 = int(input("enter second number = "))
# if num1>num2:
#     for x in range (1,num1+1):
#         if num1%x==0 and num2%x==0:
#             pass
#             y = x
#     print(y)
# elif num1<num2:
#     for x in range (1,num2+1):
#         if num1%x==0 and num2%x==0:
#             pass
#             y = x
#     print(y)
# else:
#     print(num1)

# num = int(input("enter number = "))
# x = 1
# while x<num:
#     y = 1
#     while x>=y:
#         print(y ,end = " ")
        
#         y += 1
#     print()
#     x += 1

# x = 5
# for y in range(1,x+1):
#     for z in range(1,y+1):
#         print(y , end=" ")
#     print()   

# x = int(input("enter number = "))
# for y in range (1,x+1):
#     z= y*y
#     print( y,"*",y,"=" ,z)


# start = int(input("enter start = "))
# end = int(input("enter end = "))
# for x in range (start,end+1):
#     if (x%4==0 and x%100 !=00) or (x%400==0):
#          print(f"leap year is {x}")
        
# for x in range (1,101):
#     a= 0
#     for j in range (1,x+1):
#         if x%j==0:
#             a = a+1
#     if a==2:
#         print(x)

# x=  int(input("enter number = "))
# i=1
# count = 0
# while x>=i:
#     if x%i==0:
#         count +=1
#     i +=1
# if count ==2:
#     print("prime number")
# elif x==1:
#     print("it is nothing")
# else:
#     print("it is not prime number")


# number = int(input("enter number = "))
# empty = 0
# for x in range(1,number+1):
#      y = x**2
#      empty= empty+y
# print(empty)

# number = int(input("enter number = "))
# add = 0
# a= 1
# for x in range(1,number+1):
#      a= a*x
#      add=add+a
# print(add)

# a= "*"
# for x in range(1,5):
#     b=x*a
#     print(b)

# a = 10
# x =0
# y = 1
# z = 0
# while z<=a:
#     print(z,end=" ")
#     x =y
#     y =z
#     z = x+y

# list1 = []
# num = int(input("enter number : "))
# for num1 in range(1,num+1):
#     if num1 % 2 != 0:
#         list1.append(num1)    
# for x in list1:
#     c = 0
#     if x>19:
#         a = 1
#         b = 1
#         while x>=a:
#             b = x*b*a
#             x -= 1
        
#         c = c+b
# print(c)


# number = int(input("enter number : "))
# count = 0
# for num1 in range(2,number+1):
#     if number%num1 == 0:
#         count += 1
# if count == 1:
#     print(f"{number} is prime number")
# else:
#     print("not prime number")
 
# start = int(input("enter start number : "))
# end = int(input("enter last number : "))

# for num in range(start,end+1):
#     count = 0
#     for num1 in range(2,num+1):
#         if num%num1 == 0:
#             count += 1
#     if count == 1:
#         print(f"{num} is prime number")
#     else:
#         print(f"{num} is not prime number")


# n = int(input(""))
# if n%2 != 0 or 6 <= n >= 20:
#     print("weird")
# else:
#     print("not weird")

# n = (input(""))

# if len(n) == 16 and (n.startswith("4") or n.startswith("5") or n.startswith("6")) :
#     print("valid")
# else:
#     print("invalid")

# list1 = []
# num = int(input("enter number : "))
# for num1 in range(1,num+1):
#     if num1 % 2 != 0:
#         list1.append(num1)    
# for x in list1:
#     c = 0
#     if x>19:
#         a = 1
#         b = 1
#         while x>=a:
#             b = x*b*a
#             x -= 1
        
#         c = c+b
# print(c)

# a = 5
# b = 1
# c=1
# while a>b: 
#     c = a*c
#     a -= 1
# print(c)

# num = int(input("enter number : "))
# a = num
# reverse_number= 0
# while num>0:
#     reminder = num%10
#     reverse_number=( reverse_number*10)+reminder
#     num = num//10
# if reverse_number ==  a:
#     print(f"{a} is  palindrome number")
# else:
#     print(f"{a} is not palindrome number")