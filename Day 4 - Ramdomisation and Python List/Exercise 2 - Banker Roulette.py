import random
"""
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#print (names[])
# new_length = length - 1

# random_choice = random.randint(0, new_length)
# person_who_will_pay_today = names[random_choice]
# print( person_who_will_pay_today + " is going to buy the meal today!")

person_who_will_pay_today = random.choice(names)
print( person_who_will_pay_today + " is going to buy the meal today.")
"""

num = int(input("How many people are there? "))
names = []

for i in range(0,num):
    name = input("Enter name: ")
    names.append(name)

person_who_will_pay_today = random.choice(names)
print( person_who_will_pay_today + " is going to buy the meal today.")
