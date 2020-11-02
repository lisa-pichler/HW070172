#Programming exercises chapter 3
# exercise 7
# A program that accepts two points and determines the distance between them

def main():
   import math
   
   print("A program that determines the distance between two points.")
   x1 = eval(input("Enter the first coordinate for point 1: "))
   y1 = eval(input("Enter the second coordinate for point 1: "))
   x2 = eval(input("Enter the first coordinate for point 2: "))
   y2 = eval(input("Enter the second coordinate for point 2: "))
   
   distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
   print("The distance is:", distance)
main()
