"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of 8 marketing campaign budgets.
# 2. Process: Display the list, select one budget, sort the list and calculate the total.
# 3. Out: The list, one budget, the sorted list and the total.
# 4. What my list is about, and what I computed from it: My list contains marketing campaign budgets in euros. I calculated the total to know the overall marketing spending.


# Your code below

budgets = [1000, 2000, 1500, 3000, 2500, 4000, 3500, 5000]

# Display the whole list
print("Listing all budgets")
print(budgets)

# Display the third item
print("The third budget:")
print(budgets[2])

# Sort the list
print("The budgets after sorting")
budgets.sort()
print(budgets)

# Calculate the total
print("Total budget:", sum(budgets))

# Check:
# First 3 budgets: 1000 + 2000 + 1500 = 4500
# Python gives 4500 for these three budgets.
# Total of all 8 budgets = 22500 euros.