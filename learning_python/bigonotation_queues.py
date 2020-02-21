# n^2 + 5n
# O(n^2)

# (n + 7) (n + 2)
# O(n^2)

# (n + 1) 5
# O(n^5)

# 2^(n+1)
# O(2^n)

# 2^100
# O(1)

# Algorithm A executes an O (log n) time computation for each entry of an
# n-element array. What is the worst-case running time of algorithm A?
# O(nlog(n))

# Given an n-element array, Algorithm B chooses log n elements from the
# array at random and executes an O (n) time calculation for each. What
# is the worst-case running time of Algorithm B?
# O(nlog(n))

# Given an n-element array of integers, algorithm C executes an O (n)-time
# computation for each even number in the array, and O (log n)-time com-
# putation for each odd number in the array. What are the best-case and
# worst-case running times of Algorithm C?
# O(n^2 + nlog(n))

# Given an element array X, Algorithm D calls Algorithm E on each element
# X[i]. Algorithm E runs in 7i time when it is called on element X[i]. What
# is the worst-case running time of Algorithm D?
# O(n^2)

# S1: O
# S2: V
# S3: S, E, R, U, T, C, U, R, T, S
# os: F
# S1.push ("T")
# S2.push ("C")
# S1.push ("R")
# S2.push ("U")
# S1.push ("S")
# S2.push ("E")
# os = S1.pop ( )
# while os != "F":
#     S3.push(os)
#     S3.push(S2.pop())
#     os = S1.pop()
