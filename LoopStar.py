#why do we need loops? execute a code for n amount of times without writing it over and over
#promt user for number of stars

numberOfStars=int (input("Number of stars?"))
#2 ways of loops, for loop and the while loop
"""
for row in range (numberOfStars):
    for col in range (numberOfStars):
        print ("*", end='')
    print()
    numberOfStars -= 1
"""

for row in range (0, numberOfStars, 2):
        print("* " * (numberOfStars-row))


        
