def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base case: Fill first row and column
    for i in range(m + 1):
        dp[i][0] = i  # delete all characters from word1
    for j in range(n + 1):
        dp[0][j] = j  # insert all characters to word1

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # characters match
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # delete
                    dp[i][j - 1],    # insert
                    dp[i - 1][j - 1] # replace
                )
    
    return dp[m][n]
word1 = "intention"
word2 = "execution"
print(minDistance(word1, word2))  # ✅ Output should be 5


# ✅ Output: 5




# # --- 🚀 Run with User Input ---
# if __name__ == "__main__":
#     word1 = input("Enter first word: ")
#     word2 = input("Enter second word: ")
#     result = minDistance(word1, word2)
#     print(f"Minimum edit distance to convert '{word1}' → '{word2}': {result}")



# DT
# if __name__ == "__main__":--- WHY
# ---When Python runs any script, it needs to keep track of how that script is being
# used:
# Is this script being run directly by you?

# Or is it being imported as a module into another script?




# Python sets __name__ = "__main__" in this file.

# So, the code inside the if __name__ == "__main__": block runs.

# This is where you put things like:

# Running tests

# Calling functions

# Printing output

# Basically, this code runs only when you want the script to do something directly.