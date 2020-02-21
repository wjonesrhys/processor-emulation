import random
import math

# def star_wrap(string):
#     return "**"+string+"**"
#
# print(star_wrap("not Rey"), end="")

# def triangle(height):
#     str = ""
#     for i in range(height+1):
#         str+="*"*i +"\n"
#     return str
#
# s1 = triangle(3)
# s2 = triangle(7)
#
# print(s1)
# print(s2)

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# random_letter = random.choice(alphabet)
#
# user_letter = ""
# nr_guesses = 0
# while (random_letter != user_letter):
#     user_letter = input("Please enter a letter to guess: ")
#     nr_guesses += 1
#
#     if (random_letter == user_letter):
#         print("You're correct! Well done! You did it in {} guesses!".format(nr_guesses))
#     elif random_letter > user_letter:
#         print('Higher..')
#     elif random_letter < user_letter:
#         print('Lower..')

# def convert_degree_to_radians(x):
#     rad = x / 360 * 2 * math.pi
#     return rad
#
# # Ask for user input
# degree = float(input('Enter the degree you want to convert: '))
# # Call the conversion function
# rad = convert_degree_to_radians(degree)
# # Print the result
# print('An angle of {} in degrees is {} in radians'.format(degree, rad))

# a = list(range(10))
# [0,1,2,3,4,5,6,7,8,9]
# print(a)

# print(a[2])        # 2
# # a[10]            # Error
# print(a[-3])       # 7
# print(a[0:3])      # 0,1,2
# print(a[:3])       # 0,1,2
# print(a[4:])       # 4,5,6,7,8,9
# print(a[:])        # whole list
# print(a[::2])      # all even
# # print(a[5::-1])    # 9,8,7,6,5 -----------
# print(a[::2][3])   # 6

# print(a[4])    # 4
# print(a[-6])   # 4
# print(a[0:2])  # [0, 1]
# print(a[:3])   # [0, 1, 2]
# # print(a[-2:])  # [8, 9] --------------
# print(a[::3])  # [0, 3, 6, 9]
# print(a[::-3]) # [9, 6, 3, 0]

# All even numbers in ascending order
# print(a[::2])
# The reverse of a
# print(a[::-1])
# All odd numbers in descending order
# print(a[::-2])
# The two highest odd numbers in descending order
# print(a[:6:-2])

# a = list(range(10))
# a[0] = 10               # [10,1,2,3,4,5,6,7,8,9]
# print(a)

# a = list(range(10))
# a[2:4] = ["a", "b"]     # [0,1,a,b,4,5,6,7,8,9]
# print(a)

# a = list(range(10))
# a[2:4] = ["a", "b", "c", "d"] # [0,1,a,b,c,d,4,5,6,7,8,9]
# print(a)

# a = list(range(10)) --------------
# a[2:4:2] = ["a", "b"]   # error, slices have to have the exact amount of elements added
# print(a)

# a = list(range(10))
# a[2:6:2] = ["a", "b"]   # [0,1,a,3,b,5,6,7,8,9]
# print(a)

# a = list(range(10))
# del a[0:2]              # [2,3,4,5,6,7,8,9]
# print(a)

# a = list(range(10))
# del a[::2]              # [1,3,5,7,9]
# print(a)

# a = list(range(10))
# a[1::2] = a[::-2]       # [0,9,2,7,4,5,6,3,8,1]
# print(a)

# def is_valid_name(name):
#     valid_characters = '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#ăCheck whether only valid characters are used
#     for c in name:
#         if not c in valid_characters:
#             return False
#
#     # All characters are valid. Now we need to check that the variable name does NOT
#     # start with a number
#     if name[0] in '0123456789':
#         return False
#     # If we haven't returned False yet, the name is valid: we can return True
#     return True
#
# name = "1____2"
# isvalid = is_valid_name(name)
# if isvalid:
#     print(name, 'is a valid variable name')
# else:
#     print(name, 'is an invalid variable name')

# def fix_variable_name(name):
#     if is_valid_name(name):
#         # if it's valid we can just return the name
#         return name
#     # If the function hasn't returned yet, the name is invalid.
#     # The strategy for fixing is simply replacing invalid letters
#     # by underscores _
#     new_name = list(name)
#     valid_characters = '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#     for i in range(len(name)):
#         if not name[i].isalnum():
#             new_name[i] = '_'
#     # All characters may be valid but we must still not start with a number
#     if name[0] in '0123456789':
#         new_name[0] = '_'
#     return ''.join(new_name)
#
# name = "10myvar"
# isvalid = is_valid_name(name)
# new_name = fix_variable_name(name)
# if isvalid:
#     print(name, 'is a valid variable name')
# else:
#     print(name, 'is an invalid variable name')
#     print('It was fixed to', new_name)

# def intersect(a,b):
#     both = []
#     for char in a:
#         if ((char in b) and (char not in both)):
#             both.append(char)
#     return both
#
# a = (2, 3, 4, 6, 7, 7, 8, 8)
# b = (5, 1, 2, 7, 8, 7, 8, 10, 35)
# out = intersect(a,b)
# print(out)

# sports = ["football", "rugby", "hockey", "tennis"]
# print(sports[0])
# print(sports[-1])
#
# sports.append("cycling")
# print(sports)
# print(len(sports))
#
# for sport in sports:
#     print(sport[0])
#
# del sports[0]
# print(sports)
#
# sports.remove("rugby")
# print(sports)
#
# median = int(len(sports)/2)
# print(median)
#
# if len(sports) % 2 == 0:
#     del sports[median]
#     del sports[median-1]
#
# if len(sports) % 2 == 1:
#     del sports[median]
#
# print(sports)

# x = [1,2,3,4]
# x.pop(3)
# print(x)
#
# x = [1,2,3,4]
# x.remove(3)
# print(x)
#
# newlist = ["a","b","c","d","e"]
# newlist.pop(3)
# newlist.remove("a")
# print(newlist)

# def load_pallets(weights):
#     max_weight = 3000
#     total_weight = 0
#     i = 0
#     while i < len(weights):
#         if total_weight + weights[i] < max_weight:
#             total_weight += weights[i]
#             print("Loaded item {} with a weight of {} kg".format(i, weights[i]))
#         else:
#             print('Lorry fully loaded. Total weight: {} kg.'.format(total_weight))
#             break
#         i += 1
#
# weights = [750, 387, 291, 712, 100, 622, 109, 750, 282]
# load_pallets(weights)
