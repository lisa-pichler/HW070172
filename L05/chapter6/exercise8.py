# Programming exercises chapter 6
# exercise 8

import math
def nextGuess(guess, x):
    g = guess + (x / guess) / 2
    return g

def main():
    x = eval(input("Find the square root of: "))
    y = eval(input("How many iterations would you like: "))
    g = x / 2
    for i in range (y):
        g = nextGuess(g, x)
        print(g)
main()