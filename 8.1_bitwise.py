"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in? 
# Three permissions represented by numbers:
# VIEW = 1, EDIT = 2 and PUBLISH = 4.
    2. What happens to it?
# First, I combine VIEW and EDIT.
# Then, I check if PUBLISH is allowed.
# Next, I add PUBLISH.
# Finally, I remove EDIT using bitwise operators.
    3. What comes out?
# The program displays the permissions in binary.
# It also shows True or False to indic
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.
# My permissions are about organizing a luxury VIP event.
# VIEW allows someone to see event information.
# EDIT allows someone to change event information.
# PUBLISH allows someone to publish event communication.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below

# Define the permissions
VIEW = 1
EDIT = 2
PUBLISH = 4

# Combine two permissions
permissions = VIEW | EDIT
print("Initial permissions:", bin(permissions))

# Check if PUBLISH is present
print("Can publish:", bool(permissions & PUBLISH))

# Add PUBLISH
permissions = permissions | PUBLISH
print("After adding PUBLISH:", bin(permissions))

# Remove EDIT
permissions = permissions & ~EDIT
print("After removing EDIT:", bin(permissions))

# Check:
# 0b011 means VIEW and EDIT.
# 0b111 means VIEW, EDIT and PUBLISH.
# 0b101 means VIEW and PUBLISH.
# All binary results are correct.