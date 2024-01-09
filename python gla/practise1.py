               # list 
# mylist = [9,8,5]
# mylist.append(12)
# print(mylist)

# list = ["aditya","nhr","nitin"]
# list1 = ["adi","nhr","nitin"]
# list.extend(list1)
# print(list)

# newlist = ["apple","banana"]
# final_list = newlist.copy()
# print(final_list)

# list = ["a","b","c"]
# list1 = [1,2,3,4]
# list2 = list + list1
# print(list2)

# z = ["a","b","c"]
# z.pop()
# print(z)

# x = [1,2,8,53,8,5,6]
# print(x[3])
# print(x[6])
# print(x[0:5])
# x[2]=10
# print(x)

# x = input("enter input = ")
# z = input("enter second input = ")
# y = ["nitin","nhr"]
# y.append(z)
# y.append(x)
# print(y)



# x = [5,6,8,3]
# print(sum(x))
# y = x[0]+x[1]+x[2]+x[3]
# y = 0
# for i in x:
#      y =y+i
    
# print(y)

# mylist = []
# x = int(input("enter the items"))
# for i in range(x):
#     y = input(f"enter item{i+1}:")
#     mylist.append(y)
# print(mylist)
 
# list = [8,9,74,23,45]
# list.sort()
# print(list)
# for x in list:
#      y = x
# print(y)

# mylist = [12,56,8,6,452]
# max_element = mylist[0]
# for num in mylist:
#     if num>max_element:
#         max_element = num
# print(f"largest element in the list is: {max_element}")

# x = [1,1,2,3,2,1,8]
# count = 0
# num = 1
# for a in x:
#     if a==num:
#        count += 1
# print(count)

# nitin=[]
# a = int(input("enter items = "))
# for x in range(a):
#     y = input(f"enter element {x} = ")
#     nitin.append(y)
# print(nitin)

# nitin = [2,8,2,55,15,5]
# max = nitin[0]
# for a in nitin:
#     if max<=a:
#         max = a
# print(max)

# a = [1,2,3,4,1,29,1,15]
# count = 0
# b = 2
# for x in a:
#     if x==b:
#         count += 1
# print(count)

# a = ["nitin","ram","hanuman"]
# b = []
# for x in a:
#     if "a" in x:
#         b.append(x)
# print(b)

# a = ["nitin","ram","hanuman"]
# # b = a.copy()
# b = a
# print(b)

# a = "hello"
# count = {}
# for char in a:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1
# for char,count in count.items():
#     print(f"{char}-{count}")
# print(char,count)

# a = "hello"
# # char = "l"
# count = a.count("o")
# print(count)

# a = "hello"
# unique = []
# for char in a:
#     if char not in unique:
#         unique.append(char)
# print(unique)

# square = [x**2 for x in range(5)]
# print(square)

# even_number = [x for x in range(10) if x%2==0]
# print(even_number)

# result = ['pass' if score >= 60 else 'fail' for score in[75,59,4,69,78,125,74]]
# print(result)

# names = ["nitin" , "ram" ,"hanuman"]
# name_length = [len(name) for name in names]
# print(name_length) 

# a  = [1,2,3,6]
# b = []
 # for x in a:
# b = a
# print(b)

# a = [1,2,8,89,5,65]
# b = [2,8,6,4,1,9,3]
# intersection = []
# for num in a:
#     if num in b and num not in interection:
#         intersection.append(num)
# print(intersection)   

# a = [78,45,95,7,8,2,9,3,33,59]
# count = 0
# count1 = 0
# for x in a:
#     if x%2 == 0:
#         count += 1

#     else:
#         count1 += 1
# print(count)
# print(count1)

# a = [87,78,15,955,74,75]
# largest = a[0]
# for x in a:-
#      if x>largest:
#         largest = x
# print(largest)


# a = [78,9,5,26,85,52,856]
# a.sort()
# b = a
# b.reverse()
# i = int(input("enter n largest number = "))
# # for x in b:
# print(b[i-1])


# number = int(input("enter items: "))
# nitin = []
# for items in range(number):
#     item = (input(f"enter {items} : "))
#     nitin.append(item)
# a = nitin
# print(a)
# frequency = (input("enter frequency number = "))
# for x in range(a):
#     if "frequency"==x:
#         count += 1
# print(count)

# number = int(input("enter items: "))
# nitin = []
# for items in range(number):
#     item = (input(f"enter {items} : "))
#     nitin.append(item)
# a = nitin


# a = int(input("enter number = "))
# b = []
# for x in range(1,a+1):
#     if x%5==0:
#         b.append([x,"-",x+2])
# print(b)   



# number = int(input("enter number: "))
# a = 0
# while number>0:
#     reminder = number%10
#     a = a+reminder
#     number=number//10
# print(a)

# a=[x for x in range(50) if x%2==0] 
# print(a) 

# a=["nitin","hanuman","ram","mahadev"]
# name_length=[len(name) for name in a]
# print(name_length)

# items=int(input("enter item number: "))
# list=[]
# for x in range(1,items+1):
#     y=input( f"{x} items: ")
#     # list.append(y)
#     z=y
# print(z)   
# # print(list)
while True:
    print(" 1.addition \n 2. subtract \n 3. multiplication \n 4. division \n 5. display operation \n 6. quit")
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    operator=input("enter operator: ")

    if operator=="1":
        c=a+b
        print(c)
        # list=[]
        # list.append(c)
    elif operator=="2":
        c=a-b
        print(c)
        # list=[]
        # list.append(c)
    elif operator=="3":
        c=a*b
        print(c)
       
    elif operator=="4":
        c=a/b
        print(c)
        
    elif operator=="5":
        list=[]
        list.append(c)
        print(list)
        
    elif operator=="6":
        break

