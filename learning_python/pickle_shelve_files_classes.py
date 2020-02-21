import pickle
import shelve

# a = [i for i in range(1, 11) if i % 2 == 1]
# b = [i for i in range(1, 11) if i % 2 == 0]
# c = [i for i in range(5, 26, 5)]
#
# f1 = open('p_week5.dat', 'wb')
# pickle.dump(a, f1)
# pickle.dump(b, f1)
# pickle.dump(c, f1)
# f1.close()
#
# f1 = open('p_week5.dat', 'rb')
# listA = pickle.load(f1)
# listB = pickle.load(f1)
# listC = pickle.load(f1)
# f1.close()
# print(listA, listB, listC, end="\n")

# s = shelve.open('s_week5.dat')
# s['odd'] = listA
# s['even']= listB
# s['fives']= listC
# s.close()
#
# s = shelve.open('s_week5.dat')
# print(s['fives'])
# s.close()

# s = '3 2 -5 8 2 -4 1 4 6 -1 -6 10'
# s_split = s.split(" ")

# Part a
# inputs = [s_split[x] for x in range(len(s_split)-1)]
# equal_to = s_split[len(s_split)-1]
#
# total = 0
# for item in inputs:
#     total += int(item)
# print(total)

# for i in range(len(s_split)):
#     indexes = [i for i in range(len(s_split))]
#     indexes.remove(i)
#     answer = int(s_split[i])
#     sum = 0
#     for x in indexes:
#         sum += int(s_split[x])
#     if sum == answer:
#         print("answer is {}".format(answer))

# Question 4

# with open('input.txt', 'r') as afile:
#     num_of_lines = afile.readline()
#     inputs = [afile.readline().split() for _ in range(int(num_of_lines))]
#     for a,b in inputs:
#         try:
#             print(int(a)/int(b))
#         except (ValueError, ZeroDivisionError) as e:
#             print('Error Code: {}'.format(e))

# Question 5

# name = input("Please input your name: ")
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def say_hi(self):
#         print('Hello {}, this is my first OOP attempt'.format(self.name))
#
# p = Person(name)
# p.say_hi()

# Question 6

# number = random.randint(1,100)
#
# class Game():
#     def __init__(self, attempts):
#         self.greeting = "Welcome to Play!"
#         self.attempts = attempts
#         self.player = None
#         self.afterwords= "thanks for playing. See you again soon."
#     def greet(self):
#         self.player = input("Please Enter Your Name: ")
#         print("Hello {}\n{}\nI have {} attempts.".format(self.player, self.greeting, self.attempts))
#     def play(self): #to be overwritten
#         pass
#     def finish(self):
#         print("{}, {}".format(self.player, self.afterwords))
#         input("Please click any key to exit.")
#
# class GuessNumberGame(Game): #subclass of Game
#     def __init__(self, attempts):
#         super(GuessNumberGame, self).__init__(attempts)
#         self.greeting = """You, the player, are thinking of a number between 1 and 100.
# I, the clever computer will try to guess it in as few attempts as possible."""
#
#     def play(self):
#         count=0
#         try:
#             number = int(input("Think of a number between 1 and 100: "))
#         except (ValueError) as e:
#             print("Error Code: ",e)
#
#         startrange = 1
#         endrange = 100
#         while count<self.attempts:
#             guess = random.randint(startrange,endrange)
#
#             print("Is it {}(Yes, Higher, Lower)?".format(guess))
#             answer = input().strip().lower()
#
#             if(answer == "yes"):
#                 print("Ha, I won!")
#                 break
#             elif(answer == "higher"):
#                 startrange = guess
#                 count += 1
#             else:
#                 endrange = guess
#                 count += 1
#
#         print("Arrrgh, you beat me.")
#
# guessNumberGame = GuessNumberGame(2)
# guessNumberGame.greet()
# guessNumberGame.play()
# guessNumberGame.finish()
