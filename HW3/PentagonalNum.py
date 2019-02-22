def getPentagonalNumber(n):
    return n*(3*n-1)//2

for n in range(1, 101):
    print(getPentagonalNumber(n), end=' ')
    if n % 10 == 0:
        print()
