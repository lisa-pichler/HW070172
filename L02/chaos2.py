# File: chaos.py
# A simple program illustrating chaotic behaviour.
def main():
    print("This programm illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)
main()    