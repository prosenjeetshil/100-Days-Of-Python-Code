"""
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
    You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers
Example Input
56
Example Output
You have 12410 days, 1768 weeks, and 408 months left.
"""

max_age = 90
current_age = int(input("What is your current age?\n"))
remaining_age = max_age - current_age

day = remaining_age * 365
weeks = remaining_age * 52
months = remaining_age * 12

print(f"You have {day} days, {weeks} weeks, {months} months left.")
