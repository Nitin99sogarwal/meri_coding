#tuple

# x = (5,5,1,77,1,4,5,5,1,5,5,8,1,1,)


# y = x[::-1]
# print(y)
# print(x[::-1])

# x = ("nitin","nhr",[1,3,5,8],86,45)
# print(x[2])

# x = (50,2)
# print(x)

# x= (1,2,3,4)
# a,b,c,d=x
# print(a+b)
# print(b)
# print(c)
# print(d)
# print(x[0])
# print(x[1])
# print(x[3])
# print(x[2])

# n = int(input())
# if n%2!=0:
#     print("weird")
# elif n%2==0:
#     if 2<=n and n<=5 :
#         print("not weird")
#     elif  6<=n and n<=20:
#         print("weird")
#     elif n>20:
#         print("not weird")

# Krishna = [67,68,69]
# Arjun = [70,98,63]
# Malika = [52,56,60]
# a = 0
# for x in Malika:
#     a = x+a
# b = a/3
# print(f"{b:.2f}")

# n = int(input(""))
# a = 0
# for x in range(n+1):
#     if x%2==0 and x%3==0:
#         a += x
# print(a)

# sentence = input("enter sentense : ")
# b = ["a","e","i","o","u","A","E","I","O","U"]
# count = 0
# for x in sentence:
#     if x  in b:
#     # if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="U" or x=="O" :
        
#         count += 1
# print(count)

# element = int(input("enter number : "))
# list1 = []
# for x in range(1,element+1):
#     a = int(input(f"enter {x} number : "))
#     list1.append(a)
# print(f"your list is {list1}")
# list2 = []
# for y in list1:
#     if y%2!=0:
#         z = y*y
#         list2.append(z)
# print(f"your final list is {list2}")

# i = 0
# j = 1
# k = (i<10) and (j>10)
# print(int(k))

# number = int(input("enter number : "))
# i = 1
# while (i<=number):
#     print(i*str(number))
#     i += 1

# number = int(input("enter number : "))
# i = 1
# while (i<=number):
#     j = 1
#     while (j<i):
#         print(j, end=(' '))
#         j += 1
#     print(" ")
    # i += 1

# number = int(input("enter number : "))
# a = 0
# while number>0:
#     reminder = number % 10
#     a = a + reminder
#     number = number//10
# print(a)

# number = int(input("enter number: "))
# a= 0
# while number>0:
#     reminder = number%10
#     a = a+ (reminder*reminder*reminder)
#     number = number//10
# print(a)


# for i in range(5):
#     x = "* "
#     x = x*i
#     print(f"{x:^9}")


# x = "a "
# print(f"{x:^11}")


# for i in range(5):
#     x = "* "
#     x = x*(5-i)
#     print(f"{x:^11}")


# vehicle = input("enter vechile : ")
# time = int(input("enter time(in hours) : "))
# # amount = 0
# if vehicle == "bus" or "truck" :
#     amount = 100*time
#     print(f"your total amount is {amount}")
# elif vehicle =="car":
#     amount = 40 * time
#     print(f"your total amount is {amount}")
# elif vehicle=="motorcycle":
#     amount = 10*time
#     print(f"your total amount is {amount}")
# else:
#     print("parking is not allowed for this vehicle")


# first_string = "fear leads to anger anger leads to hatred"
# second_string = "leads"

# positions = [i for i in range(len(first_string)) if first_string.startswith(second_string, i)]
# print(positions)

# a= ["aditya","rajsweta","sujal","krishna"]
# age = [20,85,23,101]
# dict = dict(zip(a,age))
# print(dict)


# a = [51,62,15,3564,16]
# print(max(a))
# print(min(a))

# row = 0
# col = 0
# for row in range(0,2):
#     for col in range(0,3):
       
#         col += 1
#     row += 1

# a = 9
# b = 29
# c = 7
# d = 27
# print((a**29)+(7**27))

# n = 5
# for a in range(1,n):
#     print(ascii(a)*a)

# p = 10000
# r = 2
# n = 2
# ci = p*((1+(r/100))**n) - p
# print(f"{ci:.2f}")

# n = int(input(""))
# m = int(input(""))
# element = n*m
# matrix = []
# for i in range(1,element+1):
#     row = [int(x) for x in input("").split()]
#     matrix.append(row)
# print(matrix)


# print("\n".join([" ".join(map(str, row)) for row in matrix]))
# matrix = [list(map(int, input("").split())) for _ in range (1,element+1)]
# for row in matrix:
#     print(row)


# n = int(input("enter number : "))
# row = 1
# while row<=n:
#     col = 1
#     while col<=n:
#         print(" ",end=(" "))
#         col += 1
    
#     print(" ")
    
#     n -= 1

# for i in range(5):
#     a = "* "
#     x = i*a
#     print(f"{x:^10}")

# k = 1
# i = 1
# while i<=5:
#     b = 1
#     while b<=5-i:
#         print(" ",end="")
#         b += 1
#     j = 1
#     while j<=k:
#         print(i,end="")
#         j += 1
#     k += 2
#     print(" ")
#     i += 1

