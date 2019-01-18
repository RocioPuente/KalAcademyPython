subtotal=eval(input("Enter the subtotal:"))
gratuityRate=eval(input("Enter the gratuity rate:"))

decimalGratuity=gratuityRate/100
gratuity=subtotal*decimalGratuity
total=subtotal+gratuity
print("The gratuity is",(round (gratuity, 2)), "and the total is", (round (total,2)))
