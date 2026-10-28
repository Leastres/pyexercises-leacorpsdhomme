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
# Make the original list from Exercise 4.0
list_of_numbers = [10, 9, 1, 7, 8, 6, 2, 3, 4, 5]

# Make copies and reorder them
ascending = list_of_numbers.copy()
ascending.sort()

descending = sorted(list_of_numbers, reverse=True)

backwards = list_of_numbers.copy()
backwards.reverse()

# Display the list in four different orders
print("Original order:", list_of_numbers)
print("Ascending order:", ascending)
print("Descending order:", descending)
print("Backwards order:", backwards)

# Display the original list again to check it stayed unchanged
print("Original list at the end:", list_of_numbers)