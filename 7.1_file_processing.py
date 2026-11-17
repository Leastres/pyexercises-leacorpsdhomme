"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - There are two empty lines.
# - Some names have extra spaces at the beginning.
# - Capital letters are not consistent.
# - "van rossum" is a last name made of two words.

# 1. In: A text file called names.txt containing people's names.
# 2. Process, problem by problem: 
# Remove empty lines. 
# Remove extra spaces. 
# Use the same capitalization for every name. 
# Keep all words after the first name together as the last name, then sort. 
# 3. Out: A new file called names_cleaned.txt with sorted, cleaned names.
# 4. How I decide which word is the last name:
# The first word is the first name. Everything after it is the last name.
# This keeps "Van Rossum" together.


# Your code below
names = []

# Read the original file and clean each name.
with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        name = " ".join(line.split()).title()
        if name != "":
            names.append(name)

# Sort by last name (everything after the first word).
names.sort(key=lambda name: name.split(" ", 1)[1].lower())

# Save the cleaned names to a different file.
with open("names_cleaned.txt", "w", encoding="utf-8") as file:
    for name in names:
        file.write(name + "\n")

# Check: names.txt has 10 lines and names_cleaned.txt has 8.
# Two empty lines were removed.
# First name in the sorted file: Margaret Hamilton.
# Last name in the sorted file: Guido Van Rossum.