from math import pi
from math import sqrt
from math import log
from math import pow
from math import exp
from math import sin
import random
# import math

# t1=True
# t2=False
# a, b, c = 100, 200, 300
# print( a < b < c, t1 and t2, (not t1) or (not t2))
# true, false, true

# for i in range(40, 0, -5):
#     if (i % 3 == 0):
#         print(i, end=',')
# 30, 15,

# st1 = 'He had a run in the park.'
# st2 = 'The family went to the park to feed the ducks.'
# st3 = ''
# for c in st1:
#     if c in st2:
#         st3 += c
# print(st3)
# e had a run...

# for i in range(3, 40):
#     if i == 36:
#         break
#     if (i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0):
#         continue
#     print(i, end= ' ')
# no multiples of 2, 3 and 5, stops at 36

# st ='Hello World!'
# st2 = st[::-1]
# print(st2)
# prints backwards

# def foo (a, b):
#     return a+b, a//b, a%b
# i, j, k = foo(20, 5)
# print("{}, {}, {}".format(i, j, k))
# 25, 4, 0

# print(sqrt(2498))
# print(pi)
# print(log(1 + pow(exp(1), 2)))
# for i in range(1,20):
#     print(sin(i))

# def secs_to_time(seconds):
#     hours = seconds // (60*60)
#     mins = (seconds % (60*60)) // 60
#     seconds = (seconds % (60*60)) % 60
#     return "hours: " + str(hours) + ", minutes: " + str(mins) + ", seconds: " + str(seconds)
#
# print(secs_to_time(3800))

# w = "word"
# str = ""
#
# jw = random.sample(w, len(w))
# print(jw)
#
# jw = str.join(jw)
# print(jw)

# help(chr)
# help(ord)
# for i in range (256):
#     print(chr(i))
# print(chr(7))

# sentences = input("What would you like to jumble? :) ")
# def jumble_sentences(sentences):
#     words = sentences.split(" ")
#     jumbled = ""
#     for i in range(len(words)):
#         str = ""
#         letters = random.sample(words[i], len(words[i]))
#         joined = str.join(letters)
#         jumbled += joined + " "
#     return jumbled
#
# print(jumble_sentences(sentences), end="")

# for char in "1bc4":
#     # print(char)
#     print(char.isalpha())
#     # print(not char.isnumeric())
#     # print(type(char))

# str = "1bc4"
# for i in range(len(str)):
#     if str[i].isalpha():
#         print(str[i].upper())
#     else:
#         print("not a letter")

# heads, tails, count = 0, 0, 0
# while (count<10000):
#     rand_num = random.randint(0,1)
#     if rand_num == 0:
#         heads += 1
#     else:
#         tails += 1
#     count += 1
# print("Heads: {}, Tails: {}".format(heads, tails))

# rhyme = "child_a and child_b went up the hill, to fetch a pail of water. child_a fell down and broke his crown, and child_b came tumbling after."
# child_a = input("First name: ")
# child_b = input("Second name: ")
# rhyme = rhyme.replace("child_a", child_a)
# rhyme = rhyme.replace("child_b", child_b)
# print(rhyme)
