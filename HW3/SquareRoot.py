def sqrt(n):
    lastGuess= 1.0
    nextGuess= lastGuess+1
    diff=nextGuess-lastGuess
    while diff >= 0.0001:
        nextGuess=(lastGuess+(n/lastGuess))/2
        diff=nextGuess-lastGuess
        # Si diff es negativo, multiplicalo por menos 1.
        if diff < 0:
            diff=diff*-1
        #print ("{0} {1} {2}".format (nextGuess, lastGuess, diff))
        lastGuess=nextGuess

    return(nextGuess)

n = float(input("Calculate square root of?:"))
print (sqrt(n))
