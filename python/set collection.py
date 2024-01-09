#a set is also a collection which is unordered. use curly brackets and unchangeable not repeat
# hardware={"monitor","printer","mouse","keyboard"}
# print(hardware)

# hardware={"monitor","printer","mouse","keyboard"}
# hardware.add("printer")
# print(hardware)

# hardware={"monitor","printer","mouse","keyboard"}
# # hardware.add("cpu")
# # hardware.remove("monitor")
# # print(hardware)
# set1 = set(("apple","banana","coconut"))
# set1.update(hardware)

# print(set1)

# a = 4
# b = 1
# c = 2
# d = 0
# while a>b:
#     j = 0
#     while j<b:
       
#         print(c,end=" ")
        
#         j += 1
   
#     print(" + ",end=(" "))
#     b  += 1
# print(d)

set1 = {"a","b","c"}
set2 = {1,2,3}
# set3 = set1.union(set2)

# print(set3)
# set3 = set1.intersection(set2)
set3 = set1.symmetric_difference(set2)
print(set3)