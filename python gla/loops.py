# n = int(input("enter a positive integer (n) : "))
# sum_of_numbers = 0

# for i in range (1, n+1):
#     sum_of_numbers += i
# print(f"the sum of first {n} natural number is: {sum_of_numbers}")

# num = int(input("enter number = "))
# sum = 0
# for x in range (1,num+1):
#     sum = sum + x
# print(sum)        

# num = int(input("enter no. = "))
# sum = 0
# for x in range(0,num+1,2):
#     sum= sum+x
# print(sum)

# n = int(input("enter any no. = "))
# for i in range (0,1):
#     if n%2==0 :
#         print("even")
#     else:
#         print("odd")

# a = int(input("enter any number = "))
# for x in range(1,a+1,2) :
#     print(x  )
# for  y in range(0,a+1,2):
#     print(y)


# start = int(input("enter the start of the range = "))
# end = int(input("enter the end of the range = "))
#            #f is format string
# print(f" even number between {start} and {end}: ")
# for num in range (start,end+1):
#     if num%2==0:
#         print(num ,end=" ")

# n = int(input("enter any number."))
# c = 1
# for x in range (1,n+1):
#     c *=x
# print(f"the factorial {n} is  =",c)

# limit = 1000
# series = [0,1]

# while True:
#     next_number = series[-1] + series[-2]
#     if next_number> limit :
#         break
#     series += [next_number]
# print(series)   

 #fabonacci series
# n= int(input("enter any number = "))
# x = 1
# y = 0
# z = 0
# while(z<=n):
#     print(z ,end =" ")
#     y= x
#     x=z
#     z=x+y

 #multiplication table 
# n = int(input("enter any number = "))
# for x in range (1,11):
#     b = n*x
#     print(f" {n}*{x} = {b} ")
