# Programming exercises chapter 3
# ecercise 6
# A program that calculatees the slope of a line through two points.

def main(): 
    print("A program that calculates the slope of a line through two points.")

    x1 = eval(input("Enter the first coordinate for point 1: "))
    y1 = eval(input("Enter the second coordinate for point 1:"))
    x2 = eval(input("Enter the first coordinate for point 2: "))
    y2 = eval(input("Enter the second coordinate for point 2: "))

    slope = (y2 - y1) / (x2 - x1)
    print("the slope is:", slope) 
main()
