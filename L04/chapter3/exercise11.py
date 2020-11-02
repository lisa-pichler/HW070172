# Programming exercises chapter 3
# Exercise 11
# A program to find the sum of the first n natural numbers

def main():
    print("The sum of the first n natural numbers")
    n = int(input("Entre a positive natural number: "))
    sum = 0
    for n in range(1, n + 1):
        sum = sum + n
    print("sum of first", n, "numbers is", sum)
main()
