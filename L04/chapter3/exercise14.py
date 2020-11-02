#Programming exercises chapter 3
# exercise 14
# A program that finds the averge of numbers entered by the user

def main():
    print("The average of a series of numbers.")
    n = int(input("How many numbers should be counted: "))
    sum = 0
    for i in range(n):
        x = float(input("Enter a number: "))
        sum = sum + x
        average = sum /n
    print("the average of the sum of",n,"number is", average)
main()
