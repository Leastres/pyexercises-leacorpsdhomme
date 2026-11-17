"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
# The user enters a first name, an email address and an invitation code.
    2. What happens to it?
# The program checks each value using regular expressions.
# If all three values are valid, the information is saved.
# Otherwise, the program displays an error message.
    3. What comes out?
# A confirmation message if all three fields are valid.
# An error message if at least one field is invalid.
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.
#
# FIRST NAME:
# Only letters (A-Z or a-z), between 2 and 20 characters.
# No numbers, spaces or special characters.
#
# EMAIL:
# Letters, numbers, dots, underscores or hyphens before @.
# Then letters, numbers or hyphens for the domain.
# Then a dot and 2 to 6 letters for the extension.
# Spaces are not allowed.
#
# INVITATION CODE:
# Exactly 3 capital letters followed by 3 numbers.
# Example: VIP123.
#
# Explanation of the patterns:
# ^ means the beginning of the text.
# $ means the end of the text.
# [A-Za-z] means an uppercase or lowercase letter.
# [0-9] means a number.
# {2,20} means between 2 and 20 characters.
# {3} means exactly 3 characters.
# + means one or more characters.
# A backslash followed by a dot means a real dot.
# @ represents the @ symbol.


WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below

import re

# Ask the user for information
first_name = input("Enter your first name: ")
email = input("Enter your email: ")
invitation_code = input("Enter your invitation code: ")

# Validate the three fields
valid_name = re.fullmatch(r"[A-Za-z]{2,20}", first_name)
valid_email = re.fullmatch(
    r"[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,6}",
    email
)
valid_code = re.fullmatch(r"[A-Z]{3}[0-9]{3}", invitation_code)

# Save only if everything is valid
if valid_name and valid_email and valid_code:

    with open("vip_guests.txt", "a", encoding="utf-8") as file:
        file.write(first_name + "," + email + "," + invitation_code + "\n")

    print("Registration successful!")
    print("Information saved.")

else:
    print("Registration failed.")

    if not valid_name:
        print("Invalid first name.")

    if not valid_email:
        print("Invalid email.")

    if not valid_code:
        print("Invalid invitation code.")

# I tested all 9 values.
# The three valid values were accepted.
# The six invalid values were rejected.
# All results matched my predictions.