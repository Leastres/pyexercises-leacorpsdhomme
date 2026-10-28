"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of 8 marketing budgets.
# 2. Process: Calculate 10% of each budget.
# 3. Out: Display each budget, its position and 10%.
# 4. What I compute for each item, and why it is worth showing: I calculate 10% to estimate advertising spending.


# Your code below

budgets = [1000, 2000, 1500, 3000, 2500, 4000, 3500, 5000]

position = 1

for budget in budgets:
    print("Position:", position, "Budget:", budget, "10%:", budget * 0.10)
    position = position + 1

# Check: 8 budgets = 8 lines printed.

