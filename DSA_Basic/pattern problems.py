# pattern programs
# Basic concepts
## To print horizontal
n = int(input("Enter a number: "))
print("*"*n)

# O/P:- n = 5 -- *****

#for space
# 1
print("* "* n) # * * * * * 
# 2 (or)
print(" ".join(["*"] * n))
# possible like this also -- print(" ".join("*" * n))

## to print vertical

n = int(input("Enter a number: "))
for i in range(n):
    print("*")

# Enter a number: 5
# *
# *
# *
# *
# *


# both 

# 1))Enter a number: 5
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

n = int(input("Enter a number: "))
for i in range(n):             # i controls the vertical (rows) & # i moves to next line
    for j in range(n):         # j controls the horizontal (columns)
        print("*", end=" ")    # prints * on the same line with a space
    print()                    # moves to the next line after inner loop

# i = 0, 1, 2, 3, 4
# Each loop, i goes up by +1 automatically.

# 2)) for increasing order 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# change only this 1 word up code for this 
for j in range(i + 1): # -- i - 1

# how i + 1 work 
# range(n) → goes from 0 to 4 (i = 0, 1, 2, 3, 4)
# For each row i, the inner loop runs i + 1 times:
# So row 0 → 1 star
# Row 1 → 2 stars
# Row 2 → 3 stars
# ...
# Row 4 → 5 stars

# 3)) for decreasing order
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# change only this 1 word
for j in range(i,n):


# 4)) 
  #         * 
  #       * * 
  #     * * * 
  #   * * * * 
  # * * * * * 



n = 5

# Outer loop for each row (i ranges from 0 to 4)
for i in range(n):

    # First inner loop to print spaces
    # It prints (n - i) spaces to shift stars to the right
    for j in range(i, n):
        print(" ", end=" ")

    # Second inner loop to print stars
    # It prints (i + 1) stars on each row
    for j in range(i + 1): # +1 --i initially starts at 0.
        print("*", end=" ")

    # Move to the next line after each row
    print()


# 5)) 
  # * * * * * 
  #   * * * * 
  #     * * * 
  #       * * 
  #         * 

# change this 2 word --- j -- i,n and i+1
for j in range(i+1):
for j in range(i,n):
# 6)) Upper pyramid (increasing stars):

  #         * 
  #       * * * 
  #     * * * * * 
  #   * * * * * * * 
  # * * * * * * * * * 
# add this 3 word -- j --- i,n, i , i + 1
n = 5
for i in range(n): # i moves to next line 
    for j in range(i,n):
        print(" ", end = " ")
    for j in range(i):
        print("*", end = " ")
    for j in range(i + 1):
        print("*", end = " ")
    print()

# for more clear understanding
n = 4
for i in range(n):
    for j in range(i,n):
        print(" ",end = " ")
    for j in range(i):
        print("7", end=" ")
    for j in range(i+1):
        print("6", end=" ")
    print()

#         6 
#       7 6 6 
#     7 7 6 6 6 
#   7 7 7 6 6 6 6 

# 7)) Lower inverted pyramid (decreasing stars):

  # * * * * * * * * * 
  #   * * * * * * * 
  #     * * * * * 
  #       * * * 
  #         * 
# change only 3 words -- (i+1),(i,n-1),(i , n)
n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end = " ")
    for j in range(i,n-1):
        print("*", end = " ")
    for j in range(i , n):
        print("*", end = " ") 
    print()


# 8)) 
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 


# combine both of above
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ", end = " ")
    for j in range(i):
        print("*", end = " ")
    for j in range(i + 1):
        print("*", end = " ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ", end = " ")
    for j in range(i,n-1):
        print("*", end = " ")
    for j in range(i , n):
        print("*", end = " ") 
    print()

# (or)

n = 5  # height of the upper half

# Upper Half (including middle row)
for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end=" ")
    # Print stars (2*i + 1) for symmetry
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()  # Move to next line

# Lower Half
for i in range(n):
    # Print leading spaces
    for j in range(i):
        print(" ", end=" ")
    # Print stars (2*(n - i) - 1)
    for j in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()  # Move to next line

# 9))
  #           * 
  #         * * * 
  #       * * * * * 
  #     * * * * * * * 
  #   * * * * * * * * * 
  # * * * * * * * * * * * 
  #   * * * * * * * * * 
  #     * * * * * * * 
  #       * * * * * 
  #         * * * 
  #           * 
n = 6  # change this to any positive integer

# top half (including middle row)
for i in range(1, n + 1):
    # (n - i) groups of two spaces to align like your examples
    print("  " * (n - i), end="")
    # (2*i - 1) stars separated by single spaces
    print(" ".join(["*"] * (2 * i - 1)))

# bottom half (excluding middle row)
for i in range(n - 1, 0, -1):
    print("  " * (n - i), end="")
    print(" ".join(["*"] * (2 * i - 1)))

  
# 10))

# combining IO and DO
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

n = 4
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for i in range(i,n):
        print("*",end=" ")
    print()

# 13))

  #         1 
  #       2 3 4 
  #     5 6 7 8 9 
  #   10 11 12 13 14 15 16 
  # 17 18 19 20 21 22 23 24 25 
  # 26 27 28 29 30 31 32 33 34 
  #   35 36 37 38 39 40 41 
  #     42 43 44 45 46 
  #       47 48 49 
  #         50 

# add count += 1
n = 5
count = 1

# 🔺 Upper half (including middle row)
for i in range(n):
    for j in range(i, n):              # Print leading spaces
        print(" ", end=" ")
    for j in range(i):                 # Left side numbers
        print(count, end=" ")
        count += 1
    for j in range(i + 1):             # Right side numbers
        print(count, end=" ")
        count += 1
    print()

# 🔻 Lower half
for i in range(n):
    for j in range(i + 1):             # Print leading spaces
        print(" ", end=" ")
    for j in range(i, n - 1):          # Left side numbers
        print(count, end=" ")
        count += 1
    for j in range(i, n):              # Right side numbers
        print(count, end=" ")
        count += 1
    print()


# 13)) numbers
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print()


# 14))

# A 
# A B 
# A B C 
# A B C D 
# A B C D E 

n = 5
for i in range(1,n+1):
    for j in range(i):
        print(chr(65 + j),end = " ")
    print()

#chr A
# chr(65)  → 'A'  
# chr(66)  → 'B'  
# chr(67)  → 'C'

#chr a
# chr(97)  → 'a'

# only A
# A 
# A A 
# A A A 
# A A A A 
# A A A A A 
# chr(65) -- change this line

# 1
# 1 1
# 1 1 1
# 1 1 1 1 

print("1",end = " ")

# B  
# B C  
# B C D  
# B C D E  
# B C D E F

chr(66 + j)

# 2  
# 2 3  
# 2 3 4  
# 2 3 4 5  
# 2 3 4 5 6

print(2 + j, end=' ')

# 1  
# 0 1  
# 1 0 1  
# 0 1 0 1


# change this line print((i + j) % 2, end=' ')--- remender 0 1

n = 4  # number of rows

for i in range(1, n + 1):
    for j in range(i):
        print((i + j) % 2, end=' ')
    print()




