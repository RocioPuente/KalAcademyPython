from fractions import Fraction
a = []
for i in range (1, 17, 2):
    a = a + [Fraction(1,i)]
    
print(a)
