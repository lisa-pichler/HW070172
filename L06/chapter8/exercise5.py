# Programming exercises chapter 8
# exercise 5
import math

def main():
    number = eval(input("Please enter a number: "))

    for i in range(2, round(math.sqrt(number) + 1 )):
        if number % i == 0:
            print(number, "is not a prime number")
        else:
            print(number, "is a prime number")
main()
