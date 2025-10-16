# Day 1 : Generate Parentheses
# Medium Recursion
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. Parentheses should be sorted, i.e. 
# consider two parentheses with the first position of difference having '(' and ')' then parenthesis with '(' should be printed first.
# Input Format:
# The first and only line of input contains an integer n
# Output Format:
# You need to input the number of combinations C followed by C
# lines each containing the parentheses.

# Constraints:
# (1≤n≤8)
# Examples:
# Example 1:
# Input:
# 1
# Output:
# 1
# ()
# Example 2:
# Input:
# 2
# Output:
# 2
# (())
# ()()

def generate_parentheses(n):
    """
    Generate all combinations of well-formed parentheses for a given number of pairs.
    
    Args:
        n (int): Number of pairs of parentheses (1 ≤ n ≤ 8)

    Returns:
        List[str]: A sorted list containing all valid combinations of parentheses.
    """
    
    # ---- Input validation ----
    if not isinstance(n, int) or n < 1 or n > 8:
        raise ValueError("Input must be an integer between 1 and 8 (inclusive).")
    
    results = []
    path = []  # Use list instead of string for better performance

    def backtrack(open_parens_used, close_parens_used):
        """
        Recursively build valid parentheses combinations using backtracking.
        """
        # Base case: when the length equals 2*n, we have a complete valid combination
        if len(path) == 2 * n:
            results.append("".join(path))  # Join list into string once
            return

        # Add '(' if we can still place more
        if open_parens_used < n:
            path.append('(')
            backtrack(open_parens_used + 1, close_parens_used)
            path.pop()  # Backtrack

        # Add ')' if it keeps the parentheses balanced
        if close_parens_used < open_parens_used:
            path.append(')')
            backtrack(open_parens_used, close_parens_used + 1)
            path.pop()  # Backtrack

    # Start recursion
    backtrack(0, 0)
    return results


# ---- Main Driver Code ----
if __name__ == "__main__":
    try:
        n = int(input("Enter number of parentheses pairs: "))
        combinations = generate_parentheses(n)
        
        print(len(combinations))  # Print total count
        for combo in combinations:
            print(combo)
    except ValueError as e:
        print(f"Error: {e}")
