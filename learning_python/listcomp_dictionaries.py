import math

# list_of_lists = [[1,2,3,4], [5,6,7,8], ['a','b','c','d']]
# for list in list_of_lists:
#     for item in list:
#         print(item)

# a = [x*x - 1 for x in range(9)]
# print("a: ", a)
# b = [(x,x*x) for x in range(9)]
# print("b: ", b)
# c = [a[x]+b[x][0] for x in range(9) if x % 2 == 0]
# print("c: ", c)
# d = [' alpha ','beta\n\n ', ' \n gamma \n']
# e = [x.strip() for x in d]
# print("e: ", e)

# d = {"Tom" : 500, "Stuart" : 1000, "Bob" : 55, "Dave" : 21274}
# print(len(d))
#
# del d["Bob"]
# print(d)
#
# d["Phil"] = 100
# print(d)
#
# print("Dave" in d, "Peter" in d, 500 in d)
# # True False False
#
# for key, value in d.items():
#     print(key, value)
#
# # Only prints the keys, the previous allows you to access the values too.
# for i in d:
#     print(i)

# s = 'structure'
# dic = {}
# for i in range(len(s)):
#     dic[s[i]] = i
# # print(dic)
# # {'s':1, 't':2 etc...}
#
# listA = list(range(11, 100, 11))
# # [11,22,33,44,55,66,77,88,99]
# listB = list(range(1, 10))
# # [1,2,3,4,5,6,7,8,9]
# listC = [(listA[i], listB[i]) for i in range(9)]
# # [(11,1), (22,2), etc...]
# dicB = dict(listC)
# print(dicB)
# {11:1, 22:2 etc...}
#
# for a, b in dicB.items():
#     print(a, b, end=" # " )
# print()
# # 11 1 # 22 2 # etc...

# adict = {}
# with open("./towns.csv", "r") as afile:
#     file_text = afile.read().strip()
#     alist = file_text.split("\n")
#     for item in alist:
#         ungrouped = item.split(",")
#         adict[ungrouped[0]] = ungrouped[1]
#     print(adict)
#
# width = max([len(x) for x in adict])
# for town, pop in adict.items():
#     print("{0:&>{2}} : {1:<}".format(town, pop, width))

# for k in dicB:
#     if (k+11) in dicB:
#         dicB[k] += dicB[(k+11)]
# print(dicB)
# # {11:3 etc...}
#
# info = "Jack: Ben, 3,Cardiff; Jill: Sara, five, Bath"
# records=info.split(';')
# adic={}
# for item in records:
#     str1, str2 = item.split(':')
#     alist = str2.split(',')
#     adic[str1.strip()]=tuple([x.strip() for x in alist])
# print(adic)
# # {"Jack": (Ben, 3, Cardiff) etc...}
#
# with open ('test.txt', 'w') as f:
#     sts = "Python for Data Analysis.".split()
#     for st in sts:
#         f.write(st+"\n")
#
# with open ('test.txt', 'r') as f:
#     st=f.read()
#     print(st)
# # Prints each word on a separate new line

# ids = ('a', 'b', 'c', 'd', 'e', 'f')
# mywords = ('Tim', 'Sara', 'flew', 'space', 'pair', 'slippers')
#
# def to_dict(list_a, list_b):
#     list = [(list_a[i], list_b[i]) for i in range(len(list_a))]
#     adict = dict(list)
#     return adict
#
# print(to_dict(ids, mywords))
