#################################
#Name: Jaleel Savoy
#Example: Function for the Newton-Raphson for square root
    #finds x such that x**2 - y is within the epsilon of 0
#################################
def newtonRaphsonForSqrt():
    epsilon = 0.01
    guessNum = 0
    guess = x/2.0
    while abs(guess*guess - x) >= epsilon:
        guess = guess - (((guess**2) - x)/(2*guess))
        guessNum += 1
    print("Square root of", y, "is about", guess, ". The number of guesses:",
    guessNum)
    
newtonRaphsonForSqrt()