# programming exercises chapter 3
# exercise 2
# A program that calculates the cost per square inch of a pizza

def main():
    print("A program to calculate the cost per square inch of a pizza")
    from math import pi
    diameter = eval(input("Enter the diameter of the pizza in inches: "))
    price = eval(input("Enter the price of the pizza in Euro: "))
    radius = diameter / 2
    A = pi * (radius ** 2)
    cost = price / A
    print("The cost per square inch is:", cost, "Euro")
main()