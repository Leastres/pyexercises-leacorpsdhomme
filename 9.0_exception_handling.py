"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
# The user enters the number of conversions of a marketing campaign.
    2. What happens to it?
# The program divides a campaign budget of 1000 EUR
# by the number of conversions.
# It allows 3 attempts if the user enters an invalid value.
    3. What comes out?
# The cost per conversion, or an error message.
# The program never crashes because of invalid user input.
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.
# ZeroDivisionError: The user enters 0.
# ValueError: The user enters text or leaves the answer empty.
# They should have different messages because the problems are different.
# Catching errors separately helps the user understand what went wrong.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. The two failures, and whether they deserve the same message:


# Your code below

budget = 1000
attempts = 0

while attempts < 3:

    try:
        conversions = float(input("Enter the number of conversions: "))

        cost = budget / conversions

        print("Cost per conversion:", cost, "EUR")
        break

    except ZeroDivisionError:
        print("Error: Conversions cannot be zero.")

    except ValueError:
        print("Error: Please enter a valid number.")

    attempts = attempts + 1

else:
    print("Too many attempts. Program finished.")

# Check:
# Test 1: 10 gives a cost of 100 EUR per conversion.
# Test 2: 0 displays a ZeroDivisionError message and asks again.
# Test 3: "abc" displays a ValueError message and asks again.
# Test 4: An empty line displays a ValueError message and asks again.
# The program keeps running after invalid inputs.