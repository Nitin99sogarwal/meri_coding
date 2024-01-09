#a function is a reusable block of code that performs a specific task.

# def nitin():
#     x = 5  #local scope 
#     print(x)
# nitin()


# x = 22 #global scope
# def nhr():
   
#     y = 4
#     c = x+y
#     print(c)
# nhr()


#modify a global variable from within function

# x = 10
# def nb():
#     global x
#     x = 20      #non local scope

# print(x)


import random
def guess_number():
    return random.randint(1,100)
target_number = guess_number()
attempts = 0
while True:
    user_guess = int(input("guess the number : "))
    attempts += 1
    if user_guess == target_number:
        print(f"congrats! you gussed the number your attempts is {attempts}")
        break
    elif user_guess < target_number:
        print("guess high number")
    else:
        print("guess low number")




# score = 0
# def increase_score(points):
#     global score
#     score += points
# increase_score(10)
# print("score : ",score)


# def start_adventure():
#     hero_name = input("enter your hero's name : ")
#     print(f" welcome , {hero_name} you embark on an epic adventure")
# start_adventure()


# high_score = 0
# def update_high_score(score):
#     global high_score
#     if score > high_score:
#         high_score = score
# update_high_score(50)
# print("high_score",high_score)

#non local variable
# def game_round():
#     score = 0
#     def increase_score(points):
#         nonlocal score
#         score += points
#     increase_score(10)
#     return score
# round_score = game_round()
# print("round score",round_score)


# a = {"name":"players","score":100,"level":5}
# def display_player_info():
#     print(f"name:{a['name']}")  
#     print(f"score:{a['score']}")
#     print(f"level:{a['level']}")
# display_player_info()