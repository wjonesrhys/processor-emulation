# Prints in descending order numbers from n decreasing in 5's and an X at the end if n<0
# def reFun_A(n):
#     if n<0:
#         return "X"
#     return str(n)+"-"+reFun_A(n-5)
#
# print(reFun_A(20))

# Prints in ascending order numbers from n increasing in 5's and an X at the end if n<0
# def reFun_B(n):
#     if n<0:
#         return "X"
#     return reFun_B(n-5)+"-"+str(n)
#
# print(reFun_B(20))

# Reverses a string
# def reFun_C(st):
#     if len(st)==1:
#         return st
#     if len(st) == 0:
#         return ''
#     print(st[len(st)-1])
#     print(st[1:len(st)-1])
#     return st[-1]+reFun_C(st[1:len(st)-1])+st[0]
#
# print(reFun_C("Structure"), end="")

# adds the last number to the second to last number and then the second to last to the
# third to last number and repeats.
# def reFun_D(n, alist):
#     if n==0:
#         return
#     alist[n-1]+=alist[n]
#     reFun_D(n-1, alist)
#
# # [2,2,2,2,2,2,2,2,2,2]
# alist = [2]*10
# reFun_D(len(alist)-1, alist)
# print(alist)

# Reverses the list.
# def reFun_E(alist):
#     end = len(alist)-1
#     for i in range(len(alist)//2):
#         alist[i], alist[end-i] = alist[end-i], alist[i]
#
# # makes a list from 2-30 incrementing in 3's (not including 30 but including 2)
# alist = list(range(2, 30, 3))
# reFun_E(alist)
# print(alist)

# alist = [[2, 3, [4, 5, [6]]], [7, 8, [[9]]], [], 10, [11]]
#
# def print_nested_list(nested):
#     if type(nested) == list :
#         for item in nested:
#             print_nested_list(item)
#     else:
#         print(' ' + str(nested) + ' ', end='')
#
# print_nested_list(alist)

# alist = [[2, 3, [4, 5, [6]]], [7, 8, [[9]]], [], 10, [11]]
# empty_list = []
# def flatten_nested_list(nested, empty):
#     if type(nested) == list :
#         for item in nested:
#             flatten_nested_list(item, empty)
#     else:
#         empty.append(nested)
#
# flatten_nested_list(alist, empty_list)
# print(empty_list)

# def merge_sorted_lists(listA, listB):
#     merge_sorted_listsR(listA, listB, 0, 0)
#
# def merge_sorted_listsR(listA, listB, stA, stB):
#     if len(listB) == 0: return
#     if listA[stA] >= listB[stB]:
#         listA.insert(stA, listB[stB])
#         listB.pop(0)
#         merge_sorted_listsR(listA,listB,stA+1,stB)
#     else :
#         listA.insert(stA+1, listB[stB])
#         listB.pop(0)
#         merge_sorted_listsR(listA,listB,stA+1,stB)
#
# listA = [2, 5, 8, 10, 11]
# listB = [1, 3, 4, 6, 7, 8, 9, 11, 12, 13]
# merge_sorted_lists(listA, listB)
# print("The final listA: ", listA)

# The final listA: [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13]
