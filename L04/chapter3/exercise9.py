#Programming exercises chapter 3
# exercise 9
# A program to calculate the area of a triangle

def main():
    import math 
    print("The area of a triangle")
    a = eval(input("Enter the length of side a: "))
    b = eval(input("Enter the length of side b: "))
    c= eval(input("Enter the length of side c: "))
    s = (a + b + c) / 2

    A = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area is:", A)
main()
