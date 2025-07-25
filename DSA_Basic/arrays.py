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
for i in range(n):             # i controls the vertical (rows)
    for j in range(n):         # j controls the horizontal (columns)
        print("*", end=" ")    # prints * on the same line with a space
    print()                    # moves to the next line after inner loop



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
    for j in range(i + 1):
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

# 6)) Upper pyramid (increasing stars):

  #         * 
  #       * * * 
  #     * * * * * 
  #   * * * * * * * 
  # * * * * * * * * * 
# add this 3 word -- j --- i,n, i , i + 1
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ", end = " ")
    for j in range(i):
        print("*", end = " ")
    for j in range(i + 1):
        print("*", end = " ")
    print()

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







