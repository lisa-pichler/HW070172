# Programming exercises chapter 5
# exercise 11; A programm to aloow users to input two values into chaos.py
# File chaos.py
# A simple programm illustrating chaotic behaviour
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    for i in range (10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(x, "", y)
main()