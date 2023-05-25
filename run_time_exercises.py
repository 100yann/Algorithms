# Asymptotic Analysis - vocabulary for the design and analysis of algorithms
# -------------

# Example: One Loop
# Given: A(array of length n), and integer X
# Problem: Does array A contain int X?

def solution1(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return True
    return False

# print(solution1([2, 5, 10, 11, 20, 35], 35))

# Running Time: O(n) - a linear algorithm
# it executes a constant number of operations based on the size of the input
# --------------------------


# Example: Two Loops
# Given: 2 arrays - A,B, and int X
# Problem: Does A or B contain contain X?

def solution2(a, b, x):
    for i in range(len(a)):
        if a[i] == x:
            return True
    for i in range(len(b)):
        if b[i] == x:
            return True
    return False

# print(solution2(a=[1,3,5], b=[4,7,9], x=10))

# Running Time: O(n) - linear; 
# If the input doubles, the num of operations double as well
# ----------------------------


# Example: Two Nested Loops
# Given: 2 arrays - A,B, and int X
# Problem: Do arrays A,B have a number in common

def solution3(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                return True
    return False

# print(solution3(a=[1,2,3], b=[4,5,3]))

# Run Time: O(n^2) - quadratic time algorithm;
# If you double the input length, the running time of the algorithm will go up
# by a factor of 4
# ---------------------------------------


# Example: Two Nested Loops(II)
# Given: An array A of length n
# Problem: Does array A have any duplicate entries

def solution4(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return True
    return False

# print(solution4(a=[1,0,6,2,5,4,23,32,55,34,1]))

# Run Time: O(n^2)