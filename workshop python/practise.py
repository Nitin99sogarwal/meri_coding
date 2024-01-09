# a = {0:10,1:20}
# a[2]=30
# print(a)
# a = {1:10,2:20}
# b = {3:30,4:40}
# c = {5:50,6:60}
# a.update(b)
# a.update(c)
# print(a)
# print(a,b,c)

# a = {"data":100,"data1":-54,"data2":247}


# b= 0
# for value in a.values():
#     # print(key)
#     b = b+value
# print(b)

# a = {num:num**2 for num in range(1,16)}
# print(a)

# d = {"x":10,"y":20,"z":30}
# for key,value in d.items():
#     print(f"{key}:{value}")

# a = {
#     'red':"ff0000",
#     'green':"00800",'black':'00000','white':'ffff'
# }
# b = list(a)
# b.sort()
# print(b)
# for key in sorted(a):
#     print("%s:%s"%(key,a[key]))

# a = {1:10,2:20,3:30,4:40,5:50,6:60,1:10}
# b = int(input("enter number : "))
# # for x,y in a.items():
# #     print(x,y)
# if b in a:
#     print("exist")

# else:
#     print("does not exist")

# a = {"name":5,"age":8,"one":52}
# b= a.values()
# # print(b)
# print(max(b))
# print(min(b))

# a  = [8,2,3,-1,7]
# b= 1
# for x in a:
#     b= b*x
# print(b)

# a = [1,2,3,4,5,6,7,8,9]
# b = []
# for x in a:
#     if x%2==0:
#         b.append(x)
# print(b)


# # non local variable
# def game_round():
#     score = 0
#     def increase_score(points):
#         nonlocal score
#         score += points
#     increase_score(10)
#     return score
# round_score = game_round()
# print("round score",round_score)


# class car :
#     def __init__(self,make,model):
#         self.make = make 
#         self.model = model
# car1 = car ("toyota","camry")
# car2 = car ("honda","civics")
# a = [("toyota","camry"),("honda","civics")]
# b = dict(a)
# print(b)

