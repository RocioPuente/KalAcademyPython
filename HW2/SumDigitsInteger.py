num = int(input("Input a number between 0 and 1000: "))

x  = num //1000
x1 = (num%10)
x2 = (num//10)%10
x3 = (num//100)%100
print("The sum of digits in the number is", x+x1+x2+x3)

#temp = num
#resultado = 0
#for _ in range (3):
    #resultado = resultado + temp %10
    #temp = temp // 10
#print (resultado)
