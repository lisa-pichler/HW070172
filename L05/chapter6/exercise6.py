# Programming exercises chapter 6
# exercise 6
# A Program to compute the area of a triangel given the lengths of the sides

import math
def triangle(a, b, c):
    s = (a + b + c) / 2
    A = math.sqrt(s*(s-a) * (s-b) * (s-c))
    return A
def main():
    a = eval(input("Enter the length of side a: "))
    b = eval(input("Enter the length of side b: "))
    c = eval(input("Enter the length of side c: "))
    A = triangle(a, b, c) 
    print("The area of your triangel is: ", A)
main()