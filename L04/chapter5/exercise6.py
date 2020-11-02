#Programming exercises chapter 5
# exercise 6
# A program to determine the numeric value of a complete name

def main(): 
    print("This is a program to determine the numeric value of a name")
    first = input("Enter your name: ")
    last = input("Enter your lastname: ")

    sum1 = 0 
    sum2 = 0
    for ch in first:
        sum1 = int(ord(ch)) + sum1 - 96
    for ch in last:
        sum2 = int(ord(ch)) + sum2 - 96
    numeric = sum1 + sum2
    print("The numeric value of the name", first, last, "is", numeric)
main()

