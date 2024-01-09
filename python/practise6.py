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


# a = ["nitin","nhr"]
# b = "nitin"
# for x in range(len(a)):
#     if a[x]==b:
#         print(x)

# a = [x*x for x in range(1,11)]
# a = [x**2 for x in range(1,11)]
# print(a)

# a= "hello nitin"
# if (a.startswith('hello')):
#     print("trues")

# a = [1,2,3,6,4]
# (a.pop())
# print(a)


# a = False
# if a:
#     print("yes")


# num = 23
# is_prime =True
# for i in range (2,num):
#     if num%i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(f"{num} is prime number.")
# else:
#     print(f"{num} is not prime number")

# a = [4,54,545,5]
# a.sort(reverse = True)
# print(a)

# a = "Good Morning"
# result = ""
# for char in a:
#     if char.isalpha():
#         # result += char
# print(char)

# a = "123456"
# a = "nitinisnhr"
# print(a.isalpha())
# print(a.isdigit())
# print(a.isalnum())

# a = "nitin is nhr bholenath mahadev hanuman ram"
# a = "13 7 8 87 4815  5 48 78 5 481"
# b = a.split()
# list = []
# for i in range(len(b)):
#     c = b[i]
#     d = int(c)
#     list.append(d)
# for x in list:
#     print(x*x,end=" ")

# thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
# }
# for x in thisdict:
#  print(x)


# thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)


# thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
# }
# thisdict.popitem()
# print("My Data",thisdict)


# thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
# }
# del thisdict["model"]
# print(thisdict)


# thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
# }
# thisdict.update({"year":2000})
# print(thisdict)


# myStudents = {
#  "stud1" : {
#  "name" : "Sachin",
#  "year" : 2004
#  },
#  "stud2" : {
#  "name" : "Laxman",
#  "year" : 2007
#  },
#  "stud3" : {
#  "name" : "Ram",
#  "year" : 2011
#  }
# }
# print(myStudents)
# for x in myStudents:
#  print(x)
# print(myStudents["stud2"]["name"])
# for x, y in myStudents.items():
#  print(x,y)


# grades = {'John': 85, 'Jane': 92, 'Tom': 78, 'Emily': 95, 'Sam': 88}
# hg = 0
# for key,value in grades.items():
#     if value>hg:
#         hg = value
#         name = key
# print(f"{name}:{hg}")

# grades = {'John': 85, 'Jane': 92, 'Tom': 78, 'Emily': 95, 'Sam': 88}
# # Initializing a variable to hold the highest grade
# highest_grade = -1
# # Iterating through the grades to find the highest
# for grade in grades.values():
#     if grade > highest_grade:
#         highest_grade = grade
# # Finding the student(s) with the highest grade
# top_students = [student for student, grade in grades.items() if grade == 
# highest_grade]
# # Printing the highest grade and the student(s)
# print(f"The highest grade is: {highest_grade}")
# print(f"The student(s) with the highest grade: {', '.join(top_students)}")

# students = ['John', 'Jane', 'Tom', 'Emily', 'Sam']
# scores = [85, 92, 78, 95, 88]
# a = {}
# for i in range(len(students)):
#     # b = students[i]
#     # c = scores[i]
#     # a.update({b:c})
#     a[students[i]] = scores[i]
# print(a)
# total = 0
# for x,y in a.items():
#     total += y 
#     avg = total/len(a)
# print(avg)


# students = ['John', 'Jane', 'Tom', 'Emily', 'Sam']
# scores = [85, 92, 78, 95, 88]
# # Creating the dictionary manually
# score_dict = {}
# for i in range(len(students)):
#  score_dict[students[i]] = scores[i]
# # Calculating the total score and counting the number of scores
# total_score = 0
# num_scores = 0
# for score in scores:
#  total_score += score
#  num_scores += 1
# # Calculating the average score
# average_score = total_score / num_scores
# # Printing the average score
# print(f"The average score is: {average_score}")


# books = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5']
# authors = ['Author1', 'Author2', 'Author3', 'Author4', 'Author5']
# book_dict = {}
# for i in range(len(authors)):
#     book_dict[books[i]]=authors[i]
# print(book_dict)
# findbook = input("input book name: ")
# # for x,y in book_dict.items():
    
# #     if x == findbook:
# #         print(f"book is {x} and author is {y}")
# #     else:
# #         print("not found")
# if findbook in book_dict:
#     print("found")
# else:
#     print("not found")



# books = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5']
# authors = ['Author1', 'Author2', 'Author3', 'Author4', 'Author5']
# book_dict = {}
# for i in range(len(books)):
#  book_dict[books[i]] = authors[i]
# print(book_dict)
# # Asking the user for a book to search
# search_book = input("Enter the name of the book you want to search for: ")
# # Checking if the book is in the dictionary
# if search_book in book_dict:
#  author_of_specific_book = book_dict[search_book]
#  print(f"The author of {search_book} is: {author_of_specific_book}")
# else:
#  print(f"The book '{search_book}' is not found in the dictionary.")


# students = ['John', 'Jane', 'Tom', 'Emily', 'Sam']
# grades = {'John': {'Math': 85, 'Science': 90, 'History': 75},
# 'Jane': {'Math': 92, 'Science': 88, 'History': 85},
# 'Tom': {'Math': 78, 'Science': 82, 'History': 80},
# 'Emily': {'Math': 95, 'Science': 88, 'History': 92},
# 'Sam': {'Math': 88, 'Science': 90, 'History': 85}}
# subjects = ['Math', 'Science', 'History']
# # Report card for John:
# # Math: 85
# # Science: 90
# # History: 75
# # Average Grade: 83.33333333333333
# for x,y in grades.items():
#     if x == 'John':
#         # print(y)
#         sum = 0
#         for a,b in y.items():
#             print(f"{a}:{b}")
#             sum += b
#             avg = sum/len(y)
#         print(avg)
#     elif x == 'Jane':
#         print(y)

# a=int(input())
# b=int(input())
# print( a*(a>b)+b*(a<=b) )

# def LeapYear(year):
#     leap = (year%4==0 and (year%100!=00 or year%400==0))
#     return "leap year"*leap or "not a leap year"
# n = int(input())
# re = LeapYear (n)
# print(re)


# def LeapYear(year):
#     return ["Leap Year","Not a Leap Year"][n%4==0 and n%100!=0 or n%400==0]
# n = int(input())
# re = LeapYear (n)
# print(re)

# def ck_e_o(n):
#     return ["Even","Odd"][n%2!=0]
# n=int(input())
# re=ck_e_o(n)
# print(re)


# def ab_value(n):
#     return [-n,n][n>0]
# n=int(input())
# re=ab_value(n)
# print(re)   

# def nitin():
#     a = int(input())
#     b = int(input())
#     return[b,a][a>b]

# c = nitin()
# print(c)