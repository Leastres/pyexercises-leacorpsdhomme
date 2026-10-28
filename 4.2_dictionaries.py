"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Information about a marketing campaign.
# 2. Process: Read, modify, add and remove information.
# 3. Out: Display the campaign information.
# 4. My object, my five fields, and why those: My object is a luxury marketing campaign.
# Fields: name, brand, budget, city, platform.
# These help identify and organize the campaign.


# Your code below

campaign = {
    "name": "Summer Campaign",
    "brand": "Tiffany",
    "budget": 5000,
    "city": "Paris",
    "platform": "Instagram"}

# Read the dictionary
print("The dictionary is:", campaign)

# Read one field
print("Brand:", campaign["brand"])

# Add a field
campaign["year"] = 2026

# Remove a field
campaign.pop("city")

# Display every field and its value
for key, value in campaign.items():
    print(key, ":", value)

# Test a field that does not exist
print(campaign.get("country", "Not found"))

# Check:
# Using campaign["country"] gives a KeyError.
# Using .get() displays "Not found" without stopping the program.