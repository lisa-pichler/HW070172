# Programming exercises chapter 6
# exercise 7

import math
def fibonnaci(n):
    x = 0 
    y = 1
    z = 0
    for i in range (n+1):
        z = x + y
        x = y
        y = z
    return z
def main():
    n = eval(input("Enter the number in the Fibonnaci sequence you want to see: "))
    y = fibonnaci(n)
    print("The Fibonnaci number is:", y)
main()