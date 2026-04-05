
# 🟥 PROBLEM 1: Gym Fee Calculation
# 📌 Problem Statement

# A gym offers subscription plans based on duration.

# The available plans are:

# Duration (months) Cost (₹)
# 1 2000
# 3 5000
# 6 9000
# 9 12000
# 12 15000

# Your task is to determine the total fee based on the number of months selected.

# If the input does not match any of the available plans, print "Error".

# 📥 Input Format
# A single integer M representing number of months
# 📤 Output Format
# Print the corresponding fee
# If invalid → print "Error"
# 🧪 Example
# Input
# 3
# Output
# 5000

months = int(input())
d = {
    1:2000,
    3:5000,
    6:9000,
    9:12000,
    12:15000
}

if months not in d:
    print("Error")
else:
    print(d[months])


# 🟥 PROBLEM 2: Fraud Transactions Detection
# 📌 Problem Statement

# You are given a list of transaction records.

# Each transaction is provided as a single string in the format:

# Sender Receiver Amount Timestamp

# A transaction is considered fraudulent if:

# Another transaction with the same Sender, Receiver, and Amount already exists
# The time difference is less than 60 seconds
# 📥 Input Format
# First line: integer N (number of transactions)
# Next N lines: transaction string
# 📤 Output Format
# Print all fraudulent transactions
# Each transaction should be printed in the same format
# 🧪 Example
# Input
# 3
# A B 100 1000
# A B 100 1040
# A B 200 1100
# Output
# A B 100 1040
N = int(input())
d = {}
for _ in range(N):
    s = input().split()
    sender = s[0]
    receiver = s[1]
    amount = s[2]
    time = s[3]
    key = (senior, receiver, amount)
    if key in d and ads(time-d[key]) < 60:
       print("FRAUD:",sender,receiver,amount,time)
    d[key] = time

# 🟥 Problem 3: Parking Fee Calculation
# 📌 Problem Statement

# A parking area charges fees based on the number of hours a vehicle is parked:

# For the first 2 hours, the charge is ₹100 per hour
# For the next 3 hours (i.e., from hour 3 to 5), the charge is ₹50 per hour
# For any time beyond 5 hours, the charge is ₹20 per hour
# 📥 Input Format
# A single integer hours representing the total number of hours the vehicle is parked
# 📤 Output Format
# Print a single integer representing the total parking fee
# ⚠️ Constraints
# 0 ≤ hours ≤ 10^5

# 🧪 Example
# Input
# 6
# Output
# 370
hours = int(input())
charges = 0
if (hours <= 2):
    charges = hours * 100
elif (3>= hours <= 5):
    charges = (2*100) + ((hours -2) * 50)
else:
    charges = (2*100) + (3*50) + ((hours - 5) * 20)
print(charges)


# 🟥 Problem 4: Hot Air Balloon - Maximum People
# 📌 Problem Statement

# A hot air balloon has a maximum weight capacity of W kilograms.

# You are given an array of integers representing the weights of N people:

# w1, w2, w3, ..., wn

# Your task is to determine the maximum number of people that can fit into the balloon such that the total weight does not exceed W.

# 📥 Input Format
# First line: Integer N (number of people)
# Second line: N space-separated integers (weights of people)
# Third line: Integer W (maximum capacity)
# 📤 Output Format
# Print a single integer → maximum number of people that can fit
# ⚠️ Constraints
# 1 ≤ N ≤ 10^5
# 1 ≤ wi ≤ 10^5
# 1 ≤ W ≤ 10^9

# 🧪 Example
# Input
# 5
# 40 50 60 70 80
# 200
# Output
# 3



🟥 Problem 5: Ticket Price Analysis
📌 Problem Statement

In a theatre, ticket prices are recorded for a show.
Each ticket price lies in the range 30 to 100000 (inclusive).

You are given a list of ticket prices as input.

Your task is to process only the valid ticket prices (i.e., prices within the given range) and perform the following operations:

Calculate the sum of all odd ticket prices
Count the total number of odd ticket prices
Calculate the mean (average) of the odd ticket prices
📥 Input Format
A single line containing space-separated integers representing ticket prices
📤 Output Format

Print three values:

Sum of odd ticket prices
Count of odd ticket prices
Mean of odd ticket prices

🔍 Example

Input:

55 60 70 45

Output:

100 2 50
