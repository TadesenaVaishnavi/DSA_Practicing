List → Ordered, mutable
Tuple → Ordered, immutable
Set → Unique elements
Dictionary → Key-value pairs
Stack → LIFO
Queue → FIFO

------------------------
Important Python Topics
-------------------------


Lists --> A built-in data type, ordered collection of items that can hold multiple data types.
-----
Ordered, changeable collection of items.
Example: [1, 2, 3]

-->Syntax: Defined using square brackets [] with items separated by commas.
-->zero-based indexing
-->Characteristics: They are dynamic (size can change at runtime) and allow for efficient processing using iteration.

Tuples
------
Ordered, but cannot be changed (immutable).
Example: (1, 2, 3)

Dictionaries
-------------
Store data in key–value pairs.
Example: {"name": "Vaishnavi", "age": 21}

List Comprehension
----------------------
Short way to create lists in one line.
Example:
[x for x in range(5)]

🔹 Why Use?
Makes code shorter
Improves readability
Faster than normal loops

I use list comprehension when I need to create a list efficiently in a single line instead of writing a full loop.

Lambda Functions
----------------
Small, anonymous (no-name) function written in one line.
Example:
lambda x: x + 1

I use lambda functions for small, one-time operations where defining a full function is unnecessary.


Exception Handling
-------------------
Used to handle errors without crashing the program.
Example:
try:
    print(10/0)
except:
    print("Error handled")
  
File Handling
-----------------
Used to read or write data into files.
Example:
open("file.txt", "r")

Virtual Environments
---------------------
Used to create an isolated Python environment for a project so dependencies don’t conflict.



----------------
Data Structures
----------------
A data structure is a way of organizing and storing data so it can be used efficiently.

Basic Data Structures in Python
~~~~~ ~~~~~~ ~~~~~~ ~~~~~ ~~~~~~

Perfect 👍 Let’s revise **Data Structures** in very easy + short interview format.

---

# ✅ What is a Data Structure?

> A data structure is a way of organizing and storing data so it can be used efficiently.

---

# ✅ Basic Data Structures in Python

## 🔹 1. List

* Ordered
* Mutable (can change)
* Allows duplicates

Use when: You need a collection of items that can change.

---

## 🔹 2. Tuple

* Ordered
* Immutable (cannot change)
* Allows duplicates

Use when: Data should not be modified.

---

## 🔹 3. Set

* Unordered
* No duplicates

Use when: You need unique values.

---

## 🔹 4. Dictionary

* Key–Value pairs
* Fast lookup

Use when: You need to store data with labels.

---

# ✅ Linear Data Structures (Concept Level)

## 🔹 Stack

* LIFO (Last In First Out)
  Example: Undo feature

## 🔹 Queue

* FIFO (First In First Out)
  Example: Task scheduling

---

# 🎯 Interview Answer (Short)

> Data structures are used to store and organize data efficiently.
> In Python, common data structures are lists, tuples, sets, and dictionaries.
> Advanced structures include stacks and queues.

---

If you want, I can next explain **difference between list and tuple (very common interview question)**.
