t=eval(input("Enter the tempretaure in Fahrenheit between -58 and 41: "))
v=eval(input("Enter the wind speed in miles per hour: "))

windChill= 35.74 + (0.6215*t)-(35.75*(v**0.16))+(0.4275*(t*(v**0.16)))

print ("The wind chill index is: ", windChill)
