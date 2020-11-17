# Programming exercises chapter 8
# exercise 4
# modify exercise 5

import math
def prime(number):
    prime = True 
    for i in range(2, round(math.sqrt(number) + 1)):
        if number % i == 0:
            prime = False
            quit 
    return prime


def main():
    number = eval(input("Please enter a number: "))

    for i in range(2, number + 1):
        if prime(i):
            if i == 2:
                print(2, end= "")
            else:
                print(",", i, end= "")
    
main()
