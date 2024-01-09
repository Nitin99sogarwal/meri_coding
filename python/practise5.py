# n = 10
# a = [0,1]
# for i in range(2,n):
#     a.append(a[i-1]+a[i-2])
# print(a)
# for x in a:
#     print(x,end=" ")


# a = 370
# b = a
# x = 0
# while a>0:
#     rem = a%10
#     x = x+(rem**3)
#     a = a//10
# if b == x:
#     print("armstrong number")
# else :
#     print("not armstrong number")


# a = "ram is good boy ram ram"
# b = a.split()
# c = 0
# for x in b:
#     if x =="ram":
#         c += 1
# print(c)


# def nitin():
#     number = int(input("enter number : "))
#     list = [0,1]
#     for i in range(2,number):
#         list.append(list[i-2]+list[i-1])
#     for x in list:
#         if x%2 == 0:
#             print(f"{x} - it's even.")
#         else:
#             count = 0
#             for y in range(1,x+1):
#                 if x%y==0:
#                     count += 1
#             if count == 1:
#                 print(f"{x} - it's odd.")
#             elif count == 2:
#                 print(f"{x} - it's odd and prime.")
# nitin()












# # n = 45
# list = []
# for i in range(2,51):
#     count = 0
#     for x in range(2,i+1):
#         if i%x==0:
#             count += 1
#     if count==1:
#         list.append(i)
#         # print(f"{i} prime number")
#     # else:
#         # print(f"{i} not a prime number")
# print(list)


# a = input("enter any string : ")
# a  = 8
# b = [0,1]
# for x in range(2,a+1):
#     b.append(b[x-1]+b[x-2])
# print(b)

# a = "154"
# if a == a[::-1]:
#     print("palindrome number")
# else:
#     print("it is not palindrome")



# a = 371
# d= (len(str(a)))
# c = a
# rever = 0
# while a>0:
#     rem = a%10
#     rever += (rem**d)
#     a = a//10 
# print(rever)
# if rever == c:
#     print("it is armstrong")
# else:
#     print("it is not armstrong")


# a = open('nitin.txt','r')
# b = a.readline()
# print(b)

# a = open("nitin1.txt","x")
# print(a)

# a = open("nitin1.txt","w")
# b = a.write("i love nhr")
# print(b)


# a = open("nitin1.txt","a")
# b = a.write("\nnitin is nhr")