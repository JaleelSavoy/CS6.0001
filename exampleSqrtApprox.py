#################################
#Example: Square Root Approximator with a bisection search
#################################
import math as m
x = (float(input("Enter a number: ")))
epsilon = 0.0000001
low = 0.0
high = (max(1.0, x))
numGuesses = 0
ans = (high+low)/2.0
while abs(ans**2 - x) >= epsilon:
    print(("Low: ", low), ("High: "), ("Ans: ", ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print( 'numGuesses =', numGuesses)
print(ans, "is close to square root of", x, "...which is: ", m.sqrt(x))