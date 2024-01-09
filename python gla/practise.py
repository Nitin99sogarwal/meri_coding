# a= int(input("enter = "))
# for x in range(1,a+1):
#      a="*"
#      print(a*x)

# a= int(input("enter = "))
# for x in range(a+1,0,-1):
#      a="*"
#      print(a*x)


# for year in range(2000,2021):
#     if (year %4==0 ):
#         print("leap year")
#     else:
#         print("it is not leap year")
    
# a = "hello world"
# # b = a.lower()
# # print(b)
# c= a.upper()
# c = a.isupper()
# c= a.isspace()
# print(c)
# c = a.replace("hi", "nitin")
# print(c)

# start = int(input(" enter start number = "))
# end = int(input("enter last number = "))
# for x in range(start,end+1):
#     if (x%5==0):
#         print(x-1 + x-2)

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
        
text =("python is amazing")
# print(text[0:4])
# print(text[6])
# print(text[:4])
# print(text[-1])
# print (text[9:2])
# print(text[slice(5)])
# print(text[slice(5,8)])
# print(text[slice(-8,-1)])
# print(text[:])
# print(text[0:4:2])
print(text[::-1])
print(text[-8::-1])
print(text[1::2])
print(text[::3])




# # text ="   python  programing   "
# # trimmed_text = text.strip()
# # print(trimmed_text)
# # print(text[0:5])

# text ="nitin"
# check = (text.isalpha())
# check = (text.isdigit())
# print(check)

# a = input("enter text = ")
# num = 0
# char = 0
# for x in a:
#     if x.isalpha():
#         char += 1
#     elif x.isdigit():
#         num += 1
#     else:
#         continue
# print("no of character is :", char)    
# print("no of integer is :", num)            

# while True:
#     x = input("enter password = ")

#     if len(x) >= 12  and x.isalpha() and x.isdigit() and x.isupper() and x.islower():

#         print("valid")
        
#     else:
#         print("please try again and make strong password")
#         continue
# while True:
#     x= "fgv1256"
#     if len(x)>2:
#         print("valid")
#         break
#     else:
#         print("invalid")


# while True:
#      x = input("enter password = ")

#      if len(x) >= 12 :
#         continue
#         if 
        
        
#      else:
#          print("please try again and make strong password")
#          continue


# while True:
#     password = input("enter password = ")
#     if len(password)<12:
#         print("password must be at least 12 character long")
#         continue
#     else:
        # has_uppercase = False
        # has_lowercase = False
        # has_digit = False
        # has_special = False 
        # has_space = False
        # for char in password:
        #     if char.isalpha():
        #         if char.isupper():
        #             has_isupper = True
        #         elif char.islower():
        #             has_lowercase = True
        #     elif char.isdigit():
        #         has_digit = True
        #     elif char.isspace():
        #         has_space = True
        #     else:
        #         has_special = True
        # if has_uppercase and has_lowercase and has_special and has_digit:
        #     print("this is strong password")
        #     break
        # else:
        #     print("this is not  a strong password .please try again")

# text = ("hello , world")
# x= text.split(',')
# print(x)

# text = ["hello ", "world"]
# print(",".join(text))

# text = ("hello world,hello nitin")
# count = text.count("hello")
# print(count)

# name = "nitin"
# age = 20
# x = ("my name is {} and my age is {}").format(name,age)
# print(x)

# text = "NITINnhr123"
# print(text.isalnum())

# text1 = "1234678"
# print(text1.isnumeric())

# text2 = "Hello World"
# print(text2.istitle())


# text3 = "hello nitin how are you"
# print(text3.title())

# nitin = ["nitin","hanuman","ram","nhr","nitin"]
# nhr = [1,2,5,9,"nitin",9]
# tuple = (1,2,5,"nitin")
# nitin.extend(nhr)
# nitin.append("mahadev")
# nitin.insert(0,'ram')
# print(nitin)
# nitin.extend(tuple)
# print(nitin)
# nhr.remove(5)
# nhr.remove(9)
# nhr.pop(3)            #specific value remove
# del nhr[0]            #specific value remove
# nhr.clear()
# print(nhr)

# nitin = ["nitin","hanuman","ram","nhr","n"]
# for x in nitin:
#         print(x)

# for x in range(len(nitin)):
#         print(nitin[x])

# i = 0
# while i<(len(nitin)):
#         print(nitin[i])
#         i += 1

# [print(x) for x in nitin]

# fruits = ["banana","apple","kiwi","mango","cherry"]
# newlist = []
# for x in fruits:
#         if "a" in x:
#                 newlist.append(x)
# print(newlist)

# start = int(input("enter start number : "))
# end = int(input("enter end no.: "))
# for x in range(start,end+1):
#         if x % 2 !=0 and x%3!=0:
#                 print(f"{x}:")
#         elif x % 2 ==0 and x%3!=0:
#                 print(f"{x}: good")
#         elif x % 3 ==0 and x%2 !=0:
#                 print(f"{x}: student")
#         elif  x % 2 ==0 and x%3==0:
#                 print(f"{x}: good student")
        
dict = {"pencil":100,"eraser":200}
a=0
for x in dict.values():
        a = a+x
print(f"total sum is {a} ")

