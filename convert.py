1) # Function to convert binary string to decimal
def binary_to_decimal(s):
    base = 1
    ans = 0

    # Traverse from right to left
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '1':
            ans += base
        base *= 2

    return ans

# Sample input
s = "1011" or s = input().strip()

# Print the result
print(binary_to_decimal(s))


or 

# Binary string input
s = "1011"

# Use int() with base 2 to convert
print(int(s, 2))

Example 1:
Input: N = 1011
Output: 11
Explanation: 1011 when converted to decimal number is “11”.

Example 2:
Input: 100
Output: 4
Explanation: 100 when converted to decimal number is “4”.
Perfect 👏
Now I will explain the **entire program line by line** using one example:

Let’s take:

```
s = "1010"
```

---

# 🔹 The Code

```python
def binary_to_decimal(s):
    base = 1
    ans = 0

    for i in range(len(s) - 1, -1, -1):
        if s[i] == '1':
            ans += base
        base *= 2

    return ans
```

---

# 🔥 Step-by-Step Execution for `"1010"`

Binary:

```
Index:   0   1   2   3
Value:   1   0   1   0
```

We move from right → left
(3 → 2 → 1 → 0)

---

## 🔹 Line 1

```python
base = 1
```

Meaning:

```
base = 2⁰ = 1
```

---

## 🔹 Line 2

```python
ans = 0
```

Start total as 0.

---

# 🔄 Now Loop Starts

```python
for i in range(3, -1, -1)
```

This gives:

```
3 → 2 → 1 → 0
```

---

# 🔸 Iteration 1 (i = 3)

Digit:

```
s[3] = 0
```

Check:

```python
if s[i] == '1'
```

It is 0 → so skip adding.

Then:

```python
base *= 2
```

```
base = 1 × 2 = 2
```

Now:

```
base = 2  (2¹)
ans = 0
```

---

# 🔸 Iteration 2 (i = 2)

Digit:

```
s[2] = 1
```

Now:

```python
ans += base
```

```
ans = 0 + 2 = 2
```

Then:

```python
base *= 2
```

```
base = 2 × 2 = 4
```

Now:

```
base = 4  (2²)
ans = 2
```

---

# 🔸 Iteration 3 (i = 1)

Digit:

```
s[1] = 0
```

Skip adding.

Then:

```
base = 4 × 2 = 8
```

Now:

```
base = 8  (2³)
ans = 2
```

---

# 🔸 Iteration 4 (i = 0)

Digit:

```
s[0] = 1
```

Add:

```
ans = 2 + 8 = 10
```

Then:

```
base = 8 × 2 = 16
```

(Loop ends, so this 16 is not used.)

---

# 🔥 Final Answer

```python
return ans
```

```
10
```

---

# 🧠 What Actually Happened?

Binary:

```
1   0   1   0
```

Means:

```
1×8 + 0×4 + 1×2 + 0×1
```

Which equals:

```
8 + 2 = 10
```

The program automatically builds:

```
1 → 2 → 4 → 8
```

by doing:

```
base *= 2
```

Every step.

---

# 🎯 Important Understanding

* `base` = power of 2
* `ans` = total sum
* If digit is 1 → add power
* If digit is 0 → skip
* But base always increases


# 2) Convert Binary to Octal

3 binary digits = 1 octal digit
8 = 2³
Group in 3 digits from right:
101 110
Now convert each group:
101 → 5
110 → 6
56

def binary_to_octal(s):
    n = len(s)

    # Pad leading zeros to make length a multiple of 3
    if n % 3 == 1:
        s = "00" + s
    elif n % 3 == 2:
        s = "0" + s

    n = len(s)
    ans = ""

    # Process every group of 3 bits
    for i in range(0, n, 3):
        temp = int(s[i]) * 4 + int(s[i + 1]) * 2 + int(s[i + 2]) * 1
        ans += str(temp)

    return ans

# Driver code
s = "1100110"
print(binary_to_octal(s))


logic
------
    if n % 3 == 1:
        s = "00" + s
    elif n % 3 == 2:
        s = "0" + s

Case 1: n % 3 == 0

Already perfect.
No need to add zeros.
  
Case 2: n % 3 == 1
Length = 4
4 % 3 = 1 We need 2 more zeros to make it multiple of 3:
4 + 2 = 6 So: "00" + s

Case 3: n % 3 == 2
Example:
Length = 5
5 % 3 = 2
5 + 1 = 6
We need 1 more zero: 5 + 1 = 6
So: "0" + s


--
        temp = int(s[i]) * 4 + int(s[i + 1]) * 2 + int(s[i + 2]) * 1
        ans += str(temp)

1×4 + 0×2 + 1×1
= 4 + 0 + 1
= 5
temp = 5 ,ans += str(temp) --> ans = "5"

next 3
1×4 + 1×2 + 0×1
= 4 + 2 + 0
= 6
ans = "56"


3) Convert Decimal to Binary Number

binary = [0] * 32 --> Is 32 not Mandatory so
or 
binary = []
👉 Standard integer size = 32 bits
👉 Maximum binary digits needed = 32
👉 So we allocate fixed space


def binary_to_octal(s):
    n = len(s)

    # Pad leading zeros to make length a multiple of 3
    if n % 3 == 1:
        s = "00" + s
    elif n % 3 == 2:
        s = "0" + s

    n = len(s)
    ans = ""

    # Process every group of 3 bits
    for i in range(0, n, 3):
        temp = int(s[i]) * 4 + int(s[i + 1]) * 2 + int(s[i + 2]) * 1
        ans += str(temp)

    return ans

# Driver code
s = "1100110"
print(binary_to_octal(s))


Convert Decimal to Binary Number
---------------------------------

class BinaryConverter:
    def to_binary(self, n):
        binary = [0] * 32  # Predefine a list to hold binary digits
        i = 0

        # Convert to binary by dividing by 2 repeatedly
        while n > 0:
            binary[i] = n % 2
            i += 1
            n //= 2

        # Print the binary number in correct order
        for ind in range(i - 1, -1, -1):
            print(binary[ind], end='')

# Example usage
converter = BinaryConverter()
number = 28
print(f"Binary of {number} is: ", end='')
converter.to_binary(number)


how it work 
------------
converter = BinaryConverter()
number = 28
print(f"Binary of {number} is: ", end='')
converter.to_binary(number)


--> converter = BinaryConverter()
Python creates an object from the class BinaryConverter.
👉 Python creates an object from the class BinaryConverter.

Think like:
Create a machine that can convert decimal → binary
Now:
converter → object in memory
Nothing printed yet.
number = 28
👉 A variable named number is created.
👉 It stores value 28.

Memory now: number → 28

print(f"Binary of {number} is: ", end='') --> Python replaces {number} with 28.
Binary of 28 is: 
end='' means:

👉 Do NOT go to next line
👉 Stay on same line



Perfect 👏 now let’s understand this **line by line** with a full example.

We are converting **Decimal → Binary** using division by 2.

---

# 🔹 The Code

```python
i = 0

# Convert to binary by dividing by 2 repeatedly
while n > 0:
    binary[i] = n % 2
    i += 1
    n //= 2
```
28 ÷ 2 = 14 remainder 0
14 ÷ 2 = 7 remainder 0
7 ÷ 2 = 3 remainder 1
3 ÷ 2 = 1 remainder 1
1 ÷ 2 = 0 remainder 1

1 ÷ 2
2 cannot fully divide 1.
So:
Quotient = 0
Remainder = 1
1 = (2 × 0) + 1
---

# 🔥 What Is Happening Here?

We are repeatedly:

1. Taking remainder when dividing by 2
2. Storing that remainder
3. Dividing number by 2
4. Repeating

This is the standard binary conversion method.

---

# 🔥 Let’s Take Example: n = 10

Binary of 10 is:

```
1010
```

Now see how program builds it.

---

## 🔹 Start

```
n = 10
i = 0
binary = [0] * 32
```

---

## 🔹 Iteration 1

```
n = 10
```

```python
binary[i] = n % 2
```

```
10 % 2 = 0
```

So:

```
binary[0] = 0
```

Then:

```
i = 1
```

Then:

```
n //= 2
10 // 2 = 5
```

---

## 🔹 Iteration 2

```
n = 5
```

```
5 % 2 = 1
```

```
binary[1] = 1
```

```
i = 2
```

```
5 // 2 = 2
```

---

## 🔹 Iteration 3

```
n = 2
```

```
2 % 2 = 0
```

```
binary[2] = 0
```

```
i = 3
```

```
2 // 2 = 1
```

---

## 🔹 Iteration 4

```
n = 1
```

```
1 % 2 = 1
```

```
binary[3] = 1
```

```
i = 4
```

```
1 // 2 = 0
```

Loop stops because:

```
n = 0
```

---

# 🔥 What Is Stored?

```
Index:   0   1   2   3
Value:   0   1   0   1
```

So array contains:

```
[0, 1, 0, 1]
```

But wait…

This is reverse order.

Because:

Binary should be:

```
1 0 1 0
```

But we stored:

```
0 1 0 1
```

---

# 🔥 Why Reverse?

Because:

Binary is built from **right to left**.

Division method always gives:

```
Least Significant Bit first
```

So we must print in reverse:

```python
for j in range(i-1, -1, -1):
    print(binary[j], end="")
```

Output:

```
1010
```

Correct ✅

---

# 🎯 Important Understanding

| Line            | Meaning                   |
| --------------- | ------------------------- |
| `n % 2`         | gives last binary digit   |
| `n //= 2`       | removes last binary digit |
| `i += 1`        | move to next position     |
| loop stops when | number becomes 0          |

---

# 🔥 Very Simple Logic

Binary conversion =

```
Divide by 2
Store remainder
Repeat
```

---

Now small question for you 😊

If n = 7
What will be stored in binary array (before reversing)

----

  Short answer for TCS NQT 👇

✅ Best approach:

Use:

binary = []

NOT

binary = [0] * 32
🎯 Why?

In TCS NQT:

They care about correct logic

They care about clean code

They don’t require fixed 32-bit representation unless the question says so

Dynamic list (binary = []) is:

✔ Cleaner
✔ More Pythonic
✔ Less memory waste
✔ Easier to reverse

When use [0] * 32?

Only if question says:

"Print 32-bit binary"

"Consider signed 32-bit integer"

Final Answer

For normal decimal → binary in TCS:

👉 Use binary = []

That is the better and safer approach.
              
28 → 14 → 7 → 3 → 1 → 0
Method	Time	Space
Dynamic list	O(log n)	O(log n)
Fixed 32 list	O(log n)	O(1)

Convert Decimal to Octal
class Solution:
    # Function to convert a decimal number to its octal representation
    def decimalToOctal(self, decimal: int) -> str:
        # Handle the edge case where the input is 0
        if decimal == 0:
            return "0"

        octal = ""
        n = decimal
        
        # Loop until the number becomes 0
        while n > 0:
            # Get the remainder when dividing by 8
            remainder = n % 8
            # Prepend the remainder to the result string
            octal = str(remainder) + octal
            # Update the number using integer division
            n = n // 8
            
        return octal

# Driver code to test the solution
if __name__ == "__main__":
    sol = Solution()
    decimal_number = 17
    result = sol.decimalToOctal(decimal_number)
    print(f"Decimal: {decimal_number}, Octal: {result}")

(self, decimal: int)

self → refers to the object of the class
(Used only because this function is inside a class.)
decimal: int
decimal is a parameter.
: int is a type hint (it suggests that decimal should be an integer).
It does NOT force it strictly — it’s just for readability.
🔹 -> str
This is a return type hint.
It means:
👉 This function will return a string.
Because octal is returned as a string like "21".
🎯 Simple Meaning
This line means:
Define a function named decimalToOctal that takes an integer input and returns a string.
That’s it ✅


Convert Octal to Binary

class Solution:
    # Convert Octal to Decimal
    def octal_to_decimal(self, Octal):
        Decimal = 0
        i = 0
        while Octal != 0:
            rem = Octal % 10
            Decimal += rem * (8 ** i)
            i += 1
            Octal //= 10
        return Decimal

    # Convert Decimal to Binary
    def decimal_to_binary(self, decimal):
        Binary = 0
        i = 0
        while decimal != 0:
            rem = decimal % 2
            Binary += rem * (10 ** i)
            i += 1
            decimal //= 2
        return Binary

if __name__ == "__main__":
    # Create solution object
    sol = Solution()
    # Example input
    Octal = 345
    # Convert octal to decimal
    Decimal = sol.octal_to_decimal(Octal)
    # Print binary conversion
    print(sol.decimal_to_binary(Decimal))


Convert Octal to Decimal

class Solution:
    # Function to convert octal to decimal
    def octal_to_decimal(self, Octal):
        # Initialize decimal result
        Decimal = 0
        # Position counter (power of 8)
        i = 0
        # Loop until all octal digits are processed
        while Octal != 0:
            # Get the last digit of octal number
            rem = Octal % 10
            # Add to decimal result after multiplying by 8^i
            Decimal += rem * (8 ** i)
            # Increment position
            i += 1
            # Remove the last digit from octal
            Octal //= 10
        # Return final decimal value
        return Decimal

if __name__ == "__main__":
    # Create solution object
    sol = Solution()
    # Example octal number
    Octal = 345
    # Call method to convert and print
    print("The decimal equivalent of the given octal number is",
          sol.octal_to_decimal(Octal))


Convert digits/numbers to words

class Solution:
    def convert_num_into_word(self, s):
        # Words for single digits
        single_digit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

        # Words for numbers from 10 to 19
        two_digits = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

        # Words for multiples of ten from 20 onwards
        tens_multiple = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        # Words for higher powers
        tens_power = ["hundred", "thousand"]

        # Handle empty input
        if len(s) == 0:
            print("")
            return

        # Handle single digit input
        elif len(s) == 1:
            print(single_digit[int(s[0])])
            return

        # Store length of string
        length = len(s)

        # Loop through each digit
        for i in range(len(s)):
            # If more than two digits remain
            if length > 2:
                # Print digit and its place value if digit is not zero
                if int(s[i]) != 0:
                    print(single_digit[int(s[i])], end=" ")
                    print(tens_power[length - 3], end=" ")
                length -= 1
            else:
                # Handle numbers between 10 and 19
                if int(s[i]) == 1:
                    print(two_digits[int(s[i + 1])], end=" ")
                    return
                # Handle multiples of 10 and following digit
                # This handles numbers from 20 to 99 (except 10–19).
                elif int(s[i]) != 0:
                    print(tens_multiple[int(s[i])], end=" ")
                    if int(s[i + 1]) != 0:
                        print(single_digit[int(s[i + 1])], end=" ")
                    return

if __name__ == "__main__":
    # Create solution object
    sol = Solution()

    # Example input
    num = "9090"

    # Call method
    sol.convert_num_into_word(num)

| Index | Word     |
| ----- | -------- |
| 0     | hundred  |
| 1     | thousand |
length - 3
3 - 3 = 0
tens_power[0] → "hundred"
4 - 3 = 1
tens_power[1] → "thousand"
If number has 4 digits → first digit is thousand place.
If number has 3 digits → first digit is hundred place.

    
line works from 10 to 19
if int(s[i]) == 1:
 print(two_digits[int(s[i + 1])], end=" ")
 return
    
int('5') == 1 ?
❌ NO.
So it does NOT enter that block.


1. Make word lists
STEP 1 — Create word lists
(single_digit, two_digits, tens_multiple, tens_power)
2. Handle empty and single
STEP 2 — Handle edge cases
If empty → return
If single digit → print and return
STEP 3 — Store length
3. Loop through digits
4. If more than 2 → place value
STEP 5 — If length > 2
→ Print digit + place value
→ Reduce length
5. If 2 left → handle 10–19
6. Else → handle tens and ones
STEP 6 — If length ≤ 2
→ If tens digit = 1 → special case
→ Else → print tens + ones
That’s it.
You don’t need to remember 40 lines.
You only need to remember:
Lists → Edge case → Loop → Place values → Tens logic


You’re asking **“how to remember this?”** — not logic, but memory trick 👍
Good question.

Don’t try to remember full code.

Remember this **pattern only** 👇

---

# 🔥 1️⃣ Break number into 4 parts

Always think:

1. Single digits (0–9)
2. Special numbers (10–19)
3. Multiples of 10 (20, 30, 40…)
4. Place values (hundred, thousand)

That’s it.

If you remember this structure, you can rebuild code anytime.

---

# 🔥 2️⃣ Core Logic Rule (Very Important)

When converting number to words:

### Rule 1:

If digit is not 0 → print digit word.

### Rule 2:

If position is hundred/thousand → print place word.

### Rule 3:

If tens digit = 1 → use special list (10–19).

### Rule 4:

Else → use tens_multiple list.

That’s the full algorithm.

---

# 🔥 3️⃣ Don’t Memorize Code — Memorize Flow

Flow is:

```
Check empty
Check single digit
Loop through digits
   If more than 2 digits → handle place values
   Else → handle tens & ones
```

That’s it.

---

# 🔥 4️⃣ Real Trick to Remember

Instead of remembering:

```python
tens_power[length - 3]
```

Just remember:

👉 “Place value depends on position from right.”

Code can be recreated.

---

# 🎯 Final Advice

In TCS or interview:

They don’t expect memorized code.

They expect:

* Clear logic
* Clean structure
* Edge case handling

If you understand pattern, you can write it again in 5–7 minutes.


