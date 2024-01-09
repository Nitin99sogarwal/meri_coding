                        #keys and valueee
# mobile={
# "brand": "nokia",
# "model": "ta-105",
# "year": 2003
# }
# print(mobile)

# mobile={
# "brand": "nokia",
# "model": "ta-105",
# "year": 2003
# }
# x= mobile["brand"]
# print(x)

# mobile={
# "brand": "nokia",
# "model": "ta-105",
# "year": 2003
# }
# mobile["year"] = 2019
# print(mobile)  

# mobile={
# "brand": "nokia",
# "model": "ta-105",
# "year": 2003
# }
# print(len(mobile))

# mobile={
# "brand": "nokia",
# "model": "ta-105",
# "year": 2003
# }
# mobile["color"]="black"
# print(mobile)

# mobile={
# "brand": "nokia",
# "model": "ta-105",
# "year": 2002
# }
# del mobile["year"]
# print(mobile)

# mobile={
# "brand": "nokia",
# "model": "ta-105",
# "year": 2003
# }
# mobile.clear()
# print(mobile)

# mobile={
# "brand": "nokia",
# "model": "ta-105",
# "year": 2003,
# "color":"blue"
# }
# phone = mobile.copy()
# print(phone)

# for x in mobile:
    # print(x)
    # print(mobile[x])

# for x in mobile.values():
#     print(x)

# for x in mobile.keys():
#     print(x)

# for x  in mobile.items():
#     print(x)



# mobile["color"] = "red"
# print(mobile)

# mobile.update({"color":"red"})
# print(mobile)

# mobile.pop("brand")
# print(mobile)

# mobile.popitem()
# print(mobile)

# mobile.clear()
# print(mobile)

# del mobile["model"]
# print(mobile)

# del mobile
# print(mobile)    #it's show error 

# mystudents = {
#     "student1":{
#         "name":"nitin","year":2007
#     },
#     "stydent2":{
#         "name":"nhr","year":2008
#     },
#     "student3":{
#         "name":"nb","year":2009
#     }
# }
# for x in mystudents:
#     print(x)

# print(mystudents["student1"]["name"])

# dict1 = {}
# entry = int(input("enter number : "))
# for x in range(entry):
#     keys = input(f"enter {x} key : ")
#     value = input(f"enter {x} value : ")
#     dict1.update({keys : value})
# print(dict1)


# mobile={
# "brand": "nokia",
# "model": "ta-105",
# "year": 2003
# }
# if "nokia" in mobile.values():
#     print("yes")
# else:
#     print("no")



# student =("nitin","nhr","nb")
# marks = (8)
# dict1 = dict.fromkeys(student,marks)
# print(dict1)


# mobile={
# "brand": "nokia",
# "model": "ta-105",
# "year": 2003
# }
# mobile["color"] = "black"
# mobile.update({"color":"red"})
# print(mobile)



# mobile={
# "brand": "nokia",
# "model": "ta-105",
# "year": 2003
# }
# for x in mobile.keys():
#     print(x)


# dict1 = {
#     "john" : 85,
#     "jane":80,
#     "bob":75,
#     "alice" : 95
# }
# dict1["bob"] = 80
# dict1.update({"bob":80})
# dict1.pop("jane")
# print(dict1.items())


# n = int(input("enter number : "))
# fruit = {
#     "apple":10 ,
#     "banana":5,
#     "orange":8,
#     "grape":3
# }
# fruit["apple"] += n
# print(fruit)
# if "banana" in fruit:
#     print("yes") 
# print(len(fruit))
# a = 0
# for x in fruit.values():
#     a = a+x
# print(a)

# fruit = {
#     "apple":10 ,
#     "banana":5,
#     "orange":8,
#     "grape":3
# }
# for x,y in fruit.items():
#     # print(x,y)
#     if y>4:
#         print(x)

# gradeJohn': 85, 'Jane': 92, 'Tom': 78, 'Emily': 95, 'Sam': 88}
# mydict ={}
# scores = 0
# for name,score in grades.items():
#     if score >= scores:
#         scores = score
#         names = name 
# mydict.update({names : scores})
# print(mydict)


# books = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5']
# authors = ['Author1', 'Author2', 'Author3', 'Author4', 'Author5']
# mydict = {}
# for x  in range(len(books)):
#     mydict[books[x]] = authors[x]

# print(mydict)


# grades = {'John': 85, 'Jane': 92, 'Tom': 78, 'Emily': 95, 'Sam': 88}
# highest_grade = -1
# for grade in grades.values():
#  if grade > highest_grade:
#     highest_grade = grade
# top_students = [student for student, grade in grades.items() if grade == 
# highest_grade]
# print(f"The highest grade is: {highest_grade}")
# print(f"The student(s) with the highest grade: {', '.join(top_students)}")

# employees = [
#  {'name': 'John', 'salary': 50000, 'department': 'Sales'},
#  {'name': 'Jane', 'salary': 60000, 'department': 'Sales'},
#  {'name': 'Tom', 'salary': 55000, 'department': 'Marketing'},
#  {'name': 'Emily', 'salary': 70000, 'department': 'Marketing'},
#  {'name': 'Sam', 'salary': 65000, 'department': 'HR'},
#  {'name': 'Alex', 'salary': 75000, 'department': 'HR'},
#  {'name': 'Sarah', 'salary': 60000, 'department': 'IT'},
#  {'name': 'Michael', 'salary': 80000, 'department': 'IT'},
#  {'name': 'Jessica', 'salary': 70000, 'department': 'Sales'}
# ]
# d= 0
# b = 0
# c = 0
# for i in range(len(employees)):
#     a = employees[i]
#     if a['department'] == 'Sales':
#         d = d + a['salary']
       
#     elif (a['department'] == 'IT'):
#         b = b + a['salary']
       
#     elif (a['department'] == 'Marketing'):
#         c = c + a['salary']
     
# print(d)
# print(b)
# print(c)

# students = ['John', 'Jane', 'Tom', 'Emily', 'Sam']
# grades = {'John': {'Math': 85, 'Science': 90, 'History': 75},
#  'Jane': {'Math': 92, 'Science': 88, 'History': 85},
#  'Tom': {'Math': 78, 'Science': 82, 'History': 80},
#  'Emily': {'Math': 95, 'Science': 88, 'History': 92},
#  'Sam': {'Math': 88, 'Science': 90, 'History': 85}}
# subjects = ['Math', 'Science', 'History']
# a = 0
# b  = 0
# c = 0
# for x in ((grades)):
#     d = (grades[x])
#     for y,z in d.items():
#         a = a+z
#     print(f"{x}:{a}")
