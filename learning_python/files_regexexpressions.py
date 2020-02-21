import re

# text = '''
# John and Jane went to Coffee #1 on 140 Queen Street.
# They had coffees that cost a total of GBP 5.20 and then
# waited for a couple of friends 20times.
# They hadn't seen each other for over 6 years.
# Both of them have a sweet tooth so they also spend
# almost GBP 20 on cakes in a shop at 30 Castle Street.
# '''

# # . can be any character but in brackets it's just the value of a full stop.
# print(re.findall(r'\w+[.]', text))

# # The first attempt misses out Coffee because it's expecting a letter after ee
# print(re.findall(r'\w+ee\w+', text))
# # * means zero or many, + means once or many
# print(re.findall(r'\w*ee\w*', text))

# # use [a-z] instead of w because w means [a-zA-Z0-9_]
# print(re.findall(r'[A-Z][a-z]*', text))

# All words excluding numbers, including the ' too
# print(re.findall(r'[A-Za-z\']+', text))

# All prices but in pounds.
# print(re.findall(r'GBP [\d\.]+', text))

# this is a bit trickier: we require that the word consists only of lower case letters
# To make sure that we do not extract the space as well we usee \b
# or add the space and then use group to ignore it.
# print(re.findall(r'\b[a-z\']+', text))
# print(re.findall(r' ([a-z\']+)', text))

# data = []
#
# with open('tweets.txt','r') as f:
#     for line in f:
#         line = line.strip()
#         if line:
#             data.append(line)
#
# data_str = '\n'.join(data)
#
# # part 1
# print(re.findall(r'@\w+', data_str))
#
# # part 2
# print(re.findall(r'(demonetization is )([\w ]*)', data_str))
# print(re.findall(r'([dD]emonetization is)\s(\w+)',data_str))
