"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of 8 marketing campaign budgets.
# 2. Process: Display the list in four different orders.
# 3. Out: Four reordered lists and the original list.
# 4. My four orders, and which ones modify the original:
# Original order: No modification.
# Ascending order: Creates a new sorted list.
# Descending order: Creates a new sorted list.
# Reversed order: Creates a new reversed list.
# None of these operations modify the original list.



# Your code below

budgets = [1000, 2000, 1500, 3000, 2500, 4000, 3500, 5000]

print("Original order:", budgets)

print("Ascending order:", sorted(budgets))

print("Descending order:", sorted(budgets, reverse=True))

print("Reversed order:", budgets[::-1])

print("Original list at the end:", budgets)
