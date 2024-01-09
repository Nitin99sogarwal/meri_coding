# while True:
#     rollno = [1,2,3]
#     grades = {'jane':{'subject1': 85, 'subject2': 90, 'subject3': 75,},
#      'sane': {'subject1': 92, 'subject2': 88, 'subject3': 85,},
#      'dane': {'subject1': 78, 'subject2': 82, 'subject3': 80,},
#     }
    

#     choice = int(input("enter choice : "))
#     if choice == 1:
      
#         name = input("enter student name : ")
#         rollno = int(input("enter roll number : "))
#         subject1 = int(input("enter subject1 no. : "))
#         subject2 = int(input("enter subject1 no. : "))
#         subject3 = int(input("enter subject1 no. : "))
#         grades['name'] = name
#         grades['subject1'] = subject1
#         grades['subject2'] = subject2
#         grades['subject3'] = subject3
#         print(grades)
#     elif choice == 2:
#     #    : n = int(input("enter number : "))
#         for x in grades:
#              d = grades[x]
#              print(d)
#     elif choice == 5:
#         break


# while True:
#     mydict = {
#         1:{'name':'nitin','age':20,'gender':'male','contactno.':1234},
#                 2:{'name':'raj','age':21,'gender':'male','contactno.':4234}
#     }
#     choice = int(input("enter choice : "))
#     if choice == 1 :
#         mydict2 ={ 3:{'name':'nhr','age':11,'gender':'male','contactno.':5234}}
#         dict1 = mydict2 + mydict
#         print(dict1)
#     elif choice == 3:
#         if 1 in mydict:
#             mydict[1]['name'] = "addi"
#             print(mydict)
#     elif choice == 4:
#         print(mydict)
#     elif choice == 5:
#         break



       
# student_database = {}

# while True:
#     print("\n1. Add new student")
#     print("2. Display student details")
#     print("3. Display average marks")
#     print("4. Display percentage of all students")
#     print("5. Display grade of a specific student")
#     print("6. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         name = input("Enter student name: ")
#         roll_number = input("Enter roll number: ")
#         marks_subject1 = float(input("Enter marks in Subject 1: "))
#         marks_subject2 = float(input("Enter marks in Subject 2: "))
#         marks_subject3 = float(input("Enter marks in Subject 3: "))

#         student_database[roll_number] = {
#             'name': name,
#             'marks': [marks_subject1, marks_subject2, marks_subject3]
#         }
        

#     elif choice == '2':
#         roll_number = input("Enter roll number of the student: ")
#         if roll_number in student_database:
#             student = student_database[roll_number]
#             print(f"Name: {student['name']}")
#             print(f"Roll Number: {roll_number}")
#             print(f"Marks in Subject 1: {student['marks'][0]}")
#             print(f"Marks in Subject 2: {student['marks'][1]}")
#             print(f"Marks in Subject 3: {student['marks'][2]}")
#         else:
#             print("Student not found in the database.")

#     elif choice == '3':
#         num_students = len(student_database)
#         if num_students == 0:
#             print("No students in the database.")
#         else:
#             total_subject1 = sum(student['marks'][0] for student in student_database.values())
#             total_subject2 = sum(student['marks'][1] for student in student_database.values())
#             total_subject3 = sum(student['marks'][2] for student in student_database.values())

#             average_subject1 = total_subject1 / num_students
#             average_subject2 = total_subject2 / num_students
#             average_subject3 = total_subject3 / num_students

#             print("Average Marks:")
#             print(f"Subject 1: {average_subject1}")
#             print(f"Subject 2: {average_subject2}")
#             print(f"Subject 3: {average_subject3}")

#     elif choice == '4':
#         if not student_database:
#             print("No students in the database.")
#         else:
#             print("Percentage of Students:")
#             for roll_number, student in student_database.items():
#                 total_marks = sum(student['marks'])
#                 percentage = (total_marks / (3 * 100)) * 100
#                 print(f"{student['name']} (Roll Number {roll_number}): {percentage:.1f}%")

#     elif choice == '5':
#         roll_number = input("Enter roll number of the student: ")
#         if roll_number in student_database:
#             student = student_database[roll_number]
#             total_marks = sum(student['marks'])
#             percentage = (total_marks / (3 * 100)) * 100

#             if percentage >= 90:
#                 grade = 'A'
#             elif 80 <= percentage < 90:
#                 grade = 'B'
#             elif 70 <= percentage < 80:
#                 grade = 'C'
#             elif 60 <= percentage < 70:
#                 grade = 'D'
#             else:
#                 grade = 'F'

#             print("Grade of Student:")
#             print(f"Name: {student['name']}")
#             print(f"Roll Number: {roll_number}")
#             print(f"Percentage: {percentage:.1f}%")
#             print(f"Grade: {grade}")
#         else:
#             print("Student not found in the database.")

#     elif choice == '6':
#         print("Exiting the program. Goodbye!")
#         break

#     else:
#         print("Invalid choice. Please enter a valid option.")
