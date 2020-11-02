# Programming exercises chapter 3
# exercise 12
# A program to find the sum of the cubes of the first n natural numbers

def main():
    print("The sum of the cubes of the first n natural numbers")
    n = int(input("Enter a posotive natural number: "))
    sum = 0
    for n in range(1, n + 1):
        sum = (sum + n) ** 3
    print("The sum of the cubes of",n,"is", sum)
main()
