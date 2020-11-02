#Programming exercises chapter 3
# exercise 10
# A program to determine the length of a ladder

def main():
    print("The length of a ladder required to reach a given height")
    import math

    from math import pi
    height = eval(input("Enter the height of the house: "))
    angle = eval(input(" Enter the angle of the ladder in degrees: "))
    radians = (pi / 180) * angle

    length = height / radians
    print("The length is:", length)
main()

