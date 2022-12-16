"""
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

bmi = weight (kg) / height square (m sq)

Example Input

weight = 80
height = 1.75

Example Output

80 ÷ (1.75 x 1.75) = 26.122448979591837
26

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

    Under 18.5 they are underweight
    Over 18.5 but below 25 they have a normal weight
    Over 25 but below 30 they are slightly overweight
    Over 30 but below 35 they are obese
    Above 35 they are clinically obese.

"""

weight = int(input("Enter your weight: "))
height = float(input("Enter your height: "))

bmi = int(weight / ( height**2))
print("Your BMI is:",bmi)

if bmi < 18.50:
    print("You are underweight")
elif 18.50 <= bmi < 25:
    print("You are normal weight")
elif 25 <= bmi < 30:
    print("You are slightly overweight")
elif 30 <= bmi <= 35:
    print("You are obese")
else:
    print("You are clinically obese")

    
