"""
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
"""
"""
Example Input

size = "L"
add_pepperoni = "Y"
extra_cheese = "N"

Example Output

Your final bill is: $28.
"""
bill = 0

print("Welcome to Python Pizza Deliveries!\n")
pizza_size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
elif pizza_size == "L":
    bill += 25
else:
    print("Invalid input")

if add_pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    if pizza_size == "M" or "L":
        bill += 3

if extra_cheese == "Y":
    bill +=1

print("Your final bill is:",bill)
