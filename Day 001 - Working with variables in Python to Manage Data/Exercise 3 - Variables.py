"""
Write a program that switches the values stored in the variables a and b.

Example Input

a: 3
b: 5

Example Output

a: 5
b: 3
"""

a = int(input("a: "))
b = int(input("b: "))

c = a
a = b
b = c

print("a: ",a)
print("b: ",b)
