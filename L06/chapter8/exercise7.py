# Programming exercises chapter 8
# exercise 7
# Goldbach conjecture
import math
    # every even number is the sum of to prime numbers
    # check to make sure that I got an even number
def prime(number):
    x = math.sqrt(number)
    i = 2
    while i <= x:
        value = number % i
        if value == 0:
            return None
        else:
            i = i + 1
        return number
# find the two numbers
def main():
    number = eval(input("Plese enter a number: "))
    while number > 0:
        primenumber = prime(number+1)
        if primenumber != None:
            primenumber2 = number - primenumber
            test = prime(primenumber2)
            if test != None:
                print("{0} + {1} = {2}, number")
main()
   

