# Programming exercises chapter 3
# exercise 13
# A program to sum a series of numbers entered by the user

def main():
    print("The sum of a series of numbers.")
    n = int(input("How many numbers are to be summed: "))
    sum = 0
    for i in range(n):
        x = eval(input("Enter a natural number: "))
        sum = x + sum 
    print("Sum of",n ,"numbers is", sum)
main()
