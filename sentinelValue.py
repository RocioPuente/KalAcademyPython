data=eval(input("Enter an number. The program ends if it is 0: "))
sum = 0

# != means not equal to

while data != 0:
    sum += data
    data=eval(input("Enter an number. The program ends if it is 0: "))

print ("The sum is", sum)
