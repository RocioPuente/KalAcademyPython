M= eval(input("Enter the amount of water in kilograms:"))
initialTemp=eval(input("Enter the initial temperature in Celsius:"))
finalTemp=eval(input("Enter the final temperature in Celsius:"))

Q= M*(finalTemp-initialTemp)*4184
print("The energy needed is:", Q)
