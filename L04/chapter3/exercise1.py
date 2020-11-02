# Programming exercises chapter 3
# 1. Write a program to calculate the volume and surface area of a sphere
# from its radius given as input

def main():
    from math import pi
    print("A program to calculate Volume and surface of a sphere")
    radius = eval(input("Enter the radius: "))
    V = 4/3 * pi * (radius ** 3)
    A = 4 * pi * (radius ** 2)
    print("The volume is:", V, "The surface area is:", A)
main()
