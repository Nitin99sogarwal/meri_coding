#it is pre installed in python
#example 1
# import time 
# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

# import calendar
# cal = calendar.month(2021, 4)
# print(cal)

# import mere_module
# square = mere_module.sqr(5)
# print(square)

# import mere_module as m
# cube = m.cube(3)
# print(cube)


# a = "hello"
# hello = "a"
# print(eval(eval(a)))

# a = '09'
# b = max(map(ord,a))
# print(b)

#import random
#a = random.randint(1,10)
#print(a)


import random
def guess_number():
    return random.randint(1,100)
target_number = guess_number()
print(target_number)




