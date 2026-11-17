"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
"""Exercise 8.0 — Operators (bonus, not graded)"""

# 1. In: Two strings, "Paris" and "paris".
# 2. Process: Compare the two strings using comparison and logical operators.
# 3. Out: A table showing True or False for each comparison.
# 4. I chose "Paris" and "paris".
# I was surprised that "Paris" == "paris" is False because Python is case-sensitive.

# My two values
value1 = "Paris"
value2 = "paris"

# Comparisons
equal = value1 == value2
different = value1 != value2
greater = value1 > value2
smaller = value1 < value2
greater_equal = value1 >= value2
smaller_equal = value1 <= value2

# Display the results
print("COMPARISON TABLE")
print("-------------------------")
print("Equal:", equal)
print("Different:", different)
print("Greater:", greater)
print("Smaller:", smaller)
print("Greater or equal:", greater_equal)
print("Smaller or equal:", smaller_equal)

# Logical operators
print("\nLOGICAL OPERATORS")
print("-------------------------")
print("Equal AND greater:", equal and greater)
print("Equal OR smaller:", equal or smaller)
print("NOT equal:", not equal)

# My prediction:
# Equal: False
# Different: True
# Greater: False
# Smaller: True
# Greater or equal: False
# Smaller or equal: True
# Equal AND greater: False
# Equal OR smaller: True
# NOT equal: True

# Number of correct predictions: 9/9 (to check after running)