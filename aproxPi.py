from fractions import Fraction
f1=Fraction(1,1)
f2=Fraction(1,3)
f3=Fraction(1,5)
f4=Fraction(1,7)
f5=Fraction(1,9)
f6=Fraction(1,11)
f7=Fraction(1,13)
f8=Fraction(1,15)

total1 = float(4*(f1-f2+f3-f4+f5-f6))

print ("First equation:")
print (total1)

total2 = float(4*(f1-f2+f3-f4+f5-f6+f7-f8))
print ("Second equation:")
print (total2)
