#Prompt the user for weight in pounds
weight = eval (input ("Enter weight in pounds:"))
height = eval (input ("Enter height in inches:"))

#Making a constant for the conversion to kg and cm

KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254

weightInKg = weight * KILOGRAMS_PER_POUND
heightInMt = height * METERS_PER_INCH

#Compute BMI
bmi = weightInKg / (heightInMt ** 2)

print("BMI is:", bmi)
if bmi < 18.5:
    print ("Underweight")
elif bmi < 25:
    print ("Normal")
elif bmi < 30:
    print ("Overweight")
else:
    print ("Obese")
