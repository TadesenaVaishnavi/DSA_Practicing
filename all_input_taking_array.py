# Case 1: input: [1,2,3,4,5]
#         output: [1, 2, 3, 4, 5]
def input_array_format():
    arr = list(map(int, input().strip("[]").split(',')))
    return arr

# Case 2: input: 1 2 3 4 5
#         output: [1, 2, 3, 4, 5]
def input_space_separated():
    arr = list(map(int, input().split()))
    return arr

# Case 3: input: 1,2,3,4,5
#         output: [1, 2, 3, 4, 5]
def input_comma_separated():
    arr = list(map(int, input().split(',')))
    return arr
# Case 4:
# Case with size not given
def input_array_size_not_given():
    arr = []
    while True:
        try:
            num = input().strip()
            if num == "":
                break
            arr.extend(map(int, num.split()))
        except ValueError:
            print("Please enter valid integers separated by space.")
    return arr



# to print and test output
def input_array_size_not_given2():
    arr = list(map(int, input().split()))
    return arr


print(input_array_format())
print(input_space_separated())
print(input_comma_separated())
print(input_array_size_not_given2())

# Explaination 
------------------
# Case 1: [1,2,3,4,5]
def input_array_format():
    arr = list(map(int, input().strip("[]").split(',')))
    return arr

# short note
strip() removes brackets,
split() breaks string into list,
map(int, …) converts strings to integers,
list() makes final integer list.

# in detail
| Step          | Result                  |
| ------------- | ----------------------- |
| input()       | `"[1,2,3,4,5]"`         |
| strip("[]")   | `"1,2,3,4,5"`           |
| split(',')    | `['1','2','3','4','5']` |
| map(int, ...) | 1,2,3,4,5               |
| list(...)     | `[1,2,3,4,5]`           |

Good question 👍 Let’s understand **how this line works step by step**.

```python
arr = list(map(int, input().strip("[]").split(',')))
```

Assume user enters:


[1,2,3,4,5]


---

## 🔹 1️⃣ `input()`

Takes input as a **string**.

```
"[1,2,3,4,5]"
```

👉 Important: Even numbers come as string.

---

## 🔹 2️⃣ `.strip("[]")`

### 📌 What is `strip()`?

`strip()` removes characters from the **start and end** of a string.

```python
"[1,2,3]".strip("[]")
```

Output:

```
"1,2,3"
```

⚠ It removes `[` and `]` only from beginning and end — not middle.

So after strip:
"1,2,3,4,5"


---

## 🔹 3️⃣ `.split(',')`

### 📌 What is `split()`?

It divides a string into pieces using a separator.

```python
"1,2,3,4,5".split(',')
```

Output:

```python
['1', '2', '3', '4', '5']
```

Now we have a **list of strings**, not integers.

---

## 🔹 4️⃣ `map(int, ...)`

### 📌 What is `map()`?

`map(function, iterable)` applies a function to every element.

Here:

```python
map(int, ['1','2','3'])
```

It converts each string into integer:

```
1
2
3
```

But `map()` does NOT return a list.
It returns a **map object (iterator)**.

So we convert it into list.

---

## 🔹 5️⃣ `list(...)`

Converts the map object into list.

Final result:

[1, 2, 3, 4, 5]


---

# 🔥 Full Flow Summary

Input:

"[1,2,3,4,5]"


Step by step:

| Step          | Result                  |
| ------------- | ----------------------- |
| input()       | `"[1,2,3,4,5]"`         |
| strip("[]")   | `"1,2,3,4,5"`           |
| split(',')    | `['1','2','3','4','5']` |
| map(int, ...) | 1,2,3,4,5               |
| list(...)     | `[1,2,3,4,5]`           |

---

# 💡 Easy Interview Explanation (Short Version)

> strip() removes brackets,
> split() breaks string into list,
> map(int, …) converts strings to integers,
>list() makes final integer list.



# Doubt
Why we are strip removing square brackets?
because 
That is a string, not a real list. 
If we don’t remove [ and ], then after splitting we get:
['[1', '2', '3', '4', '5]']

'[1' cannot convert to int
'5]' cannot convert to int


case 2: Okay 👍 Let’s clearly understand this function.

### Code:

def input_space_separated():
    arr = list(map(int, input().split()))
    return arr


---

## ✅ What type of input does this expect?

User should enter numbers like this:


1 2 3 4 5


(space separated, NOT commas, NOT brackets)

---

## 🔍 Step-by-step Working

### 1️⃣ `input()`

Takes input as a string:

```
"1 2 3 4 5"
```

---

### 2️⃣ `.split()`

Since no argument is given, it splits using spaces.

```
"1 2 3 4 5".split()
```

Result:

```
['1', '2', '3', '4', '5']
```

Now it is a list of strings.

---

### 3️⃣ `map(int, ...)`

Converts each string into integer:

```
'1' → 1
'2' → 2
'3' → 3
'4' → 4
'5' → 5
```

---

### 4️⃣ `list(...)`

Converts the map object into list.

Final result:

```
[1, 2, 3, 4, 5]
```

---

## 🎯 Final Output of Function

If input is:

1 2 3 4 5


Function returns:

```python
[1, 2, 3, 4, 5]
```

---

## 💡 Important Notes (Interview Point)

✔ `split()` without argument → splits by space
✔ No need for `strip()` here
✔ Time Complexity = O(n)


